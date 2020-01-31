from sqlalchemy import create_engine, Column, String, Integer, Boolean
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


class EsoDungeonRunsTable(_base):
    __tablename__ = db_constants.TABLE_ESO_DUNGEON_RUNS

    id = Column(Integer, primary_key=True)
    dungeon_name = Column(String)
    player_count = Column(Integer)
    time_needed = Column(Integer)
    hardmode = Column(Boolean)
    flawless = Column(Boolean)
    wipes = Column(Integer)
    class_one = Column(String)
    class_two = Column(String)
    class_three = Column(String)
    class_four = Column(String)


class EsoRaidRunsTable(_base):
    __tablename__ = db_constants.TABLE_ESO_RAID_RUNS

    id = Column(Integer, primary_key=True)
    raid_name = Column(String)
    player_count = Column(Integer)
    time_needed = Column(Integer)
    hardmode = Column(Boolean)
    flawless = Column(Boolean)
    wipes = Column(Integer)
    class_one = Column(String)
    class_two = Column(String)
    class_three = Column(String)
    class_four = Column(String)
    class_five = Column(String)
    class_six = Column(String)
    class_seven = Column(String)
    class_eight = Column(String)
    class_nine = Column(String)
    class_ten = Column(String)
    class_eleven = Column(String)
    class_twelve = Column(String)
    num_tanks = Column(Integer)
    num_dps = Column(Integer)
    num_heals = Column(Integer)
    total_party_dps = Column(Integer)
    total_party_hps = Column(Integer)


_base.metadata.create_all(_db)


