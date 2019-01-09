from Monster_Gen import Monster_Gen
from Equipment_Gen import Equipment_Gen

MG = Monster_Gen()
EG = Equipment_Gen()


def MonsterHandler():
    # race, body_dict = MG.Monster_SwitchHandler()
    # person_dict = {'race': race, 'body' : body_dict}
    # print(person_dict)
    EG.Equipment_Basic()

def run():
    MonsterHandler()



if __name__ == "__main__":
    run()