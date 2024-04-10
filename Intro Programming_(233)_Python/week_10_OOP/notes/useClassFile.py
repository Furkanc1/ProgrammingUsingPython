from OOP import Car;

car1 = Car(
    "Nissan",
    "Sentra",
    "2010",
    "Black"
)

car2 = Car(
    "audi",
    "S4",
    "2018",
    "Black"
)

print(f"Car 1:\n{car1.make}\n{car1.model}\n{car1.year}\n{car1.color}")

car1.drive()
car2.stop()
