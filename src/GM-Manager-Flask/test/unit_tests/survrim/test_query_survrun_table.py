from database import constants as db_constants
from database.query_survrun_table import QuerySurvrunTable
from modes.survrim import constants as c


class TestQuerySurvrunTable:

    def test_survrun_insert_query(self):
        db_cursor = QuerySurvrunTable()
        status, msg = db_cursor.survrun_insert_query(c.CLASS_WARRIOR, c.CITY_WINDHELM,
                                                     c.CITY_WHITERUN, 40, c.SURVRIM_YES, 32, 3,
                                                     c.DIFFICULTY_HARDCORE)

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
        status, msg = db_cursor.survrun_insert_query(c.CLASS_WARRIOR, c.CITY_WINDHELM,
                                                     c.CITY_WHITERUN, 40, c.SURVRIM_YES, 32, 3,
                                                     c.DIFFICULTY_HARDCORE)
        status, msg = db_cursor.survrun_delete_last_added_record_query()

        assert status == 200
        assert msg == db_constants.SUCCESS_QUERY_COMPLETED

    def test_survrun_delete_query(self):
        db_cursor = QuerySurvrunTable()

        status, msg = db_cursor.survrun_insert_query(c.CLASS_WARRIOR, c.CITY_WINDHELM,
                                                     c.CITY_WHITERUN, 40, c.SURVRIM_YES, 32, 3,
                                                     c.DIFFICULTY_HARDCORE)

        assert status == 200
        assert msg == db_constants.SUCCESS_QUERY_COMPLETED

        last_id = db_cursor.survrun_get_id_of_last_added_record()
        assert last_id > -1

        status, msg = db_cursor.survrun_delete_record_by_id_query(last_id)
        assert status == 200
        assert msg == db_constants.SUCCESS_QUERY_COMPLETED
