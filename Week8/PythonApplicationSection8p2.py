class Car:
    def __init__(self, make, model, sticker):
        self.make = make
        self.model = model
        self.sticker = sticker

    def discount_price(self):
        return self.sticker * 0.90

class Sport(Car):
    def __init__(self, make, model, sticker):
        super().__init__(make, model, sticker)
        self.opt_wheels = "N"
        self.opt_engine = "N"
        self.opt_interior = "N"

    def set_options(self, wheels, engine, interior):
        self.opt_wheels = wheels
        self.opt_engine = engine
        self.opt_interior = interior

    def price_with_options(self):
        total = self.discount_price()
        if self.opt_wheels.upper() == "Y":
            total += 1000
        if self.opt_engine.upper() == "Y":
            total += 3000
        if self.opt_interior.upper() == "Y":
            total += 2000
        return total

# User input version
make = input("Enter car make: ")
model = input("Enter car model: ")
sticker = float(input("Enter sticker price: "))

car = Sport(make, model, sticker)

wheels = input("Add sport wheels (Y/N)? ")
engine = input("Add sport engine (Y/N)? ")
interior = input("Add sport interior (Y/N)? ")

car.set_options(wheels, engine, interior)

print("\n--- Car Summary ---")
print("Make:", car.make)
print("Model:", car.model)
print("Sticker Price:", car.sticker)
print("Discount Price:", car.discount_price())
print("Final Price with Options:", car.price_with_options())