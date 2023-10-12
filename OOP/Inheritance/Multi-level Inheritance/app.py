# ================================Multi-level Inheritance=====================


class Animals():

    def eat(self):
        print("eat")


class Birds(Animals):
    def fly(self):
        print("fly")


class Chickens(Birds):
    pass

#  Chickens --> Birds --> Animals
