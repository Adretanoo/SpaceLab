class Pizza:
    def prepare(self):
        pass

class CheesePizza(Pizza):
    def prepare(self):
        print("Приготування сирної піци")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Приготування піци пепероні")

class PizzaFactory:
    def create_pizza(self, type):
        if type == "сирна":
            return CheesePizza()
        elif type == "папероні":
            return PepperoniPizza()

factory = PizzaFactory()
pizza = factory.create_pizza("сирна")
pizza.prepare()