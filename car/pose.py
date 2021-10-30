import cv2
import mediapipe as mp
from math import sqrt
import pyautogui

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
            if no==11 or no==15:
                if no==11:
                  ly1=ele.y*image.shape[0]
                  lx1=ele.x*image.shape[1]
                elif no==15:
                  ly2=ele.y*image.shape[0]
                  lx2=ele.x*image.shape[1]
                #print(ele.x*image.shape[1],ele.y*image.shape[0])
                try:
                  leftcurl = calculateDistance(ly2,ly1,lx2,lx1)
                  print(leftcurl)
                  if leftcurl<150:
                    print("moving left...")
                    pyautogui.keyDown('left')
                  elif leftcurl>200:
                    pyautogui.keyUp('left')
                  
                except Exception as e:
                  print(e)
                
                image = cv2.circle(image, (int(ele.x*image.shape[1]),int(ele.y*image.shape[0])), 10, (255,0,255), 5)

            elif no==12 or no==16:
                if no==12:
                  y1=ele.y*image.shape[0]
                  x1=ele.x*image.shape[1]
                elif no==16:
                  y2=ele.y*image.shape[0]
                  x2=ele.x*image.shape[1]
                #print(ele.x*image.shape[1],ele.y*image.shape[0])
                try:
                  rightcurl = calculateDistance(y2,y1,x2,x1)
                  if rightcurl<150:
                    print("moving right...")
                    pyautogui.keyDown('right')
                  elif rightcurl>200:
                    pyautogui.keyUp('left')
                
                except Exception as e:
                  print(e)
                
                image = cv2.circle(image, (int(ele.x*image.shape[1]),int(ele.y*image.shape[0])), 10, (255,0,255), 5)    
              
    except:
        pass
    
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
