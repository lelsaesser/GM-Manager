from modes.survrim.survrun_rule_generator import SurvrimRuleGenerator
from modes.survrim import constants as c


class TestSurvrimRuleGenerator:

    def test_pick_class(self):
        roll_count_limit = 1000
        roll_count = 0
        picked_classes = []

        while len(picked_classes) != len(c.LIST_SURVRIM_CLASSES):
            pick = SurvrimRuleGenerator.pick_class()
            if pick not in picked_classes:
                picked_classes.append(pick)
            if roll_count >= roll_count_limit:
                raise Exception("Not all classes picked within 1000 tries... are the pick chances correct?")
            roll_count += 1

        assert len(picked_classes) == len(c.LIST_SURVRIM_CLASSES)

    def test_get_skills_for_class(self):
        for class_name in c.LIST_SURVRIM_CLASSES:
            skill_list = SurvrimRuleGenerator.get_skills_for_class(class_name)
            if class_name == c.CLASS_WARRIOR:
                assert skill_list == c.CLASS_WARRIOR_SKILLS
            elif class_name == c.CLASS_CLERIC:
                assert skill_list == c.CLASS_CLERIC_SKILLS
            elif class_name == c.CLASS_WARLORD:
                assert skill_list == c.CLASS_WARLORD_SKILLS
            elif class_name == c.CLASS_SLAYER:
                assert skill_list == c.CLASS_SLAYER_SKILLS
            elif class_name == c.CLASS_RANGER:
                assert skill_list == c.CLASS_RANGER_SKILLS
            elif class_name == c.CLASS_NYMPH:
                assert skill_list == c.CLASS_NYMPH_SKILLS
            elif class_name == c.CLASS_RANDOMANCER:
                assert skill_list is not None
