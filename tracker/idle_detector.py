# tracker/idle_detector.py

import ctypes
import time

# Windows structure for getting last input info
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ctypes.c_uint),
        ('dwTime', ctypes.c_uint)
    ]

def get_idle_duration():
    """
    Returns the idle time in seconds since last user input (mouse/keyboard)
    """
    liinfo = LASTINPUTINFO()
    liinfo.cbSize = ctypes.sizeof(LASTINPUTINFO)

    # Call Windows API
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(liinfo))
    milliseconds = ctypes.windll.kernel32.GetTickCount() - liinfo.dwTime
    seconds = milliseconds / 1000.0
    return seconds

def is_idle(threshold=120):
    """
    Determines if the user is idle.

    Args:
        threshold (int): Idle time in seconds to consider user idle

    Returns:
        bool: True if idle, False otherwise
    """
    idle_time = get_idle_duration()
    return idle_time >= threshold

# -----------------------------
# Quick test
# -----------------------------
if __name__ == "__main__":
    while True:
        idle_seconds = get_idle_duration()
        idle_status = is_idle()
        print(f"Idle: {idle_status}, Idle seconds: {int(idle_seconds)}")
        time.sleep(2)
