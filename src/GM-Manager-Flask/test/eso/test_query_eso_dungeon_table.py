from database.query_eso_dungeon_table import QueryEsoDungeonTable
from modes.eso import constants as c


class TestQueryEsoDungeonTable:

    def test_eso_insert_query(self):
        db_cursor = QueryEsoDungeonTable()
        status = db_cursor.eso_insert_dungeon_run_query(dungeon_name=c.DUNGEON_SPINDLECLUTCH_I,
                                                        player_count=4, time_needed=30, hardmode=c.ESO_YES,
                                                        flawless=c.ESO_NO,
                                                        wipes=1, class_one=c.CLASS_DRAGONKNIGHT,
                                                        class_two=c.CLASS_NIGHTBLADE,
                                                        class_three=c.CLASS_SORCERER,
                                                        class_four=c.CLASS_TEMPLAR)

        assert status == 200

        # remove the created table record
        status = db_cursor.eso_delete_last_added_record_query()
        assert status == 200

    def test_eso_select_query(self):
        db_cursor = QueryEsoDungeonTable()
        data = db_cursor.eso_select_dungeon_runs_query()

        assert data is not None

    def test_eso_delete_query(self):
        db_cursor = QueryEsoDungeonTable()
        status = db_cursor.eso_insert_dungeon_run_query(dungeon_name=c.DUNGEON_SPINDLECLUTCH_I,
                                                        player_count=4, time_needed=30, hardmode=c.ESO_YES,
                                                        flawless=c.ESO_NO,
                                                        wipes=1, class_one=c.CLASS_DRAGONKNIGHT,
                                                        class_two=c.CLASS_NIGHTBLADE,
                                                        class_three=c.CLASS_SORCERER,
                                                        class_four=c.CLASS_TEMPLAR)

        assert status == 200

        last_id = db_cursor.eso_get_id_of_last_added_record()
        assert last_id > -1

        status = db_cursor.eso_delete_dungeon_run_by_id(last_id)
        assert status == 200
