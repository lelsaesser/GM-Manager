from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import constants as c_db
from database.table_schemas import ShcRankingTable
from modes.stronghold import constants as c


class QueryShcRankingTable:

    def __init__(self):
        self._db_string = c_db.POSTGRE_FULL_DB_STRING
        self._db = _db = create_engine(self._db_string)
        self._session = sessionmaker(self._db)

    def insert_update_ranking(self, ai_name: str, rating_update: int) -> int:
        """
        Update the rating of an ai or insert it if not present
        :return: 200 on success, 400 if bad request
        """
        if ai_name not in c.AI_CHAR_LIST:
            return 400
        if rating_update is None:
            return 400
        if rating_update == 0:
            return 200

        sess = self._session()
        try:
            # get current rating for requested ai and update it
            ai = sess.query(ShcRankingTable).filter(ShcRankingTable.ai_name == ai_name).one()
            ai.rating += rating_update
            ai.played_games += 1
            if ai.rating < 0:
                ai.rating = 0
            sess.commit()
            return 200

        except Exception:
            # create if not present
            try:
                if rating_update < 0:
                    rating_update = 0
                query = ShcRankingTable(ai_name=ai_name, rating=rating_update, played_games=1)
                sess.add(query)
                sess.commit()
                return 200
            except IntegrityError:
                return 500
