from Monster_Gen import Monster_Gen
from Equipment_Gen import Equipment_Gen

MG = Monster_Gen()
EG = Equipment_Gen()


def MonsterHandler():
    race, body_dict = MG.Monster_SwitchHandler()
    equipment = EG.Equipment_Basic()
    # person_dict = {'race': race, 'body' : body_dict, 'equipment' : equipment}
    # print(person_dict)

def run():
    MonsterHandler()



if __name__ == "__main__":
    run()