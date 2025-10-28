class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} was defeated."
        return f"{self.name} has {self.health} health left."
    def heal(self, amount):
        self.health += amount
        return f"{self.name} has {self.health} health left."

hero = Hero("Ragnar", 100)

print(hero.defend(50))

hero.heal(50)

print(hero.defend(99))

print(hero.defend(1))