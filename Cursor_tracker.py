import pyautogui

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()

        # Print the coordinates
        print(f"X: {x}, Y: {y}", end="\r")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
