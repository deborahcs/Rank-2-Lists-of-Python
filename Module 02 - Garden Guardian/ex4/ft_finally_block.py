class PlantError(Exception):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    capitalize_plant: str = plant_name.capitalize()
    if capitalize_plant != plant_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    try:
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    mixed_plants: list[str] = ["Tomato", "lettuce"]
    try:
        print("Opening watering system")
        for plant in mixed_plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print(".. ending tests and returning to main")
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
