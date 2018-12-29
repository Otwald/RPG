import random
from Body_Gen import Body_Gen

BG = Body_Gen()

class Monster_Gen:

    def Monster_NumberGen(self, data_list):
        count = 0
        random_int = random.randint(0,100)
        data_listlen = len(data_list)
        data_int = 100/data_listlen
        while count < (data_listlen):
            if (int(count * data_int) <= random_int <= (int(count + 1) *  data_int)):
                return (data_list[count])
            count = count + 1

    # Untote, Bestien
    def Monster_ArtGen(self):
        mon_list = [self.Monster_Orcoid, self.Monster_Undead, 
                self.Monster_Human, self.Monster_Repte, 
                self.Monster_Demon]
        return self.Monster_NumberGen(mon_list)

    def Monster_SwitchHandler(self):
        statement = self.Monster_ArtGen()
        race, over_list = statement()
        count = 0
        ran_list = []
        for item in over_list:
            item_list = BG.Body_General(item, count)
            ran_list.append(self.Monster_NumberGen(item_list))
            count = count + 1
        person ={'race': race , 'body' : {'skin_color' : ran_list[0], 'body_type': ran_list[1]}, 
            'head': {'form' : ran_list[2], 'eye_color' : ran_list[3] , 
            'hair': {'lengt': ran_list[4], 'type': ran_list[5], 'color': ran_list[6]},
            'nose': ran_list[7], 'chin': ran_list[8],  
            'ear': {'form': ran_list[9], 'size': ran_list[10]},
            'lip_form': ran_list[11]}}
        print(person)


    def Monster_Orcoid(self):
        skin_c_list = [4, 5,6,7]
        body_list = [0,1,3,4,7,9] 
        headform_list = [2,3] 
        eye_list = [0,2,3] 
        hair_l_list = [0,4] 
        hair_t_list = [1,2] 
        hair_c_list = [0,1] 
        nose_list = [0,1,2] 
        chin_list = [0,1,2,3,4] 
        ear_f_list = [2,3] 
        ear_s_list = [0,1] 
        lip_f_list = [0,1]
        over_list = [skin_c_list, body_list, headform_list, eye_list, hair_l_list, hair_t_list, hair_c_list, nose_list,
            chin_list, ear_f_list, ear_s_list, lip_f_list]
        race = 'Orc'
        return race , over_list

    def Monster_Undead(self):
        ran_list = []
        skin_c_list = [1,2,3,5]
        body_list = [0,1,2,3,4,5,6,7,8,9] 
        headform_list = [0,1,2,3] 
        eye_list = [0,1,2] 
        hair_l_list = [0,1,2,3,4] 
        hair_t_list = [0,1,2] 
        hair_c_list = [0,1,2,3] 
        nose_list = [0,1,2,3] 
        chin_list = [0,1,2,3,4] 
        ear_f_list = [0,1] 
        ear_s_list = [0,1] 
        lip_f_list = [0,1,2,3,4]
        over_list = [skin_c_list, body_list, headform_list, eye_list, hair_l_list, hair_t_list, hair_c_list, nose_list,
            chin_list, ear_f_list, ear_s_list, lip_f_list] 
        race = 'Undead'
        return race, over_list

    def Monster_Human(self):
        ran_list = []
        skin_c_list = [0,1,2,3,4]
        body_list = [0,1,2,3,4,5,6,7,8,9] 
        headform_list = [0,1,2,3] 
        eye_list = [0,1,2] 
        hair_l_list = [0,1,2,3,4] 
        hair_t_list = [0,1,2] 
        hair_c_list = [0,1,2,3] 
        nose_list = [0,1,2,3] 
        chin_list = [0,1,2,3,4] 
        ear_f_list = [0,1] 
        ear_s_list = [0,1] 
        lip_f_list = [0,1,2,3,4]
        over_list = [skin_c_list, body_list, headform_list, eye_list, hair_l_list, hair_t_list, hair_c_list, nose_list,
            chin_list, ear_f_list, ear_s_list, lip_f_list]
        race = 'Human'
        return race, over_list
        
    def Monster_Repte(self):
        ran_list = []
        skin_c_list = [3,4,5,6,7,8]
        body_list = [0,1,2,3,4,5,6,7,8,9] 
        headform_list = [0,1,2,3] 
        eye_list = [0,1,3] 
        hair_l_list = [0,1,2,3,4] 
        hair_t_list = [0,1,2] 
        hair_c_list = [0,1,2,3] 
        nose_list = [0,1,2,3] 
        chin_list = [0,1,2,3,4] 
        ear_f_list = [0,1] 
        ear_s_list = [0,1] 
        lip_f_list = [0]
        over_list = [skin_c_list, body_list, headform_list, eye_list, hair_l_list, hair_t_list, hair_c_list, nose_list,
            chin_list, ear_f_list, ear_s_list, lip_f_list]
        # ran_list[4] = 'none'
        # ran_list[9] = 'none'
        race = 'Lizardmen'
        return race , over_list
        
    def Monster_Demon(self):
        skin_c_list = [1,2,9,4]
        body_list = [0,1,2,3,4,5,6,7] 
        headform_list = [0,1,2,3] 
        eye_list = [0,1,2,3,4] 
        hair_l_list = [0,1,2,3,4] 
        hair_t_list = [0,1,2] 
        hair_c_list = [0,1,2,3] 
        nose_list = [0,1,2,3] 
        chin_list = [0,1,2,3,4] 
        ear_f_list = [0,1] 
        ear_s_list = [0,1] 
        lip_f_list = [0]
        over_list = [skin_c_list, body_list, headform_list, eye_list, hair_l_list, hair_t_list, hair_c_list, nose_list,
            chin_list, ear_f_list, ear_s_list, lip_f_list]
        race = 'Demonkin' 
        return race, over_list

    # def Monster_HeadBuilder(self, color):
