def remove_elements(list1, list2):
    # Создаем множество из элементов второго списка для быстрой проверки на вхождение
    set2 = set(list2)
    # Оставляем в первом списке только те элементы, которых нет во втором списке
    return [item for item in list1 if item not in set2]


chosen_delimiter = ','
# Запрос ввода для первого списка
input_list1 = input("Введите элементы первого списка через запятую: ")

# Преобразование введенной строки в список
list1 = [int(num.strip()) for num in input_list1.split(chosen_delimiter)]

# Запрос ввода для второго списка
input_list2 = input("Введите элементы второго списка через запятую: ")

# Преобразование введенной строки в список
list2 = [int(num.strip()) for num in input_list2.split(chosen_delimiter)]

# Удаление элементов из первого списка
result_list = list(set(list1) - set(list2))


# Вывод итогового списка
print("Итоговый список после удаления:", result_list)
