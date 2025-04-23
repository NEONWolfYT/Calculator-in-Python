expensive_list = []


def add_expensive(amount: float, category: str, description: str = ""):
    """
    Добавляет новый расход.

    args:
        :amount: amount
        :category: category
        :description: description
    """
    expensive = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expensive_list.append(expensive)


def get_expensive():
    """
    Возвращает полный список всех расходов.
    Список: expensive_list

    returns:
        :list: expensive_list
    """
    return expensive_list


def get_expensive_sum():
    """
    Возвращает общую сумму всех расходов.

    returns:
        :float: сумма
    """
    return sum(expense['amount'] for expense in expensive_list)


def get_category(category: str):
    """
    Возвращает расходы по указанной категории.

    args:
        :category: выбранная категория

    Заранее переводим всё в нижний регистр, чтобы не получать несоответствие при выводе
    """
    return [expensive for expensive in expensive_list if expensive['category'].lower() == category.lower()]
