class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name
        self._height = 0
        self._days_age = days_age if days_age >= 0 else 0
        print(f"Plant created: {self.name}: "
              f"{round(self.height), 1}, {self.days_age} days old")

    def show(self) -> None:
        print("")
    def set_height(self) -> None:
        if self._height >= 0:
            print("")
        else:
            0.0
    def set_age(self) -> None:
        if self._days_age >= 0:

        else:

    def get_height(self) -> None:
        
    def get_age(self) -> None:
