
from alchemy import DbInterface as Db
from base import RaceTplTorso, RaceTplHead, RaceTplLimps

class MonsterGen:

    def checkDB(self):
        """calls the DB to check if DB was already created, if not calls a creator
        """
        print('test')

    # def Monster_SwitchHandler(self):

    #     output_list = []
    #     for item in input_list:
    #         item = BG.Body_General(item)
    #         output_list.append(item)
    #     head_dict = self.Monster_Head(output_list[1])
    #     limbs_dict = self.Monster_limbs(output_list[2])

    #     body_dict = {'skin_color': output_list[0]['skin_color'], 'body_type': output_list[0]['body_type'], 'body_size': output_list[0]['body_size'],
    #                  'head': head_dict, 'limbs': limbs_dict, 'wing_size': output_list[0]['wing_size'], 'tail_length': output_list[0]['tail_length']}
    #     return race, body_dict
    #     count = 0
    #     # for item in over_list:
    #     #     item_list = BG.Body_General(item, count)
    #     #     item_list.append(self.Monster_NumberGen(item_list))
    #     #     count = count + 1
    #     # if horn:
    #     #     item_list = BG.Body_General(head_list, 'head')
    #     #     head_dict = {'form' : item_list[0], 'eye_color' : item_list[1] ,
    #     #     'hair': {'lengt': item_list[2], 'type': item_list[3], 'color': item_list[4]},
    #     #     'horn' : {'pair_number' : item_list[10], 'horn_size' : item_list[11], 'horn_form' : item_list[12]},
    #     #     'nose': item_list[5], 'chin': item_list[6],
    #     #     'ear': {'form': item_list[7], 'size': item_list[8]},
    #     #     'lip_form': item_list[9]}
    #     # else:
    #     #     pass
    #     person_dict = {'race': race, 'body': body_dict}
    #     # person ={'race': race , 'body' : {'skin_color' : item_list[0], 'body_type': item_list[1]},
    #     #     'head': {'form' : item_list[2], 'eye_color' : item_list[3] ,
    #     #     'hair': {'lengt': item_list[4], 'type': item_list[5], 'color': item_list[6]},
    #     #     'nose': item_list[7], 'chin': item_list[8],
    #     #     'ear': {'form': item_list[9], 'size': item_list[10]},
    #     #     'lip_form': item_list[11]}}
    #     print(person_dict)
    #     #print ( 'Es ist ein' + person['race'])

    def Monster_Orcoid(self):
        skin_c_list = [4, 5, 6, 7]
        body_t_list = [0, 1, 2, 3, 4, 6]
        body_s_list = [0, 1, 2]
        headform_list = [2, 3]
        eye_list = [0, 2, 3]
        hair_l_list = [0, 4]
        hair_t_list = [1, 2]
        hair_c_list = [0, 1]
        nose_list = [0, 1, 2]
        chin_list = [0, 1, 2, 3, 4]
        ear_f_list = [2, 3]
        ear_s_list = [0, 1]
        lip_f_list = [0, 1]
        tusk_s_list = [0, 1, 2, 3, 4, 5]
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = [
            0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]
        foot_t_list = [0]
        body_dict = {'skin_color': skin_c_list, 'body_type': body_t_list,
                     'body_size': body_s_list, 'wing_size': None, 'tail_length': None}
        head_dict = {'head_form': headform_list, 'eye_color': eye_list, 'nose': nose_list, 'chin': chin_list, 'lip_form': lip_f_list,
                     'ear_form': ear_f_list, 'ear_size': ear_s_list,
                     'hair_lengt': hair_l_list, 'hair_type': hair_t_list, 'hair_color': hair_c_list,
                     'pair_number': None, 'horn_size':  None, 'horn_form': None,
                     'tusk_size': tusk_s_list}
        limbs_dict = {'arm_length': arm_l_list, 'hand_size': hand_s_list, 'hand_claw_size': handclaw_s_list,
                      'leg_length': leg_l_list, 'foot_size': foot_s_list, 'foot_claw_size': footclaw_s_list, 'foot_type': foot_t_list}
        race = 'Orc'

        input_list = [body_dict, head_dict, limbs_dict]

        return race, input_list

    def Monster_Undead(self):
        skin_c_list = [1, 2, 3, 5]
        body_t_list = [0, 1, 2, 3, 4, 5, 6]
        body_s_list = [0, 1, 2]
        headform_list = [0, 1, 2, 3]
        eye_list = [0, 1, 2]
        hair_l_list = [0, 1, 2, 3, 4]
        hair_t_list = [0, 1, 2]
        hair_c_list = [0, 1, 2, 3]
        nose_list = [0, 1, 2, 3]
        chin_list = [0, 1, 2, 3, 4]
        ear_f_list = [0, 1]
        ear_s_list = [0, 1]
        lip_f_list = [0, 1, 2, 3, 4]
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = [
            0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]
        foot_t_list = [0]
        body_dict = {'skin_color': skin_c_list, 'body_type': body_t_list,
                     'body_size': body_s_list, 'wing_size': None, 'tail_length': None}
        head_dict = {'head_form': headform_list, 'eye_color': eye_list, 'nose': nose_list, 'chin': chin_list, 'lip_form': lip_f_list,
                     'ear_form': ear_f_list, 'ear_size': ear_s_list,
                     'hair_lengt': hair_l_list, 'hair_type': hair_t_list, 'hair_color': hair_c_list,
                     'pair_number': None, 'horn_size':  None, 'horn_form': None,
                     'tusk_size': None}
        limbs_dict = {'arm_length': arm_l_list, 'hand_size': hand_s_list, 'hand_claw_size': handclaw_s_list,
                      'leg_length': leg_l_list, 'foot_size': foot_s_list, 'foot_claw_size': footclaw_s_list, 'foot_type': foot_t_list}
        race = 'Human'

        input_list = [body_dict, head_dict, limbs_dict]

        return race, input_list

    def Monster_Human(self):
        skin_c_list = [0, 1, 2, 3, 4]
        body_t_list = [0,1,2,3,4,5,6]
        body_s_list = [0, 1, 2]
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
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = [
            0,1,2], [0,1,2], [0, 1, 2], [0,1,2], [0,1,2], [0, 1, 2]
        foot_t_list = [0]
        body_dict = {'skin_color': skin_c_list, 'body_type': body_t_list,
                     'body_size': body_s_list, 'wing_size': None, 'tail_length': None}
        head_dict = {'head_form': headform_list, 'eye_color': eye_list, 'nose': nose_list, 'chin': chin_list, 'lip_form': lip_f_list,
                     'ear_form': ear_f_list, 'ear_size': ear_s_list,
                     'hair_lengt': hair_l_list, 'hair_type': hair_t_list, 'hair_color': hair_c_list,
                     'pair_number': None, 'horn_size':  None, 'horn_form': None,
                     'tusk_size': None}
        limbs_dict = {'arm_length': arm_l_list, 'hand_size': hand_s_list, 'hand_claw_size': handclaw_s_list,
                      'leg_length': leg_l_list, 'foot_size': foot_s_list, 'foot_claw_size': footclaw_s_list, 'foot_type': foot_t_list}
        race = 'Human'

        input_list = [body_dict, head_dict, limbs_dict]
        return race, input_list

    def Monster_Repte(self):
        skin_c_list = [3, 4, 5, 6, 7, 8]
        body_t_list = [0, 1, 2, 3, 4, 5, 6]
        body_s_list = [0, 1, 2]
        headform_list = [0, 1, 2, 3]
        eye_list = [0, 1, 3]
        nose_list = [0, 1, 2, 3]
        chin_list = [0, 1, 2, 3, 4]
        # ear_f_list = [0,1]
        ear_s_list = [0, 1]
        horn_n_list = [0, 1, 2, 3]
        horn_s_list = [0, 1, 2]
        horn_f_list = [2, 3, 4]
        foot_t_list = [0]
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = [
            0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]
        tail_l_list = [0, 1, 2]
        body_dict = {'skin_color': skin_c_list, 'body_type': body_t_list,
                     'body_size': body_s_list, 'wing_size': None, 'tail_length': tail_l_list}
        head_dict = {'head_form': headform_list, 'eye_color': eye_list, 'nose': nose_list, 'chin': chin_list, 'lip_form': None,
                     'ear_form': None, 'ear_size': ear_s_list,
                     'hair_lengt': None, 'hair_type': None, 'hair_color': None,
                     'pair_number': horn_n_list, 'horn_size':  horn_s_list, 'horn_form': horn_f_list,
                     'tusk_size': None}
        limbs_dict = {'arm_length': arm_l_list, 'hand_size': hand_s_list, 'hand_claw_size': handclaw_s_list,
                      'leg_length': leg_l_list, 'foot_size': foot_s_list, 'foot_claw_size': footclaw_s_list, 'foot_type': foot_t_list}
        race = 'Lizardmen'

        input_list = [body_dict, head_dict, limbs_dict]

        return race, input_list

    def Monster_Demon(self):
        skin_c_list = [1, 2, 9, 4]
        body_t_list = [0, 1, 2, 3, 4]
        body_s_list = [0, 1, 2]
        headform_list = [0, 1, 2, 3]
        eye_list = [0, 1, 2, 3, 4]
        hair_l_list = [0, 1, 2, 3, 4]
        hair_t_list = [0, 1, 2]
        hair_c_list = [0, 1, 2, 3]
        nose_list = [0, 1, 2, 3]
        chin_list = [0, 1, 2, 3, 4]
        ear_f_list = [0, 1]
        ear_s_list = [0, 1]
        lip_f_list = [0]
        horn_n_list = [1, 2, 3]
        horn_f_list = [1, 2, 3, 4]
        horn_s_list = [0, 1, 2, 3, 4]
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = [
            0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]
        foot_t_list = [0, 1, 2, 3, 4, 5]
        wing_s_list = [0, 1, 2, 3, 4]
        tail_l_list = [0, 1, 2]
        body_dict = {'skin_color': skin_c_list, 'body_type': body_t_list,
                     'body_size': body_s_list, 'wing_size': wing_s_list, 'tail_length': tail_l_list}
        head_dict = {'head_form': headform_list, 'eye_color': eye_list, 'nose': nose_list, 'chin': chin_list, 'lip_form': lip_f_list,
                     'ear_form': ear_f_list, 'ear_size': ear_s_list,
                     'hair_lengt': hair_l_list, 'hair_type': hair_t_list, 'hair_color': hair_c_list,
                     'pair_number': horn_n_list, 'horn_size':  horn_s_list, 'horn_form': horn_f_list,
                     'tusk_size': None}
        limbs_dict = {'arm_length': arm_l_list, 'hand_size': hand_s_list, 'hand_claw_size': handclaw_s_list,
                      'leg_length': leg_l_list, 'foot_size': foot_s_list, 'foot_claw_size': footclaw_s_list, 'foot_type': foot_t_list}
        race = 'Demonkin'

        input_list = [body_dict, head_dict, limbs_dict]

        return race, input_list

    def Monster_Head(self, head):

        if head['hair_lengt'] != None and head['hair_lengt'] != 'none':
            hair = {'length': head['hair_lengt'],
                    'type': head['hair_type'], 'color': head['hair_color']}
        else:
            hair = None

        if head['ear_form'] != None:
            ear = {'form': head['ear_form'], 'size': head['ear_size']}
        else:
            ear = None

        if head['pair_number'] == None:
            horn = None
        else:
            horn = {'pair_number': head['pair_number'],
                    'size': head['horn_size'], 'form': head['horn_form']}

        if head['tusk_size'] == None:
            tusk = None
        else:
            tusk = {'size': head['tusk_size']}

        head_dict = {'form': head['head_form'], 'eye_color': head['eye_color'],
                     'hair': hair,
                     'horn': horn,
                     'nose': head['nose'], 'chin': head['chin'],
                     'ear': ear,
                     'lip_form': head['lip_form'], 'tusk': tusk}

        return head_dict

    def Monster_limbs(self, limbs):
        limbs_dict = {'arm_length': limbs['arm_length'], 'hand': {'size': limbs['hand_size'], 'claw_size': limbs['hand_claw_size']},
                      'leg_length': limbs['leg_length'], 'foot': {'size': limbs['foot_size'], 'claw_size': limbs['foot_claw_size'], 'type': limbs['foot_type']}}
        return limbs_dict
