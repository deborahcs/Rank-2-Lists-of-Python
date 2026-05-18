def secure_archive(file_name: str, action: str,
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(file_name, action) as file_handle:
                return (True, file_handle.read())
        elif action == "w":
            with open(file_name, action) as file_handle:
                file_handle.write(content)
                return (True, "Content successfully written to file")
    except FileNotFoundError as error:
        return (False, str(error))
    except PermissionError as error:
        return (False, str(error))
    except OSError as error:
        return (False, str(error))
    return (False, "Please, inform if you want read <r> or write <w>")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    existing: tuple[bool, str] = secure_archive("ancient_fragment.txt", "r")
    print(existing)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", existing[1]))


if __name__ == "__main__":
    main()
