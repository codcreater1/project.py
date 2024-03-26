import random

class Cars():
    def __init__(self, brand, price, color, speed):
        self.brand = brand
        self.price = price
        self.color = color
        self.speed = speed
        
    def compare_features(self, other_car):
        if self.speed > other_car.speed:
            print(f"{self.brand} is faster than {other_car.brand}.")
        elif self.speed < other_car.speed:
            print(f"{self.brand} is slower than {other_car.brand}.")
        else:
            print(f"{self.brand} has the same speed as {other_car.brand}.")

        if self.price > other_car.price:
            print(f"{self.brand} is more expensive than {other_car.brand}.")
        elif self.price < other_car.price:
            print(f"{self.brand} is cheaper than {other_car.brand}.")
        else:
            print(f"{self.brand} has the same price as {other_car.brand}.")


car_brand = input("Please enter the brand of the car: ")
car_speed = int(input("Please enter the speed of the car: "))
car_price = int(input("Please enter the price of the car: "))

speed_car = random.randint(0, 1000)

car_1 = Cars("Audi", 50000, "Red", speed_car)
car_2 = Cars(car_brand, car_price, None, car_speed)  

car_1.compare_features(car_2)
