from Random_Gen import Monster_NumberGen
from race import human
from base import Race
from alchemy import DbInterface
from body import Body


class BodyFactory:
    """a factory that gives out the different race classes.

        race needs to be in a List at the Moment the List is static
    """

    db: DbInterface

    def __init__(self):
        self.db = DbInterface()

    def _getRaces(self) -> list:
        """makes a query to the Race Table and builds a list from the response
        """
        s = self.db.getSession()
        out = []
        for row in s.query(Race):
            out.append({'name': row.race, 'torso': row.raceTplTorso,
                        'head': row.raceTplHead, 'limps': row.raceTplLimps})
        return out

    def Monster_ArtGen(self) -> object:
        races = self._getRaces()
        race = Monster_NumberGen(races)
        # module = __import__('race')
        # submodule = getattr(module, 'human')
        # raceClass = getattr(submodule, 'Human')
        return Body(race)
