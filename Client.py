from Monster_Gen import Monster_Gen
from Equipment_Gen import Equipment_Gen

MG = Monster_Gen()
EG = Equipment_Gen()


def MonsterHandler():
    deutsch ={'Orc' : 'Ork', 'Human' : 'Mensch', 'Undead': 'Untoter', 'Lizardmen' : 'Echsenmensch', 'Demonkin' : 'Dämon',
    'pale' : 'blasser' , 'peach' : 'weiße', 'olive' : 'gebräunter', 'brown' : 'brauner' , 'black' : 'schwarzer', 'purple': 'lila' , 
        'light_green' : 'grünlicher', 'dark_green' : 'dunkel grüner', 'blue' : 'blauer', 'red' : 'roter',
        'strong' : 'kräftigen',
        'muscular' : 'muskolüses', 'slender' : 'langestreckten', 'athletic' : 'athletischen', 'thin' : 'dürren', 'slim' : 'dünnen', 'chubby' : 'dicklichen' 
        ,'large' : 'groß' , 'medium' : 'durchschnittlich', 'small' : 'klein' , 'oval' : 'eierförmig', 'long_h' : 'langezogen', 'round' : 'rund', 'angular' : 'kantig',
        'short' : 'kurzem', 'chin-length' : 'kinnlangen', 'shoulder-length' : 'schulterlangen', 'long' : 'sehr langen', 'none' : 'keinen', 
        'smooth' : 'glatten', 'curly' : 'gewellten', 'frizzy' : 'krausen', 'brown_h' : 'braunen', 'black_h' :'schwarzen', 'blond_h' : 'blonden', 'red_h' :'roten',
        'green_e' : 'grünen', 'blue_e' : 'blauen', 'purple_e' : 'lilanen', 'crooked' : 'hacken', 'small_n' : 'kleine', 'tall_n'  : 'große', 'pointed_n' : 'spitze',
        'energetic_c' : 'energisches', 'pointed_c' : 'spitzes', 'round_c' : 'rundes', 'small_c' :'kleines', 'protruding_c' : 'hervorstehendes',
        'sticking_out_e' : 'abstehende', 'fitting_e' : 'anliegende', 'pointy_e' : 'spitze', 'pointy_ragged_e' : 'zackige', 'big_e' : 'große', 'small_e' : 'kleine',
        'thin_l' : 'dünne Lippen', 'balanced_l' : 'gleichmäßige Lippen' , 'plump_l' : 'dicke Lippen', 'thin_upperlip_l' : 'eine dünne Oberlippe', 'thin_lowerlip_l' : 'eine dünne Unterlippe',
        'none_t' : 'keine','tiny_t' : 'winzige', 'small_t' : 'kleine', 'medium_t' : 'normale', 'large_t' : 'große', 'giant_T' : 'gewaltige',
        'tiny_h' : 'winzigen', 'small_h' : 'kleinen', 'medium_h' : 'normalen', 'large_h' : 'großen', 'giant_h' : 'gigantischen',
        'long_l' : "lang", 'medium_l' : 'normal', 'small_l' : 'klein', 'huge_l' : 'groß', 'medium_s' : 'mittelgroß',  'medium_claw': 'durschnittlichen', 'small_claw' : 'kurzen','long_claw' : 'sehr langen',
        'cowhoof' : 'Kuhhufen', 'elkhoof' : 'Elchhufen', 'goathoof' : 'Ziegenhufen', 'lionpaw' : 'Löwenpfoten', 'chicken' : 'Hühnerfüßen',
        'tiny_w': 'winzige', 'small_w' : 'kleine', 'medium_w' : 'mittelgroße', 'large_w' : 'große' , 'huge_w' : 'riesige',
        'short_tail' : 'kurz', 'medium_tail' : 'normal lang', 'long_tail' : 'lang', 'medium_c' : 'durchschnittlichen'
        }
    # deutsch = {'skin_color': {'pale' : 'blasser' , 'peach' : 'weiße', 'olive' : 'gebräunter', 'brown' : 'brauner' , 'black' : 'schwarzer', 'purple': 'lila' , 
    #     'light_green' : 'grünlicher', 'dark_green' : 'dunkel grüner', 'blue' : 'blauer', 'red' : 'roter'}, 'body_type': { 'strong' : 'kräftigen',
    #     'muscular' : 'muskolüses', 'slender' : 'langestreckten', 'athletic' : 'athletischen', 'thin' : 'dürren', 'slim' : 'dünnen', 'chubby' : 'dicklichen'},
    #     'body_size' : output_list[0]['body_size'], 
    #         'head' : head_dict, 'limbs' : limbs_dict, 'wing_size' :output_list[0]['wing_size'], 'tail_length' : output_list[0]['tail_length']}



    race, body_dict = MG.Monster_SwitchHandler()
    equipment = EG.Equipment_Basic()
    person_dict = {'race': race, 'body' : body_dict, 'equipment' : equipment}
    # print(person_dict)
    def wordfinder(body_dict):
        for key, value in body_dict.items():
            if(type(value) is dict):
                wordfinder(value)
            else:
                print(deutsch[key][value])
                
    
    # wordfinder(body_dict)
    lips = ""
    tusk = ""
    horn = ""
    wing = ""
    tail = ""
    if(person_dict['body']['head']['hair'] == None):
        hair = 'keinen Haar'
    else:
        hair = deutsch[person_dict['body']['head']['hair']['length']] + ' ' + deutsch[person_dict['body']['head']['hair']['type']] + ' ' + deutsch[person_dict['body']['head']['hair']['color']] + ' Haar'
    
    if(person_dict['body']['head']['ear'] != None):
        ear = 'dazu ' + deutsch[person_dict['body']['head']['ear']['form']] + ' ' + deutsch[person_dict['body']['head']['ear']['size']] + ' Ohren' 
    else:
        ear = 'dazu Ohrlöcher'

    if(person_dict['body']['head']['lip_form'] != None):
       lips = deutsch[person_dict['body']['head']['lip_form']]

    if(person_dict['body']['head']['tusk'] != None):
        if(person_dict['body']['head']['tusk']['size'] != 'None'):
            tusk = '. Zusätzlich besitzt es ' + deutsch[person_dict['body']['head']['tusk']['size']] + ' Hauer'
        else:
            tusk = '. Es besitzt keine Hauer'

    if(person_dict['body']['head']['horn'] != None):
        horn = ' Zusätzlich besitzt es ' + deutsch[person_dict['body']['head']['horn']['size']] + " Hörner"

    def nail(item):
        if(item):
            claw = deutsch[person_dict['body']['limbs']['hand']['claw_size']]
        else:
            claw = deutsch[person_dict['body']['limbs']['foot']['claw_size']]
        if(person_dict['body']['limbs']['foot']['type'] != 'foot'):
            if(item):
                return (claw + ' Klauen') 
            else:
                # foot = person_dict['body']['limbs']['foot']['type']
                # if(foot == 'cowhoof' or foot == 'elkhoof' or foot == 'goathoof'):
                # else:
                #     return (claw + ' Klauen') 
                return deutsch[person_dict['body']['limbs']['foot']['type']]
        elif (person_dict['race'] == 'Lizardmen' or person_dict['race'] == 'Demonkin'):
            return (claw + ' Klauen') 
        else:
            if(item):
                return (claw + ' Fingernägel')
            else:
                return (claw + ' Zehennägel')
    
    if(person_dict['body']['wing_size'] != None):
        wing = '. Zusätzlich besitzt es ' +deutsch[person_dict['body']['wing_size']] + ' Schwingen'
    if(person_dict['body']['tail_length'] != None):
        tail = '. Der Schwanz ist ' +deutsch[person_dict['body']['tail_length']] 


    print( 'Es ist ein '+ deutsch[person_dict['race']] + ' mit ' + deutsch[person_dict['body']['skin_color']] + ' Hautfarbe. Es besitzt einen ' + 
        deutsch[person_dict['body']['body_type']] + ' Körperbau und ist für die Art relativ ' + deutsch[person_dict['body']['body_size']] + ' . Der Kopf ist eher ' +
        deutsch[person_dict['body']['head']['form']] + ', mit '+ hair + '. Es blickt mit ' + deutsch[person_dict['body']['head']['eye_color']] + 
        ' Augen in die Welt. Es besitzt eine ' +  deutsch[person_dict['body']['head']['nose']] + ' Nase, ein ' + deutsch[person_dict['body']['head']['chin']] + ' Kinn, ' +
        ear  +  ' und ' + lips + tusk + horn + '. Die Arme sind im Verhältnis zum restlichen Körper eher ' + deutsch[person_dict['body']['limbs']['arm_length']] + 
        ', die Hände sind relativ gesehen ' + deutsch[person_dict['body']['limbs']['hand']['size']] + ' , mit ' +  deutsch[person_dict['body']['limbs']['hand']['claw_size']] + 
        nail(True) + '. Die Beine sind im Verhältnis zum restlichen Körper eher '+ deutsch[person_dict['body']['limbs']['leg_length']] + 
        ', die Füße sind relativ gesehen ' + deutsch[person_dict['body']['limbs']['foot']['size']] + ', mit '  + nail(False) + wing + tail)
    # print()

def run():
    MonsterHandler()



if __name__ == "__main__":
    run()
