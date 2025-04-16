import tkinter as tk
import math
import UI.log_panel as log_panel
current_angle = 0  # Global variable to store angle

def create_angle_meter_gui():
    # Create the frame for the angle meter
    master = tk.Frame()  # This is a Frame, not a Tk window
    canvas_width = 500
    canvas_height = 400

    # Create the scale slider for rotating the arrow
    slider = tk.Scale(master, from_=0, to=180, orient="horizontal", length=400, showvalue=False, command=lambda val: update_arrow_from_slider(val))
    slider.set(0)  # Initial position of the slider
    slider.pack(pady=10)

    # Create the canvas widget inside the frame
    canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Create the "Angle Meter" label at the top of the window
    canvas.create_text(canvas_width // 2, 20, text="Angle Meter", font=("Arial", 20, "bold"))

    # Create the initial angle label (which will be updated later)
    angle_label = canvas.create_text(canvas_width // 2, 60, text="Angle: 0°", font=("Arial", 12, "bold"), fill="red")

    # Circle configuration
    center_x = canvas_width // 2
    center_y = canvas_height // 2 + 100  # Adjusting center to make space for the angle meter text
    radius = 150  # Radius of the circle

    # Draw the semi-circle (top half only)
    canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                      start=0, extent=180, outline="black", width=3)

    # Draw the numbers along the arc (reversed from 45 to 0)
    num_marks = 9  # Dividing the semi-circle into 9 parts for multiples of 5
    for i in range(num_marks + 1):
        angle = (180 / num_marks) * i
        x = center_x + (radius + 20) * math.cos(math.radians(angle))
        y = center_y - (radius + 20) * math.sin(math.radians(angle))
        label_angle = 45 - (i * 5)  # Start from 45 and decrease by 5 for each step
        canvas.create_text(x, y, text=f"{label_angle}", font=("Arial", 12))

    # Draw the smaller and larger markings along the arc
    for angle in range(46):  # From 0 to 45 degrees
        angle_rad = math.radians(angle * 4)  # scale the range 0-45 to 0-180 degrees
        x_start = center_x + radius * math.cos(angle_rad)
        y_start = center_y - radius * math.sin(angle_rad)
        
        if angle % 5 == 0:
            length = 10  # Larger mark length
        else:
            length = 5  # Smaller mark length
        
        x_end = center_x + (radius - length) * math.cos(angle_rad)
        y_end = center_y - (radius - length) * math.sin(angle_rad)
        canvas.create_line(x_start, y_start, x_end, y_end, width=2)

    # Initial angle for the arrow (pointing upwards)
    arrow_angle = 90
    arrow_length = radius - 10  # Adjust the length to leave a small gap at the end

    # Function to draw the arrow
    def draw_arrow(angle):
        canvas.delete("arrow")
        arrow_x_end = center_x + arrow_length * math.cos(math.radians(angle))
        arrow_y_end = center_y - arrow_length * math.sin(math.radians(angle))
        canvas.create_line(center_x, center_y, arrow_x_end, arrow_y_end, arrow=tk.LAST, fill="red", width=2, tags="arrow")
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black", tags="arrow")
        angle_value = 180 - angle   # Convert the angle to 0-45 degree scale
        canvas.itemconfig(angle_label, text=f"Angle: {int(angle_value)/4}°")  # Update the angle value text

    # Function to update the arrow based on the slider value
    def update_arrow_from_slider(val):
        global current_angle
        angle = float(val)
        current_angle = angle
        draw_arrow(180 - angle)  # Convert 0-45 range to 180-135 degree range for clockwise rotation
        log_panel.log_message(f"[INFO] Angle set to {current_angle/4:.1f} degree")
        return angle
    # Return the frame containing the angle meter and the slider
    return master

def get_current_angle():
    return current_angle
