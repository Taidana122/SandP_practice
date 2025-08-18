#Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
#принимающим на вход name и calories (не обязательные параметры), а также двумя
#методами is_healthy (возвращает true при условии калорийности десерта менее
#200) и is_delicious (возвращает true для всех десертов). 


class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value1):
        if not isinstance(value1, str):
            raise ValueError("Название десерта должно быть строкой.")
        self._name = value1

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Калории должны быть числом.")
        if value < 0:
            raise ValueError("Калории не могут быть отрицательными.")
        self._calories = value

    def is_delicious(self):
        return True

    def is_healthy(self):
        try:
            return self._calories is not None and float(self._calories) < 200
        except (ValueError, TypeError):
            return False

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        if not isinstance(value, str):
            return False
        self._flavor = value

    def is_delicious(self):
        return self._flavor != "black licorice"
    



