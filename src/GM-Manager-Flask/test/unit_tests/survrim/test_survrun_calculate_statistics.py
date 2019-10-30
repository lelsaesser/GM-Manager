from modes.survrim.survrun_calculate_statistics import SurvrunCalculateStatistics


class TestSurvrunCalculateStatistics:

    def test_get_statistics(self):
        obj = SurvrunCalculateStatistics()
        stats = obj.get_statistics()

        assert stats is not None
        assert type(stats) == dict
        assert type(stats["total_time_played"]) == int
        assert type(stats["total_r_count"]) == int
        assert type(stats["total_runs"]) == int
        assert type(stats["total_runs_completed"]) == int
        assert type(stats["total_class_uses"]) == dict
        assert type(stats["total_runs_with_difficulty"]) == dict

        stats_total_class_uses = stats["total_class_uses"]
        for key, value in zip(stats_total_class_uses.keys(), stats_total_class_uses.values()):
            assert key is not None
            assert type(value) == int

        stats_total_runs_with_difficulty = stats["total_runs_with_difficulty"]
        for key, value in zip(stats_total_runs_with_difficulty.keys(), stats_total_runs_with_difficulty.values()):
            assert key is not None
            assert type(value) == int
