from database.query_survrun_table import QuerySurvrunTable
from modes.survrim import constants as survrim_constants
from database import constants as db_constants


class TestQuerySurvrunTable:

    def test_survrun_insert_query(self):
        db_cursor = QuerySurvrunTable()
        status, msg = db_cursor.survrun_insert_query(survrim_constants.CLASS_WARRIOR, survrim_constants.CITY_WINDHELM,
                                                     survrim_constants.CITY_WHITERUN, 40, "yes", 32, 3,
                                                     survrim_constants.DIFFICULTY_HARDCORE)

        assert status == 200
        assert msg == db_constants.SUCCESS_QUERY_COMPLETED

        # remove the created table record
        db_cursor.survrun_delete_last_added_record_query()

    def test_survrun_select_query(self):
        db_cursor = QuerySurvrunTable()
        data = db_cursor.survrun_select_query()

        assert data is not None

    def test_survrun_delete_last_added_record_query(self):
        db_cursor = QuerySurvrunTable()

        # create test entry and delete it
        status, msg = db_cursor.survrun_insert_query(survrim_constants.CLASS_WARRIOR, survrim_constants.CITY_WINDHELM,
                                                     survrim_constants.CITY_WHITERUN, 40, "yes", 32, 3,
                                                     survrim_constants.DIFFICULTY_HARDCORE)
        status, msg = db_cursor.survrun_delete_last_added_record_query()

        assert status == 200
        assert msg == db_constants.SUCCESS_QUERY_COMPLETED
