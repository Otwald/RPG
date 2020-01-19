from alchemy import DbInterface
from sqlalchemy import Column, String, Integer, Table

import base as b


class BodyGen:

    db: DbInterface
    bodypart: list
    baseTable: dict

    def __init__(self):
        self.db = DbInterface()
        self.baseTable = {
            b.BodyTorsoSkinC.__tablename__: b.BodyTorsoSkinC,
            b.BodyTorsoBodyT.__tablename__: b.BodyTorsoBodyT,
            b.BodyTorsoBodyS.__tablename__: b.BodyTorsoBodyS,
            b.BodyTorsoTailL.__tablename__: b.BodyTorsoTailL,
            b.BodyTorsoWingS.__tablename__: b.BodyTorsoWingS,
            b.BodyHeadHeadF.__tablename__: b.BodyHeadHeadF,
            b.BodyHeadEyeC.__tablename__: b.BodyHeadEyeC,
            b.BodyHeadHairL.__tablename__: b.BodyHeadHairL,
            b.BodyHeadHairT.__tablename__: b.BodyHeadHairT,
            b.BodyHeadHairC.__tablename__: b.BodyHeadHairC,
            b.BodyHeadNoseF.__tablename__: b.BodyHeadNoseF,
            b.BodyHeadChinF.__tablename__: b.BodyHeadChinF,
            b.BodyHeadEarF.__tablename__: b.BodyHeadEarF,
            b.BodyHeadEarS.__tablename__: b.BodyHeadEarS,
            b.BodyHeadLipF.__tablename__: b.BodyHeadLipF,
            b.BodyHeadHornS.__tablename__: b.BodyHeadHornS,
            b.BodyHeadHornF.__tablename__: b.BodyHeadHornF,
            b.BodyHeadHornN.__tablename__: b.BodyHeadHornN,
            b.BodyHeadTuskS.__tablename__: b.BodyHeadTuskS,
            b.BodyLimpsArmL.__tablename__: b.BodyLimpsArmL,
            b.BodyLimpsHandS.__tablename__: b.BodyLimpsHandS,
            b.BodyLimpsHandclawS.__tablename__: b.BodyLimpsHandclawS,
            b.BodyLimpsLegL.__tablename__: b.BodyLimpsLegL,
            b.BodyLimpsFootS.__tablename__: b.BodyLimpsFootS,
            b.BodyLimpsFootclawS.__tablename__: b.BodyLimpsFootclawS,
            b.BodyLimpsFootT.__tablename__: b.BodyLimpsFootT,
        }
        self.bodypart = [self.bodyTorso, self.bodyHead, self.bodyLimbs]

    def __initDB(self, tclass, context, session):
        for item in context:
            table = tclass(item)
            # print(table)
            session.add(table)

    def checkDB(self):
        """calls the DB to check if DB was already created, if not calls a creator
        """
        session = self.db.getSession()
        for part in self.bodypart:
            for key, value in part().items():
                tableClass = self.baseTable[key]
                if not self.db.checkTable(tableClass):
                    print(value)
                    # print('mäh')
                    # self.db.createTable()
                    # self.__initDB(temp, value, session)
                else:
                    pass
                    # for row in session.query(BodyPartTpl).all():
                    # print(row)
        session.commit()
        print(session)
        session.close()

    def bodyTorso(self):
        return {
            b.BodyTorsoSkinC.__tablename__: ['pale', 'peach', 'olive', 'brown', 'black',
                                             'light_green', 'dark_green', 'blue', 'red', 'purple'],
            b.BodyTorsoBodyT.__tablename__: ['strong', 'muscular', 'slender',
                                             'athletic', 'thin', 'slim', 'chubby'],
            b.BodyTorsoBodyS.__tablename__: ['large', 'medium', 'small'],
            b.BodyTorsoTailL.__tablename__: ['short_tail', 'medium_tail', 'long_tail'],
            b.BodyTorsoWingS.__tablename__: ['tiny_w', 'small_w',
                                             'medium_w', 'large_w', 'huge_w']
        }

    def bodyHead(self):
        return {
            b.BodyHeadHeadF.__tablename__: ['oval', 'long_h', 'round', 'angular'],
            b.BodyHeadEyeC.__tablename__: ['green_e', 'blue_e', 'brown_h', 'red_h', 'purple_e'],
            b.BodyHeadHairL.__tablename__: ['short', 'chin-length',
                                            'shoulder-length', 'long', 'none'],
            b.BodyHeadHairT.__tablename__: ['smooth', 'curly', 'frizzy'],
            b.BodyHeadHairC.__tablename__: ['brown_h', 'black_h', 'blond_h', 'red_h'],
            b.BodyHeadNoseF.__tablename__: ['crooked', 'small_n', 'tall_n', 'pointed_n'],
            b.BodyHeadChinF.__tablename__: ['energetic_c', 'pointed_c',
                                            'round_c', 'small_c', 'protruding_c'],
            b.BodyHeadEarF.__tablename__: ['sticking_out_e', 'fitting_e',
                                           'pointy_e', 'pointy_ragged_e'],
            b.BodyHeadEarS.__tablename__: ['big_e', 'small_e'],
            b.BodyHeadLipF.__tablename__: ['thin_l', 'balanced_l', 'plump_l',
                                           'thin_upperlip_l', 'thin_lowerlip_l'],
            b.BodyHeadHornS.__tablename__: ['tiny_h', 'small_h',
                                            'medium_h', 'large_h', 'giant_h'],
            b.BodyHeadHornF.__tablename__: ['antlers', 'goat', 'straight', 'curved', 'hooked'],
            b.BodyHeadHornN.__tablename__: ['none', '1', '2', '3', '4'],
            b.BodyHeadTuskS.__tablename__: ['none_t', 'tiny_t', 'small_t',
                                            'medium_t', 'large_t', 'giant_T'],
        }

    def bodyLimbs(self):
        return {
            b.BodyLimpsArmL.__tablename__: ['long_l', 'medium_l', 'small_l'],
            b.BodyLimpsHandS.__tablename__: ['huge_l', 'medium_s', 'small_l'],
            b.BodyLimpsHandclawS.__tablename__: ['long', 'medium_c', 'small_c'],
            b.BodyLimpsLegL.__tablename__: ['long_l', 'medium_l', 'small_l'],
            b.BodyLimpsFootS.__tablename__: ['huge_l', 'medium_s', 'small_l'],
            b.BodyLimpsFootclawS.__tablename__: ['long_claw', 'medium_claw', 'small_claw'],
            b.BodyLimpsFootT.__tablename__: ['foot', 'cowhoof', 'elkhoof',
                                             'goathoof', 'lionpaw', 'chicken'],
        }

    # def Body_General(self, switch_list):
    #     output = {}
    #     ele_list = self.Body_Head()
    #     for key, value in switch_list.items():
    #         if value != None:
    #             index = Monster_NumberGen(value)
    #             output.update({key : ele_list[key](index)})
    #         else:
    #             output.update({key : value})
    #     return output

    # def Body_Head(self):
    #     body_list = {'skin_color':self.Body_Skin, 'body_type':self.Body_Type, 'body_size' : self.Body_Size ,'head_form' :  self.Body_HeadForm, 'eye_color' : self.Body_EyeColor,
    #         'hair_lengt': self.Body_HairLength, 'hair_type': self.Body_HairType, 'hair_color': self.Body_HairColor,
    #         'nose':self.Body_Nose, 'chin': self.Body_Chin,  'pair_number' :self.Body_HornNumb , 'horn_size': self.Body_HornSize, 'horn_form': self.Body_HornForm,
    #         'ear_form': self.Body_EarForm, 'ear_size': self.Body_EarSize, 'tusk_size': self.Body_TuskSize,
    #         'lip_form': self.Body_LipForm, 'arm_length': self.Body_ArmLength, 'hand_size' : self.Body_HandSize, 'hand_claw_size': self.Body_HandClawSize,
    #         'leg_length': self.Body_LegLength, 'foot_size' : self.Body_FootSize, 'foot_claw_size': self.Body_FootClawSize, 'foot_type' : self.Body_FootType,
    #         'wing_size' : self.Body_WingSize, 'tail_length' : self.Body_TailLength  }
    #     return body_list

    # TO Init the DB
    # db = DataBase()
    # # db.makeRequest('SELECT * FROM test')
    # bg = Body_Gen()
    # funcs = [func for func in dir(
    #     Body_Gen) if callable(getattr(Body_Gen, func))]
    # for fun in funcs:
    #     if(fun[0] != '_'):
    #         table = fun.lower()
    #         db.makeRequest(
    #         """CREATE TABLE `rpgproject`.`"""+table+"""`
    #         (`id` INT NOT NULL AUTO_INCREMENT,
    #         `name` VARCHAR(45) NOT NULL,
    #         PRIMARY KEY(`id`),
    #         UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
    #         COMMENT = '	'
    #         """)
    #         getList = getattr(bg, fun)
    #         content = getList()
    #         for item in content:
    #             db.makeRequest("""INSERT INTO `rpgproject`.`"""+table+"""`
    #             (`name`)
    #             VALUES ( '"""+item+"""' )""")
    #         db.makeRequest('SELECT * FROM `rpgproject`.`'+table+'`')
