import cv2
import mediapipe as mp
from math import sqrt
import pyautogui
import time

import traceback

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def calculateDistance(y2,y1,x2,x1):
  d=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
  return d
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    
    try:
        for no, ele in enumerate(results.pose_landmarks.landmark):
            #ly1=ly2=lx1=lx2=y1=y2=x1=x2=0
            if no==14 or no==24:
                if no==14:
                  ly1=ele.y*image.shape[0]
                  lx1=ele.x*image.shape[1]
                elif no==24:
                  ly2=ele.y*image.shape[0]
                  lx2=ele.x*image.shape[1]
                  print(ly2)
                #print(ele.x*image.shape[1],ele.y*image.shape[0],no)

                try:
                    text = str(int(lx1-lx2))
                    if abs(lx1-lx2)>150:
                        pyautogui.keyDown('A')
                    elif abs(lx1-lx2)<100:
                        pyautogui.keyUp('A')
                except:
                    traceback.print_exc()
                                
                
                image = cv2.circle(image, (int(ele.x*image.shape[1]),int(ele.y*image.shape[0])), 10, (255,0,255), 5)
                image = cv2.putText(image, text, (int(ele.x*image.shape[1]),int(ele.y*image.shape[0])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2, cv2.LINE_AA)
            
            elif no==11 or no==23:
                if no==11:
                  y1=ele.y*image.shape[0]
                  x1=ele.x*image.shape[1]
                elif no==23:
                  y2=ele.y*image.shape[0]
                  x2=ele.x*image.shape[1]
                #print(ele.x*image.shape[1],ele.y*image.shape[0],no)

                try:
                    text = str(int(x1-x2))
                except:
                    traceback.print_exc()
                                
                
                image = cv2.circle(image, (int(ele.x*image.shape[1]),int(ele.y*image.shape[0])), 10, (255,0,255), 5)
                image = cv2.putText(image, text, (int(ele.x*image.shape[1]),int(ele.y*image.shape[0])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2, cv2.LINE_AA)
 
              
    except Exception as e:
        print(e)
        pass
    
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
