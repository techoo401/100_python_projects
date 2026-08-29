from datetime import datetime
import time

print("Press CTRL + C to exit")
try:
    while True:
        current_time = datetime.now()

        print(
            current_time.strftime("%H:%M:%S"),
            end="\r",
            flush=True
        )

        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram exited.")