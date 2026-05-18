import random
from typing import Generator

NAMES: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab",
                      "move", "swim", "climb", "release", "use"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name: str = random.choice(NAMES)
        action: str = random.choice(ACTIONS)
        yield (name, action)


def consume_event(event_list:
                  list[tuple[str, str]]) -> Generator[tuple[str,
                                                            str], None, None]:
    while len(event_list) > 0:
        idx: int = random.randint(0, len(event_list) - 1)
        item: tuple[str, str] = event_list.pop(idx)
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream: Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    event_list: list[tuple[str, str]] = [next(event_stream) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {event_list}\n")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
