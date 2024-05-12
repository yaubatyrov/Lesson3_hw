# Получаем строку ввода от пользователя
user_input = input("Введите числа через запятую, точку с запятой или слэш: ")

# Определяем возможные разделители
delimiters = [',', ';', '/']
chosen_delimiter = None

# Проверяем, что используется только один разделитель
for delimiter in delimiters:
    if delimiter in user_input:
        if chosen_delimiter is None:
            chosen_delimiter = delimiter
        else:
            print("Пожалуйста, используйте только один тип разделителя.")
            exit()

if chosen_delimiter is None:
    print("Неверный формат ввода.")
else:
    # Преобразуем введенные данные в список чисел
    numbers = [int(num.strip()) for num in user_input.split(chosen_delimiter)]
    # Получаем список уникальных чисел
    unique_numbers = list(set(numbers))
    # Выводим результат
    print("Результат:", ", ".join(map(str, unique_numbers)))
