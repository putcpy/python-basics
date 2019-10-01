# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armour):
        self.name = name
        self.health = health
        self.damage = damage
        self.armour = armour
        self.show_atributes
    
    def show_atributes(self):
        return self.name, self.health, self.damage, self.armour,

    def _income_damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage*random.uniform(0.1, 1.0))
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage*random.uniform(0.1, 1.0))
            if self.health <= 0:
                self.health = 0

        print('{} Получил по щщам и теперь имеет {} здоровья и {} брони'.format(self.name, self.health, self.armor))

    def punch(self, person):
        person._income_damage(self.damage)

  
class Player(Person):
        def __init__(self, name, health, damage, armour):
            Person.__init__(self, name, health, damage, armour)

class Enemy(Person):
        def __init__(self, name, health, damage, armour):
            Person.__init__(self, name, health, damage, armour)
    
class Game:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def fight(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.punch(person2)
            if person2.health == 0:
                print('============ {} победил!'.format(person1.name))
                break
            person2.punch(person1)
            if person1.health == 0:
                print('============ {} победил!'.format(person2.name))


player = Player('Шрек', 100, 10, 50)
enemy = Enemy('Ослик', 100, 10, 50)

Round = Game(player, enemy)
Round.fight(player, enemy)