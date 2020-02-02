from typing import List

from modes.survrim import constants as c
import random


class SurvrimRuleGenerator:

    @staticmethod
    def pick_class() -> str:
        """
        Choose a random class based on the pick %chance defined in constants
        :return: string containing chosen class name
        """
        if sum(c.LIST_CLASS_PICK_PERCENT) is not 100:
            raise Exception(c.SR_ERROR_INVALID_PICK_PERCENTAGE_SUM)

        pick_warrior_range = c.PICK_PERCENT_WARRIOR  # warrior is picked if roll is 0 - 20
        pick_cleric_range = pick_warrior_range + c.PICK_PERCENT_CLERIC  # ...if roll is 21 - 40 etc.
        pick_warlord_range = pick_cleric_range + c.PICK_PERCENT_WARLORD
        pick_slayer_range = pick_warlord_range + c.PICK_PERCENT_SLAYER
        pick_ranger_range = pick_slayer_range + c.PICK_PERCENT_RANGER
        pick_nymph_range = pick_ranger_range + c.PICK_PERCENT_NYMPH
        pick_randomancer_range = pick_nymph_range + c.PICK_PERCENT_RANDOMANCER

        roll = random.randint(0, 100)  # each class has a %chance to be picked
        if 0 <= roll < pick_warrior_range:  # 0 - 19
            return c.CLASS_WARRIOR
        elif pick_warrior_range <= roll <= pick_cleric_range:  # 20 - 40
            return c.CLASS_CLERIC
        elif pick_cleric_range < roll <= pick_warlord_range:
            return c.CLASS_WARLORD
        elif pick_warlord_range < roll <= pick_slayer_range:
            return c.CLASS_SLAYER
        elif pick_slayer_range < roll <= pick_ranger_range:
            return c.CLASS_RANGER
        elif pick_ranger_range < roll <= pick_nymph_range:
            return c.CLASS_NYMPH
        elif pick_nymph_range < roll <= pick_randomancer_range:
            return c.CLASS_RANDOMANCER
        else:
            raise Exception(c.SR_ERROR_PICK_CLASS_EXCEPTION)

    @staticmethod
    def get_skills_for_class(class_name: str):
        """
        Return skill list for requested class
        :param class_name: valid class name string
        :return: string list containing full names of all skills for this class
        """
        if class_name not in c.LIST_SURVRIM_CLASSES:
            raise Exception(c.SR_ERROR_INVALID_CLASS_NAME)

        randomancer_skills = SurvrimRuleGenerator.create_randomancer_class()
        if not randomancer_skills:
            raise Exception(c.SR_ERROR_RANDOMANCER_SKILL_LIST_NOT_CREATED)

        class_name_skill_map = {
            c.CLASS_WARRIOR: c.CLASS_WARRIOR_SKILLS,
            c.CLASS_CLERIC: c.CLASS_CLERIC_SKILLS,
            c.CLASS_WARLORD: c.CLASS_WARLORD_SKILLS,
            c.CLASS_SLAYER: c.CLASS_SLAYER_SKILLS,
            c.CLASS_RANGER: c.CLASS_RANGER_SKILLS,
            c.CLASS_NYMPH: c.CLASS_NYMPH_SKILLS,
            c.CLASS_RANDOMANCER: randomancer_skills
        }

        return class_name_skill_map[class_name]

    @staticmethod
    def create_randomancer_class() -> List[str]:
        """
        Create and return a completely randomized class.
        :return: string list containing the skills of the randomized class. Min length is 1.
        """
        class_randomancer_skills = []
        for skill in c.LIST_SURVRIM_SKILLS:
            roll = random.randint(0, 2)  # have a 33% chance for each skill
            if roll == 1:
                class_randomancer_skills.append(skill)

        # prevent that both 1H and 1H only dagger is in skill list
        if c.SKILL_COMBAT_ONE_HANDED in class_randomancer_skills and \
                c.SKILL_COMBAT_ONE_HANDED_DAGGER_ONLY in class_randomancer_skills:
            class_randomancer_skills.remove(c.SKILL_COMBAT_ONE_HANDED_DAGGER_ONLY)

        # prevent that offhand casting, but no magic talent is in skill list
        if c.SKILL_COMBAT_OFFHAND_CAST in class_randomancer_skills and \
                c.SKILL_MAGIC_DESTRUCTION not in class_randomancer_skills and \
                c.SKILL_MAGIC_RESTORATION not in class_randomancer_skills:
            class_randomancer_skills.remove(c.SKILL_COMBAT_OFFHAND_CAST)

        # prevent that dual wield, but no 1H talent is in skill list
        if c.SKILL_COMBAT_DUAL_WIELD in class_randomancer_skills and \
                c.SKILL_COMBAT_ONE_HANDED not in class_randomancer_skills and \
                c.SKILL_COMBAT_ONE_HANDED_DAGGER_ONLY not in class_randomancer_skills:
            class_randomancer_skills.remove(c.SKILL_COMBAT_DUAL_WIELD)

        # prevent that a randomancer can have 0 skills
        elif len(class_randomancer_skills) == 0:  # worst case: only daggers available
            class_randomancer_skills.append(c.SKILL_COMBAT_ONE_HANDED_DAGGER_ONLY)
        return class_randomancer_skills
