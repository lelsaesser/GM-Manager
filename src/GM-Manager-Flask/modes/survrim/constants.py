# Error
ERROR_LOCATION_MISSING = "Error: invalid location name."

# Survrun times
TIME_SURVRUN_MIN_TIMEBOX = 30
TIME_SURVRUN_MAX_TIMEBOX = 70

# City names
CITY_WINDHELM = "Windhelm"
CITY_FALKREATH = "Falkreath"
CITY_SOLITUDE = "Solitude"
CITY_MORTHAL = "Morthal"
CITY_DAWNSTAR = "Dawnstar"
CITY_MARKARTH = "Markarth"
CITY_RIFTEN = "Riften"
CITY_WHITERUN = "Whiterun"
CITY_WINTERHOLD = "Winterhold"

# Village names
VILLAGE_DRAGON_BRIDGE = "Dragon Bridge"
VILLAGE_KARTHWASTEN = "Karthwasten"
VILLAGE_RORIKSTEAD = "Rorikstead"
VILLAGE_RIVERWOOD = "Riverwood"
VILLAGE_HELGEN = "Helgen"
VILLAGE_IVARSTEAD = "Ivarstead"
VILLAGE_SHORS_STONE = "Shors Stone"

# Locations
LOC_HIGH_HROTHGAR = "High Hrothgar"
LOC_STAUBMANSGRAB = "Staubmansgrab"
LOC_HEXENFELSENSCHANZE = "Hexenfelsenschanze"

# Complete Survrun possible target location list
LIST_SURVRUN_TARGET_LOCATIONS = locations = [
    ERROR_LOCATION_MISSING,
    CITY_WINDHELM,
    CITY_FALKREATH,
    CITY_SOLITUDE,
    CITY_MORTHAL,
    CITY_DAWNSTAR,
    CITY_MARKARTH,
    CITY_RIFTEN,
    CITY_WHITERUN,
    CITY_WINTERHOLD,
    VILLAGE_DRAGON_BRIDGE,
    VILLAGE_KARTHWASTEN,
    VILLAGE_RORIKSTEAD,
    VILLAGE_RIVERWOOD,
    VILLAGE_HELGEN,
    VILLAGE_IVARSTEAD,
    VILLAGE_SHORS_STONE,
    LOC_HIGH_HROTHGAR,
    LOC_STAUBMANSGRAB,
    LOC_HEXENFELSENSCHANZE
]

# Survrun locations split in vertical sectors
LIST_SURVRUN_SECTOR_A = [
    CITY_MARKARTH,
    VILLAGE_KARTHWASTEN,
    LOC_HEXENFELSENSCHANZE
]

LIST_SURVRUN_SECTOR_B = [
    CITY_SOLITUDE,
    CITY_MORTHAL,
    CITY_DAWNSTAR,
    VILLAGE_DRAGON_BRIDGE
]

LIST_SURVRUN_SECTOR_C = [
    CITY_WHITERUN,
    CITY_FALKREATH,
    VILLAGE_RORIKSTEAD,
    VILLAGE_RIVERWOOD,
    VILLAGE_HELGEN,
    VILLAGE_IVARSTEAD,
    LOC_STAUBMANSGRAB,
    LOC_HIGH_HROTHGAR
]

LIST_SURVRUN_SECTOR_D = [
    CITY_WINDHELM,
    CITY_WINTERHOLD
]

LIST_SURVRUN_SECTOR_E = [
    CITY_RIFTEN,
    VILLAGE_SHORS_STONE
]

# Skill names COMBAT
SKILL_COMBAT_HEAVY_ARMOR = "Heavy Armor"
SKILL_COMBAT_LIGHT_ARMOR = "Light Armor"
SKILL_COMBAT_SHIELD = "Shields"
SKILL_COMBAT_ONE_HANDED = "1H Weapons"
SKILL_COMBAT_ONE_HANDED_DAGGER_ONLY = "Daggers (only)"
SKILL_COMBAT_TWO_HANDED = "2H Weapons"
SKILL_COMBAT_DUAL_WIELD = "Dual Wield"
SKILL_COMBAT_OFFHAND_CAST = "Offhand Casting (1H with Spell)"
SKILL_COMBAT_LONGBOW = "Longbows"
SKILL_COMBAT_SHORTBOW = "Shortbows"
SKILL_COMBAT_CROSSBOW = "Crossbows"

# Skill names MAGIC
SKILL_MAGIC_DESTRUCTION = "Destruction Magic"
SKILL_MAGIC_RESTORATION = "Restoration Magic"

