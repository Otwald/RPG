from Random_Gen import Monster_NumberGen
from Random_Gen import Weighted_NumberGen
from Random_Gen import Multi_NumberGen

class Equipment_Gen:


    def Equipment_Basic(self):
        quality_list = ['poor', 'middle' ,'rich']
        quality_list = Monster_NumberGen(quality_list)

        weapon , shield = self.Equipment_Weapon()
        backpack, tent_dict = self.Equipment_TravelGear()
        armor = ['None' ,'Gambeson', 'Chainmail', 'Plate']
        # armor = Weighted_NumberGen(armor, [40, 40, 20])
        armor_dict = {'head' : Weighted_NumberGen(armor, [40, 40, 20]), 'torso' : Weighted_NumberGen(armor, [40, 40, 20]), 
            'legs' : Weighted_NumberGen(armor, [40, 40, 20]), 'arms' : Weighted_NumberGen(armor, [40, 40, 20])}

        
        equip_dict = {'armor' : armor_dict, 'weapon' : weapon, 'shield' : shield , 'backpack' : backpack , 'tent' : tent_dict}
        # print(equip_dict)

        return equip_dict

    def Equipment_TravelGear(self):
        backpack = Monster_NumberGen(['none', 'small', 'medium', 'huge'])
        back_dict = {'none' : 0, 'small' : 2, 'medium' : 4, 'huge' : 4}
        # small = 2 , medium = 4 : zelt = small, huge = 8 : zelt all
        
        tent = ['none', 'cover', 'small', 'medium', 'huge']
        tent_dict = None
        travel_dict = None
        if backpack != 'none' :
            travel_gear = ['compass', 'waterskin', 'ration', 'map', 'rope_10m', 'sleepingbag', 'cooking_equipment', 'pipe', 'flint_steel', 'mug']
            travel_dict = Multi_NumberGen(travel_gear, back_dict[backpack])
        if backpack == 'medium':
            tent_dict =  Monster_NumberGen(tent[:-2])
        elif backpack == 'huge':
            tent_dict =  Monster_NumberGen(tent)
        backpack = {'size' : backpack , 'invetory' : travel_dict}
        return backpack, tent_dict
        
    def Equipment_Weapon(self):
        weapon_category = ['Simple', 'Military', 'Exotic']
        weapon_category = Weighted_NumberGen(weapon_category, [50,40, 10])
        weapon_genre = ['Light', 'One-Handed', 'Two-Handed', 'Ranged']
        weapon_index = Monster_NumberGen([0,1,2,3])
        weapon_genre = weapon_genre[weapon_index]
        weapon_dict = { 'Simple' : { 'Light': ['Dagger', 'Sickle'] , 'One-Handed': ['Club', 'Mallet'], 'Two-Handed': ['Spear', 'Staff'], 'Ranged': ['Slingshot', 'Bow'] },
                        'Military' :  { 'Light': ['Gladius', 'Machete'] , 'One-Handed': ['Sword', 'Mace'],
                                         'Two-Handed': ['Greatsword', 'Polearm'], 'Ranged': ['Crossbow', 'LongBow'] },
                        'Exotic' :  { 'Light': ['Kama', 'Waveblade'] , 'One-Handed': ['Rapier', 'Whip'], 'Two-Handed': ['Harpoon', 'Flailpole'], 'Ranged': ['Blowgun', 'Net'] }
            }
        weapon = Monster_NumberGen(weapon_dict[weapon_category][weapon_genre])
        metal = ['copper', 'bronze', 'iron', 'steel', 'obsidian']
        wood = ['birch', 'ash', 'oak', 'fir']
        leather = ['rabbit', 'cow', 'wolf', 'deer']
        shield = None
        if weapon_index < 2:
            shield = self.Equipment_Shield(metal, leather, wood)
        wood = Monster_NumberGen(wood)
        leather = Monster_NumberGen(leather)
        metal = Weighted_NumberGen(metal, [20, 20, 30, 20, 10 ])

        weapon_dict =  {'type' : weapon, 'metal_part' : metal, 'wood_parts': wood, 'leather_part' : leather} 
        return weapon_dict , shield

    def Equipment_Shield(self, metal, leather, wood):
            shield = ['Buckler', 'light_Shield', 'heavy_Shield', 'tower_Shield']
            shield = Weighted_NumberGen(shield, [30,30,30,10])
            wood = Monster_NumberGen(wood)
            leather = Monster_NumberGen(leather)
            metal = Weighted_NumberGen(metal, [20, 20, 30, 20, 10 ])
            return {'type' : shield , 'metal_part' : metal , 'wood_parts' : wood, 'leather_part' : leather}





