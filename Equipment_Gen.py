from Random_Gen import Monster_NumberGen
from Random_Gen import Weighted_NumberGen

class Equipment_Gen:


    def Equipment_Basic(self):
        quality_list = ['poor', 'middle' ,'rich']
        quality_list = Monster_NumberGen(quality_list)

        weapon = self.Equipment_Weapon()
        armor = ['Gambeson', 'Chainmail', 'Plate']
        # armor = Weighted_NumberGen(armor, [40, 40, 20])
        armor_dict = {'armor' :{'head' : Weighted_NumberGen(armor, [40, 40, 20]), 'torso' : Weighted_NumberGen(armor, [40, 40, 20]), 
            'legs' : Weighted_NumberGen(armor, [40, 40, 20]), 'arms' : Weighted_NumberGen(armor, [40, 40, 20])}}
        print(armor_dict)


        return weapon
        
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

        return  {'main_weapon': {'type' : weapon, 'metal_part' : metal, 'wood_parts': wood, 'leather_part' : leather}, 'shield' : shield}

    def Equipment_Shield(self, metal, leather, wood):
            shield = ['Buckler', 'light_Shield', 'heavy_Shield', 'tower_Shield']
            shield = Weighted_NumberGen(shield, [30,30,30,10])
            wood = Monster_NumberGen(wood)
            leather = Monster_NumberGen(leather)
            metal = Weighted_NumberGen(metal, [20, 20, 30, 20, 10 ])
            return {'type' : shield , 'metal_part' : metal , 'wood_parts' : wood, 'leather_part' : leather}





