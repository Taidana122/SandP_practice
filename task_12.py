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
        self._calories = value

class JellyBean:
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(self, name, calories)
        self._flavor = flavor
    
    @property
    def flavor(self):
        return self._flavor
    
    @flavor.setter
    def flavor(self, value):
        self._flavor = value
    
    def is_delicious(self):
        if self.flavor == 'black licorice':
            return True
        else:
            return False
    
