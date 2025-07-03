#Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором, 
#принимающим на вход name и calories (не обязательные параметры), а также двумя
#методами is_healthy (возвращает true при условии калорийности десерта менее
#200) и is_delicious (возвращает true для всех десертов). 

class Dessert:
    def __init__(self, name='', calories=0):
        self._name = name
        self._calories = calories   
    
    def is_healthy(self):
        return self.calories < 200

    def is_delicious(self):
        return True
    
    @property #превращает метод name в геттер
    def name(self):
        return self._name #Позволяет обращаться к name, как к свойству, а не ф-ции
    
    @property #calories в геттер
    def calories(self):
        return self._calories
    
    @name.setter #сеттер для name
    def name(self, value):
        self._name = value

    @calories.setter #сеттер для name
    def calories(self, value):
        self._calories = value
    
    
