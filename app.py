import cv2
import time
from emailing import send_email
from datetime import datetime
import os
import shutil

email_frequency_seconds = 10

os.mkdir( "motion_captures" )

video = cv2.VideoCapture( 0 )
time.sleep( 1 )

first_frame = None
detected_time = None

while True:
    
    object_detected = False

    check, frame = video.read()
    
    time_now = datetime.now()
    
    formatted_time = datetime.strftime( time_now, "%d, %m, %y %H:%M:%S" )
    formatted_filename = f"motion_capture_{datetime.strftime( time_now, "%d%m%y%H%M%S")}.png"
    
    cv2.putText( img = frame, text = formatted_time, org = (50,50), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 2, color = (200, 100, 20), thickness = 2, lineType = cv2.LINE_AA )
    
    grey_frame = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
    grey_frame_blur = cv2.GaussianBlur( grey_frame, (21, 21), 0)
    
    if first_frame is None:
        first_frame = grey_frame_blur
        
    delta_frame = cv2.absdiff( first_frame, grey_frame_blur )
    
    threshold_frame = cv2.threshold( delta_frame, 60, 255, cv2.THRESH_BINARY )[1]
    
    dilate_frame = cv2.dilate( threshold_frame, None, iterations = 2 ) # type: ignore
    
    contours, check = cv2.findContours( dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
    
    for contour in contours:
        if cv2.contourArea( contour ) < 5000:
            continue
        x, y, width, height = cv2.boundingRect( contour )
        rectangle = cv2.rectangle( frame, (x, y), (x + width, y + height), (0, 255, 0), 3 )
        
        if rectangle.any() == True and detected_time == None:
            cv2.imwrite( f"motion_captures/{formatted_filename}", frame )
            send_email( attachment_image_filename = f"motion_captures/{formatted_filename}" )
            detected_time = time_now
        try:
            time_delta = time_now - detected_time # type: ignore
            if time_delta.total_seconds() >= email_frequency_seconds:
                detected_time = None
        except:
            pass

    cv2.imshow( "Webcam video", frame )
    
    key = cv2.waitKey( 1 )
    if key == ord( "q" ):
        break

video.release()

shutil.rmtree( "motion_captures" )