from random_gen import RandInterface as Ri
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
        self.ri = Ri()

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
        out = ['head','limps', 'torso']
        races = self._getRaces()
        race = self.ri.getRanEle(races)
        body =Body(race)
        body.genBody()
        for part in out:
            yield getattr(body, part)
