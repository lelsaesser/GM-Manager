from modes.survrim import constants as survrim_constants
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_db_string = "postgres://lelsaesser:@localhost:5432/gm-manager-db"
_db = create_engine(_db_string)
_base = declarative_base()


class SurvrimTable(_base):
    __tablename__ = 'survrim'

    run_id = Column(Integer, primary_key=True)
    player_class = Column(String)
    target_a = Column(String)
    target_b = Column(String)
    timebox = Column(Integer)
    completed = Column(String)
    time_needed = Column(Integer)


Session = sessionmaker(_db)
session = Session()

_base.metadata.create_all(_db)


# Create
run_1 = SurvrimTable(run_id=1, player_class=survrim_constants.CLASS_WARRIOR, target_a=survrim_constants.CITY_WINDHELM,
                     target_b=survrim_constants.CITY_FALKREATH, timebox=60, completed="yes", time_needed=45)

session.add(run_1)
session.commit()
