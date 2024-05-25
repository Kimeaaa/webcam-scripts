import cv2

def find_connected_cameras():
    # Initialize an empty list to hold active camera indices
    active_cameras = []
    index = 0
    # Try a large range to ensure you don't miss any potential camera
    while index < 10:  # You can increase this limit if you expect more cameras
        # Try to open the camera
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            # If the camera opens successfully, add the index to the list
            print(f"Camera found at index {index}")
            active_cameras.append(index)
            cap.release()
        index += 1

    return active_cameras

# Get the list of connected cameras
cameras = find_connected_cameras()

# Print the list of active camera indices
print("Active cameras indices:", cameras)
