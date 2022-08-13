class UserExcept(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'Введенное число должно быть больше 0'


while True:
    try:
        x = float(input("Input: "))
        if x <= 0:
            raise UserExcept()
        break
    except (ValueError, UserExcept) as err:
        print(f'Opps:\n {err}')

print(x)