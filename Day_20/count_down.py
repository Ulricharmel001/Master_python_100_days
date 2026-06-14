# event countdown timer using Python's datetime module
from datetime import datetime
import time

# step 1: get the event date and time from the user
def get_event_datetime():
    try:
        event_date_str = input("Enter the event date (YYYY-MM-DD): ")
        event_time_str = input("Enter the event time (HH:MM:SS): ")
        event_datetime_str = f"{event_date_str} {event_time_str}"
        event_datetime = datetime.strptime(event_datetime_str, "%Y-%m-%d %H:%M:%S")
        return event_datetime
    except ValueError:
        print("Invalid date or time format. Please try again.")
        return get_event_datetime()
    
# step 2: calculate the time remaining until the event
def calculate_time_remaining(event_datetime):
    current_datetime = datetime.now()
    time_remaining = event_datetime - current_datetime
    return time_remaining

# step 3: display the countdown timer
def display_countdown(time_remaining):
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time remaining until the event: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# main countdown loop to update the countdown timer every second
def countdown_loop(event_datetime):
    while True:
        time_remaining = calculate_time_remaining(event_datetime)
        if time_remaining.total_seconds() <= 0:
            print("The event has started!")
            break
        display_countdown(time_remaining)
        time.sleep(1)
# main function to run the countdown timer
while True:
    event_datetime = get_event_datetime()
    countdown_loop(event_datetime)
    restart = input("Do you want to set another countdown? (yes/no): ")
    if restart.lower() != "yes":
        print("Exiting the countdown timer. Goodbye!")
        break