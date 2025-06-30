#Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
#геттером и сеттером для атрибута flavor (все параметры являются не
#обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
#false только в тех случаях, когда flavor равняется «black licorice».

class Dessert:
    def __init__(self, name=None, calories=0):
        self.name = name
        self.calories = calories   
    
    def is_healthy(self):
        return self.calories < 200

    def is_delicious(self):
        return True
    
    @property #превращает метод name в геттер
    def name(self):
        return self.name #Позволяет обращаться к name, как к свойству, а не ф-ции
    
    @property #calories в геттер
    def calories(self):
        return self.calories
    
    @name.setter #сеттер для name
    def name(self, value):
        self.value = value

    @calories.setter #сеттер для name
    def calories(self, value):
        self.value = value

class JellyBean:
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self.flavor=flavor
    
    @property
    def flavor(self):
        return self.flavor

    @flavor.setter
    def flavor(self, value):
        self.value = value

    def is_delicious(self):
        if self.flavor != 'black licorice':
            return False
        else:
            return True