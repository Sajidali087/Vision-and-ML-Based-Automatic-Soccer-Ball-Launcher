# frame_drawer.py
import cv2
import threading
from config import TEXT_FONT, SHOW_FPS
from monitor import monitor  # Assuming you have a monitor function in monitor.py   

def draw_and_annotate_frame(frame, detected_center_x, h, distance_in_m, distance_in_ft, angle, fps):
    # Annotating the frame with relevant information
    # if detected_center_x is not None:
        # Drawing the detection-related information on the frame
    cv2.putText(frame, f'Distance: {distance_in_m:.2f}m, {distance_in_ft:.2f}ft', (10, 140),
                TEXT_FONT, 0.5, (255, 0, 0), 1)
    cv2.putText(frame, f'Height: {h}px', (10, 170),
                TEXT_FONT, 0.5, (255, 0, 0), 1)
    print(f'Pixel height {h} px, Distance: {distance_in_m} m')
        
    
    # Annotating FPS and angle
    if SHOW_FPS:
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 80), TEXT_FONT, 0.5, (255, 0, 0), 1)
    cv2.putText(frame, f'Angle: {angle:.2f}°', (10, 110), TEXT_FONT, 0.5, (255, 0, 0), 1)
    threading.Thread(target=monitor, daemon=True).start()
    # monitor()  # Call the monitor function to print shared state information
    return frame
