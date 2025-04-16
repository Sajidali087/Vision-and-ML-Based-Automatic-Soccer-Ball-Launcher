class PIDController:
    def __init__(self, Kp, Ki, Kd, integral_limit=100):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0
        self.integral_limit = integral_limit

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
