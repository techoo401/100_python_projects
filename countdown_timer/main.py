from playsound3 import playsound
import time

print("Set Timer")

while True:
    try:
        hour = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))

        if hour < 0 or minutes < 0 or seconds < 0:
            print("Time cannot be negative.")
            continue

        if hour == 0 and minutes == 0 and seconds == 0:
            print("Timer must be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter numbers only.")

total_seconds = (hour * 3600) + (minutes * 60) + seconds

while total_seconds > 0:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r", flush=True)

    time.sleep(1)
    total_seconds -= 1

print("00:00:00")
playsound("song.mp3")