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
    
    
