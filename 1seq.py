# Запрос количества элементов
num_elements = int(input("Введите количество элементов списка: "))

# Инициализация пустого списка
elements = []

# Заполнение списка элементами, введенными пользователем
for i in range(num_elements):
    # Запрос числа у пользователя
    number = int(input(f"Введите элемент {i + 1}: "))
    # Добавление числа в список
    elements.append(number)

# Сортировка списка по возрастанию
elements.sort()

# Вывод отсортированного списка
print("Отсортированный список:", elements)
