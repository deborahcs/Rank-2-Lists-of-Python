class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._days_age = days_age if days_age >= 0 else 0
        print(f"Plant created: {self._name}: "
              f"{round(self._height, 1)}cm, {self._days_age} days old")

    def show(self) -> None:
        print(f"Current state: {self._name}: {round(self._height, 1)}cm, "
              f"{self._days_age} days old")

    def set_height(self, new_height) -> None:
        if new_height < 0:
            print("Error, height can't be negative\nHeight update rejected")
        else:
            self._height = new_height
            print(f"Height uptaded: {new_height}cm")

    def set_age(self, new_age) -> None:
        if new_age < 0:
            print("Error, age can't be negative\nAge update rejected")

        else:
            self._days_age = new_age
            print(f"Age uptaded: {new_age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_age


def ft_garden_factory() -> None:

    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-10.0)
    rose.set_age(-8)
    print("")
    rose.show()


if __name__ == "__main__":
    ft_garden_factory()
