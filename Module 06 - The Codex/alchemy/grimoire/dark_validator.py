from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    allowed: list[str] = dark_spell_allowed_ingredients()
    ingredients_normalized: str = ingredients.lower()
    is_valid: bool = False
    for ingredient in allowed:
        if ingredient in ingredients_normalized:
            is_valid = True
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
