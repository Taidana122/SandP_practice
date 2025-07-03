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

class JellyBean:
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self._flavor=flavor
    
    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        if self._flavor != 'black licorice':
            return False
        else:
            return True
    
    
