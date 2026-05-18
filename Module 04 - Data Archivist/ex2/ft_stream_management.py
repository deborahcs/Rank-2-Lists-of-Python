import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    content: str = ""

    print("=== Cyber Archives Recovery & Preservation ===")

    file_handle: IO[str] | None = None
    try:
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"Accessing file '{filename}'")
        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': "
                         f"{error}\n")
        return
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{filename}' closed.")

    print("\nTransform data:\n---")
    lines: list[str] = content.splitlines()
    new_content: str = "\n".join([line + "#" for line in lines]) + "\n"
    print(new_content)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    save_name: str = sys.stdin.readline().strip()

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
        sys.stderr.write(f"[STDERR] Error opening file "
                         f"'{save_name}': {error}\n")
        print("Data not saved.")
    finally:
        if file_w is not None:
            file_w.close()


if __name__ == "__main__":
    main()
