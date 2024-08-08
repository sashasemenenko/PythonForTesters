from datetime import date, datetime, timedelta

d = date(2023, 8, 15)

dt = datetime(2024, 8, 8, 18, 30, 15)

current_dt = datetime.now()

formatted_date = dt.strftime("%B %d, %Y, %H:%M:%S")
print(formatted_date)

dt_string = "2024-08-8 12:11:15"
parsed_date = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)

td = timedelta(days=5)

new_date = current_dt + td
print(current_dt)
print(new_date)