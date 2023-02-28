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

def videoRecorder():
    img = frame_read.frame
    height, width, _ = img.shape
    # cv2.namedWindow("preview", cv2.WINDOW_NORMAL)

    if showVideo:
        while continue_thread:
            cv2.imshow("Tello Vid", frame_read.frame)
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

# Put any move commands here
# tello.takeoff()
time.sleep(10)
# tello.rotate_counter_clockwise(360)
# tello.land()

continue_thread = False
recorder.join()