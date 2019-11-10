from db_handler import DataBase
from Random_Gen import Monster_NumberGen


class Body:
    """acts as an abstract Class for different Body generators
    """

    def __init__(self, race):

        self.race = race

    def getHead(self):
        raise NotImplementedError

    def getLimbs(self):
        raise NotImplementedError

    def getTorso(self):
        raise NotImplementedError

    def getParts(self, parts: list, strut: str) -> list:
        out = []
        for part in parts:
            for key, value in part.items():
                if(key.split('_')[0] == strut):
                    out.append({key: value})
        return out

    def getDBRace(self) -> list:
        """ acts as an interface to the MySQL

            at first collects from the race view the possible bodyparts +
            ids
            then chooses one random id and collects the id from the given table
        """
        db = DataBase()
        bodyDict = db.makeRequest(
            """Select * from v_race where race = '""" + self.race + "'"
        )
        out = []
        for key, value in bodyDict.items():
            if(value != None and key != 'id' and key != 'race'):
                test = db.makeRequest(
                    """Select name from body_"""+key+""" where id = """ +
                    Monster_NumberGen(value.split(','))
                )
                out.append({key: test['name']})
        return out

    def genBody(self):
        self.bodyParts = self.getDBRace()
        self.getHead()
        self.getLimbs()
        self.getTorso()


# class Head:

#     def makeReturn(self):
#         raise NotImplementedError


# class Limbs:

#     def makeReturn(self):
#         raise NotImplementedError


# class Torso:

#     def makeReturn(self):
#         raise NotImplementedError
