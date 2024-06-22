import math


# 1
# print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0\n")
#
# a = input("введите коэфицент a: ")
# b = input("введите коэфицент b: ")
# c = input("введите коэфицент с: ")
#
# # костяк программы
# def search_roots(a: float, b: float, c: float) -> float:
#
#     if check_type(a, b, c) == False:
#         return "TypeError"
#
#     a = float(a)
#     b = float(b)
#     c = float(c)
#
#     discriminant = b * b - 4 * a * c
#
#     if discriminant > 0 and a != 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return f"Корни уравнения, {round(root1, 2)}, и, {round(root2, 2)}"
#
#     elif discriminant == 0 and a != 0:
#         root = -b / (2 * a)
#         return f"Единственный корень уравнения {root}"
#
#     else:
#         return f"No root"
#
#
#
#
# def check_type(a, b, c) -> bool:
#     try:
#         a = float(a)
#         b = float(b)
#         c = float(c)
#         return True
#
#     except ValueError:
#         return False
#
# print(search_roots(a, b, c))






# 2
# a = input("введите сторону a: ")
# b = input("введите сторону b: ")
# c = input("введите сторону c: ")
#
# # костяк программы
# def finding_square(a, b, c):
#     if check_type(a, b, c) == False:
#         return "TypeError"
#
#     a = float(a)
#     b = float(b)
#     c = float(c)
#
#     if is_negative_num(a, b, c) == True:
#         return "ValueError"
#
#     if (a + b  > c) and (a + c > b) and (b + c > a):
#         s = (a + b + c) / 2
#         area = math.sqrt((s * (s - a) * (s - b) * (s - c)))
#
#         return f"Площадь треугольника: {round(area, 2)}"
#
#     else:
#         return "Error"
#
#
#
#
#
#
# def check_type(a, b, c) -> bool:
#     try:
#         a = float(a)
#         b = float(b)
#         c = float(c)
#         return True
#
#     except ValueError:
#         return False
#
#
#
#
# def is_negative_num(a: float, b: float, c: float):
#     for i in [a, b, c]:
#         if i < 0:
#             return True
#
#     return False
#





# 3
# костяк программы
def Translator_degree():

    choise = query_choise()

    if choise == "1":
        celsius = query_Celsius()
        if check_type(celsius, 0, 0 ) == False:
            return "TypeError"

        else:
            F = Pharyngeist_convert(float(celsius))
            return f"Температура в градусах Фаренгейта: {round(F, 2)}"


    elif choise == "2":
        fahrenheit = query_fahrenheit()
        if check_type(0, fahrenheit, 0) == False:
            return "TypeError"

        else:
            C = Celsius_convert(float(fahrenheit))
            return f"Температура в градусах Цельсия: {round(C, 2)}"

    else:
        return "Wrong choice"




def Pharyngeist_convert(celsius: float):
    return celsius * (9/5) + 32


def Celsius_convert(fahrenheit: float):
    return (fahrenheit - 32) * 5/9


def check_type(celsius=0, fahrenheit=0, choise=0) -> bool:
    try:
        celsius = float(celsius)
        fahrenheit = float(fahrenheit)
        choise = int(choise)
        return True

    except ValueError:
        return False

def query_Celsius():
    celsius = input("Введите градусы Цельсия: ")
    return celsius


def query_fahrenheit():
    fahrenheit = input("Введите градусы Фаренгейта: ")
    return fahrenheit


def query_choise():
    choise = input("Введите команду: ")
    return choise


print(Translator_degree())