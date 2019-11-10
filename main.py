from person import Person
from db_handler import DataBase

def main():
    p = Person()
    p.generatePerson()
    print(p.body)


if __name__ == "__main__":
    main()