# Skill list, contains all skills used in survrim / survrun
LIST_SURVRIM_SKILLS = [
    SKILL_COMBAT_HEAVY_ARMOR,
    SKILL_COMBAT_LIGHT_ARMOR,
    SKILL_COMBAT_SHIELD,
    SKILL_COMBAT_ONE_HANDED,
    SKILL_COMBAT_ONE_HANDED_DAGGER_ONLY,
    SKILL_COMBAT_TWO_HANDED,
    SKILL_COMBAT_DUAL_WIELD,
    SKILL_COMBAT_OFFHAND_CAST,
    SKILL_COMBAT_LONGBOW,
    SKILL_COMBAT_SHORTBOW,
    SKILL_COMBAT_CROSSBOW,
    SKILL_MAGIC_DESTRUCTION,
    SKILL_MAGIC_RESTORATION
]

# Survrim class names
CLASS_WARRIOR = "Warrior"
CLASS_CLERIC = "Cleric"
CLASS_WARLORD = "Warlord"
CLASS_SLAYER = "Slayer"
CLASS_RANGER = "Ranger"
CLASS_NYMPH = "Nymph"
CLASS_RANDOMANCER = "Randomancer" # special class which is created in survrim_rule_generator.py

# Survrim class list, contains all classes available in survrim / survrun
LIST_SURVRIM_CLASSES = [
    CLASS_WARRIOR,
    CLASS_CLERIC,
    CLASS_WARLORD,
    CLASS_SLAYER,
    CLASS_RANGER,
    CLASS_NYMPH,
    CLASS_RANDOMANCER
]

# Survrim classes with allowed skills
CLASS_WARRIOR_SKILLS = [
    SKILL_COMBAT_HEAVY_ARMOR,
    SKILL_COMBAT_LIGHT_ARMOR,
    SKILL_COMBAT_SHIELD,
    SKILL_COMBAT_ONE_HANDED,
    SKILL_COMBAT_CROSSBOW
]

CLASS_CLERIC_SKILLS = [
    SKILL_COMBAT_LIGHT_ARMOR,
    SKILL_COMBAT_ONE_HANDED,
    SKILL_COMBAT_OFFHAND_CAST,
    SKILL_COMBAT_CROSSBOW,
    SKILL_MAGIC_RESTORATION
]

CLASS_WARLORD_SKILLS = [
    SKILL_COMBAT_HEAVY_ARMOR,
    SKILL_COMBAT_LIGHT_ARMOR,
    SKILL_COMBAT_TWO_HANDED,
    SKILL_COMBAT_CROSSBOW
]

CLASS_SLAYER_SKILLS = [
    SKILL_COMBAT_LIGHT_ARMOR,
    SKILL_COMBAT_ONE_HANDED,
    SKILL_COMBAT_DUAL_WIELD,
    SKILL_COMBAT_OFFHAND_CAST,
    SKILL_COMBAT_CROSSBOW,
    SKILL_MAGIC_RESTORATION
]

CLASS_RANGER_SKILLS = [
    SKILL_COMBAT_LIGHT_ARMOR,
    SKILL_COMBAT_ONE_HANDED_DAGGER_ONLY,
    SKILL_COMBAT_DUAL_WIELD,
    SKILL_COMBAT_LONGBOW,
    SKILL_COMBAT_SHORTBOW,
]

CLASS_NYMPH_SKILLS = [
    SKILL_COMBAT_ONE_HANDED,
    SKILL_COMBAT_OFFHAND_CAST,
    SKILL_COMBAT_SHORTBOW,
    SKILL_MAGIC_DESTRUCTION,
    SKILL_MAGIC_RESTORATION
]

# Class pick percentage chance, used in survrim_rule_generator.py. Need to add up to 100.0
PICK_PERCENT_WARRIOR = 15
PICK_PERCENT_CLERIC = 15
PICK_PERCENT_WARLORD = 15
PICK_PERCENT_SLAYER = 15
PICK_PERCENT_RANGER = 15
PICK_PERCENT_NYMPH = 15
PICK_PERCENT_RANDOMANCER = 10

# Class pick percentage list
LIST_CLASS_PICK_PERCENT = [
    PICK_PERCENT_WARRIOR,
    PICK_PERCENT_CLERIC,
    PICK_PERCENT_WARLORD,
    PICK_PERCENT_SLAYER,
    PICK_PERCENT_RANGER,
    PICK_PERCENT_NYMPH,
    PICK_PERCENT_RANDOMANCER
]
