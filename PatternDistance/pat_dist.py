import math


POINT_COUNT = 6
DISTANCE = 10
MATH_WAIT = 0.05


def define_distance(iteration, object_type):
    """In case of different object, return appropriate distance"""

    if object_type == "t":
        return iteration * 5, "тромбон"
    elif object_type == "v":
        return iteration * 10, "веер"
    else:
        print("Неизвестный объект")
        return iteration, None


def calculate_puasson(point, tim):
    """Use formula to calculate puasson distribution"""
    a = point / 60 * tim
    a = round(a, 2)
    return round(a * math.exp(-a), 4)


def decrement_last(planes_list):
    """Decrement two last distinct values in the list inplace"""
    list_for_change = [[val, ind] for ind, val in enumerate(planes_list)]
    for decr in sorted(list_for_change)[-2:]:
        planes_list[decr[1]] -= 1


def iterate_points(planes_list, tim):
    """Use iteration method to calculate the probability
    of the presence of two or more aircraft on the same distance"""

    p_obs = float("inf")
    iteration = 0

    while p_obs >= MATH_WAIT:
        iteration += 1
        print(f"{iteration} итерация:")
        var_list = []
        for point in planes_list:
            puasson = calculate_puasson(point, tim)
            var_list.append(puasson)
            print(f"{puasson} / {point}")

        var_list.sort()
        p_obs = round(var_list[-1] * var_list[-2] * math.comb(6, 2), 4)
        print(f"Наибольшая вероятность: {p_obs} \n")

        decrement_last(planes_list)

    return iteration


def main():
    """Script to calculate the appropriate safe distance for traffic pattern"""

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
        "Введите интервал в (км), если он " "отличается от стандартного значения = "
    )
    km = int(km) if km else DISTANCE

    sum_stream = sum(planes_list)
    print(f"Суммарная часовая ИВД равна: {sum_stream} вс/час.")
    tim = 60 / 300 * km
    print(f"Определяем вероятности попадания на {km} км-й участок каждого ВС:")

    iteration = iterate_points(planes_list, tim)

    res_distance, object_name = define_distance(iteration, object_type)

    if object_name:
        print(f"Окончательная длина для {object_name}а составляет: {res_distance} км")


if __name__ == "__main__":
    main()