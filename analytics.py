from collections import defaultdict

import pandas as pd
from collections import defaultdict




def get_summary_stats():
    output_lines=[]
    try:
        df = pd.read_excel("data/10000_hour_log.xlsx")

        topic_minutes=df.groupby('Topic')['Duration (minutes)'].sum()
        total_minutes = df['Duration (minutes)'].sum()
        for topic,minutes in topic_minutes.items():
            hours = minutes/60
            output_lines.append( f"{topic}: {hours:.2f} hours")
        total_hours = total_minutes/60
        output_lines.append("\n------------------------\n")
        output_lines.append(f"Total hours: {total_hours:.2f} hours")
        return "\n".join(output_lines)
    except FileNotFoundError:
        return "unable to find file"
