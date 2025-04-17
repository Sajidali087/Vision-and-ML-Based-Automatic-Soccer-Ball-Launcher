import cv2
from config import CUSTOM_RESOLUTION, CAMERA_INDEX, SHOW_FRAME_DIMENSIONS,TEXT_FONT

# # Global variable to hold frame dimensions
# frame_width = 240
# frame_height = 320
# frame_dimensions = (0, 0)

def capture_frames(device_index=CAMERA_INDEX):
    global frame_dimensions

    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        raise IOError(f"[ERROR] Could not open camera at index {device_index}.")

    # Get the actual resolution set by the camera
    actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_dimensions = (actual_width, actual_height)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to read frame from camera.")
                break

            # Resize frame to custom resolution from config
            frame = cv2.resize(frame, (CUSTOM_RESOLUTION))  # Resize to half the custom resolution

            # Draw original and scaled dimensions on frame
            if SHOW_FRAME_DIMENSIONS:
                cv2.putText(frame, f'Original Dimensions: {frame_dimensions[0]}x{frame_dimensions[1]}',
                            (10, 30), TEXT_FONT, 0.5, (0, 255, 0), 1)
                cv2.putText(frame, f'Scaled Dimensions: {CUSTOM_RESOLUTION[0]}x{CUSTOM_RESOLUTION[1]}',
                            (10, 50), TEXT_FONT, 0.5, (0, 255, 0), 1)

            yield frame
    finally:
        cap.release()
        cv2.destroyAllWindows()


# -------------- 🔍 Test the capture_frames function ------------------
if __name__ == "__main__":
    try:
        for frame in capture_frames():
            cv2.imshow("Camera Feed - Test", frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        cv2.destroyAllWindows()
