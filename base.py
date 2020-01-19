from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey

Base = declarative_base()


class Race(Base):
    __tablename__ = 'race'

    id = Column(Integer, primary_key=True)
    race = Column(String, nullable=False, unique=True)
    raceTplTorso = Column(Integer, ForeignKey('race_TplTorso.id'))
    raceTplHead = Column(Integer, ForeignKey('race_TplHead.id'))
    raceTplLimps = Column(Integer, ForeignKey('race_TplLimps.id'))

    def __init__(self,
                 race: str = '',
                 raceTplTorso: str = '',
                 raceTplHead: str = '',
                 raceTplLimps: str = ''
                 ):
        self.race = race
        self.raceTplTorso = raceTplTorso
        self.raceTplHead = raceTplHead
        self.raceTplLimps = raceTplLimps


class RaceTplTorso(Base):
    __tablename__ = 'race_TplTorso'

    id = Column(Integer, primary_key=True)
    race = Column(String,nullable=False, unique=True)
    SkinC = Column(String)
    BodyT = Column(String)
    BodyS = Column(String)
    TailL = Column(String)
    WingS = Column(String)

    def __init__(self,
                 race: str = '',
                 SkinC: str = '',
                 BodyT: str = '',
                 BodyS: str = '',
                 TailL: str = '',
                 WingS: str = ''
                 ):
        self.race = race
        self.SkinC = SkinC
        self.BodyT = BodyT
        self.BodyS = BodyS
        self.TailL = TailL
        self.WingS = WingS


class RaceTplHead(Base):
    __tablename__ = 'race_TplHead'

    id = Column(Integer, primary_key=True)
    race = Column(String,nullable=False, unique=True)
    HeadF = Column(String)
    EyeC = Column(String)
    HairL = Column(String)
    HairT = Column(String)
    HairC = Column(String)
    NoseF = Column(String)
    ChinF = Column(String)
    EarF = Column(String)
    EarS = Column(String)
    LipF = Column(String)
    HornS = Column(String)
    HornF = Column(String)
    HornN = Column(String)
    TuskS = Column(String)

    def __init__(
            self,
            race: str = '',
            HeadF: str = '',
            EyeC: str = '',
            HairL: str = '',
            HairT: str = '',
            HairC: str = '',
            NoseF: str = '',
            ChinF: str = '',
            EarF: str = '',
            EarS: str = '',
            LipF: str = '',
            HornS: str = '',
            HornF: str = '',
            HornN: str = '',
            TuskS: str = ''
    ):
        self.race = race
        self.HeadF = HeadF
        self.EyeC = EyeC
        self.HairL = HairL
        self.HairT = HairT
        self.HairC = HairC
        self.NoseF = NoseF
        self.ChinF = ChinF
        self.EarF = EarF
        self.EarS = EarS
        self.LipF = LipF
        self.HornS = HornS
        self.HornF = HornF
        self.HornN = HornN
        self.TuskS = TuskS


class RaceTplLimps(Base):
    __tablename__ = 'race_TplLimps'

    id = Column(Integer, primary_key=True)
    race = Column(String,nullable=False, unique=True)
    ArmL = Column(String)
    HandS = Column(String)
    HandclawS = Column(String)
    LegL = Column(String)
    FootS = Column(String)
    FootclawS = Column(String)
    FootT = Column(String)

    def __init__(self,
                 race: str = '',
                 ArmL: str = '',
                 HandS: str = '',
                 HandclawS: str = '',
                 LegL: str = '',
                 FootS: str = '',
                 FootclawS: str = '',
                 FootT: str = ''
                 ):
        self.race = race
        self.ArmL = ArmL
        self.HandS = HandS
        self.HandclawS = HandclawS
        self.LegL = LegL
        self.FootS = FootS
        self.FootclawS = FootclawS
        self.FootT = FootT


class BodyTorsoSkinC(Base):
    __tablename__ = 'body_TorsoSkinC'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyTorsoBodyT(Base):
    __tablename__ = 'body_TorsoBodyT'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyTorsoBodyS(Base):
    __tablename__ = 'body_TorsoBodyS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyTorsoTailL(Base):
    __tablename__ = 'body_TorsoTailL'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyTorsoWingS(Base):
    __tablename__ = 'body_TorsoWingS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadHeadF(Base):
    __tablename__ = 'body_HeadHeadF'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadEyeC(Base):
    __tablename__ = 'body_HeadEyeC'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadHairL(Base):
    __tablename__ = 'body_HeadHairL'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadHairT(Base):
    __tablename__ = 'body_HeadHairT'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadHairC(Base):
    __tablename__ = 'body_HeadHairC'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadNoseF(Base):
    __tablename__ = 'body_HeadNoseF'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadChinF(Base):
    __tablename__ = 'body_HeadChinF'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadEarF(Base):
    __tablename__ = 'body_HeadEarF'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadEarS(Base):
    __tablename__ = 'body_HeadEarS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadLipF(Base):
    __tablename__ = 'body_HeadLipF'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadHornS(Base):
    __tablename__ = 'body_HeadHornS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadHornF(Base):
    __tablename__ = 'body_HeadHornF'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadHornN(Base):
    __tablename__ = 'body_HeadHornN'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyHeadTuskS(Base):
    __tablename__ = 'body_HeadTuskS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyLimpsArmL(Base):
    __tablename__ = 'body_LimpsArmL'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyLimpsHandS(Base):
    __tablename__ = 'body_LimpsHandS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyLimpsHandclawS(Base):
    __tablename__ = 'body_LimpsHandclawS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyLimpsLegL(Base):
    __tablename__ = 'body_LimpsLegL'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyLimpsFootS(Base):
    __tablename__ = 'body_LimpsFootS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyLimpsFootclawS(Base):
    __tablename__ = 'body_LimpsFootclawS'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class BodyLimpsFootT(Base):
    __tablename__ = 'body_LimpsFootT'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
