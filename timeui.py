import time
start_time = time.time()  # Get the current time in seconds
while True:
    current_time = time.time() - start_time  # Calculate elapsed time
    if current_time >= 300:  # 300 seconds = 5 minutes
        print("Timer reached 5 minutes. Resetting to 0.")
        start_time = time.time()  # Reset the timer
    print(f"Elapsed time: {current_time:.2f} seconds")
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage