import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")

    all_cap: list[str] = [name.capitalize() for name in players]
    only_cap: list[str] = [name for name in players if name[0].isupper()]

    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list of capitalized names only: {only_cap}")

    scores: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_cap}
    print(f"Score dict: {scores}")

    avg: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    high_scores: dict[str, int] = {
        k: v for k, v in scores.items() if v > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
