from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest

ingredient = Ingredient('bacon')


# Req 2
def test_dish():
    instance = Dish('Carbonara', 3)
    instance2 = Dish('Carbonara', 3)
    instance3 = Dish('Bolonhesa', 5)

    assert instance.name == 'Carbonara'
    assert instance.__hash__() == hash(f"Dish('{instance.name}', R$3.00)")

    assert instance == instance2
    assert instance != instance3

    instance.add_ingredient_dependency(ingredient, 3)
    assert instance.recipe == {ingredient: 3}
    assert instance.get_restrictions() == ingredient.restrictions
    assert instance.get_ingredients() == {ingredient}

    with pytest.raises(TypeError):
        Dish('Carbonara', 'aa')

    with pytest.raises(ValueError):
        Dish('Pizza', -3)
