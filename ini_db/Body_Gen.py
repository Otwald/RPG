from alchemy import DbInterface

from base import BodyTorso
from base import BodyHead
from base import BodyLimps


class BodyGen:

    db: DbInterface
    bodypart : list

    def __init__(self):
        self.db = DbInterface()
        self.bodypart = [BodyTorso, BodyHead, BodyLimps]

    def __initDB(self, tclass):
        func = tclass.__tablename__
        context = {}
        if func == 'bodyTorso':
            context = self.bodyTorso()
        elif func == 'bodyHead':
            context = self.bodyHead()
        elif func == 'bodyLimps':
            context = self.bodyLimbs()
            length = 0
            for key,value in context.items():
                if length < len(value):
                    length = len(value)
                # print(len(value))
            i = 0
            while i < (length-1):
                BodyLimps()
    
    def checkDB(self):
        """calls the DB to check if DB was already created, if not calls a creator
        """
        for part in self.bodypart:
            if not self.db.checkTable(part) :
                self.__initDB(part)
        # session = self.db.getSession()

    def bodyTorso(self):
        return {
            'skin_c': ['pale', 'peach', 'olive', 'brown', 'black',
                            'light_green', 'dark_green', 'blue', 'red', 'purple'],
            'body_t': ['strong', 'muscular', 'slender',
                            'athletic', 'thin', 'slim', 'chubby'],
            'body_s': ['large', 'medium', 'small'],
            'tail_l': ['short_tail', 'medium_tail', 'long_tail'],
            'wing_s': ['tiny_w', 'small_w',
                            'medium_w', 'large_w', 'huge_w']
        }

    def bodyHead(self):
        return {
            'head_f': ['oval', 'long_h', 'round', 'angular'],
            'eye_c': ['green_e', 'blue_e', 'brown_h', 'red_h', 'purple_e'],
            'hair_l': ['short', 'chin-length',
                            'shoulder-length', 'long', 'none'],
            'hair_t': ['smooth', 'curly', 'frizzy'],
            'hair_c': ['brown_h', 'black_h', 'blond_h', 'red_h'],
            'nose_f': ['crooked', 'small_n', 'tall_n', 'pointed_n'],
            'chin_f': ['energetic_c', 'pointed_c',
                            'round_c', 'small_c', 'protruding_c'],
            'ear_f': ['sticking_out_e', 'fitting_e',
                           'pointy_e', 'pointy_ragged_e'],
            'ear_s': ['big_e', 'small_e'],
            'lip_f': ['thin_l', 'balanced_l', 'plump_l',
                           'thin_upperlip_l', 'thin_lowerlip_l'],
            'horn_s': ['tiny_h', 'small_h',
                            'medium_h', 'large_h', 'giant_h'],
            'horn_f': ['antlers', 'goat', 'straight', 'curved', 'hooked'],
            'horn_n': ['none', '1', '2', '3', '4'],
            'tusk_s': ['none_t', 'tiny_t', 'small_t',
                            'medium_t', 'large_t', 'giant_T'],
        }

    def bodyLimbs(self):
        return {
            'arm_l': ['long_l', 'medium_l', 'small_l'],
            'hand_s': ['huge_l', 'medium_s', 'small_l'],
            'handclaw_s': ['long', 'medium_c', 'small_c'],
            'leg_l': ['long_l', 'medium_l', 'small_l'],
            'foot_s': ['huge_l', 'medium_s', 'small_l'],
            'footclaw_s': ['long_claw', 'medium_claw', 'small_claw'],
            'foot_t': ['foot', 'cowhoof', 'elkhoof',
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
