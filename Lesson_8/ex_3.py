# Напишите функцию, которая применит к списку чисел произвольную
# пользовательскую функцию и вернет суммы элементов полученного списка.

def parent_func(ulist: list, ufunc):
    if not isinstance(ulist, list):
        raise TypeError("ulist must be a list")

    ulist = ufunc(ulist)
    return sum(ulist)


def user_func(u_list):
    for i in range(len(u_list)):
        u_list[i] = (u_list[i] - 5) * 2

    return u_list


uu_list = [2, 1, 5, 6, 34, 6, 3, -2, 3, 54, 2, 4]

print(parent_func(uu_list, user_func))
