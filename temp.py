# import subprocess
import os
# output = subprocess.check_output(["./darknet", "detector", "demo", "cfg/coco.data", "cfg/yolov3-tiny.cfg",
#                                   "yolov3-tiny.weights", 'sample1.h264'])
# print("Rahul Sanjay")
# s = set()
# for line in output.splitlines():
#     if "%" in line:
#         l = line.split(':')
#         s.add(l[0])
#
# print(str(s))

# output = subprocess.check_output('ps')
# for line in output.decode('utf-8').splitlines():
#     if 'darknet' in line:
#         l = line.split()
#         pid = l[0]

# path = "/home/pi/darknet/videos_currently_processing/sample1.h264"
# l = path.split('/')
# print(l[-1])
# os.system("Xvfb :1 & export DISPLAY=:1")

no_gui_flag = False
output = subprocess.check_output('ps')
for line in output.decode('utf-8').splitlines():
    if 'Xvfb' in line and 'Killed' not in line:
        l = line.split()
        no_gui_flag = True
        pid = l[0]
        break
if not no_gui_flag:
    print("enabling no gui")
    subprocess.call(['sudo','Xvfb',':1','&','export','DISPLAY=:1'])
else:
    print("no gui already enabled")