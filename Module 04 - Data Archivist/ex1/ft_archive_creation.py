import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv} <file>")
        return

    filename: str = sys.argv[1]
    content: str = ""

    print("=== Cyber Archives Recovery & Preservation ===")
    file_handle: IO[str] | None = None
    try:
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"Accessing file '{filename}'")
        print("---")
        print(content, end="")
        if content and not content.endswith('\n'):
            print()
        print("---")
    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Error opening file '{filename}': {error}")
        return
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{filename}' closed.\n")

    print("Transform data:")
    print("---")
    lines: list[str] = content.splitlines()
    new_content: str = "\n".join([line + "#" for line in lines]) + "\n"
    print(new_content, end="")
    print("---")

    save_name: str = input("Enter new file name (or empty): ")
    if not save_name:
        print("Not saving data.")
        return

    file_w: IO[str] | None = None
    try:
        print(f"Saving data to '{save_name}'")
        file_w = open(save_name, 'w')
        file_w.write(new_content)
        print(f"Data saved in file '{save_name}'.")
    except OSError as error:
        print(f"Error saving file '{save_name}': {error}")
    finally:
        if file_w is not None:
            file_w.close()


if __name__ == "__main__":
    main()
