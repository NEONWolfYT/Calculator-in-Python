import pytest
from main import add_expensive, get_expensive, get_expensive_sum, get_category


def test_add_expensive():
    add_expensive(1000, "Бытовые", "")
    add_expensive(750, "Одежда")
    add_expensive(0, "Одежда", "Барахолка")
    add_expensive(0, "Бесплатно", "Бесплтано")
    assert len(get_expensive()) == 4


def test_get_expensive_sum():
    add_expensive(250, "Поездка", "Домой")
    assert get_expensive_sum() == 2000


def test_get_category():
    result = get_category("Бытовые")
    assert len(result) == 1
    assert result[0]['amount'] == 1000
    assert result[0]['description'] == ""
    result = get_category("Одежда")
    assert len(result) == 2
    assert result[0]['amount'] == 750
    assert result[0]['description'] == ""


def test_empty_expenses():
    from main import expensive_list
    expensive_list.clear()
    assert len(get_expensive()) == 0
    assert get_expensive_sum() == 0
    assert len(get_category("")) == 0


def test_invalid_expense():
    with pytest.raises(TypeError):
        add_expensive("Строка", "Категория", "Описание")
