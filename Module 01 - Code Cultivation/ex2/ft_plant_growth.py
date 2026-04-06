class Plant:
    def __init__(self, name: str, height: float, days_age: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self.days_age = days_age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.days_age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.days_age += 1


def ft_plant_growth() -> None:
    rose: Plant = Plant("Rose", 25.0, 30, 0.8)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        rose.grow()
        rose.age()
    total_height = rose.height - initial_height
    print(f"Growth this week: {round(total_height)}cm")


if __name__ == "__main__":
    ft_plant_growth()
