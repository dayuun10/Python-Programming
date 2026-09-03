#반복문: while문, for문

# while문
# 1 ~ 10까지의 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("end") # while문이 정상적으로 종료되면 실행됨, break문으로 종료되면 실행되지 않음

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print(f"Found {target} at index {i}")
        break
    i += 1
else:
    print(f"{target} not found in the list") # => 훨씬 깔끔해짐


# 1 ~ 10까지의 합
total = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        total += i  
    i += 1
print(total)