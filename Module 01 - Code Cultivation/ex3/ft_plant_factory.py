class Plant:
    def __init__(self, name: str, height: float, days_age: 
                 int, growth: float) -> None:
        self.name = name
        self.height = name
        self.days_age = days_age

    def show(self) -> None:
        print(f"Created: {self.name}: {round(self.height)}cm, "
              f"{self.days_age} days old")
    def grow(self, growth) -> None:
        self.height = self.growth

    def age(self) -> None:
        self.days_age += 1
            
