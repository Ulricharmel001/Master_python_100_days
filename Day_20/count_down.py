# event countdown timer using Python's datetime module
from datetime import datetime
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# step 1: get the event date and time from the user
def get_event_datetime():
    try:
        event_date_str = input("Enter the event date (YYYY-MM-DD): ")
        event_time_str = input("Enter the event time (HH:MM:SS): ")
        event_datetime_str = f"{event_date_str} {event_time_str}"
        event_datetime = datetime.strptime(
            event_datetime_str,
            "%Y-%m-%d %H:%M:%S"
        )
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

    print(
        f"Time remaining until the event: "
        f"{days} days, {hours} hours, "
        f"{minutes} minutes, {seconds} seconds"
    )

# main countdown loop to update the countdown timer every second
def countdown_loop(event_datetime):
    while True:
        time_remaining = calculate_time_remaining(event_datetime)

        if time_remaining.total_seconds() <= 0:
            print("The countdown has finished!")
            engine.say("The countdown has finished!")
            engine.runAndWait()
            break

        display_countdown(time_remaining)
        time.sleep(1)

def menu():
    print("Welcome to the Countdown Timer!")
    print("1. Set a single countdown timer")
    print("2. Set multiple countdown timers")
    print("3. Exit")

# all countdown timers run together in a list format
def set_multiple_countdowns():
    countdowns = []

    while True:
        event_datetime = get_event_datetime()
        countdowns.append(event_datetime)

        more = input(
            "Do you want to set another countdown timer? (yes/no): "
        )

        if more.lower() != "yes":
            break

    return countdowns

# main function to run the countdown timer
while True:
    menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        event_datetime = get_event_datetime()
        countdown_loop(event_datetime)

    elif choice == "2":
        countdowns = set_multiple_countdowns()

        while countdowns:
            print("\n" + "=" * 60)

            finished_countdowns = []

            for event_datetime in countdowns:
                print(f"Countdown for event on {event_datetime}:")

                time_remaining = calculate_time_remaining(
                    event_datetime
                )

                if time_remaining.total_seconds() <= 0:
                    print("The countdown has finished!")

                    engine.say(
                        "The countdown has finished!"
                    )
                    engine.runAndWait()

                    finished_countdowns.append(
                        event_datetime
                    )
                else:
                    display_countdown(
                        time_remaining
                    )

            for countdown in finished_countdowns:
                countdowns.remove(countdown)

            time.sleep(1)

        print("All countdown timers have finished!")

    elif choice == "3":
        print("Exiting the Countdown Timer. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")