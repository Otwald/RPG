
from alchemy import DbInterface
from base import RaceTplTorso, RaceTplHead, RaceTplLimps, Race, Base


class MonsterGen:

    races: list
    tables: list
    db: DbInterface

    def __init__(self):
        self.races = [
            self.Monster_Demon, self.Monster_Human, self.Monster_Undead,
            self.Monster_Orcoid, self.Monster_Repte,
        ]
        self.tables = [RaceTplTorso, RaceTplHead, RaceTplLimps]
        self.db = DbInterface()

    def __insertEntry(self, tclass: Base, context: dict, race: str, session) -> Base:
        """populates the newly created table with context
        """
        initclass = tclass(race=race, **context)
        session.add(initclass)
        return initclass

    def __insertMapping(self, view: dict, session) -> None:
        """creates an entry for the race mapping
        """
        for key, value in view.items():
            torso, head, limps = value
            session.add(Race(key, torso, head, limps))
        session.commit()

    def checkDB(self) -> None:
        """calls the DB to check if DB was already created, if not calls a creator
        """
        view = {}
        session = self.db.getSession()
        for tableClass in self.tables:
            if not self.db.checkTable(tableClass):
                self.db.createTable(tableClass)
                for race in self.races:
                    name, body = race()
                    initclass = self.__insertEntry(
                        tableClass,
                        body[tableClass.__tablename__],
                        name,
                        session
                    )
                    session.commit()
                    if name not in view:
                        view[name] = []
                    view[name].append(initclass.id)
        if view:
            self.db.createTable(Race)
            self.__insertMapping(view, session)
        session.close()

    def Monster_Orcoid(self) -> list:
        body_dict = {
            'SkinC': '4, 5, 6, 7', 'BodyT': '0, 1, 2, 3, 4, 6',
            'BodyS': '0, 1, 2', 'WingS': None, 'TailL': None
        }
        head_dict = {
            'HeadF': '2, 3', 'EyeC': '0, 2, 3', 'NoseF': '0, 1, 2',
            'ChinF': '0, 1, 2, 3, 4', 'LipF': '0, 1',
            'EarF': '2, 3', 'EarS': '0, 1',
            'HairL': '0, 4', 'HairT': '1, 2', 'HairC': '0, 1',
            'HornN': None, 'HornS':  None, 'HornF': None,
            'TuskS': '0, 1, 2, 3, 4, 5'
        }
        limbs_dict = {
            'ArmL': '0, 1, 2', 'HandS': '0, 1, 2',
            'HandclawS': '0, 1, 2', 'LegL': '0, 1, 2', 'FootS': '0, 1, 2',
            'FootclawS': '0, 1, 2', 'FootT': '0'
        }
        race = 'Orc'

        input_list = {
            RaceTplTorso.__tablename__: body_dict,
            RaceTplHead.__tablename__: head_dict,
            RaceTplLimps.__tablename__: limbs_dict
        }

        return race, input_list

    def Monster_Undead(self) -> list:
        body_dict = {
            'SkinC': '1, 2, 3, 5', 'BodyT': '0, 1, 2, 3, 4, 5, 6',
            'BodyS': '0, 1, 2', 'WingS': None, 'TailL': None
        }
        head_dict = {
            'HeadF': '0, 1, 2, 3', 'EyeC': '0, 1, 2',
            'NoseF': '0, 1, 2, 3', 'ChinF': '0, 1, 2, 3, 4', 'LipF': '0, 1, 2, 3, 4',
            'EarF': '0, 1', 'EarS': '0, 1',
            'HairL': '0, 1, 2, 3, 4', 'HairT': '0, 1, 2', 'HairC': '0, 1, 2, 3',
            'HornN': None, 'HornS':  None, 'HornF': None,
            'TuskS': None
        }
        limbs_dict = {
            'ArmL': '0, 1, 2', 'HandS':  '0, 1, 2', 'HandclawS':  '0, 1, 2',
            'LegL':  '0, 1, 2', 'FootS': '0, 1, 2', 'FootclawS': '0, 1, 2', 'FootT': '0'
        }
        race = 'Undead'

        input_list = {
            RaceTplTorso.__tablename__: body_dict,
            RaceTplHead.__tablename__: head_dict,
            RaceTplLimps.__tablename__: limbs_dict
        }

        return race, input_list

    def Monster_Human(self) -> list:
        body_dict = {
            'SkinC': '0, 1, 2, 3, 4', 'BodyT': '0, 1, 2, 3, 4, 5, 6',
            'BodyS': '0, 1, 2', 'WingS': None, 'TailL': None
        }
        head_dict = {
            'HeadF': '0, 1, 2, 3', 'EyeC': '0, 1, 2', 'NoseF': '0, 1, 2, 3',
            'ChinF': '0, 1, 2, 3, 4', 'LipF': '0, 1, 2, 3, 4',
            'EarF': '0, 1', 'EarS': '0, 1',
            'HairL': '0, 1, 2, 3, 4', 'HairT': '0, 1, 2', 'HairC': '0, 1, 2, 3',
            'HornN': None, 'HornS':  None, 'HornF': None,
            'TuskS': None
        }
        limbs_dict = {
            'ArmL': '0, 1, 2', 'HandS': '0, 1, 2', 'HandclawS': '0, 1, 2',
            'LegL': '0, 1, 2', 'FootS': '0, 1, 2', 'FootclawS': '0, 1, 2', 'FootT': '0'
        }
        race = 'Human'

        input_list = {
            RaceTplTorso.__tablename__: body_dict,
            RaceTplHead.__tablename__: head_dict,
            RaceTplLimps.__tablename__: limbs_dict
        }
        return race, input_list

    def Monster_Repte(self) -> list:
        body_dict = {
            'SkinC': '3, 4, 5, 6, 7, 8', 'BodyT': '0, 1, 2, 3, 4, 5, 6',
            'BodyS': '0, 1, 2', 'WingS': None, 'TailL': '0, 1, 2'
        }
        head_dict = {
            'HeadF': '0, 1, 2, 3', 'EyeC': '0, 1, 3', 'NoseF': '0, 1, 2, 3',
            'ChinF': '0, 1, 2, 3, 4', 'LipF': None,
            'EarF': None, 'EarS': '0, 1',
            'HairL': None, 'HairT': None, 'HairC': None,
            'HornN': '0, 1, 2, 3', 'HornS':  '0, 1, 2', 'HornF': '2, 3, 4',
            'TuskS': None
        }
        limbs_dict = {
            'ArmL': '0, 1, 2', 'HandS': '0, 1, 2', 'HandclawS':  '0, 1, 2',
            'LegL': '0, 1, 2', 'FootS': '0, 1, 2', 'FootclawS': '0, 1, 2', 'FootT': '0'
        }
        race = 'Lizardmen'

        input_list = {
            RaceTplTorso.__tablename__: body_dict,
            RaceTplHead.__tablename__: head_dict,
            RaceTplLimps.__tablename__: limbs_dict
        }

        return race, input_list

    def Monster_Demon(self) -> list:
        body_dict = {
            'SkinC': '1, 2, 9, 4', 'BodyT': '0, 1, 2, 3, 4',
            'BodyS': '0, 1, 2', 'WingS': '0, 1, 2, 3, 4', 'TailL': '0, 1, 2'
        }
        head_dict = {
            'HeadF':  '0, 1, 2, 3', 'EyeC': '0, 1, 2, 3, 4',
            'NoseF': '0, 1, 2, 3', 'ChinF': '0, 1, 2, 3, 4', 'LipF': '0',
            'EarF': '0, 1', 'EarS': '0, 1',
            'HairL': '0, 1, 2, 3, 4', 'HairT': '0, 1, 2', 'HairC': '0, 1, 2, 3',
            'HornN': '1, 2, 3', 'HornS':  '0, 1, 2, 3, 4', 'HornF': '1, 2, 3, 4',
            'TuskS': None
        }
        limbs_dict = {
            'ArmL': '0, 1, 2', 'HandS': '0, 1, 2', 'HandclawS': '0, 1, 2',
            'LegL': '0, 1, 2', 'FootS': '0, 1, 2', 'FootclawS': '0, 1, 2', 'FootT': '0, 1, 2, 3, 4, 5'
        }
        race = 'Demonkin'

        input_list = {
            RaceTplTorso.__tablename__: body_dict,
            RaceTplHead.__tablename__: head_dict,
            RaceTplLimps.__tablename__: limbs_dict
        }

        return race, input_list
