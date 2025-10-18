import time
from tracker.activity_detector import is_actively_working
from tracker.idle_detector import is_idle
from tracker.topic_classifier import is_learning_activity

# Idle threshold in seconds
IDLE_THRESHOLD = 120


def run_tracker():
    """
    Main tracker loop. Continuously checks active window,
    idle status, classifies learning, and logs to Excel.
    """
    print("10,000 Hour Tracker Started. Press Ctrl+C to stop.")

    try:
        while True:
            # 1️⃣ Check if user is idle
            if not is_idle(IDLE_THRESHOLD):
                # 2️⃣ Get active window or Chrome tab title properly
                working, active_name = is_actively_working()

                # 3️⃣ Classify learning activity
                learning, topic = is_learning_activity(active_name)

                # 4️⃣ Log to Excel (we’ll implement this later)

                # 5️⃣ Debug print
                print(f"Working: {working}, Active: {active_name}, Learning: {learning}, Topic: {topic}")
            else:
                print("User is idle, tracker paused.")

            time.sleep(2)  # Check every 2 seconds
    except KeyboardInterrupt:
        print("Tracker stopped by user.")
