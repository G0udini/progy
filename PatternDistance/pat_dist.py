import math


POINT_COUNT = 6
DISTANCE = 10
MATH_WAIT = 0.05
TRANSLATE_COEFICIENT = 0.2
CONST_COMB_FORMUL = math.comb(6, 2)


def define_distance(iteration, object_type):
    """In case of different object, return appropriate distance"""

    if object_type == "t":
        return iteration * 5, "тромбон"
    elif object_type == "v":
        return iteration * 10, "веер"


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


def iterate_points(planes_list, tim, output_string):
    """Use iteration method to calculate the probability
    of the presence of two or more aircraft on the same distance"""

    p_obs = float("inf")
    iteration = 0

    while p_obs >= MATH_WAIT:
        iteration += 1
        output_string += f"\n{iteration} итерация:\n"
        var_list = []
        for point in planes_list:
            puasson = calculate_puasson(point, tim)
            var_list.append(puasson)
            output_string += f"{puasson} / {point}\n"

        var_list.sort()
        p_obs = round(var_list[-1] * var_list[-2] * CONST_COMB_FORMUL, 4)
        output_string += f"Наибольшая вероятность: {p_obs} \n"

        decrement_last(planes_list)

    return iteration, output_string


def output_to_file(output_string):
    """create file at the same directory where script located
    and output all data in correct format for further use"""

    with open("script.txt", "w") as f:
        f.write(output_string)


def check_input_object(object_type):
    """Validation of object type to correctly calculate distance"""

    veer_abr = {"veer", "v", "веер"}
    tromb_abr = {"tromb", "t", "trombon", "тромбон"}

    if object_type.lower() in veer_abr:
        object_type = "v"
    elif object_type.lower() in tromb_abr:
        object_type = "t"
    else:
        print("Неизвестный объект")
        object_type = None
    return object_type


def check_input_planes(planes_list):
    """Check for length of the planes list"""

    if len(planes_list) > POINT_COUNT:
        print("Колличество введенных точек превышает допустимое значение")
        return True
    elif len(planes_list) < 3:
        print("Недостаточно точек для вычисления")
        return True
    else:
        return


def main():
    """Script to calculate the appropriate safe distance for traffic pattern"""

    object_type = input("Выполнить расчет для (t/v): ")
    object_type = check_input_object(object_type)
    if not object_type:
        return

    planes_list = [int(plane) for plane in input("список ВС/час: ").split()]
    if check_input_planes(planes_list):
        return

    km = input("Введите интервал в (км), если он отличается от стандартного значения: ")
    km = int(km) if km else DISTANCE

    output_string = ""

    output_string += f"Суммарная часовая ИВД равна: {sum(planes_list)} вс/час.\n"
    tim = km * TRANSLATE_COEFICIENT
    output_string += (
        f"Определяем вероятности попадания на {km} км-й участок каждого ВС:\n"
    )

    iteration, output_string = iterate_points(planes_list, tim, output_string)

    res_distance, object_name = define_distance(iteration, object_type)

    output_string += (
        f"Окончательная длина для {object_name}а составляет: {res_distance} км"
    )

    output_to_file(output_string)


if __name__ == "__main__":
    main()
