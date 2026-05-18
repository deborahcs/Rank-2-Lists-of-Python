class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    for error_to_raise in [PlantError(), WaterError()]:
        try:
            raise error_to_raise
        except GardenError as error:
            print(f"Caught GardenError: {error}")
    print("\nAll custom error types works correctly!")


if __name__ == "__main__":
    test_custom_errors()
