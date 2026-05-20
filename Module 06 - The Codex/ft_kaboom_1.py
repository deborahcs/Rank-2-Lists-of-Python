from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    result: str = dark_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
