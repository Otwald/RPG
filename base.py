from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

Base = declarative_base()


class BodyTorso(Base):
    __tablename__ = 'bodyTorso'

    id = Column(Integer, primary_key=True)
    skin_c = Column(String)
    body_t = Column(String)
    body_s = Column(String)
    tail_l = Column(String)
    wing_s = Column(String)

    def __init__(self, skin_c, body_t, body_s, tail_l, wing_s):
        self.skin_c = skin_c
        self.body_t = body_t
        self.body_s = body_s
        self.tail_l = tail_l
        self.wing_s = wing_s


class BodyHead(Base):
    __tablename__ = 'bodyHead'

    id = Column(Integer, primary_key=True)
    head_f = Column(String)
    eye_c = Column(String)
    hair_l = Column(String)
    hair_t = Column(String)
    hair_c = Column(String)
    nose_f = Column(String)
    chin_f = Column(String)
    ear_f = Column(String)
    ear_s = Column(String)
    lip_f = Column(String)
    horn_s = Column(String)
    horn_f = Column(String)
    horn_n = Column(String)
    tusk_s = Column(String)


def __init__(self,
             head_f,
             eye_c,
             hair_l,
             hair_t,
             hair_c,
             nose_f,
             chin_f,
             ear_f,
             ear_s,
             lip_f,
             horn_s,
             horn_f,
             horn_n,
             tusk_s
             ):
    self.head_f = head_f
    self.eye_c = eye_c
    self.hair_l = hair_l
    self.hair_t = hair_t
    self.hair_c = hair_c
    self.nose_f = nose_f
    self.chin_f = chin_f
    self.ear_f = ear_f
    self.ear_s = ear_s
    self.lip_f = lip_f
    self.horn_s = horn_s
    self.horn_f = horn_f
    self.horn_n = horn_n
    self.tusk_s = tusk_s


class BodyLimps(Base):
    __tablename__ = 'bodyLimps'

    id = Column(Integer, primary_key=True)
    arm_l = Column(String)
    hand_s = Column(String)
    handclaw_s = Column(String)
    leg_l = Column(String)
    foot_s = Column(String)
    footclaw_s = Column(String)
    foot_t = Column(String)

    def __init__(self, arm_l, hand_s, handclaw_s, leg_l, foot_s, footclaw_s, foot_t):
        self.arm_l = arm_l
        self.hand_s = hand_s
        self.handclaw_s = handclaw_s
        self.leg_l = leg_l
        self.foot_s = foot_s
        self.footclaw_s = footclaw_s
        self.foot_t = foot_t
