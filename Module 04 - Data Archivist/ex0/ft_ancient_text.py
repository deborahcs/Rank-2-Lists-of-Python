import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_handle: IO[str] | None = None
    try:
        file_handle = open(filename, 'r')
        content: str = file_handle.read()
        print("---")
        print(content.rstrip("\n"))
        print("---")
    except FileNotFoundError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    except PermissionError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
