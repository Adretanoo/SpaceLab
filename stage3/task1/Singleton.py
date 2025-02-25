class CoffeeMachine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CoffeeMachine, cls).__new__(cls)
        return cls._instance

    def make_coffee(self):
        print("Приготування кави...")


machine1 = CoffeeMachine()
machine2 = CoffeeMachine()

print(machine1 is machine2)
