from typing import List

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import constants as db_constants
from database.table_schemas import EsoDungeonRunsTable
from modes.eso import constants as eso_constants


class QueryEsoTable:

    def __init__(self):
        self._db_string = db_constants.POSTGRE_DIALECT_NAME + "://" + db_constants.POSTGRE_USER + ":" + \
                          db_constants.POSTGRE_PW + "@" + \
                          db_constants.POSTGRE_HOST + ":" + db_constants.POSTGRE_PORT + "/" + db_constants.POSTGRE_DB

        self._db = _db = create_engine(self._db_string)
        self._session = sessionmaker(self._db)

    def eso_insert_dungeon_run_query(self, dungeon_name: str, player_count: int, time_needed: int, hardmode: bool,
                                     flawless: bool, wipes: int, class_one: str, class_two: str, class_three: str,
                                     class_four: str):
        """
        Insert a dungeon run to the database
        :param dungeon_name: valid eso dungeon name
        :param player_count: integer 1-4
        :param time_needed: integer representing time in minutes
        :param hardmode: boolean, was hardmode completed?
        :param flawless: boolean, was the dungeon completed without a single group member death?
        :param wipes: integer, representing wipe count (times full party faints and battle resets)
        :param class_one: valid eso classname
        :param class_two: valid eso classname
        :param class_three: valid eso classname
        :param class_four: valid eso classname
        :return: 200 on success, 400 on bad request, 500 on insert error
        """

        if dungeon_name not in eso_constants.LIST_ESO_DUNGEONS:
            return 400
        if player_count < 1 or player_count > 4:
            return 400
        if time_needed < 1 or time_needed > 999:
            return 400
        if hardmode is None:
            hardmode = False
        if flawless is None:
            flawless = False
        if wipes < 0 or wipes > 999:
            return 400
        if class_one not in eso_constants.LIST_ESO_CLASSES:
            return 400
        if class_two not in eso_constants.LIST_ESO_CLASSES:
            return 400
        if class_three not in eso_constants.LIST_ESO_CLASSES:
            return 400
        if class_four not in eso_constants.LIST_ESO_CLASSES:
            return 400

        run_query = EsoDungeonRunsTable(dungeon_name=dungeon_name, player_count=player_count, time_needed=time_needed,
                                        hardmode=hardmode, flawless=flawless, wipes=wipes, class_one=class_one,
                                        class_two=class_two, class_three=class_three, class_four=class_four)

        sess = self._session()
        try:
            sess.add(run_query)
            sess.commit()
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
