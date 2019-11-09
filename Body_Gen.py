from Random_Gen import Monster_NumberGen


class Body_Gen:

    def Body_Torso_Skin(self):
        skin_c_list = ['pale','peach', 'olive', 'brown', 'black', 
            'light_green', 'dark_green', 'blue', 'red', 'purple']
        return skin_c_list

    def Body_Torso_Type(self):
        body_t_list = ['strong', 'muscular', 'slender', 'athletic', 'thin', 'slim', 'chubby']
        return body_t_list

    def Body_Torso_Size(self):
        body_s_list =['large', 'medium', 'small']
        return body_s_list

    def Body_Head_Form(self):
        headform_list = ['oval', 'long_h', 'round', 'angular']
        return headform_list

    def Body_Head_EyeColor(self):
        eye_list = ['green_e', 'blue_e', 'brown_h', 'red_h', 'purple_e']
        return eye_list
    
    def Body_Head_HairLength(self):
        hair_l_list = ['short', 'chin-length', 'shoulder-length', 'long', 'none']
        return hair_l_list
    
    def Body_Head_HairType(self):
        hair_t_list = ['smooth', 'curly', 'frizzy']
        return hair_t_list

    def Body_Head_HairColor(self):
        hair_c_list = ['brown_h', 'black_h', 'blond_h', 'red_h']
        return hair_c_list

    def Body_Head_Nose(self):
        nose_list = ['crooked', 'small_n', 'tall_n', 'pointed_n']
        return nose_list

    def Body_Head_Chin(self):
        chin_list = ['energetic_c', 'pointed_c', 'round_c', 'small_c', 'protruding_c']
        return chin_list
    
    def Body_Head_EarForm(self):
        ear_f_list = ['sticking_out_e', 'fitting_e', 'pointy_e' , 'pointy_ragged_e']
        return ear_f_list

    def Body_Head_EarSize(self):
        ear_s_list = ['big_e', 'small_e']
        return ear_s_list

    def Body_Head_LipForm(self):
        lip_f_list = ['thin_l', 'balanced_l' , 'plump_l', 'thin_upperlip_l', 'thin_lowerlip_l']
        return lip_f_list

    def Body_Head_HornSize(self):
        #4
        horn_s_list = ['tiny_h', 'small_h', 'medium_h', 'large_h', 'giant_h']
        return horn_s_list

    def Body_Head_HornForm(self):
        #4
        horn_f_list = ['antlers', 'goat', 'straight', 'curved', 'hooked']
        return horn_f_list

    def Body_Head_HornNumb(self):
        horn_n_list = ['none', '1','2','3','4']
        return horn_n_list

    def Body_Head_TuskSize(self):
        tusk_s_list = ['none_t' ,'tiny_t', 'small_t', 'medium_t', 'large_t', 'giant_T']
        return tusk_s_list

    def Body_Limbs_ArmLength(self):
        arm_l_list = ['long_l', 'medium_l', 'small_l']
        return arm_l_list

    def Body_Limbs_HandSize(self):
        hand_s_list = ['huge_l', 'medium_s', 'small_l']
        return hand_s_list

    def Body_Limbs_HandClawSize(self):
        handclaw_s_list = ['long', 'medium_c', 'small_c']
        return handclaw_s_list

    def Body_Limbs_LegLength(self):
        leg_l_list = ['long_l', 'medium_l', 'small_l']
        return leg_l_list

    def Body_Limbs_FootSize(self):
        foot_s_list = ['huge_l', 'medium_s', 'small_l']
        return foot_s_list

    def Body_Limbs_FootClawSize(self):
        footclaw_s_list = ['long_claw', 'medium_claw', 'small_claw']
        return footclaw_s_list

    def Body_Limbs_FootType(self):
        foot_t_list = ['foot', 'cowhoof', 'elkhoof', 'goathoof', 'lionpaw', 'chicken']
        return foot_t_list

    def Body_Torso_WingSize(self):
        wing_s_list = ['tiny_w', 'small_w', 'medium_w', 'large_w' , 'huge_w']
        return wing_s_list

    def Body_Torso_TailLength(self):
        tail_l_list = ['short_tail', 'medium_tail', 'long_tail']
        return tail_l_list

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


    ## TO Init the DB
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