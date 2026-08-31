from datetime import datetime, timedelta
import time
from playsound3 import playsound

print("Enter Alarm Time")

# Get valid hour
while True:
    try:
        hour = int(input("Enter hour of time (1-12): "))

        if 1 <= hour <= 12:
            break

        print("Hour must be between 1 and 12.")

    except ValueError:
        print("Please enter a number.")


# Get valid minute
while True:
    try:
        minute = int(input("Enter minute of time (0-59): "))

        if 0 <= minute <= 59:
            break

        print("Minute must be between 0 and 59.")

    except ValueError:
        print("Please enter a number.")


# Get valid second
while True:
    try:
        second = int(input("Enter second of time (0-59): "))

        if 0 <= second <= 59:
            break

        print("Second must be between 0 and 59.")

    except ValueError:
        print("Please enter a number.")


# Get AM/PM
while True:
    _p = input("AM or PM: ").upper()

    if _p in ("AM", "PM"):
        break

    print("Please enter AM or PM.")


now = datetime.now()

# Convert 12-hour time to 24-hour time
if _p == "PM" and hour != 12:
    hour += 12

if _p == "AM" and hour == 12:
    hour = 0


# Create alarm time
alarm = now.replace(
    hour=hour,
    minute=minute,
    second=second,
    microsecond=0
)


# If alarm time already passed, set it for tomorrow
if alarm <= now:
    alarm += timedelta(days=1)


# Calculate remaining time
remaining = alarm - now

print()
print("Alarm set for:", alarm.strftime("%I:%M:%S %p"))
print("Time remaining:", remaining)
print()
print("Press Ctrl+C to stop the alarm.")


try:
    # Wait until alarm
    time.sleep(remaining.total_seconds())

    print("\nALARM!")

    # Keep playing until Ctrl+C
    while True:
        playsound("sound.mp3")

except KeyboardInterrupt:
    print("\nAlarm stopped.")