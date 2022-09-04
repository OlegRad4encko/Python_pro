# Напишите выражение-генератор для заполнения списка. Список должен
# быть заполнен кубами чисел от 2 и до указанной вами величины.


def cube_nums_generator(n):
    start = 2
    while start <= n:
        yield start ** 3
        start += 1

tmp = cube_nums_generator(10)
for i in tmp:
    print(i)

