import cv2

# Global variable to hold frame dimensions
frame_dimensions = (0, 0)
frame_width = 240
frame_height = 320
def capture_frames(device_index=0):
    global frame_dimensions

    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        raise IOError(f"[ERROR] Could not open camera at index {device_index}.")

    # Get the actual resolution set by the camera (without requesting a specific resolution)
    actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_dimensions = (actual_width, actual_height)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to read frame from camera.")
                break
            framescaled = (frame_width, frame_height)
            frame = cv2.resize(frame, framescaled)
            # Draw original frame dimensions on the video feed
            cv2.putText(frame, f'Original Dimensions: {frame_dimensions[0]}x{frame_dimensions[1]}',
                        (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(frame, f'scaled dimensions: {framescaled}',
                        (0, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            yield frame
    finally:
        cap.release()
        cv2.destroyAllWindows()
