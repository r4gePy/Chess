import time
seconds = 50
minutes = 59
hours = 0
while True:
    seconds += 1
    time.sleep(1)
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    print(str(hours)+":"+str(minutes)+":"+str(seconds))
