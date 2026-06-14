from datetime import datetime

current_time = datetime.now()
print("Current date and time:", current_time)

event_time = datetime(2026, 8, 31, 23, 59, 59)
time_difference = event_time - current_time
print("Time remaining until the event:", time_difference)

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted current date and time:", formatted_time)
