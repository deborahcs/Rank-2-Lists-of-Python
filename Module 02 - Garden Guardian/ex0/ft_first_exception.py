def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    temperature: str = "25"
    try:
        print(f"Input data is '{temperature}'")
        temp: int = input_temperature(temperature)
        print(f"Temperature is now {temp}°C")

    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    no_temperature: str = "abc"
    try:
        print(f"Input data is {no_temperature}")
        temp2: int = input_temperature(no_temperature)
        print(f"Temperature is now {temp2}°C")
    except ValueError as error:
        print(f"Caught input_temperature error {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
