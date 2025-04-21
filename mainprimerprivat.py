class Car:
    def __init__(self, make, model):  #  исправлено тут
        self.public_make = make  # Открытый атрибут
        self._protected_model = model  # Защищенный атрибут
        self.__private_year = 2022  # Приватный атрибут

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."

    def protected_method(self):
        return "Это защищенный метод."

    def __private_method(self):
        return "Это приватный метод."


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)  # теперь работает корректно
        self.battery_size = battery_size

    def get_details(self):
        # Можно обратиться к открытому и защищённому атрибуту
        details = f"{self.public_make} {self._protected_model}, Батарея: {self.battery_size} kWh."
        return details


# Создание экземпляра ElectricCar
tesla = ElectricCar('Tesla', 'Model S', '100')

print(tesla.public_make)
print(tesla.public_method())
print(tesla._protected_model)  #  можно, но по соглашению не стоит
print(tesla.protected_method())
print(tesla.get_details())