import numpy as np
from dateutil.parser import parse

previous = 0
current = 0


for i in range(38):
    case = input()
    if len(case) != 0:
        if case[0] == '출':
            start = case[7:12]
            arrive = case[-5:]
            if i == 1: # 맨 처음 셋팅 후, 다음 정류장부터 계산 가능
                previous = (int(arrive[:2])*60)+int(arrive[3:])
            else: # 2번째 부터 계산식 작성
                if len(start) == 5:
                    if arrive[-1] != 'x':
                        print(start)
                        print("해당 정류장에 정차한 시간 : " + str((int(start[:2])*60)+int(start[3:]) - previous) + "초")
                        previous = (int(start[:2])*60)+int(start[3:])


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







