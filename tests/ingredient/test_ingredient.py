from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    instance = Ingredient('bacon')
    instance2 = Ingredient('bacon')
    instance3 = Ingredient('ovo')
    assert instance.__hash__() == hash('bacon')
    assert instance.name == 'bacon'

    assert instance == instance2
    assert instance != instance3

    assert instance.__repr__() == f"Ingredient('{instance2.name}')"

    assert Restriction.ANIMAL_MEAT in instance.restrictions
    assert Restriction.ANIMAL_DERIVED in instance.restrictions
