from random import randint

n = int(input("Введите количество кустов на грядке: "))
lst = [randint(1,50) for i in range(n)]
print(lst)

maxSum = 0
for i in range(-1, n-1):
    if lst[i-1] + lst[i] + lst[i+1] > maxSum:
        maxSum = lst[i-1] + lst[i] + lst[i+1]

print(f"Максимальное число ягод, которое можно собрать за один заход = {maxSum}")