class Superhero:
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_health(self):
        self.health_points *= 2

    def print_phrase(self):
        print(self.catchphrase)

class AirHero(Superhero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=0):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def double_health(self):
        super().double_health()
        self.fly = True

    def print_phrase(self):
        print("true in the true_phrase")

class EarthHero(Superhero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=0):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def double_health(self):
        super().double_health()
        self.fly = True

    def print_phrase(self):
        print("true in the true_phrase")

class Villain(AirHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=0):
        super().__init__(name, nickname, superpower, health_points, catchphrase, fly, damage)
        self.people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage *= 2

air_hero = AirHero("Tony Stark", "Iron man", "Flight", 500, "You idiot, wake up, you're going to be a firefighter today!")
earth_hero = EarthHero("Bob", "Rock", "Earth Manipulation", 400, "Earth is my strength!")
villain = Villain("Victor von Doom", "Dr.Doom", "Time manipulation", 800, "Fear my wrath!")

air_hero.double_health()
earth_hero.double_health()
villain.double_health()

air_hero.print_phrase()
earth_hero.print_phrase()

villain.crit()

print(air_hero.__dict__)
print(earth_hero.__dict__)
print(villain.__dict__)