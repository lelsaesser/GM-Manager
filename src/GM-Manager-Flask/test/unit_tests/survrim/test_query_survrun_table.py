from database.query_survrun_table import QuerySurvrunTable
from modes.survrim import constants as survrim_constants
from database import constants as db_constants


class TestQuerySurvrunTable:

    def test_survrun_insert_query(self):
        query_db = QuerySurvrunTable()
        status, msg = query_db.survrun_insert_query(survrim_constants.CLASS_WARRIOR, survrim_constants.CITY_WINDHELM,
                                                    survrim_constants.CITY_WHITERUN, 40, "yes", 32, 3)

        assert status == 200
        assert msg == db_constants.SUCCESS_QUERY_COMPLETED

        # remove the created table record
        query_db.survrun_delete_last_added_record_query()
