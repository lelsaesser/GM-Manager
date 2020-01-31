import constants
from database.query_survrun_table import QuerySurvrunTable
from modes.survrim import constants as c


class SurvrunCalculateStatistics:

    def __init__(self):
        self._db_cursor = QuerySurvrunTable()

    def get_statistics(self):
        """
        Query DB and track all run statistics
        :return: dict containing all statistics
        """
        total_time_played = 0
        total_r_count = 0
        total_runs = 0
        total_runs_completed = 0
        total_class_uses = dict({
            c.CLASS_WARRIOR: 0,
            c.CLASS_CLERIC: 0,
            c.CLASS_WARLORD: 0,
            c.CLASS_SLAYER: 0,
            c.CLASS_RANGER: 0,
            c.CLASS_NYMPH: 0,
            c.CLASS_RANDOMANCER: 0
        })
        total_runs_with_difficulty = dict({
            c.DIFFICULTY_EASY: 0,
            c.DIFFICULTY_PROMISING: 0,
            c.DIFFICULTY_NORMAL: 0,
            c.DIFFICULTY_HARSH: 0,
            c.DIFFICULTY_DIFFICULT: 0,
            c.DIFFICULTY_EXTREME: 0,
            c.DIFFICULTY_HARDCORE: 0
        })
        db_data = self._db_cursor.survrun_select_query()
        if not db_data:
            raise ConnectionError(constants.ERROR_GEN_DB_TABLE_EMPTY)

        for row in db_data:
            total_runs += 1
            if row.completed == c.SURVRIM_YES:
                total_runs_completed += 1
            total_r_count += row.r_count
            total_time_played += row.time_needed
            total_class_uses[row.player_class] += 1
            total_runs_with_difficulty[row.difficulty] += 1

        return dict({
            c.SR_KEY_TOTAL_RUNS: total_runs,
            c.SR_KEY_TOTAL_RUNS_COMPLETED: total_runs_completed,
            c.SR_KEY_TOTAL_TIME_PLAYED: total_time_played,
            c.SR_KEY_TOTAL_R_COUNT: total_r_count,
            c.SR_KEY_TOTAL_CLASS_USES: total_class_uses,
            c.SR_KEY_TOTAL_RUNS_WITH_DIFFICULTY: total_runs_with_difficulty
        })
