from person import Person
from db_handler import DataBase

def main():
    # p = Person()
    # p.generatePerson()
    # print(p.body.head)
    db = DataBase()
    print(db.makeRequest('Select * from v_race where race = "human"'))

if __name__ == "__main__":
    main()
