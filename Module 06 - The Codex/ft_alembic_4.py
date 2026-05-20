import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError:
        print("Testing the hidden create_earth: ")
        raise


if __name__ == "__main__":
    main()
