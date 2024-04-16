class House:  # Создали новый класс
    numberOfFloors = 10   # Задали ему новый атрибут

    def __init__(self):
        self.numberOfFloors = 'Floor'


house = House()
house.numberOfFloors = 11

for house.numberOfFloors in range(house.numberOfFloors):  # В цикле проходим по атрибуту numberOfFloors
    print('Текущий этаж равен:', house.numberOfFloors)  # Распечатываем значение "Текущий этаж равен"