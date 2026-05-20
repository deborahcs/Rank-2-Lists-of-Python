from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._buffer: list[tuple[int, str]] = []
        self._processing_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._buffer:
            raise IndexError("Buffer is empty")
        return self._buffer.pop(0)

    def total_processed(self) -> int:
        return self._processing_rank

    def remaining(self) -> int:
        return len(self._buffer)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if (
            isinstance(data, list) and
            data and all(isinstance(i, (int, float)) for i in data)
        ):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._buffer.append((self._processing_rank, str(item)))
            self._processing_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if (
            isinstance(data, list) and
            data and all(isinstance(i, str) for i in data)
        ):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._buffer.append((self._processing_rank, str(item)))
            self._processing_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_log_dict(d: Any) -> bool:
            return (
                isinstance(d, dict) and
                all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d.items()
                    )
            )
        if is_log_dict(data):
            return True
        if (
            isinstance(data, list) and
            data and all(is_log_dict(i) for i in data)
        ):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        items = data if isinstance(data, list) else [data]
        for entry in items:
            log_str = ": ".join(entry.values())
            self._buffer.append((self._processing_rank, log_str))
            self._processing_rank += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element "
                      f"in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.total_processed()} items processed, "
                  f"remaining {proc.remaining()} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message':
                'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]

    print("\nSend first batch of data on stream:", batch)
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nConsume some elements from the "
          "data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
