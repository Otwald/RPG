import os
from person import Person
from ini_db import body_gen as Bg, monster_gen as Mg

# import alchemy


def checkDB():
    body = Bg.BodyGen()
    body.checkDB()
    mon = Mg.MonsterGen()
    mon.checkDB()


def main():
    checkDB()
    p = Person()
    p.generatePerson()
    print(p.body.head)


if __name__ == "__main__":
    main()
