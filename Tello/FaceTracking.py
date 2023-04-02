import cv2
import numpy as np
from djitellopy import tello
import time
#import cv2.cv2 as cv2
from simple_pid import PID

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
drone.takeoff()
# drone.send_rc_control(0, 0, 25, 0) #allow drone to reach face level
# time.sleep(2.7) #time for drone to ascend
drone.move_up(100)

w, h  = 360, 240
fbRange = [5000, 6800]
pid = [0.4, 0.4, 0]
pid_fb = PID(0.005, 0.005, 0.005, setpoint=5000)
pid_fb.output_limits = (-15, 15)



ud_pError = 0
fb_pError = 0
yaw_pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w//2
        cy = y + h//2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0,255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

def trackFace(info, w, pid, ud_pError, fb_pError, yaw_pError):
    area = info[1]
    x, y = info[0]
    fb = 0

    if x == 0:
        yaw_speed = 0
        yaw_error = 0
        ud_speed = 0
        ud_error = 0
        fb_speed = 0
        fb_error = 0

        drone.send_rc_control(0, 0, 0, 0)

        return 0, 0, 0

    ud_error = y - h // 2
    # ud_speed = pid[0] * ud_error + pid[1] * (ud_error - ud_pError)
    # ud_speed = -1*int(np.clip(ud_speed, -100, 100))

    fb_speed = pid_fb(area)
    fb_error = area - fbRange[0]
    #fb_speed = pid[0] * fb_error + pid[1] * (fb_error - fb_pError)
    #fb_speed = -1*int(np.clip(fb_speed, -15, 15))

    yaw_error = x - w//2
    # yaw_speed = pid[0]*yaw_error + pid[1]*(yaw_error - yaw_pError)
    # yaw_speed = int(np.clip(yaw_speed, -100, 100))

    # if area > fbRange[0] and area < fbRange[1]:
    #     fb = 0 #drone will not move if at the desired range
    # elif area == 0:
    #     fb = 0 #stop moving if no image
    #     speed = 0
    # elif area > fbRange[1]:
    #     fb = -8 #if too close, move backward
    # elif area < fbRange[0] and area != 0:
    #     fb = 8 #if too far, move forward

    #print(speed, fb)

    drone.send_rc_control(0, int(fb_speed), 0, 0)

    return 0, fb_error, 0

#cap = cv2.VideoCapture(0)
while True:
    #_, img = cap.read()
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = findFace(img)
    ud_pError, fb_pError, yaw_pError = trackFace(info, w, pid, ud_pError, fb_pError, yaw_pError)
    #print("Center", info[0], "Area", info[1])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break