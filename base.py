from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

Base = declarative_base()


class BodyTorsoSkinC(Base):
    __tablename__ = 'bodyTorsoSkinC'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name

# class BodyTorsoBodyT(Base):
#     __tablename__ = 'bodyTorsoBodyT'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name
# class BodyTorsoBodyS(Base):
#     __tablename__ = 'bodyTorsoBodyS'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name
# class BodyTorsoTailL(Base):
#     __tablename__ = 'bodyTorsoTailL'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name
# class BodyTorsoWingS(Base):
#     __tablename__ = 'bodyTorsoWingS'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name
# class BodyHeadEyeC(Base):
#     __tablename__ = 'bodyTorsoEyeC'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name
# class BodyHeadHairL(Base):
#     __tablename__ = 'bodyTorsoHairL'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name

# class BodyHeadHeadF(Base):
#     __tablename__ = 'bodyHeadHeadF'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)


#     def __init__(self,name ):
#         self.name = name

#     self.ear_s = ear_s
#     self.lip_f = lip_f
#     self.horn_s = horn_s
#     self.horn_f = horn_f
#     self.horn_n = horn_n
#     self.tusk_s = tusk_s


# class BodyHeadHeadT(Base):
#     __tablename__ = 'bodyHeadHairT'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

#     def __init__(self,name ):
#         self.name = name

# class BodyHeadHairC(Base):
#     __tablename__ = 'bodyHeadHairC'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

#     def __init__(self,name ):
#         self.name = name
# class BodyHeadNoseF(Base):
#     __tablename__ = 'bodyHeadNoseF'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

#     def __init__(self,name ):
#         self.name = name
# class BodyHeadChinF(Base):
#     __tablename__ = 'bodyHeadChinF'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

#     def __init__(self,name ):
#         self.name = name
# class BodyHeadHeadF(Base):
#     __tablename__ = 'bodyHead'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# def __init__(self,name ):
#     self.name = name
# class BodyHeadHeadF(Base):
#     __tablename__ = 'bodyHead'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# def __init__(self,name ):
#     self.name = name
# class BodyHeadHeadF(Base):
#     __tablename__ = 'bodyHead'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# def __init__(self,name ):
#     self.name = name



# class BodyLimps(Base):
#     __tablename__ = 'bodyLimps'

#     id = Column(Integer, primary_key=True)
#     arm_l = Column(String)
#     hand_s = Column(String)
#     handclaw_s = Column(String)
#     leg_l = Column(String)
#     foot_s = Column(String)
#     footclaw_s = Column(String)
#     foot_t = Column(String)

#     def __init__(self, arm_l, hand_s, handclaw_s, leg_l, foot_s, footclaw_s, foot_t):
#         self.arm_l = arm_l
#         self.hand_s = hand_s
#         self.handclaw_s = handclaw_s
#         self.leg_l = leg_l
#         self.foot_s = foot_s
#         self.footclaw_s = footclaw_s
#         self.foot_t = foot_t
