import random

bushes = int(input("Введите количество кустов: "))
bush_berries = [random.randint(5,55) for _ in range(bushes)]
print(bush_berries)

max_sum = 0
for i in range(bushes):
    sum = bush_berries[i] + bush_berries[(i+1)%bushes] + bush_berries[(i+2)%bushes]
    if sum > max_sum:
        max_sum = sum

print(f"Максимальное количество ягод за один раунд составляет {max_sum}")