import pandas as pd
import os
from datetime import datetime

LOG_FILE = 'data/10000_hour_log.xlsx'

COLUMNS = ['Date','Topic','Duration (minutes)']

def log_session(topic,duration_seconds):
    today_date=datetime.now().strftime('%Y-%m-%d')

    duration_to_add_min = round(duration_seconds/60,2)

    os.makedirs(
    os.path.dirname(LOG_FILE), exist_ok=True
    )

    try:
        df=pd.read_excel(LOG_FILE)
    except FileNotFoundError:
        df=pd.DataFrame(columns=COLUMNS)
    except Exception as e:
        print(f"Error reading log file: {e}")
        return

    mask = (df['Date'] == today_date) & (df['Topic'] == topic)
    row_to_update = df[mask]

    if not row_to_update.empty:

        index_to_update = row_to_update.index[0]

        old_duration_min = df.loc[index_to_update,'Duration (minutes)']

        new_duration_min = old_duration_min + duration_to_add_min

        df.loc[index_to_update,'Duration (minutes)'] = round(new_duration_min,2)

        print(f"[Logger] Updated {topic}:added {duration_to_add_min} minutes, total today: {round(new_duration_min,2)} minutes")

    else:
        new_data={
            'Date':[today_date],
            'Topic':[topic],
            'Duration (minutes)':[duration_to_add_min]
        }

        new_row_df=pd.DataFrame(new_data)

        df=pd.concat([df,new_row_df],ignore_index=True)
        print(f"[Logger] Logged new topic {topic}: {duration_to_add_min} minutes")

    try:
        df.to_excel(LOG_FILE,index=False)
    except PermissionError:
        print(f"Error: Unable to write to log file. Please close {LOG_FILE} if it's open and try again.")
        print(f"please close the file and try again.")
    except Exception as e:
        print(f"Error writing to log file: {e}")