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


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data and all(isinstance(i, (int, float)) for i in data):
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
        if isinstance(data, list) and data and all(isinstance(i, str) for i in data):
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
            return isinstance(d, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())

        if is_log_dict(data):
            return True
        if isinstance(data, list) and data and all(is_log_dict(i) for i in data):
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    
    try:
        print("Test invalid ingestion of string 'foo' without prior validation:")
        num_proc.ingest("foo")
    except TypeError as e:
        print(f"Got exception: {e}")

    num_data =
    print(f"Processing data: {num_data}")
    num_proc.ingest(num_data)
    
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    text_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)
    
    rank, val = text_proc.output()
    print(f"Extracting 1 value...\nText value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()
