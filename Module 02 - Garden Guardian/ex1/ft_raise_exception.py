def input_temperature(temp_str: str) -> int:
    temperature: int = int(temp_str)
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    elif temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    temperature: str = "25"
    try:
        print(f"Input data is '{temperature}'")
        temp: int = input_temperature(temperature)
        print(f"Temperature is now {temp}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    no_temperature: str = "abc"
    try:
        print(f"Input data is '{no_temperature}'")
        temp2: int = input_temperature(no_temperature)
        print(f"Temperature is now {temp2}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    hot: str = "100"
    try:
        print(f"Input data is '{hot}'")
        temp3: int = input_temperature(hot)
        print(f"Temperature is now {temp3}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    cold: str = "-50"
    try:
        print(f"Input data is '{cold}'")
        temp4: int = input_temperature(cold)
        print(f"Temperature is now {temp4}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
