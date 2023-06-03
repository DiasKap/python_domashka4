
first_len = int(input("Введите номер длины для первого набора: "))
second_len = int(input("Введите номер длины для второго набора: "))
first_set = set()
second_set = set()
for i in range(first_len):
    first_set.add(int(input(f"Введите {i+1} элемент для первого набора: ")))

for i in range(second_len):
    second_set.add(int(input(f"Введите {i+1} элемент для второго набора: ")))

result_set = first_set.union(second_set).difference(first_set.intersection(second_set))
print(sorted(first_set))
print(sorted(second_set))
print("Ваш результат из отдельных чисел в порядке возрастания:")
print(sorted(result_set))