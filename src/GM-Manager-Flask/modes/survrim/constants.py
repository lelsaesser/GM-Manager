# General
TIME_SURVRUN_MIN_TIMEBOX = 30
TIME_SURVRUN_MAX_TIMEBOX = 70
SURVRIM_YES = "yes"
SURVRIM_NO = "no"

# Errors
SR_ERROR_INVALID_SECTOR_LENGTH = 'len(sectors) is expected to be 1 or 2. Actual: '
SR_ERROR_INVALID_TIME_FACTOR = 'time_factor is expected to be in range(0, 5). Actual: '
SR_ERROR_INVALID_TIME_MOD = 'Error: time_mod is expected to be in range(-15, 26). Actual: '
SR_ERROR_INVALID_PICK_PERCENTAGE_SUM = 'Error: Class pick percentage must add up to 100.0'
SR_ERROR_PICK_CLASS_EXCEPTION = '"Error in pick_class()"'
SR_ERROR_INVALID_CLASS_NAME = 'Error: requested class name not in LIST_SURVRIM_CLASSES'
SR_ERROR_RANDOMANCER_SKILL_LIST_NOT_CREATED = 'Error: randomancer skill list was not created'
SR_ERROR_TEST_PICK_CLASS_FAILED = 'Not all classes picked within 1000 tries... are the pick chances correct?'

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
CLASS_RANDOMANCER = "Randomancer" # special class which is created in survrun_rule_generator.py

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

LIST_SURVRIM_CLASS_SKILLS = [
    CLASS_WARRIOR_SKILLS,
    CLASS_CLERIC_SKILLS,
    CLASS_WARLORD_SKILLS,
    CLASS_SLAYER_SKILLS,
    CLASS_RANGER_SKILLS,
    CLASS_NYMPH_SKILLS
]

# Class pick percentage chance, used in survrun_rule_generator.py. Need to add up to 100.0
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

# Survrun difficulties
DIFFICULTY_EASY = "Easy"
DIFFICULTY_PROMISING = "Promising"
DIFFICULTY_NORMAL = "Normal"
DIFFICULTY_HARSH = "Harsh"
DIFFICULTY_DIFFICULT = "Difficult"
DIFFICULTY_EXTREME = "Extreme"
DIFFICULTY_HARDCORE = "Hardcore"

# List of survrun difficulties
LIST_SURVRUN_DIFFICULTIES = [
    DIFFICULTY_EASY,
    DIFFICULTY_PROMISING,
    DIFFICULTY_NORMAL,
    DIFFICULTY_HARSH,
    DIFFICULTY_DIFFICULT,
    DIFFICULTY_EXTREME,
    DIFFICULTY_HARDCORE
]

# dict keys
SR_KEY_SURVRIM_CONSTANTS = 'survrim_constants'
SR_KEY_LIST_SURVRUN_TARGET_LOCATIONS = 'LIST_SURVRUN_TARGET_LOCATIONS'
SR_KEY_LIST_SURVRIM_SKILLS = 'LIST_SURVRIM_SKILLS'
SR_KEY_LIST_SURVRIM_CLASSES = 'LIST_SURVRIM_CLASSES'
SR_KEY_LIST_SURVRUN_DIFFICULTIES = 'LIST_SURVRUN_DIFFICULTIES'
SR_KEY_TOTAL_RUNS = 'total_runs'
SR_KEY_TOTAL_RUNS_COMPLETED = 'total_runs_completed'
SR_KEY_TOTAL_TIME_PLAYED = 'total_time_played'
SR_KEY_TOTAL_R_COUNT = 'total_r_count'
SR_KEY_TOTAL_CLASS_USES = 'total_class_uses'
SR_KEY_TOTAL_RUNS_WITH_DIFFICULTY = 'total_runs_with_difficulty'
SR_KEY_SECTOR_A = 'sector_a'
SR_KEY_SECTOR_B = 'sector_b'
SR_KEY_SECTOR_C = 'sector_c'
SR_KEY_SECTOR_D = 'sector_d'
SR_KEY_SECTOR_E = 'sector_e'
SR_KEY_SURVRUN_DATA = 'survrunData'
SR_KEY_TARGET_LOCATION_ONE = 'target_location_one'
SR_KEY_TARGET_LOCATION_TWO = 'target_location_two'
SR_KEY_TIMEBOX = 'timebox'
SR_KEY_ID = 'id'
SR_KEY_PLAYER_CLASS = 'player_class'
SR_KEY_TARGET_A = 'target_a'
SR_KEY_TARGET_B = 'target_b'
SR_KEY_COMPLETED = 'completed'
SR_KEY_TIME_NEEDED = 'time_needed'
SR_KEY_R_COUNT = 'r_count'
SR_KEY_SURVRIM_DATA = 'survrimData'
SR_KEY_CLASS_INFO = 'class_info'
SR_KEY_PLAYER_CLASS_SKILLS = 'player_class_skills'
SR_KEY_DIFFICULTY = 'difficulty'
SR_KEY_RATING = 'rating'

SR_FORM_KEY_SUBMIT_RUN_DATA = 'submitRunFormData'
