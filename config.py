# config.py
import cv2
# ---------------------
# CAMERA CONFIGURATION
# ---------------------
CAMERA_INDEX = 0  # Default camera index
USE_CUSTOM_RESOLUTION = False  # Set to True to manually define resolution
SCALE_RESOLUTION = 0.5  # Scale factor for resolution (0.5 = half resolution)
CUSTOM_WIDTH = 480
CUSTOM_HEIGHT = 640
CUSTOM_RESOLUTION = (CUSTOM_WIDTH, CUSTOM_HEIGHT)

# ---------------------
# PID CONTROLLER CONFIGURATION
# ---------------------
PID_KP = 0.9         # Proportional gain
PID_KI = 0.005       # Integral gain
PID_KD = 0.1         # Derivative gain
INTEGRAL_LIMIT = 50  # Cap on the integral term to prevent wind-up

# ---------------------
# DETECTION CONFIGURATION
# ---------------------
# CENTER_X = 120       # Horizontal center for comparison (used in PID)
CENTER_OFFSET = 5    # Acceptable margin to consider object in center

# ---------------------
# DISPLAY CONFIGURATION
# ---------------------
SHOW_FRAME_DIMENSIONS = True  # Display dimensions on live video feed
SHOW_FPS = False
TEXT_FONT =  cv2.FONT_HERSHEY_SIMPLEX
TEXT_SCALE = 0.7
TEXT_COLOR = (0, 255, 0)
TEXT_THICKNESS = 2

# ---------------------
# ARDUINO CONFIGURATION (if needed in future)
# ---------------------
SERIAL_PORT = 'COM3'  # Or '/dev/ttyUSB0' for Linux
BAUD_RATE = 9600
