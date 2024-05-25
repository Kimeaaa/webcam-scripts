import cv2 
import schedule
import time
from datetime import datetime
import os


save_directory = '/Users/Username/Desktop/webcam-pics'
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Try each index and print if the webcam can be opened
def check_cameras():
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            cap.release()
            break
        print(f"Camera index {index} is available.")
        cap.release()
        index += 1

a = check_cameras()
print(a)



def capture_snapshot():
    # Specify the camera index for your USB webcam
    camera_index = 1  # Assuming 1 is the USB webcam and 0 is the built-in camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open USB webcam")
        return
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"snapshot_{timestamp}.png"
        filepath = os.path.join(save_directory, filename)
        cv2.imwrite(filepath, frame)
        print(f"Saved {filename} to {save_directory}")
    else:
        print("Failed to capture image from USB webcam")
    cap.release()




def run_scheduler():
    #schedule.every(1).minute.do(capture_snapshot)
    schedule.every(20).seconds.do(capture_snapshot)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Run the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

print("Scheduler started. Press Enter to stop.")
input()  # Wait for user to press Enter
schedule.clear()  # Stops all scheduled tasks
scheduler_thread.join()  # Wait for the scheduler thread to finish
print("Scheduler stopped.")