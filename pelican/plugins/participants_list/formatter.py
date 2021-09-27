import csv


def _str_formatter(x):
    extra = {
        "нет": "-",
        "": "-",
        " ": "-",
        "без доклада": "-",
    }
    # делаем замены некоторых строк фиксированными значениями
    if x in extra:
        return extra[x]
    # меняем двойные пробелы на одинарные
    x = x.replace("  ", " ")
    # если строка записана на 2-х языках через "/", то удаляем 2-ой язык
    x = x.split("/")[0]
    # если строка заканчивается пробелом, то удаляем его
    x = x.rstrip()
    return x


def format_csv(csv_in, csv_out):
    result = []
    with open(csv_in) as csvfile:
        reader = csv.reader(csvfile)
        # скипаем заголовки столбцов
        next(reader)
        for row in reader:
            # фамилия, имя, отчество, город, тема доклада
            result.append([row[1], row[2], row[3], row[4], row[10]])
    # форматируем каждый столбец в строке
    result = [tuple(map(_str_formatter, x)) for x in result]
    # убираем дубликаты
    result = set(result)
    # сортируем по алфавиту, учитывая ФИО и тему
    result = sorted(result, key=lambda x: "".join(x))

    # сохраняем обработанные данные
    with open(csv_out, "w") as csvfile:
        writer = csv.writer(csvfile)
        for x in result:
            writer.writerow(x)
