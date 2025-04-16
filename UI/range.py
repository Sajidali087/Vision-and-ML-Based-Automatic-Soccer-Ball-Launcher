import tkinter as tk
import random
import UI.log_panel as log_panel


# In range.py
# Shared global values
launch_speed = 0
selected_distance = 0.0

def update_distance_label(speed):
    global launch_speed
    launch_speed = speed

def get_current_distance():
        return selected_distance

def create_distance_control_gui():
    frame = tk.Frame(bg="white")

    # Title
    title_label = tk.Label(
        frame,
        text="Launch Control Panel",
        font=("Helvetica", 18, "bold"),
        bg="white",
        fg="black"
    )
    title_label.pack(pady=(10, 0), padx=10, fill="x")

    center_frame = tk.Frame(frame, bg="white")
    center_frame.pack(anchor="w", padx=10, pady=35)

    # User input + dropdown
    tk.Label(center_frame, text="Enter Target Distance (m):", font=("Arial", 12), bg="white", anchor="w").grid(row=0, column=0, pady=5, padx=5, sticky="w")

    distance_entry = tk.Entry(center_frame, font=("Arial", 12), width=10)
    distance_entry.grid(row=0, column=1, padx=5, pady=10, sticky="w")

    tk.Label(center_frame, text="or select:", font=("Arial", 12), bg="white").grid(row=0, column=2, padx=5, sticky="w")

    selected_int = tk.IntVar(value=5)
    distance_dropdown = tk.OptionMenu(center_frame, selected_int, *range(5, 26))
    distance_dropdown.config(font=("Arial", 11), width=5)
    distance_dropdown.grid(row=0, column=3, padx=5, sticky="w")

    # Output variables
    selected_dist_var = tk.StringVar(value="Launching Range in meters (m): 0.0")
    speed_var = tk.StringVar(value="Launch Speed: 0.00 m/s")
    tof_var = tk.StringVar(value="Time of Flight: 0.00 s")
    angle_var = tk.StringVar(value="Launch Angle: 0.00°")

    def set_distance():
        global selected_distance, launch_speed
        try:
            entry_val = distance_entry.get()
            if entry_val:
                selected_distance = float(entry_val)
            else:
                selected_distance = float(selected_int.get())
        except ValueError:
            selected_distance = 0.0

        # Random values instead of calculations
        launch_speed = round(random.uniform(10, 30), 2)
        time_of_flight = round(random.uniform(1.5, 4.5), 2)
        angle = round(random.uniform(30, 60), 2)

        selected_dist_var.set(f"Launching Range in meters (m): {selected_distance:.1f}")
        log_panel.log_message(f"[INFO] Distance set to {selected_distance:.1f} m")
        speed_var.set(f"Launch Speed: {launch_speed:.2f} m/s")
        log_panel.log_message(f"[INFO] Launch speed: {launch_speed:.2f} m/s | TOF: {time_of_flight:.2f}s | Angle: {angle:.2f}°")
        tof_var.set(f"Time of Flight: {time_of_flight:.2f} s")
        angle_var.set(f"Launch Angle: {angle:.2f}°")

    # Button to trigger distance selection
    set_button = tk.Button(center_frame, text="Set Distance", command=set_distance, font=("Arial", 11), bg="#4CAF50", fg="white")
    set_button.grid(row=0, column=4, padx=5, sticky="w")

    # Output display labels
    for i, var in enumerate([selected_dist_var, speed_var, tof_var, angle_var]):
        tk.Label(center_frame, textvariable=var, font=("Arial", 12), fg="black", bg="white", anchor="w", justify="left")\
            .grid(row=i+1, column=0, columnspan=5, sticky="w", pady=2)

    # ✅ Function to return current distanc

    return frame
