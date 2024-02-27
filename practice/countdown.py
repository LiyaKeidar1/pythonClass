import time

def countdown(t:int):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins}:{secs}"
        # timer = f'{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("timer completed")

t = input('Enter the time in seconds: ')

countdown(int(t))

