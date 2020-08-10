# recursive countdown timer
import time
def rec_timer(z):
    if z == 0:
        return z
    else:
        print(z)
        time.sleep(1)
        z -=1
        return rec_timer(z)

value = 5
rec_timer(value)