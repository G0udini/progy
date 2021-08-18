import math


POINT_COUNT = 6
DISTANCE = 10
MATH_WAIT = 0.05


def main():

    object_type = input("Выполнить расчет для [t/v]: ")
    planes_per_point = input("ВС/час = ").split()
    planes_list = [int(plane) for plane in planes_per_point]

    if len(planes_list) > POINT_COUNT:
        print("Колличество введенных точек превышает допустимое значение")
        return
    if len(planes_list) < 3:
        print("Недостаточно точек для вычисления")
        return

    km = input(
        "Введите интервал в (км), если он "
        "отличается от стандартного значения = ")
    km = int(km) if km else DISTANCE

    sum_stream = sum(planes_list)
    print(f"Суммарная часовая ИВД равна: {sum_stream} вс/час.")
    tim = 60 / 300 * km
    print(
        f"Определяем вероятности попадания на {km} км-й участок каждого ВС:")
    p_obs = float("inf")
    iteration = 0

    while p_obs >= MATH_WAIT:
        iteration += 1
        print(f"{iteration} итерация:")
        var_list = []
        for point in range(len(planes_list)):
            a = planes_list[point] / 60 * tim
            a = round(a, 2)
            p = round(a * math.exp(-a), 4)
            var_list.append(p)
            print(f"{p} / {planes_list[point]}")

        var_list.sort()
        p_obs = round(var_list[-1] * var_list[-2] * math.comb(6, 2), 4)
        print(f"Наибольшая вероятность: {p_obs} \n")

        list_for_change = [[k, v] for k, v in enumerate(planes_list)]
        list_for_change.sort(key=lambda x: x[1])
        list_for_change[-1][1] -= 1
        list_for_change[-2][1] -= 1
        for ind, change in list_for_change:
            planes_list[ind] = change

    res_distance, object_name = distance_definition(iteration, object_type)

    if object_name:
        print(f"Окончательная длина для {object_name}а\
составляет: {res_distance} км")


def distance_definition(iteration, object_type):
    """In case of different object, return appropriate distance"""

    if object_type == "t":
        return iteration * 5, "тромбон"
    elif object_type == "v":
        return iteration * 10, "веер"
    else:
        print("Неизвестный объект")
        return iteration, None


if __name__ == '__main__':
    main()
