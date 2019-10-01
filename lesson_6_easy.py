# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
 
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        #speed, color, name, is_police
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_atributes
    
    def show_atributes(self):
        return self.speed, self.color, self.name, self.is_police

    def go(self):
        print(self.name,'Автомобиль начал движение')

    def stop(self):
        print(self.name, 'Автомобиль остановился')

    def directions(self):
        direction = input("укажите направление движения автомобиля ")
        print(self.name, 'Автомобиль повернул'+ direction)
    
    def get_car_info(self):
        print

class TownCar(Car):
        def __init__(self, speed, color, name, is_police=False):
            Car.__init__(self, speed, color, name, is_police=False)

class SportCar(Car):
        def __init__(self, speed, color, name, is_police=False):
            Car.__init__(self, speed, color, name, is_police=False)

class WorkCar(Car):
        def __init__(self, speed, color, name, is_police=False):
            Car.__init__(self, speed, color, name, is_police=False)

class PoliceCar(Car):
        def __init__(self, speed, color, name, is_police=False):
            Car.__init__(self, speed, color, name, is_police=True)

car1 = TownCar(60, 'grey', 'Smart2two')
car2 = WorkCar(80, 'black', 'Camry')
car3 = PoliceCar(120, "blue", "Lada")
