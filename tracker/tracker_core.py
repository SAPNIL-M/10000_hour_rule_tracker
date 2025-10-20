import time
from tracker.activity_detector import is_actively_working
from tracker.idle_detector import is_idle
from tracker.topic_classifier import get_topic_from_activity
from tracker.logger import log_session
import threading

# Idle threshold in seconds
IDLE_THRESHOLD = 60


def run_tracker(stop_event,update_callback):
    update_callback("10,000 Hour Tracker Started. Press Ctrl+C to stop.")
    current_activity = None
    session_start_time = time.time()

    while not stop_event.is_set():

        if is_idle(IDLE_THRESHOLD):
            new_activity = "Idle"
        else:
            working, active_name = is_actively_working()

            if not working:
                new_activity = "Distraction"
            else:
                topic = get_topic_from_activity(active_name)

                if topic is not None:
                    new_activity = topic
                else:
                    new_activity = "General learning"

        if new_activity != current_activity:

            if current_activity is not None and current_activity not in ["Idle", "Distraction", "General learning"]:
                duration = time.time() - session_start_time

                if duration > 10:
                    log_session(current_activity, duration)


            update_callback(f"--- New Session Started: {new_activity} ---")
            current_activity = new_activity
            session_start_time = time.time()

        update_callback(f"Active: {current_activity}")
        stop_event.wait(2)  # Check every 2 seconds

    if current_activity is not None and current_activity not in ["Idle", "Distraction", "General learning"]:
        duration = time.time() - session_start_time
        if duration > 10:
            log_session(current_activity, duration)


    update_callback(f"\nFinal session logged. Goodbye.")