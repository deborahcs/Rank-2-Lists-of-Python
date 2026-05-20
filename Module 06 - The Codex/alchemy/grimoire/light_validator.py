def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    ingredients_normalized: str = ingredients.lower()
    is_valid: bool = False
    for ingredient in allowed:
        if ingredient in ingredients_normalized:
            is_valid = True
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
