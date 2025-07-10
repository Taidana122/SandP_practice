#Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором, 
#принимающим на вход name и calories (не обязательные параметры), а также двумя
#методами is_healthy (возвращает true при условии калорийности десерта менее
#200) и is_delicious (возвращает true для всех десертов). 

class Dessert:
    def __init__(self, name='', calories=0):
        self._name = name
        self._calories = calories   
    
    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True
    
    @property
    def name(self):
        return self._name
    
    @property
    def calories(self):
        return self._calories
    
    @name.setter
    def name(self, value):
        self._name = value

    @calories.setter
    def calories(self, value):
        try:
            self._calories = int(value)
        except (ValueError, TypeError):
            self._calories = 0
    
    
