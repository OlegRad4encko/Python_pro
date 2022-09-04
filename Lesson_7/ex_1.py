# Реализуйте генераторную функцию, которая будет возвращать по
# одному члену геометрической прогрессии с указанным множителем.
# Генератор должен остановить свою работу или по достижению указанной
# границы, или при передаче команды на завершение.


def geometrically_prog(start, stop, step):
    while start <= stop:
        tmp = yield start
        if tmp and tmp.lower() == 'stop':
            return None
        start *= step


geom_tmp = geometrically_prog(1, 1000, 2)
for item in geom_tmp:
    print(item)
    if item > 100:
        geom_tmp.send('stop')


