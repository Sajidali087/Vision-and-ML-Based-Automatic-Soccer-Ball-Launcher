from utils.video_capture import capture_frames

def main():
    # mode = input("Select mode (manual/auto): ").strip().lower()
    mode = 'manual'

    if mode == "manual":
        print("[INFO] Running in MANUAL mode.")
        from manual import run_manual_mode
        run_manual_mode(capture_frames())  # Pass generator

    elif mode == "auto":
        print("[INFO] Running in AUTOMATIC mode.")
        # from auto import run_auto_mode
        # run_auto_mode(capture_frames())

    else:
        print("[ERROR] Invalid mode selected.")

if __name__ == "__main__":
    main()
