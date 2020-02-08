import pytest

from modes.stronghold import constants as c
from modes.stronghold.shc_ai_picker import StrongholdAiPicker


class TestShcAiPicker:

    def test_pick_random_ai(self):
        with pytest.raises(ValueError):
            StrongholdAiPicker.pick_random_ai(-1)
        with pytest.raises(ValueError):
            StrongholdAiPicker.pick_random_ai(0)
        with pytest.raises(ValueError):
            StrongholdAiPicker.pick_random_ai(1)
        with pytest.raises(ValueError):
            StrongholdAiPicker.pick_random_ai(9)

        assert len(StrongholdAiPicker.pick_random_ai(8)) == 8
        assert len(StrongholdAiPicker.pick_random_ai(5)) == 5
        assert len(StrongholdAiPicker.pick_random_ai(2)) == 2

    def test_format_ai_list(self):
        with pytest.raises(ValueError):
            StrongholdAiPicker.format_ai_list([])
        with pytest.raises(ValueError):
            StrongholdAiPicker.format_ai_list(["Rat, Duc the Puce", "HelloWorld", 123])

        test_list = ['Emperor Frederick', 'Abbot of Sterling', 'Richard Lionheart', 'Nizar the Silent', 'Sultan Abdul',
                     'King Phillip', 'Sheriff of Nottingham', 'Snake, Lord Python']
        expected = "Emperor Frederick | Abbot of Sterling | Richard Lionheart | Nizar the Silent vs. " \
                   "Sultan Abdul | King Phillip | Sheriff of Nottingham | Snake, Lord Python"
        assert StrongholdAiPicker.format_ai_list(test_list) is not None
        assert StrongholdAiPicker.format_ai_list(test_list) == expected

    def test_split_ai_in_teams(self):
        with pytest.raises(ValueError):
            StrongholdAiPicker.split_ai_in_teams([])
        with pytest.raises(Exception):
            StrongholdAiPicker.split_ai_in_teams([c.AI_ABBOT])

        test_list = [c.AI_ABBOT, c.AI_RAT, c.AI_SNAKE, c.AI_PIG, c.AI_WOLF, c.AI_CALIPH, c.AI_SALADIN, c.AI_SULTAN]
        expected = [
            [c.AI_ABBOT, c.AI_RAT, c.AI_SNAKE, c.AI_PIG],
            [c.AI_WOLF, c.AI_CALIPH, c.AI_SALADIN, c.AI_SULTAN]
        ]
        assert StrongholdAiPicker.split_ai_in_teams(test_list) == expected

        test_list = [c.AI_ABBOT, c.AI_RAT, c.AI_SNAKE]
        expected = [
            [c.AI_ABBOT],
            [c.AI_RAT, c.AI_SNAKE]
        ]
        assert StrongholdAiPicker.split_ai_in_teams(test_list) == expected
