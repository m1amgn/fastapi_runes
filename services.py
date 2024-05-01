def calculate_date(number: int) -> int:
    if number >= 10:
        while number >= 10:
            number = sum(int(digit) for digit in str(number))
    return number


def calculate_name(name: str) -> int:
    name = name.upper()
    chars = {
        1: ["А", "И", "С", "Ъ"],
        2: ["Б", "Й", "Т", "Ы"],
        3: ["В", "К", "У", "Ь"],
        4: ["Г", "Л", "Ф", "Э"],
        5: ["Д", "М", "Х", "Ю"],
        6: ["Е", "Н", "Ц", "Я"],
        7: ["Ё", "О", "Ч"],
        8: ["Ж", "П", "Ш"],
        9: ["З", "Р", "Щ"]
    }

    num_name_list = []
    name_list = [char for char in name]

    for char in name_list:
        for key, value in chars.items():
            if char in value:
                num_name_list.append(key)

    sum_of_numbers = sum(num_name_list)

    if sum_of_numbers >= 10:
        while sum_of_numbers >= 10:
            sum_of_numbers = sum(int(digit) for digit in str(sum_of_numbers))

    return sum_of_numbers


def check_ett(number: int) -> int:
    etts = {
        1: [1, 4, 7],
        2: [2, 5, 8],
        3: [3, 6, 9]
    }

    if number >= 10:
        while number >= 10:
            digit_sum = sum(int(digit) for digit in str(number))
            number = digit_sum

    for key, value in etts.items():
        if number in value:
            return key


def main():
    day = 13
    month = 3
    year = 2024

    second_name = "Медведев"
    first_name = "Макар"
    father_name = "Иванович"

    number_of_day = calculate_date(day)
    ett_number_of_day = check_ett(number_of_day)

    number_of_month = calculate_date(month)
    ett_number_of_month = check_ett(number_of_month)

    number_of_year = calculate_date(year)
    ett_number_of_year = check_ett(number_of_year)

    sum_date = number_of_day + number_of_month + number_of_year
    sum_date_finish = calculate_date(sum_date)
    ett_sum_date_finish = check_ett(sum_date_finish)

    number_of_first_name = calculate_name(first_name)
    ett_number_of_first_name = check_ett(number_of_first_name)

    number_of_father_name = calculate_name(father_name)
    ett_number_of_father_name = check_ett(number_of_father_name)

    number_of_second_name = calculate_name(second_name)
    ett_number_of_second_name = check_ett(number_of_second_name)

    sum_name = number_of_first_name + number_of_father_name + number_of_second_name
    sum_name_finish = calculate_date(sum_name)
    ett_sum_name_finish = check_ett(sum_name_finish)

    day_first_name = number_of_day + number_of_first_name
    day_first_name_finish = calculate_date(day_first_name)
    ett_day_first_name = check_ett(day_first_name_finish)

    month_father_name = number_of_month + number_of_father_name
    month_father_name_finish = calculate_date(month_father_name)
    ett_month_father_name = check_ett(month_father_name_finish)

    year_second_name = number_of_year + number_of_second_name
    year_second_name_finish = calculate_date(year_second_name)
    ett_year_second_name = check_ett(year_second_name_finish)

    sum_gold = sum_date_finish + sum_name_finish
    sum_gold_finish = calculate_date(sum_gold)
    ett_sum_gold_finish = check_ett(sum_gold_finish)

    print(
        f"Sum date: {sum_date_finish}, etts: {ett_number_of_day}-{ett_number_of_month}-{ett_number_of_year} | {ett_sum_date_finish}")
    print(
        f"Sum name: {sum_name_finish}, etts: {ett_number_of_second_name}-{ett_number_of_first_name}-{ett_number_of_father_name} | {ett_sum_name_finish}")
    print(
        f"Sum gold: {sum_gold_finish}, etts: {ett_year_second_name}-{ett_day_first_name}-{ett_month_father_name} | {ett_sum_gold_finish}")
