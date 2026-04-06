class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name
        self.height = height
        self.days_age = days_age
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.days_age} days old")

    def grow(self, growth: int) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.days_age += 1


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    garden: list[Plant] = [
        Plant("Rose",  25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("")
    for plant in garden:
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
