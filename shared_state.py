# shared_state.py
predicted_distance = 0.0
fps = 0.0
# Real-time detection values (default)
person_detected = False
person_height = 0
person_height_norm = 0.0
video_width = 0
video_height = 0
person_center_x = None
distance_m = 0
distance_ft = 0


# shared values from adjust_orientation.py
frame_center_x = 0
detected_center_x = 0
pid_output = 0.0
person_in_front = False
