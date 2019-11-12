from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from database import constants as db_constants

_db_string = db_constants.POSTGRE_DIALECT_NAME + "://" + db_constants.POSTGRE_USER + ":" + db_constants.POSTGRE_PW + "@" + \
             db_constants.POSTGRE_HOST + ":" + db_constants.POSTGRE_PORT + "/" + db_constants.POSTGRE_DB
_db = create_engine(_db_string)
_base = declarative_base()


class SurvrunTable(_base):
    __tablename__ = db_constants.TABLE_SURVRUN_RUNS

    id = Column(Integer, primary_key=True)
    player_class = Column(String)
    target_a = Column(String)
    target_b = Column(String)
    timebox = Column(Integer)
    completed = Column(String)
    time_needed = Column(Integer)
    r_count = Column(Integer)
    difficulty = Column(String)


_base.metadata.create_all(_db)


