import cv2
import time
from emailing import send_email

video = cv2.VideoCapture( 0 )
time.sleep( 1 )

first_frame = None

while True:
    
    check, frame = video.read()
    
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
        if rectangle.any():
            send_email()
    
    
    cv2.imshow( "Webcam video", frame )
    
    key = cv2.waitKey( 1 )
    
    if key == ord( "q" ):
        break

video.release()