import tkinter as tk
import threading
from tracker.tracker_core import run_tracker
from analytics import get_summary_stats


window = tk.Tk()
window.title("10000 hour rule")
window.geometry("300x300")

#variables
tracker_thread=None
stop_event=None


#functions
def start_tracking():
    global tracker_thread, stop_event

    stop_event = threading.Event()

    tracker_thread = threading.Thread(target=run_tracker, args=(stop_event,schedule_label_update,))

    tracker_thread.start()
    status_label.config(text="Status:started")
    start_tracking_button.config(state="disabled")

def stop_tracking():
    global stop_event
    if stop_event:
        stop_event.set()
        status_label.config(text="Status:stopped")
        start_tracking_button.config(state="normal")

def update_status_label(message):
    status_label.config(text=message)

def schedule_label_update(message):
    window.after(0, update_status_label,message)

def show_stats():
    stats_string = get_summary_stats()
    stats_window = tk.Toplevel(window)
    stats_window.title("My stats")
    top_level_status_label = tk.Label(stats_window, text=stats_string,justify="left")
    top_level_status_label.pack(padx=10, pady=10)

#buttons
start_tracking_button = tk.Button(master=window,text="Start tracking",command=start_tracking)
stop_tracking_button = tk.Button(master=window,text="Stop tracking",command=stop_tracking)
view_status_button = tk.Button(master=window,text="View status",command=show_stats)



#labels
status_label = tk.Label(master=window,text="Status:stopped")

#alignment
status_label.pack(pady=10)
start_tracking_button.pack(pady=10)
stop_tracking_button.pack(pady=10)
view_status_button.pack(pady=10)





window.mainloop()
