import shared_state

def monitor():
    print("====== SHARED STATE ======")
    print(f"Person Detected: {shared_state.person_detected}")
    print(f"Person Height: {shared_state.person_height}")
    print(f"Person Height normalized: {shared_state.person_height_norm}")
    print(f"Person Center X: {shared_state.person_center_x}")
    print(f"Video Dimensions: {shared_state.video_width} x {shared_state.video_height}")
    print(f"Distance: {shared_state.distance_m:.2f} m | {shared_state.distance_ft:.2f} ft")
    print(f"Frame Center X: {shared_state.frame_center_x}")
    print(f"Detected Center X: {shared_state.detected_center_x}")
    print(f"PID Output: {shared_state.pid_output:.2f}")
    print(f"Person in Front: {shared_state.person_in_front}")
    print(f"FPS: {shared_state.fps:.2f}")
    print("==========================")
