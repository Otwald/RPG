from alchemy import DbInterface
from sqlalchemy import Column, String, Integer, Table

import base

class BodyGen:

    db: DbInterface
    bodypart: list

    def __init__(self):
        self.db = DbInterface()
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
                if not self.db.checkTable(temp):
                    # print('mäh')
                    bodyParts = Table(key, self.db.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('name', String)
                                      )
                    self.db.createTable()
                    self.__initDB(temp, value, session)
                else:
                    pass
                    # for row in session.query(BodyPartTpl).all():
                        # print(row)
        session.commit()
        print(session)
        session.close()

    def bodyTorso(self):
        return {
            'body_TorsoSkinC': ['pale', 'peach', 'olive', 'brown', 'black',
                                'light_green', 'dark_green', 'blue', 'red', 'purple'],
            'body_TorsoBodyT': ['strong', 'muscular', 'slender',
                                'athletic', 'thin', 'slim', 'chubby'],
            'body_TorsoBodyS': ['large', 'medium', 'small'],
            'body_TorsoTailL': ['short_tail', 'medium_tail', 'long_tail'],
            'body_TorsoWingS': ['tiny_w', 'small_w',
                                'medium_w', 'large_w', 'huge_w']
        }

    def bodyHead(self):
        return {
            'body_HeadHeadF': ['oval', 'long_h', 'round', 'angular'],
            'body_HeadEyeC': ['green_e', 'blue_e', 'brown_h', 'red_h', 'purple_e'],
            'body_HeadHairL': ['short', 'chin-length',
                               'shoulder-length', 'long', 'none'],
            'body_HeadHairT': ['smooth', 'curly', 'frizzy'],
            'body_HeadHairC': ['brown_h', 'black_h', 'blond_h', 'red_h'],
            'body_HeadNoseF': ['crooked', 'small_n', 'tall_n', 'pointed_n'],
            'body_HeadChinF': ['energetic_c', 'pointed_c',
                               'round_c', 'small_c', 'protruding_c'],
            'body_HeadEarF': ['sticking_out_e', 'fitting_e',
                              'pointy_e', 'pointy_ragged_e'],
            'body_HeadEarS': ['big_e', 'small_e'],
            'body_HeadLipF': ['thin_l', 'balanced_l', 'plump_l',
                              'thin_upperlip_l', 'thin_lowerlip_l'],
            'body_HeadHornS': ['tiny_h', 'small_h',
                               'medium_h', 'large_h', 'giant_h'],
            'body_HeadHornF': ['antlers', 'goat', 'straight', 'curved', 'hooked'],
            'body_HeadHornN': ['none', '1', '2', '3', '4'],
            'body_HeadTuskS': ['none_t', 'tiny_t', 'small_t',
                               'medium_t', 'large_t', 'giant_T'],
        }

    def bodyLimbs(self):
        return {
            'body_LimpsArmL': ['long_l', 'medium_l', 'small_l'],
            'body_LimpsHandS': ['huge_l', 'medium_s', 'small_l'],
            'body_LimpsHandclawS': ['long', 'medium_c', 'small_c'],
            'body_LimpsLegL': ['long_l', 'medium_l', 'small_l'],
            'body_LimpsFootS': ['huge_l', 'medium_s', 'small_l'],
            'body_LimpsFootclawS': ['long_claw', 'medium_claw', 'small_claw'],
            'body_LimpsFootT': ['foot', 'cowhoof', 'elkhoof',
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
