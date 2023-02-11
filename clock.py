import datetime
import os
import time

while True:
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    week_day = now.strftime("%A")
    hour = now.hour
    minute = now.minute
    second = now.second
    os.system("clear") # Sadece Unix benzeri sistemlerde çalışır, Windows için "cls" kullanılabilir.
    print("-" * 28)
    print(f"| Date: {day}/{month}/{year}")
    print(f"| Day of the Week: {week_day}")
    print(f"| Time: {hour}:{minute}:{second}")
    print("-" * 28)
    time.sleep(1)

