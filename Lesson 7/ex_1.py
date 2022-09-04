# Реализуйте генераторную функцию, которая будет возвращать по
# одному члену геометрической прогрессии с указанным множителем.
# Генератор должен остановить свою работу или по достижению указанной
# границы, или при передаче команды на завершение.

import env

LIMIT = env.LIMIT


def geometrically_prog(n):
    start = 1
    while start <= LIMIT:
        yield start ** n
        start += 1


geom_tmp = geometrically_prog(8)
for item in geom_tmp:
    print(item)
