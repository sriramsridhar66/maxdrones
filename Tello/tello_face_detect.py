import time
import cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()
tello.connect()

showVideo = True # True if you want to show the video, False if you want to record it instead
# Still gotta figure out how to do both properly :)

tello.streamon()
frame_read = tello.get_frame_read()
continue_thread = True
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def videoRecorder():
    height, width, _ = frame_read.frame.shape

    if showVideo:
        while continue_thread:
            img = frame_read.frame
            # converting image from color to grayscale
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Getting corners around the face
            # 1.3 = scale factor, 5 = minimum neighbor can be detected
            faces = faceCascade.detectMultiScale(imgGray, 1.3, 5) 
            # drawing bounding box around face
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)
            # displaying image with bounding box
            cv2.imshow('face_detect', img)
            cv2.waitKey(1)
    else:
        video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
        while continue_thread:
            video.write(frame_read.frame)
            time.sleep(1 / 30)
        video.release()

# Need to run this record/display function in a separate thread so that it doesn't block us from doing normal movements
recorder = Thread(target=videoRecorder)
recorder.start()

print(tello.get_battery())

# Put any move commands here
# tello.takeoff()
time.sleep(30)
# tello.rotate_counter_clockwise(360)
# tello.land()

continue_thread = False
recorder.join()