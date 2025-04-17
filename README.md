<h1 align="center">Calculator-in-Python></h1>
<h3 align="center">Мой проект простого калькулятора на Python 🇷🇺</h3>

<h3 align="center">Что делает (реализует) программа</h3>

1. Добавляет расходы с указанием суммы, категорий и описания
2. Просмотривает полный список всех расходов
3. Просмотривает общую сумму расходов
4. Просмотривает расходы по выбранной категории

<h3 align="center">Как запускать</h3>

1. Установите Python3 (рекомендуется Python 3.9)
2. Скачайте проект (Для простого использования достаточно main.py)
3. Запустите программу (рекомендуется использовать cmd: python main.py) или же доступные среды разработки (PyCharm / VS)

<h3 align="center">Описание функций</h3>

1. add_expensive(amount: float, category: str, description: str = None):
    Добавляет новый расход.

2. get_expensive():
    Возвращает полный список всех расходов.

3. get_total():
    Возвращает общую сумму всех расходов.

4. get_by_category(category: str):
    Возвращает расходы по указанной категории.

5. main():
    Выполнение и запуск основного блока кода.
   
<h3 align="center">Описание тестов</h3>

1. Тест добавления расходов - test_add_expensive (добавляет некоторое количество расходов)
2. Тест расчёта общей суммы - test_get_total (добавляет расход, считает сумму)
3. Тест получения информации по категории - test_get_category (вызывает категорию, получает данные о ней)
4. Тест пустого списка расходов - test_empty_expenses (очищает список расходов, вызывает его, проверяет на наличие элементов в списке)
5. Тест ввода некоректных данных - test_invalid_expense (проверяет способ ввода: суммы, категории, описания - изменяет тип данных у суммы)

Расчитывается, что все тесты за исключением 5-ого будут пройдены.

<h3 align="center">Примеры использования</h3>

1. Добавить пункт расхода:

    Введите сумму: *число (float)
    Введите категорию: *категория (str)
    Введите описание: *описание (str)

2. Показать все добавленные расходы:

    Все расходы:
   
        1. *число руб. *категория. *описание
        2. *число руб. *категория. *описание
        ...

4. Показать общую сумму:

    Общая сумма расходов: *число руб.

5. Показать расходы по категории:

    Введите категорию: *категория

    Расходы в выбранной категории:
   
        1. *число руб. *описание
        2. *число руб. *описание
        ...
    

<h1 align="center">Удачного программирования!
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
