import psutil
import win32gui
import win32process

# -----------------------------
# List of work apps (process names)
# -----------------------------
WORK_APPS = [
    'pycharm64.exe',  # PyCharm IDE
    'code.exe',       # VS Code
    'chrome.exe',     # Chrome browser
    'python.exe'      # Python scripts running
]

# -----------------------------
# Function: Get active window process name
# -----------------------------
def get_active_window_process_name():
    """
    Returns the process name of the currently active window (Windows only)
    """
    try:
        hwnd = win32gui.GetForegroundWindow()  # Get focused window handle
        _, pid = win32process.GetWindowThreadProcessId(hwnd)  # Get PID
        proc = psutil.Process(pid)
        return proc.name(), hwnd
    except Exception:
        return None, None

# -----------------------------
# Function: Get Chrome tab title
# -----------------------------
def get_chrome_tab_title(hwnd):
    """
    Returns the active Chrome tab title from the window handle
    """
    try:
        # Get the window title text
        window_title = win32gui.GetWindowText(hwnd)
        if window_title:
            # Remove the "- Google Chrome" suffix
            if " - Google Chrome" in window_title:
                window_title = window_title.split(" - Google Chrome")[0]
            return window_title.strip()
        return None
    except Exception:
        return None

# -----------------------------
# Function: Check if user is actively working
# -----------------------------
def is_actively_working():
    """
    Returns:
        (bool, str) -> (Is working, Active process name or Chrome tab title)
    """
    proc_name, hwnd = get_active_window_process_name()

    if proc_name is None:
        return False, None

    proc_name_lower = proc_name.lower()

    if proc_name_lower not in [app.lower() for app in WORK_APPS]:
        # Not a tracked work app
        return False, proc_name

    # If Chrome, parse tab title
    if proc_name_lower == 'chrome.exe':
        tab_title = get_chrome_tab_title(hwnd)
        return True, tab_title if tab_title else "Chrome (Unknown Tab)"

    # For other work apps, just return process name
    return True, proc_name
