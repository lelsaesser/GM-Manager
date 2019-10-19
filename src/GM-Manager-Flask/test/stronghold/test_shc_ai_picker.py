from modes.stronghold.shc_ai_picker import StrongholdAiPicker
import pytest


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
