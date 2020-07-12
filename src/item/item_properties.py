def get_weapons_properties():
    WEAPONS_PROPERTIES = (
        "None",
        "Sword",
        "Great Sword",
        "Rapier",
        "Scythe",
        "Great Scythe",
        "Axe",
        "Great Axe",
        "Hammer",
        "Great Hammer",
        "Spear",
        "Long Spear",
        "Shuriken",
        "Great Crossbow",
        "Hidden Blade",
        "Bow",
        "Long Bow",
        "Tome",
        "Grimoire",
        "Pistol"
    )
    return WEAPONS_PROPERTIES


def get_armors_properties():
    # "Rank 1\t\tHP: 05\t\tRed: 2\t\tEff.: 0".expandtabs(),
    # "Rank 2\t\tHP: 10\t\tRed: 3\t\tEff.: 0".expandtabs(),
    # "Rank 3\t\tHP: 15\t\tRed: 4\t\tEff.: 1".expandtabs(),
    # "Rank 4\t\tHP: 20\t\tRed: 5\t\tEff.: 1".expandtabs(),
    # "Rank 5\t\tHP: 25\t\tRed: 6\t\tEff.: 2".expandtabs()

    ARMORS_PROPERTIES = (
        "None",
        "Rank 1",
        "Rank 2",
        "Rank 3",
        "Rank 4",
        "Rank 5"
    )
    return ARMORS_PROPERTIES


def get_accessories_properties():
    ACCESSORIES_PROPERTIES = (
        "Earring",
        "Necklace"
    )
    return ACCESSORIES_PROPERTIES


def get_item_types():
    items_type = []
    items_type.extend(list(get_weapons_properties()))
    items_type.extend(get_accessories_properties())
    items_type.append("Armor")
    items_type.remove("None")

    return sorted(items_type)
