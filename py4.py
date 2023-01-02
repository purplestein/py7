class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police'
        else:
            return f'{self.name} is not from police'


lotus = SportCar(100, 'Red', 'Lotus', False)
ford = TownCar(30, 'White', 'Ford', False)
gaz = WorkCar(70, 'Black', 'GAZ', True)
skoda = PoliceCar(110, 'Blue', 'Skoda', True)
print(gaz.turn_left())
print(f'When {ford.turn_right()}, then {lotus.stop()}')
print(f'{ford.go()} with speed exactly {ford.show_speed()}')
print(f'{ford.name} is {ford.color}')
print(f'Is {lotus.name} a police car? {lotus.is_police}')
print(f'Is {ford.name}  a police car? {ford.is_police}')
print(lotus.show_speed())
print(ford.show_speed())
print(skoda.police())
print(skoda.show_speed())
