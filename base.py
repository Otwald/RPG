from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

Base = declarative_base()

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