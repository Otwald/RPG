from Random_Gen import Monster_NumberGen


class Body_Gen:

    def Body_Skin(self, index):
        skin_c_list = ['pale','peach', 'olive', 'brown', 'black', 
            'light green', 'dark green', 'black', 'blue', 'red']
        return skin_c_list[index]

    def Body_Type(self, index):
        body_t_list = ['strong', 'muscular', 'slender', 'athletic', 'thin', 'slim', 'chubby']
        return body_t_list[index]

    def Body_Size(self, index):
        body_s_list =['large', 'medium', 'small']
        return body_s_list[index]

    def Body_HeadForm(self, index):
        headform_list = ['oval', 'long', 'round', 'angular']
        return headform_list[index]

    def Body_EyeColor(self, index):
        eye_list = ['green', 'blue', 'brown', 'red', 'purple']
        return eye_list[index]

    def Body_HairLength(self, index):
        hair_l_list = ['short', 'chin-length', 'shoulder-length', 'long', 'none']
        return hair_l_list[index]
    
    def Body_HairType(self, index):
        hair_t_list = ['smooth', 'curly', 'frizzy']
        return hair_t_list[index]

    def Body_HairColor(self, index):
        hair_c_list = ['brown', 'black', 'blond', 'red']
        return hair_c_list[index]

    def Body_Nose(self, index):
        nose_list = ['crooked', 'small', 'tall', 'pointed']
        return nose_list[index]

    def Body_Chin(self, index):
        chin_list = ['energetic', 'pointed', 'round', 'small', 'protruding']
        return chin_list[index]
    
    def Body_EarForm(self, index):
        ear_f_list = ['sticking out', 'fitting', 'pointy' , 'pointy ragged']
        return ear_f_list[index]

    def Body_EarSize(self, index):
        ear_s_list = ['big', 'small']
        return ear_s_list[index]

    def Body_LipForm(self, index):
        lip_f_list = ['thin', 'balanced' , 'plump', 'thin upperlip', 'thin lowerlip']
        return lip_f_list[index]

    def Body_HornSize(self, index):
        #4
        horn_s_list = ['tiny', 'small', 'medium', 'large', 'giant']
        return horn_s_list[index]

    def Body_HornForm(self, index):
        #4
        horn_f_list = ['antlers', 'goat', 'straight', 'curved', 'hooked']
        return horn_f_list[index]

    def Body_HornNumb(self, index):
        horn_n_list = ['none', '1','2','3','4']
        return horn_n_list[index]

    def Body_TuskSize(self, index):
        tusk_s_list = ['none' ,'tiny', 'small', 'medium', 'large', 'giant']
        return tusk_s_list

    def Body_ArmLength(self, index):
        arm_l_list = ['long', 'medium', 'small']
        return arm_l_list[index]

    def Body_HandSize(self, index):
        hand_s_list = ['huge', 'medium', 'small']
        return hand_s_list[index]

    def Body_HandClawSize(self, index):
        handclaw_s_list = ['long', 'medium', 'small']
        return handclaw_s_list[index]

    def Body_LegLength(self, index):
        leg_l_list = ['long', 'medium', 'small']
        return leg_l_list[index]

    def Body_FootSize(self, index):
        foot_s_list = ['huge', 'medium', 'small']
        return foot_s_list[index]

    def Body_FootClawSize(self, index):
        footclaw_s_list = ['long', 'medium', 'small']
        return footclaw_s_list[index]

    def Body_FootType(self, index):
        foot_t_list = ['foot', ' cowhoof', 'elkhoof', 'goathoof', 'lionpaw', 'chicken']
        return foot_t_list[index]

    def Body_WingSize(self, index):
        wing_s_list = ['tiny', 'small', 'medium', 'large' , 'huge']
        return wing_s_list[index]

    def Body_TailLength(self, index):
        tail_l_list = ['short', 'medium', 'long']
        return tail_l_list[index]

    def Body_General(self, switch_list):
        output = {}
        ele_list = self.Body_Head()
 
        for key, value in switch_list.items():
            if value != None:
                index = Monster_NumberGen(value)
                output.update({key : ele_list[key](index)})
            else:
                output.update({key : value})
        return output

    def Body_Head(self):
        body_list = {'skin_color':self.Body_Skin, 'body_type':self.Body_Type, 'body_size' : self.Body_Size ,'head_form' :  self.Body_HeadForm, 'eye_color' : self.Body_EyeColor, 
            'hair_lengt': self.Body_HairLength, 'hair_type': self.Body_HairType, 'hair_color': self.Body_HairColor, 
            'nose':self.Body_Nose, 'chin': self.Body_Chin,  'pair_number' :self.Body_HornNumb , 'horn_size': self.Body_HornSize, 'horn_form': self.Body_HornForm,
            'ear_form': self.Body_EarForm, 'ear_size': self.Body_EarSize, 'tusk_size': self.Body_TuskSize, 
            'lip_form': self.Body_LipForm, 'arm_length': self.Body_ArmLength, 'hand_size' : self.Body_HandSize, 'hand_claw_size': self.Body_HandClawSize,
            'leg_length': self.Body_LegLength, 'foot_size' : self.Body_FootSize, 'foot_claw_size': self.Body_FootClawSize, 'foot_type' : self.Body_FootType,
            'wing_size' : self.Body_WingSize, 'tail_length' : self.Body_TailLength  } 
        return body_list
