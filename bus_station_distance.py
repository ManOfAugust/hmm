import numpy as np
from dateutil.parser import parse

new = []

time_diff = []
stop = []
time_diff = []

for _ in range(38):
    case = input()
    if len(case) != 0:
        if case[0] == '출':
            start = case[7:12]
            arrive = case[-5:]
            tmp = 0
            if len(start) == 5:
                if arrive[-1] != 'x':
                    start_tmp = (int(start[:2])*60)+int(start[3:])
                    arrive_tmp = (int(arrive[:2])*60)+int(arrive[3:])
                    tmp = arrive_tmp - start_tmp
                    print("이동시간 : " + str(tmp) + "초")
                    print()
        if case[1] == ")":
            print(case)






