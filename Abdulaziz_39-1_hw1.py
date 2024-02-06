class superhero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"nickname: {self.nickname}, superpower: {self.superpower}, health: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


super_hero = superhero("john", "gauss prime", "super speed", 185, "I am named after Karl Friedrich Gauss!")

super_hero.double_health()
print(super_hero)

print(len(super_hero))
