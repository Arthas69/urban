from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.dialects import registry


registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')
engine = create_engine("sqlite:///taskmanager.db", echo=True)
LocalSession = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
