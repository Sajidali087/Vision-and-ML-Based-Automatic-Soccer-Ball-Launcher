# Importing the PID gain values and integral limit from config.py
from config import PID_KP, PID_KI, PID_KD, INTEGRAL_LIMIT

class PIDController:
    def __init__(self, PID_KP, PID_KI, PID_KD, INTEGRAL_LIMIT):
        self.Kp = PID_KP
        self.Ki = PID_KI
        self.Kd = PID_KD

        self.prev_error = 0
        self.integral = 0
        self.integral_limit = INTEGRAL_LIMIT

    def compute(self, setpoint, input_value, frame_width):
        # Raw error
        error = input_value - setpoint

        # Normalize error: map range [-frame_width/2, frame_width/2] -> [-255, 255]
        max_error = frame_width // 2
        normalized_error = (error / max_error) * 255
        normalized_error = max(min(normalized_error, 255), -255)

        # PID calculations based on normalized error
        self.integral += normalized_error
        self.integral = max(min(self.integral, self.integral_limit), -self.integral_limit)

        derivative = normalized_error - self.prev_error
        self.prev_error = normalized_error

        output = (self.Kp * normalized_error) + (self.Ki * self.integral) + (self.Kd * derivative)

        return max(min(output, 255), -255)


# Test PIDController
if __name__ == "__main__":
    # Initialize the PID controller with values from config.py
    pid = PIDController(PID_KP, PID_KI, PID_KD, INTEGRAL_LIMIT)

    # Example parameters
    setpoint = 120  # Desired value (center of frame)
    input_values = [100, 110, 120, 130, 140]  # Example input values from the system
    frame_width = 240  # Width of the frame for normalization

    print("Testing PID Controller:")
    for input_value in input_values:
        output = pid.compute(setpoint, input_value, frame_width)
        print(f"Input Value: {input_value}, PID Output: {output}")
