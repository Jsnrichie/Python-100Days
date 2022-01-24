# Default value functions


# Unlimited Args
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4))

# Many keyword args

def calculate(n, **kwargs):
    print(kwargs) # Creates a dict

    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2, add = 3, multiply= 5)


class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        self.make = kwargs.get("make")
        # self.model = kwargs["model"]
        self.model = kwargs.get("model")

my_car = Car(make= "BMW")
print(my_car.model)