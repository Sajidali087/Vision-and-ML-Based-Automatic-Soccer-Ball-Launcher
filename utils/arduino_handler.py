# arduino_handler.py
import serial
import time

class ArduinoHandler:
    def __init__(self, port='COM3', baudrate=9600):
        try:
            self.arduino = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)
            print("[INFO] Arduino connected successfully.")
            while self.arduino.in_waiting > 0:
                self.arduino.readline()
            self.connected = True
        except Exception as e:
            print(f"[WARNING] Could not connect to Arduino: {e}")
            self.arduino = None  # <- Make sure the variable exists!
            self.connected = False

    def send_data(self, data):
        if self.connected:
            try:
                while self.arduino.in_waiting > 0:
                    self.arduino.readline()
                self.arduino.flushInput()
                self.arduino.write(f"{data:.2f}\n".encode())
                print(f"[INFO] PID Output: {data:.2f} sent to Arduino")
                if self.arduino.in_waiting > 0:
                    response = self.arduino.readline().decode().strip()
                    print(f"[Arduino] Response: [{response}]")
            except Exception as e:
                print(f"[WARNING] Error communicating with Arduino: {e}")
        else:
            print(f"[INFO] PID Output (simulated): {data:.2f}")
