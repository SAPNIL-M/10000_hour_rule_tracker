# tracker/topic_classifier.py

# -----------------------------
# Keywords to detect learning activities
# -----------------------------
LEARNING_KEYWORDS = [
    'tutorial', 'course', 'lesson', 'documentation', 'doc', 'guide',
    'course', 'stackoverflow', 'geeksforgeeks', 'medium', 'python', 'django','leetcode','neetcode',
    'khan academy', 'edx', 'coursera', 'udemy', 'pluralsight', 'udacity',
    'freecodecamp', 'w3schools', 'hackerrank', 'codewars', 'codecademy',
    'data structures', 'algorithms', 'machine learning', 'artificial intelligence',
]

# -----------------------------
# Apps or tabs that are always considered learning
# -----------------------------
ALWAYS_LEARNING = [
    'pycharm64.exe',   # PyCharm IDE
    'code.exe',        # VS Code
    'python.exe',      # Python scripts
    'google gemini'    # Google Gemini tabs
]

# -----------------------------
# Function: Check if a tab title or app name is learning
# -----------------------------
def is_learning_activity(active_name):
    """
    Determines whether the current active window or Chrome tab
    represents a learning activity.

    Args:
        active_name (str): The process name or tab title

    Returns:
        (bool, str): (Is learning, topic name)
    """
    if active_name is None:
        return False, None

    name_lower = active_name.lower()

    # Check always learning apps/tabs first
    if any(keyword in name_lower for keyword in ALWAYS_LEARNING):
        return True, active_name

    # For Chrome tabs, check if the tab title contains learning keywords
    for keyword in LEARNING_KEYWORDS:
        if keyword in name_lower:
            return True, active_name

    # Otherwise, not a learning activity
    return False, active_name
