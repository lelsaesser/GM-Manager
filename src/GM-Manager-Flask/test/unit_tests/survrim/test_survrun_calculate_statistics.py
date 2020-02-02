from modes.survrim import constants as c
from modes.survrim.survrun_calculate_statistics import SurvrunCalculateStatistics


class TestSurvrunCalculateStatistics:

    def test_get_statistics(self):
        obj = SurvrunCalculateStatistics()
        stats = obj.get_statistics()

        assert stats is not None
        assert type(stats) == dict
        assert type(stats[c.SR_KEY_TOTAL_TIME_PLAYED]) == int
        assert type(stats[c.SR_KEY_TOTAL_R_COUNT]) == int
        assert type(stats[c.SR_KEY_TOTAL_RUNS]) == int
        assert type(stats[c.SR_KEY_TOTAL_RUNS_COMPLETED]) == int
        assert type(stats[c.SR_KEY_TOTAL_CLASS_USES]) == dict
        assert type(stats[c.SR_KEY_TOTAL_RUNS_WITH_DIFFICULTY]) == dict

        stats_total_class_uses = stats[c.SR_KEY_TOTAL_CLASS_USES]
        for key, value in zip(stats_total_class_uses.keys(), stats_total_class_uses.values()):
            assert key is not None
            assert type(value) == int

        stats_total_runs_with_difficulty = stats[c.SR_KEY_TOTAL_RUNS_WITH_DIFFICULTY]
        for key, value in zip(stats_total_runs_with_difficulty.keys(), stats_total_runs_with_difficulty.values()):
            assert key is not None
            assert type(value) == int
