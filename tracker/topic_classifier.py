# tracker/topic_classifier.py

# -----------------------------
# Keywords to detect learning activities
# -----------------------------
TOPIC_MAP = {
    'Python': [
        'python',
        'pycharm64.exe', # IDE
        'code.exe'       # VS Code
    ],
    'Django': [
        'django'
    ],
    'Data Structures & Algorithms': [
        'leetcode',
        'neetcode',
        'hackerrank',
        'codewars',
        'data structures',
        'algorithms'
    ],
    'Web Development': [
        'w3schools',
        'freecodecamp',
        'stackoverflow'
    ],
    'General Learning': [
        'tutorial',
        'course',
        'lesson',
        'documentation',
        'doc',
        'guide',
        'geeksforgeeks',
        'medium',
        'udemy',
        'coursera'
    ],
    'Gemini': [ # You had this as a specific learning app
        'google gemini'
    ]
}

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
        return None

    name_lower = active_name.lower()

    # Check always learning apps/tabs first
    for topic,keywords in TOPIC_MAP.items():
        for keyword in keywords:
            if keyword in name_lower:
                return topic
    return None
