import random

class PowerUp:
    def __init__(self, name, type, description, cost=None, level: int=0, max_level: int=None):
        self.name = name
        self.type = type
        self.description = description
        self.cost = cost
        self.level = level
        self.max_level = max_level
    
    def upgrade(self):
        if self.max_level is not None:
            if self.level < self.max_level:
                self.level += 1
        else:
            self.level += 1
            self.update_power()
    
    def update_power(self):
        pass
        
    def __str__(self) -> str:
        return self.level

class Hit(PowerUp):
    def __init__(self, name, type, description, cost=None, level: int=0, max_level: int=None):
        super().__init__(name, type, description, cost, level, max_level)
        self.power = 10
        if self.level > 1: self.update_power()
    
    def update_power(self):
        self.power = 10 * (1.5 ** self.level)
        if self.cost is not None:
            self.cost = self.cost * (1.5 ** self.level)

class Income(PowerUp):
    def __init__(self, name, type, description, cost=None, level: int=0, max_level: int=None):
        super().__init__(name, type, description, cost, level, max_level)
        self.power = 0
        if self.level > 1: self.update_power()
    
    def update_power(self):
        self.power = self.power * (1.5 ** self.level)
        if self.cost is not None:
            self.cost = self.cost * (2 ** self.level)

class RandomIncome(Income):
    def __init__(self, name, type, description, cost=None, level: int=0, max_level: int=None):
        super().__init__(name, type, description, cost, level, max_level)
        self.power = 0
        if self.level > 1: self.update_power()
    
    def update_power(self):
        self.power = 0 + self.level * random.randint(1, 1000)
        if self.cost is not None:
            self.cost = self.cost * (2 ** self.level)

class Combo(PowerUp):
    def __init__(self, name, type, description, cost=None, level: int=0, max_level: int=None):
        super().__init__(name, type, description, cost, level, max_level)
        if self.level == 1:
            self.power = 1
        elif self.level > 1:
            self.update_power()
    
    def update_power(self):
        self.power = 1 + self.level // 125
        if self.cost is not None:
            self.cost = self.cost * (1.5 ** self.level)
