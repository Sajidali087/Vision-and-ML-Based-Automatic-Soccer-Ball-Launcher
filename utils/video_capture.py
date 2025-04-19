# utils/video_capture.py

import cv2
from config import CUSTOM_RESOLUTION, CAMERA_INDEX, SHOW_FRAME_DIMENSIONS, TEXT_FONT

def capture_frames(device_index=CAMERA_INDEX):
    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        raise IOError(f"[ERROR] Could not open camera at index {device_index}.")

    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to read frame from camera.")
                break

            frame = cv2.resize(frame, CUSTOM_RESOLUTION)

            if SHOW_FRAME_DIMENSIONS:
                cv2.putText(frame, f'Original: {original_width}x{original_height}',
                            (10, 30), TEXT_FONT, 0.5, (0, 255, 0), 1)
                cv2.putText(frame, f'Scaled: {CUSTOM_RESOLUTION[0]}x{CUSTOM_RESOLUTION[1]}',
                            (10, 50), TEXT_FONT, 0.5, (0, 255, 0), 1)

            yield frame
    finally:
        cap.release()
        cv2.destroyAllWindows()


# Optional testing block
if __name__ == "__main__":
    try:
        for frame in capture_frames():
            cv2.imshow("Camera Feed - Generator Test", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        cv2.destroyAllWindows()
