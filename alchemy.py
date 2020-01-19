from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker
from base import Base


class DbInterface:

    config: dict = {}

    def __init__(self, db: str = 'sqlite:///memory.db'):
        self.config['db'] = db
        self.__buildEngine()

    def __buildEngine(self) -> None:
        """init the db engine and binds metadata to it
        """
        self.engine = create_engine(self.config['db'])
        self.metadata = MetaData(bind=self.engine)

    def getSession(self) -> sessionmaker:
        Session = sessionmaker(bind=self.engine)
        return Session()

    def checkTable(self, tclass: Base) -> bool:
        """builds an Interface to check if an Table Exists in the DataBase
        """
        return self.engine.dialect.has_table(self.engine, tclass.__tablename__)

    def createTable(self, tclass: Base) -> None:
        """creates a table from a subclass of Base
        """
        Base.metadata.tables[tclass.__tablename__].create(bind=self.engine)

# db = DbInterface()
# s = db.getSession()


# db.metadata.create_all()

# body = Bg.BodyGen()
# bodyp = body.Body_Head_Chin()
# print(bodyp)
# for part in bodyp:
#     ins = bodyParts.insert().values(name = part)
#     result = conn.execute(ins)
#     print(result)

# test = s.query(bodyParts).filter(bodyParts.c.id == 1)

# print(bodyParts.c)
# for row in test:
#     print(row.name)
# s.commit()
# s.close()

# bodyParts.drop(db.engine)
