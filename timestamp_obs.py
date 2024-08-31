# Description: This script writes the current time to a file every second.

import time

while True:
    with open("/Users/emmakozmer/Desktop/UNI/ProAmbition/recording/timestamp.txt", "w") as file:
        file.write(time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
