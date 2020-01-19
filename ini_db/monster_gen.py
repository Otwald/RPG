
from alchemy import DbInterface
from base import RaceTplTorso, RaceTplHead, RaceTplLimps, Race, Base


class MonsterGen:

    races: list
    tables: list
    db: DbInterface

    def __init__(self):
        # self.races = [self.Monster_Demon, self.Monster_Human,
        #               self.Monster_Orcoid, self.Monster_Repte,
        #               self.Monster_Undead
        #               ]
        self.races = [self.Monster_Orcoid]
        self.tables = [RaceTplTorso, RaceTplHead, RaceTplLimps]
        self.db = DbInterface()

    def __insertEntry(self, tclass: Base, context: dict, race: str, session) -> Base:
        """populates the newly created table with context
        """
        initclass = tclass(race=race, **context)
        session.add(initclass)
        return initclass

    def __insertMapping(self, view: dict, session) -> None:
        """creates an entry for the race mapping
        """
        for key, value in view.items():
            torso, head, limps = value
            session.add(Race(key, torso, head, limps))
        session.commit()

    def checkDB(self) -> None:
        """calls the DB to check if DB was already created, if not calls a creator
        """
        view = {}
        session = self.db.getSession()
        for tableClass in self.tables:
            if not self.db.checkTable(tableClass):
                self.db.createTable(tableClass)
                for race in self.races:
                    name, body = race()
                    initclass = self.__insertEntry(
                        tableClass,
                        body[tableClass.__tablename__],
                        name,
                        session
                    )
                    session.commit()
                    if name not in view:
                        view[name] = []
                    view[name].append(initclass.id)
        if view:
            self.db.createTable(Race)
            self.__insertMapping(view, session)
        session.close()

    def Monster_Orcoid(self):
        skin_c_list = '4, 5, 6, 7'
        body_t_list = '0, 1, 2, 3, 4, 6'
        body_s_list = '0, 1, 2'
        headform_list = '2, 3'
        eye_list = '0, 2, 3'
        hair_l_list = '0, 4'
        hair_t_list = '1, 2'
        hair_c_list = '0, 1'
        nose_list = '0, 1, 2'
        chin_list = '0, 1, 2, 3, 4'
        ear_f_list = '2, 3'
        ear_s_list = '0, 1'
        lip_f_list = '0, 1'
        tusk_s_list = '0, 1, 2, 3, 4, 5'
        body_dict = {'SkinC': skin_c_list, 'BodyT': body_t_list,
                     'BodyS': body_s_list, 'WingS': None, 'TailL': None}
        head_dict = {'HeadF': headform_list, 'EyeC': eye_list, 'NoseF': nose_list, 'ChinF': chin_list, 'LipF': lip_f_list,
                     'EarF': ear_f_list, 'EarS': ear_s_list,
                     'HairL': hair_l_list, 'HairT': hair_t_list, 'HairC': hair_c_list,
                     'HornN': None, 'HornS':  None, 'HornF': None,
                     'TuskS': tusk_s_list}
        limbs_dict = {'ArmL': '0, 1, 2', 'HandS': '0, 1, 2', 'HandclawS': '0, 1, 2',
                      'LegL': '0, 1, 2', 'FootS': '0, 1, 2', 'FootclawS': '0, 1, 2', 'FootT': '0'}
        race = 'Orc'

        input_list = {RaceTplTorso.__tablename__: body_dict,
                      RaceTplHead.__tablename__: head_dict, RaceTplLimps.__tablename__: limbs_dict}

        return race, input_list

    def Monster_Undead(self):
        skin_c_list = '1, 2, 3, 5'
        body_t_list = '0, 1, 2, 3, 4, 5, 6'
        body_s_list = '0, 1, 2'
        headform_list = '0, 1, 2, 3'
        eye_list = '0, 1, 2'
        hair_l_list = '0, 1, 2, 3, 4'
        hair_t_list = '0, 1, 2'
        hair_c_list = '0, 1, 2, 3'
        nose_list = '0, 1, 2, 3'
        chin_list = '0, 1, 2, 3, 4'
        ear_f_list = '0, 1'
        ear_s_list = '0, 1'
        lip_f_list = '0, 1, 2, 3, 4'
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = \
            '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2'
        foot_t_list = '0'
        body_dict = {'SkinC': skin_c_list, 'BodyT': body_t_list,
                     'BodyS': body_s_list, 'WingS': None, 'TailL': None}
        head_dict = {'HeadF': headform_list, 'EyeC': eye_list, 'NoseF': nose_list, 'ChinF': chin_list, 'LipF': lip_f_list,
                     'EarF': ear_f_list, 'EarS': ear_s_list,
                     'HairL': hair_l_list, 'HairT': hair_t_list, 'HairC': hair_c_list,
                     'HornN': None, 'HornS':  None, 'HornF': None,
                     'TuskS': None}
        limbs_dict = {'ArmL': arm_l_list, 'HandS': hand_s_list, 'HandclawS': handclaw_s_list,
                      'LegL': leg_l_list, 'FootS': foot_s_list, 'FootclawS': footclaw_s_list, 'FootT': foot_t_list}
        race = 'Human'

        input_list = {RaceTplTorso.__tablename__: body_dict,
                      RaceTplHead.__tablename__: head_dict, RaceTplLimps.__tablename__: limbs_dict}

        return race, input_list

    def Monster_Human(self):
        skin_c_list = '0, 1, 2, 3, 4'
        body_t_list = '0, 1, 2, 3, 4, 5, 6'
        body_s_list = '0, 1, 2'
        headform_list = '0, 1, 2, 3'
        eye_list = '0, 1, 2'
        hair_l_list = '0, 1, 2, 3, 4'
        hair_t_list = '0, 1, 2'
        hair_c_list = '0, 1, 2, 3'
        nose_list = '0, 1, 2, 3'
        chin_list = '0, 1, 2, 3, 4'
        ear_f_list = '0, 1'
        ear_s_list = '0, 1'
        lip_f_list = '0, 1, 2, 3, 4'
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = '0, 1, 2',
        '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2'
        foot_t_list = '0'
        body_dict = {'SkinC': skin_c_list, 'BodyT': body_t_list,
                     'BodyS': body_s_list, 'WingS': None, 'TailL': None}
        head_dict = {'HeadF': headform_list, 'EyeC': eye_list, 'NoseF': nose_list, 'ChinF': chin_list, 'LipF': lip_f_list,
                     'EarF': ear_f_list, 'EarS': ear_s_list,
                     'HairL': hair_l_list, 'HairT': hair_t_list, 'HairC': hair_c_list,
                     'HornN': None, 'HornS':  None, 'HornF': None,
                     'TuskS': None}
        limbs_dict = {'ArmL': arm_l_list, 'HandS': hand_s_list, 'HandclawS': handclaw_s_list,
                      'LegL': leg_l_list, 'FootS': foot_s_list, 'FootclawS': footclaw_s_list, 'FootT': foot_t_list}
        race = 'Human'

        input_list = {RaceTplTorso.__tablename__: body_dict,
                      RaceTplHead.__tablename__: head_dict, RaceTplLimps.__tablename__: limbs_dict}
        return race, input_list

    def Monster_Repte(self):
        skin_c_list = '3, 4, 5, 6, 7, 8'
        body_t_list = '0, 1, 2, 3, 4, 5, 6'
        body_s_list = '0, 1, 2'
        headform_list = '0, 1, 2, 3'
        eye_list = '0, 1, 3'
        nose_list = '0, 1, 2, 3'
        chin_list = '0, 1, 2, 3, 4'
        # ear_f_list = '0,1'
        ear_s_list = '0, 1'
        horn_n_list = '0, 1, 2, 3'
        horn_s_list = '0, 1, 2'
        horn_f_list = '2, 3, 4'
        foot_t_list = '0'
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = '0, 1, 2',
        '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2'
        tail_l_list = '0, 1, 2'
        body_dict = {'SkinC': skin_c_list, 'BodyT': body_t_list,
                     'BodyS': body_s_list, 'WingS': None, 'TailL': tail_l_list}
        head_dict = {'HeadF': headform_list, 'EyeC': eye_list, 'NoseF': nose_list, 'ChinF': chin_list, 'LipF': None,
                     'EarF': None, 'EarS': ear_s_list,
                     'HairL': None, 'HairT': None, 'HairC': None,
                     'HornN': horn_n_list, 'HornS':  horn_s_list, 'HornF': horn_f_list,
                     'TuskS': None}
        limbs_dict = {'ArmL': arm_l_list, 'HandS': hand_s_list, 'HandclawS': handclaw_s_list,
                      'LegL': leg_l_list, 'FootS': foot_s_list, 'FootclawS': footclaw_s_list, 'FootT': foot_t_list}
        race = 'Lizardmen'

        input_list = {RaceTplTorso.__tablename__: body_dict,
                      RaceTplHead.__tablename__: head_dict, RaceTplLimps.__tablename__: limbs_dict}

        return race, input_list

    def Monster_Demon(self):
        skin_c_list = '1, 2, 9, 4'
        body_t_list = '0, 1, 2, 3, 4'
        body_s_list = '0, 1, 2'
        headform_list = '0, 1, 2, 3'
        eye_list = '0, 1, 2, 3, 4'
        hair_l_list = '0, 1, 2, 3, 4'
        hair_t_list = '0, 1, 2'
        hair_c_list = '0, 1, 2, 3'
        nose_list = '0, 1, 2, 3'
        chin_list = '0, 1, 2, 3, 4'
        ear_f_list = '0, 1'
        ear_s_list = '0, 1'
        lip_f_list = '0'
        horn_n_list = '1, 2, 3'
        horn_f_list = '1, 2, 3, 4'
        horn_s_list = '0, 1, 2, 3, 4'
        arm_l_list, hand_s_list, handclaw_s_list, leg_l_list, foot_s_list, footclaw_s_list = '0, 1, 2',
        '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2', '0, 1, 2'
        foot_t_list = '0, 1, 2, 3, 4, 5'
        wing_s_list = '0, 1, 2, 3, 4'
        tail_l_list = '0, 1, 2'
        body_dict = {'SkinC': skin_c_list, 'BodyT': body_t_list,
                     'BodyS': body_s_list, 'WingS': wing_s_list, 'TailL': tail_l_list}
        head_dict = {'HeadF': headform_list, 'EyeC': eye_list, 'NoseF': nose_list, 'ChinF': chin_list, 'LipF': lip_f_list,
                     'EarF': ear_f_list, 'EarS': ear_s_list,
                     'HairL': hair_l_list, 'HairT': hair_t_list, 'HairC': hair_c_list,
                     'HornN': horn_n_list, 'HornS':  horn_s_list, 'HornF': horn_f_list,
                     'TuskS': None}
        limbs_dict = {'ArmL': arm_l_list, 'HandS': hand_s_list, 'HandclawS': handclaw_s_list,
                      'LegL': leg_l_list, 'FootS': foot_s_list, 'FootclawS': footclaw_s_list, 'FootT': foot_t_list}
        race = 'Demonkin'

        input_list = {RaceTplTorso.__tablename__: body_dict,
                      RaceTplHead.__tablename__: head_dict, RaceTplLimps.__tablename__: limbs_dict}

        return race, input_list

    # def Monster_Head(self, head):

    #     if head''HairL'] != None and head''HairL'] != 'none':
    #         hair= {'length': head['HairL'],
    #                 'type': head['HairT'], 'color': head['HairC']}
    #     else:
    #         hair = None

    #     if head['EarF'] != None:
    #         ear = {'form': head['EarF'], 'size': head['EarS']}
    #     else:
    #         ear = None

    #     if head['HornN'] == None:
    #         horn = None
    #     else:
    #         horn = {'HornN': head['HornN'],
    #                 'size': head['HornS'], 'form': head['HornF']}

    #     if head['TuskS'] == None:
    #         tusk = None
    #     else:
    #         tusk = {'size': head['TuskS']}

    #     head_dict = {'form': head['HeadF'], 'EyeC': head['EyeC'],
    #                  'hair': hair,
    #                  'horn': horn,
    #                  'NoseF': head['NoseF'], 'ChinF': head['ChinF'],
    #                  'ear': ear,
    #                  'LipF': head['LipF'], 'tusk': tusk}

    #     return head_dict

    # def Monster_limbs(self, limbs):
    #     limbs_dict = {'ArmL': limbs['ArmL'], 'hand': {'size': limbs['HandS'], 'claw_size': limbs['HandclawS']},
    #                   'LegL': limbs['LegL'], 'foot': {'size': limbs['FootS'], 'claw_size': limbs['FootclawS'], 'type': limbs['FootT']}}
    #     return limbs_dict
