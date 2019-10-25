from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from modes.survrim import constants as survrim_constants
from database import constants as db_constants
from database.table_schemas import SurvrimTable


class CommitDataToDatabase:

    def __init__(self):
        self._db_string = "postgres://" + db_constants.POSTGRE_USER + ":" + db_constants.POSTGRE_PW + "@" + \
                          db_constants.POSTGRE_HOST + ":" + db_constants.POSTGRE_PORT + "/" + db_constants.POSTGRE_DB

        self._db = _db = create_engine(self._db_string)
        self._session = sessionmaker(self._db)

    def table_insert_query(self, player_class: str, target_a: str, target_b: str, timebox: int, completed: str,
                           time_needed: int, r_count: int):
        if player_class not in survrim_constants.LIST_SURVRIM_CLASSES:
            raise Exception("Error:", player_class, " is not a valid class name")
        elif target_a not in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS \
                or target_b not in survrim_constants.LIST_SURVRUN_TARGET_LOCATIONS:
            raise Exception("Error:", target_a, target_b, ": one or more are no valid target location names")

        run_query = SurvrimTable(player_class=player_class, target_a=target_a, target_b=target_b, timebox=timebox,
                                 completed=completed, time_needed=time_needed, r_count=r_count)

        sess = self._session()
        try:
            sess.add(run_query)
            sess.commit()
        except IntegrityError:  # thrown if duplicate PK (id)
            print("PK already exists, skipping")
