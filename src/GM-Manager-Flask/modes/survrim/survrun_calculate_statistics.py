import constants
from database.query_survrun_table import QuerySurvrunTable
from modes.survrim import constants as survrim_constants


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
            survrim_constants.CLASS_WARRIOR: 0,
            survrim_constants.CLASS_CLERIC: 0,
            survrim_constants.CLASS_WARLORD: 0,
            survrim_constants.CLASS_SLAYER: 0,
            survrim_constants.CLASS_RANGER: 0,
            survrim_constants.CLASS_NYMPH: 0,
            survrim_constants.CLASS_RANDOMANCER: 0
        })
        total_runs_with_difficulty = dict({
            survrim_constants.DIFFICULTY_EASY: 0,
            survrim_constants.DIFFICULTY_PROMISING: 0,
            survrim_constants.DIFFICULTY_NORMAL: 0,
            survrim_constants.DIFFICULTY_HARSH: 0,
            survrim_constants.DIFFICULTY_DIFFICULT: 0,
            survrim_constants.DIFFICULTY_EXTREME: 0,
            survrim_constants.DIFFICULTY_HARDCORE: 0
        })
        db_data = self._db_cursor.survrun_select_query()
        if not db_data:
            raise ConnectionError(constants.ERROR_GEN_DB_TABLE_EMPTY)

        for row in db_data:
            total_runs += 1
            if row.completed == "yes":
                total_runs_completed += 1
            total_r_count += row.r_count
            total_time_played += row.time_needed
            total_class_uses[row.player_class] += 1
            total_runs_with_difficulty[row.difficulty] += 1

        return dict({
            'total_runs': total_runs,
            'total_runs_completed': total_runs_completed,
            'total_time_played': total_time_played,
            'total_r_count': total_r_count,
            'total_class_uses': total_class_uses,
            'total_runs_with_difficulty': total_runs_with_difficulty
        })
