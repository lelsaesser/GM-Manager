import pytest

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
        test_result_string = "Emperor Frederick | Abbot of Sterling | Richard Lionheart | Nizar the Silent vs. " \
                             "Sultan Abdul | King Phillip | Sheriff of Nottingham | Snake, Lord Python"
        assert StrongholdAiPicker.format_ai_list(test_list) is not None
        assert StrongholdAiPicker.format_ai_list(test_list) == test_result_string
