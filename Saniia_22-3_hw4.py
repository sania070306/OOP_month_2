import random


class SuperAbility():
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    INCREASE_OR_DECREASE = 5
    REVIVAL = 6


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.__name} health: {self.__health} damage: {self.__damage}"


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        selected_hero = random.choice(heroes)
        self.__defence = selected_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            hero.health -= self.damage

    def __str__(self):
        return "BOSS " + super(Boss, self).__str__() + f" defence: {self.__defence}"


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Hero, self).__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(1, 5)
        print(f"Coefficent of critical: {coeff}")
        boss.health -= self.damage * coeff


class Mag(Hero):
    def __init__(self, name, health, damage):
        super(Mag, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_point = random.randint(5, 11)
        print(f"Boost: {boost_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self and hero.damage != 0:
                hero.damage += boost_point


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_power(self, boss, heroes):
        N = round(random.uniform(0, 1), 1)
        self.damage += boss.damage * N


class AntMan(Hero):
    def __init__(self, name, health, damage):
        self.flag = 0
        self.f = 0
        super(AntMan, self).__init__(name, health, damage, SuperAbility.INCREASE_OR_DECREASE)

    def apply_super_power(self, boss, heroes):
        size = random.randint(1, 3)
        if self.flag == 1:
            self.health -= self.f
            self.damage -= self.f
        elif self.flag == 2:
            self.health += self.f
            self.damage += self.f

        N = random.randint(2, 6)
        self.f = N
        if size == 1:
            print(f"Ant_man: + {N}")
            self.health += N
            self.damage += N
            self.flag = 1
        else:
            print(f"Ant_man: - {N}")
            self.health -= N
            self.damage -= N
            self.flag = 2


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super(Witcher, self).__init__(name, health, damage, SuperAbility.REVIVAL)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0 and hero != self:
                hero.health = self.health
                self.health = 0
                break



round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes WON!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss WON!")
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f"--------- Round {round_number} ---------")
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and hero.super_ability != boss.defence:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Aid", 1500, 50)

    warrior = Warrior("Ahiles", 270, 10)
    mag = Mag("Wale", 250, 20)
    aibolit = Medic("Aibolit", 220, 15, 20)
    livsi = Medic("Livsi", 250, 10, 5)
    witcher = Witcher("Jake", 260, 0)
    ant_man = AntMan("Niki", 250, 10)
    berserk = Berserk("Jay", 280, 10)

    heroes = [warrior, mag, aibolit, livsi, witcher, ant_man, berserk]
    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
