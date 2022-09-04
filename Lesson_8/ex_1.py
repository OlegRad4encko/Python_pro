# Реализуйте генераторную функцию, которая будет возвращать по одному
# члену числовой последовательности, закон которой задается с помощью
# пользовательской функции. Кроме этого параметром генераторной функции
# должны быть значение первого члена прогрессии и количество выдаваемых
# членов последовательности (n). Генератор должен остановить свою работу
# или по достижению n — го члена , или при передаче команды на завершение.

def gen_func(start, count):
    def my_seq(n):
        return (n ** 2) + 5

    while start < count:
        oops = yield my_seq(start)
        if oops and oops.lower() == 'stop':
            raise ValueError()
        start += 1


x = gen_func(1, 10)
for i in x:
    if i > 30:
        x.send('stop')
    print(i)




