
print("\033[1;32mpython") #\033[1,32n

import time

for number in range(10):
    print(f'\033[1;3{number+1}mnumber,end="\r')
    time.sleep(0.5)