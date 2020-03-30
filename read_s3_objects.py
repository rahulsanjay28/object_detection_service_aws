import os

for file in os.listdir():
    if ".h264" in file:
        with open(file) as f:
            print(f.readline())