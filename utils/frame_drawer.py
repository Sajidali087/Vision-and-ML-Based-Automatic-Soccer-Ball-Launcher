# frame_drawer.py
import cv2
from config import TEXT_FONT, SHOW_FPS
def draw_and_annotate_frame(frame, detected_center_x, h, distance_in_m, distance_in_ft, angle, scale, fps):
    # Annotating the frame with relevant information
    if detected_center_x is not None:
        # Drawing the detection-related information on the frame
        cv2.putText(frame, f'Distance: {distance_in_m:.2f}m, {distance_in_ft:.2f}ft', (10, 140),
                    TEXT_FONT, 0.5, (255, 0, 0), 1)
        cv2.putText(frame, f'Height: {h * scale}px', (10, 170),
                    TEXT_FONT, 0.5, (255, 0, 0), 1)
        print(f'Pixel height {h * 2} px, Distance: {distance_in_m} m')
    
    # Annotating FPS and angle
    if SHOW_FPS:
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 80), TEXT_FONT, 0.5, (255, 0, 0), 1)
    cv2.putText(frame, f'Angle: {angle:.2f}°', (10, 110), TEXT_FONT, 0.5, (255, 0, 0), 1)

    return frame
