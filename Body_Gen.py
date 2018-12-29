
class Body_Gen:

    def Body_Skin(self, index):
        skin_c_list = ['pale','peach', 'olive', 'brown', 'black', 
            'light green', 'dark green', 'black', 'blue', 'red']
        return skin_c_list[index]

    def Body_Type(self, index):
        body_list = ['large', 'medium', 'small', 'strong', 'muscular', 'slender', 'athletic', 'thin', 'slim', 'chubby']
        return body_list[index]

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
        horn_s_list = ['tiny', 'small', 'medium', 'large', 'giant']
        return horn_s_list[index]

    def Body_HornForm(self, index):
        horn_f_list = ['antlers', 'goat', 'straight', 'curved', 'hooked']
        return horn_f_list[index]

    def Body_HornNumb(self, index):
        horn_n_list = ['1','2','3']
        return horn_n_list

    def Body_General(self, index_list, i):
        output = []
        body_list = [self.Body_Skin, self.Body_Type, self.Body_HeadForm, self.Body_EyeColor,
            self.Body_HairLength, self.Body_HairType, self.Body_HairColor, self.Body_Nose,
            self.Body_Chin, self.Body_EarForm, self.Body_EarSize, self.Body_LipForm,
            self.Body_HornSize, self.Body_HornForm]
        for item in index_list:
            output.append(body_list[i](item))
        return output