"""Дополнительную информацию про функции можно прочитать в файле README"""


def add_expensive(amount: float, category: str, description: str = ""):
    expensive = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expensive_list.append(expensive)


def get_expensive():
    return expensive_list


def get_expensive_sum():
    return sum(expense['amount'] for expense in expensive_list)


def get_category(category: str):
    """Заранее переводим всё в нижний регистр, чтобы не получать несоответствие при выводе"""
    return [expensive for expensive in expensive_list if expensive['category'].lower() == category.lower()]


def main():
    print("Калькулятор запущен")
    while True:
        print("\nМеню:\n",
              "1. Добавить пункт расхода\n",
              "2. Показать все добавленные расходы\n",
              "3. Показать общую сумму\n",
              "4. Показать расходы по категории\n",
              "5. Выход\n")
        c_menu = input("Выберите действие: ").strip()

        if c_menu == "1":
            try:
                amount = float(input("Введите сумму: "))
                category = input("Введите категорию: ").strip()
                description = input("Введите описание: ").strip()
                add_expensive(amount, category, description)
                print("Расход успешно добавлен! Вы можете посмотреть список расходов в меню под цифрой 2\n")
            except ValueError:
                print("Ошибка: сумма должна быть числом! Повторите снова")

        elif c_menu == "2":
            all_expensive = get_expensive()
            if not all_expensive:
                print("Список расходов пуст")
            else:
                print("Все расходы:")
                for i, expensive in enumerate(all_expensive, 1):
                    description = expensive['description']
                    print(f"{i}. {expensive['amount']} руб. {expensive['category']}. {description}")

        elif c_menu == "3":
            print(f"Общая сумма расходов: {get_expensive_sum()} руб.")

        elif c_menu == "4":
            category = input("Введите категорию: ").strip()
            choise_category = get_category(category)
            if not choise_category:
                print(f"В данной категории расходов нет")
            else:
                print(f"Расходы в выбранной категории:")
                for index, expensive in enumerate(choise_category, 1):
                    description = expensive['description']
                    print(f"{index}. {expensive['amount']} руб. {description}")

        elif c_menu == "5":
            print("Завершение программы")
            break

        else:
            print("Неверный ввод. Выберите цифру от 1 до 5")


expensive_list = []
if __name__ == "__main__":
    main()
