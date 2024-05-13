def morogeno(self=None):
    class Restaurant:
        def __init__(self, rest_name, cuisine_type):
            self.rest_name = rest_name
            self.type = cuisine_type

        def d_restaurant(self):
            print(f"Название ресторана: {self.rest_name}")
            print(f"Тип кухни: {self.type}")

        def open_restaurant(self):
            print(f"Ресторан {self.rest_name} открыт!")

    def list_flavors():
        print("Сорта мороженого:")

    class IceCreamStand(Restaurant):
        def __init__(self, rest_name, type, flavors):
            super().__init__(rest_name, type)
            self.flavors = flavors

    for flavor in self.flavors:
        print(f"- {flavor}")

    ice_stand = IceCreamStand("Мороженое-Мопс", "Мороженое", ["Ваниль", "Шоколад", "Манго", "Соленая карамель"])
    ice_stand.open_restaurant()
    list_flavors()


class Restaurant:
    def __init__(self, rest_name, type):
        self.type = None
        self.rest_name = rest_name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.rest_name}")
        print(f"Тип кухни: {self.type}")

    def open_restaurant(self):
        print(f"Ресторан {self.rest_name} открыт")


class IceCreamStand(Restaurant):
    def __init__(self, rest_name, type, flavors, location, opening_hours):
        super().__init__(rest_name, type)
        self.flavors = flavors
        self.location = location
        self.opening_hours = opening_hours

    def open_restaurant(self):
        super().open_restaurant()
        print(f"Ресторан работает по расписанию: {self.opening_hours}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт мороженого {flavor} добавлен.")
        else:
            print(f"Сорт мороженого {flavor} уже есть в списке.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого {flavor} удален.")
        else:
            print(f"Сорт мороженого {flavor} не найден.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого {flavor} есть в списке.")
        else:
            print(f"Сорт мороженого {flavor} нет в списке.")

    def list_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def serve_ice_cream(self, flavor, type_cream):
        if flavor in self.flavors:
            print(f"Сервируем {type_cream} мороженое с вкусом {flavor}.")
        else:
            print(f"Сорт мороженого {flavor} нет в наличии.")


ice_cream_stand = IceCreamStand("Мороженое-Мопс", "Мороженое", ["Ваниль", "Шоколад", "Манго", "Соленая карамель"],
                                "ул. Ленина, 10", "9:00 - 21:00")

ice_cream_stand.open_restaurant()
ice_cream_stand.list_flavors()
ice_cream_stand.add_flavor("Вишня")
ice_cream_stand.remove_flavor("Манго")
ice_cream_stand.check_flavor("Шоколад")
ice_cream_stand.serve_ice_cream("Соленая карамель", "на палочке")
