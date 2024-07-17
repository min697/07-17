import random

result = []
i = 0
while i < 6:
    i = i+1
    new_num = random.randint(1,45)
    if new_num in result :
        print("값이 기존에 있습니다. 새롭게 추가하지 않습니다.")
    else :
        result.append(new_num)
    print()