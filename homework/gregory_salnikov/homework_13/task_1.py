import os
from datetime import datetime, timedelta


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '..', '..', 'eugene_okulik', 'hw_13', 'data.txt')


def process_dates():
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(' - ')
            num_date, action = parts[0].split('. ', 1)
            num = int(num_date)

            try:
                date_str = ' '.join(action.split()[:2])
                date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                continue

            if num == 1:
                new_date = date + timedelta(weeks=1)
                print(f"1. {new_date}")
            elif num == 2:
                weekday = date.strftime('%A')
                print(f"2. {weekday}")
            elif num == 3:
                days_ago = (datetime.now() - date).days
                print(f"3. {days_ago}")


process_dates()
