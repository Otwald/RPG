from Random_Gen import Monster_NumberGen
from race import human

class BodyFactory:
    """a factory that gives out the different race classes.

        race needs to be in a List at the Moment the List is static
    """

    def Monster_ArtGen(self) -> object:
        races = ['Orcoid', 'Undead',
                 'Human', 'Repte',
                 'Demon']
        race = Monster_NumberGen(races)
        module = __import__('race')
        submodule = getattr(module, 'human')
        raceClass = getattr(submodule, 'Human')+
        return raceClass()