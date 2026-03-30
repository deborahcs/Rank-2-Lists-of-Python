def recursive(days) -> None:
    if days >= 1:
        recursive(days - 1)
        print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive(days)
    print("Harvest time!")
