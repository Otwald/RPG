from random_gen import RandInterface as Ri
import base as b
from alchemy import DbInterface


class Body:
    """acts as an abstract Class for different Body generators
    """
    ri: Ri
    race: str
    torsoId: int
    headId: int
    limpsId: int
    db: DbInterface
    headmap: dict = {}
    limpsmap: dict = {}
    torsomap: dict = {}

    def __init__(self, race: dict):
        self.ri = Ri()
        self.db = DbInterface()
        self.race = race['name']
        self.torsoId = race['torso']
        self.headId = race['head']
        self.limpsId = race['limps']
        self.__genBodyMapDict()

    def getHead(self, session) -> dict:
        """forms interface for head querys
        """
        return self._getBodyParts(
            session=session,
            bodypart=b.RaceTplHead,
            partid=self.headId,
            partdict=self.headmap
        )

    def getLimbs(self, session) -> dict:
        """forms interface for limps querys
        """
        return self._getBodyParts(
            session=session,
            bodypart=b.RaceTplLimps,
            partid=self.limpsId,
            partdict=self.limpsmap
        )

    def getTorso(self, session) -> dict:
        """forms interface for torso querys
        """
        return self._getBodyParts(
            session=session,
            bodypart=b.RaceTplTorso,
            partid=self.torsoId,
            partdict=self.torsomap
        )

    def genBody(self):
        session = self.db.getSession()
        try:
            self.head = self.getHead(session)
            self.torso = self.getTorso(session)
            self.limps = self.getLimbs(session)
        except:
            session.rollback()
        finally:
            session.close()

    def _getBodyParts(
        self,
        session,
        bodypart,
        partid: int = 0,
        partdict: dict = {}
    ):
        """helper that querys for the race specific bodyparts and builds an dict
        with ran traits
        """
        result = object
        for row in session.query(bodypart) \
                .filter(bodypart.id == partid):
            result = row
        racetraits = self.__getTraits(result)
        return self.__makeTraitQuery(session, partdict, racetraits)

    def __getTraits(self, race: object):
        '''takes an race bodyparts obj from the quers and creates
        and dict with bodyparts and a random index
        '''
        racekeys = race.__dict__.keys()
        racetraits = {}
        for value in list(racekeys):
            if value[0].isupper():
                temp = getattr(race, value)
                if temp is not None:
                    temp = self.ri.getRanEle(temp.split(','))
                    temp = temp.strip()
                racetraits[value] = temp
        return racetraits

    def __makeTraitQuery(self, session, parts: dict = {}, traits: dict = {}) -> dict:
        out = {}
        for key, partsobj in parts.items():
            if traits[key] is not None:
                # print(traits[key])
                for row in session.query(partsobj).filter(partsobj.id == (int(traits[key])+1)):
                    traits[key] = (row.name)
            out[key] = traits[key]
        return out

    def __genBodyMapDict(self) -> None:
        """maps the sql alchemy base classes to a key with dict creation
        """
        self.headmap = {
            'EarS': b.BodyHeadEarS,
            'EarF': b.BodyHeadEarF,
            'ChinF': b.BodyHeadChinF,
            'HairC': b.BodyHeadHairC,
            'HairL': b.BodyHeadHairL,
            'HairT': b.BodyHeadHairT,
            'HeadF': b.BodyHeadHeadF,
            'TuskS': b.BodyHeadTuskS,
            'LipF': b.BodyHeadLipF,
            'NoseF': b.BodyHeadNoseF,
            'EyeC': b.BodyHeadEyeC,
            'HornF': b.BodyHeadHornF,
            'HornN': b.BodyHeadHornN,
            'HornS': b.BodyHeadHornS
        }
        self.limpsmap = {
            'ArmL': b.BodyLimpsArmL,
            'HandS': b.BodyLimpsHandS,
            'HandclawS': b.BodyLimpsHandclawS,
            'LegL': b.BodyLimpsLegL,
            'FootS': b.BodyLimpsFootS,
            'FootT': b.BodyLimpsFootT,
            'FootclawS': b.BodyLimpsFootclawS
        }
        self.torsomap = {
            'SkinC': b.BodyTorsoSkinC,
            'BodyT': b.BodyTorsoBodyT,
            'BodyS': b.BodyTorsoBodyS,
            'TailL': b.BodyTorsoTailL,
            'WingS': b.BodyTorsoWingS
        }
