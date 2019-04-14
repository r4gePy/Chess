import time
seconds = 0
minutes = 0
while True:
    seconds += 1
    time.sleep(1)
    if seconds == 61:
        minutes += 1
        seconds = 0
    print(str(minutes)+":"+str(seconds))
