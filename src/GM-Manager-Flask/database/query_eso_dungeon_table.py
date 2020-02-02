from typing import List

from sqlalchemy import create_engine, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import constants as c_db
from database.table_schemas import EsoDungeonRunsTable
from modes.eso import constants as c_eso


class QueryEsoDungeonTable:

    def __init__(self):
        self._db_string = c_db.POSTGRE_FULL_DB_STRING
        self._db = _db = create_engine(self._db_string)
        self._session = sessionmaker(self._db)

    def eso_insert_dungeon_run_query(self, dungeon_name: str, player_count: int, time_needed: int, hardmode: str,
                                     flawless: str, wipes: int, class_one: str, class_two: str, class_three: str,
                                     class_four: str) -> int:
        """
        Insert a dungeon run to the database
        :param dungeon_name: valid eso dungeon name
        :param player_count: integer 1-4
        :param time_needed: integer representing time in minutes (1-999 allowed)
        :param hardmode: boolean, was hardmode completed?
        :param flawless: boolean, was the dungeon completed without a single group member death?
        :param wipes: integer, representing wipe count (times full party faints and battle resets)
        :param class_one: valid eso classname
        :param class_two: valid eso classname
        :param class_three: valid eso classname
        :param class_four: valid eso classname
        :return: 200 on success, 400 on bad request, 500 on insert error
        """

        if dungeon_name not in c_eso.LIST_ESO_DUNGEONS:
            return 400
        if player_count < 1 or player_count > 4:
            return 400
        if time_needed < 1 or time_needed > 999:
            return 400
        if hardmode is None or hardmode == c_eso.ESO_NO:
            hardmode = False
        elif hardmode == c_eso.ESO_YES:
            hardmode = True
        else:
            return 400
        if flawless is None or flawless == c_eso.ESO_NO:
            flawless = False
        elif flawless == c_eso.ESO_YES:
            flawless = True
        else:
            return 400
        if wipes < 0 or wipes > 999:
            return 400
        if class_one not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_two not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_three not in c_eso.LIST_ESO_CLASSES:
            return 400
        if class_four not in c_eso.LIST_ESO_CLASSES:
            return 400

        run_query = EsoDungeonRunsTable(dungeon_name=dungeon_name, player_count=player_count, time_needed=time_needed,
                                        hardmode=hardmode, flawless=flawless, wipes=wipes, class_one=class_one,
                                        class_two=class_two, class_three=class_three, class_four=class_four)

        sess = self._session()
        try:
            sess.add(run_query)
            sess.commit()
            return 200
        except IntegrityError:
            return 500

    def eso_select_dungeon_runs_query(self) -> List[List]:
        """
        Return all rows from eso dungeon runs table
        :return: fetched DB data
        """
        sess = self._session()
        data = sess.query(EsoDungeonRunsTable)

        return data

    def eso_delete_dungeon_run_by_id(self, run_id) -> int:
        """
        Delete the record with the given run_id
        :param run_id: id of the record to delete
        :return: 200 if operation was successful, 400 if requested run_id does not exist
        """
        sess = self._session()
        row = sess.query(EsoDungeonRunsTable).filter(EsoDungeonRunsTable.id == run_id).first()

        if not row:
            return 400

        sess.delete(row)
        sess.commit()
        return 200

    def eso_delete_last_added_record_query(self):
        """
        Delete the last added table record. This is handy for unit/integration tests that create a record to test
        the insert functionality or for undo/revert functionality in frontend.
        Important: this is id based. The record with the highest id is interpreted as last added record. Only works
        with autoincrement.
        """
        sess = self._session()
        data = sess.query(EsoDungeonRunsTable).order_by(desc(EsoDungeonRunsTable.id)).limit(1)

        for row in data:
            sess.delete(row)
            sess.commit()
            return 200
        return 400

    def eso_get_id_of_last_added_record(self):
        """
        Returns the id (int) of the last added record
        Important: expects auto increment of id in database. This just returns the highest id of all rows.
        :return: id of last added record or -1 on failure
        """
        sess = self._session()
        data = sess.query(EsoDungeonRunsTable).order_by(desc(EsoDungeonRunsTable.id)).limit(1)

        for row in data:
            return row.id
        return -1
