import random

# Словарь известных людей и их дат рождения
celebrities = {
    'Альберт Эйнштейн': '14.03.1879',
    'Мари Кюри': '07.11.1867',
    'Леонардо да Винчи': '15.04.1452',
    'Исаак Ньютон': '04.01.1643',
    'Чарльз Дарвин': '12.02.1809',
    'Стив Джобс': '24.02.1955',
    'Билл Гейтс': '28.10.1955',
    'Маргарет Тэтчер': '13.10.1925',
    'Уинстон Черчилль': '30.11.1874',
    'Мартин Лютер Кинг': '15.01.1929'
}


def date_to_text(date):
    months = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
        '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
        '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
    }
    day, month, year = date.split('.')
    return f"{int(day)} {months[month]} {year} года"


def run_quiz():
    selected = random.sample(list(celebrities.keys()), 5)
    correct_answers = 0

    for person in selected:
        user_answer = input(f"Введите дату рождения {person} (dd.mm.yyyy): ")
        correct_date = celebrities[person]
        if user_answer == correct_date:
            print("Верно!")
            correct_answers += 1
        else:
            print(f"Неверно! Правильный ответ: {date_to_text(correct_date)}")

    incorrect_answers = 5 - correct_answers
    print(f"\nПравильных ответов: {correct_answers}")
    print(f"Неправильных ответов: {incorrect_answers}")

    # Предложение начать игру снова
    if input("Хотите начать снова? (да/нет): ").lower() == 'да':
        run_quiz()


# Запуск викторины
run_quiz()
