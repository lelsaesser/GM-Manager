from modes.survrim import constants as c
from modes.survrim.survrun_rule_generator import SurvrimRuleGenerator


class TestSurvrimRuleGenerator:

    def test_pick_class(self):
        test_class = SurvrimRuleGenerator.pick_class()

        assert test_class is not None
        assert test_class in c.LIST_SURVRIM_CLASSES

    def test_get_skills_for_class(self):
        test_warrior = SurvrimRuleGenerator.get_skills_for_class(c.CLASS_WARRIOR)

        assert test_warrior is not None
        assert test_warrior == c.CLASS_WARRIOR_SKILLS

        test_randomancer = SurvrimRuleGenerator.get_skills_for_class(c.CLASS_RANDOMANCER)

        assert test_randomancer is not None
        for skill in test_randomancer:
            assert skill in c.LIST_SURVRIM_SKILLS

    def testcreate_randomancer_class(self):
        test = SurvrimRuleGenerator.create_randomancer_class()

        assert test is not None
        assert len(test) > 0

        for skill in test:
            assert skill in c.LIST_SURVRIM_SKILLS
