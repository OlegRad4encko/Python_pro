# Реализуйте генераторную функцию, которая будет возвращать по
# одному члену геометрической прогрессии с указанным множителем.
# Генератор должен остановить свою работу или по достижению указанной
# границы, или при передаче команды на завершение.


def geometrically_prog(start, stop, step):
    while start <= stop:
        yield start
        start *= step


geom_tmp = geometrically_prog(1, 100, 3)
for item in geom_tmp:
    print(item)
