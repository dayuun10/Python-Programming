# 반복문 : while문, for문


# while문
# 1~10까지의 반복 출력

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("End")
    
    i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("End") # 실행안됨
    

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
found = False

while i <= 4:
    if nums[i] == target:
        print(f"{target} found")
        break
    i += 1
else: # if not found
    print(f"{target} not found")
    
    
# 1 ~ 10까지의 합

i = 0
tot = 0

# 1 ~ 10 짝수 합

while i <= 10:
    tot += i
    i += 2
else:
    print(f"sum: {tot}")
    
while i <= 10:
    if 1 % 2 == 0:
        tot += i
    i += 1
else:
    print(f"sum: {tot}")
    
while i <= 10:
    i += 1
    if 1 % 2 == 1:
        continue
    tot += i
else:
    print(f"sum: {tot}")