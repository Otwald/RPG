from alchemy import DbInterface

import base as b


class BodyGen:

    db: DbInterface
    bodypart: list
    baseTable: dict

    def __init__(self):
        self.db = DbInterface()
        self.baseTable = {
            b.BodyTorsoSkinC.__tablename__: b.BodyTorsoSkinC,
            b.BodyTorsoBodyT.__tablename__: b.BodyTorsoBodyT,
            b.BodyTorsoBodyS.__tablename__: b.BodyTorsoBodyS,
            b.BodyTorsoTailL.__tablename__: b.BodyTorsoTailL,
            b.BodyTorsoWingS.__tablename__: b.BodyTorsoWingS,
            b.BodyHeadHeadF.__tablename__: b.BodyHeadHeadF,
            b.BodyHeadEyeC.__tablename__: b.BodyHeadEyeC,
            b.BodyHeadHairL.__tablename__: b.BodyHeadHairL,
            b.BodyHeadHairT.__tablename__: b.BodyHeadHairT,
            b.BodyHeadHairC.__tablename__: b.BodyHeadHairC,
            b.BodyHeadNoseF.__tablename__: b.BodyHeadNoseF,
            b.BodyHeadChinF.__tablename__: b.BodyHeadChinF,
            b.BodyHeadEarF.__tablename__: b.BodyHeadEarF,
            b.BodyHeadEarS.__tablename__: b.BodyHeadEarS,
            b.BodyHeadLipF.__tablename__: b.BodyHeadLipF,
            b.BodyHeadHornS.__tablename__: b.BodyHeadHornS,
            b.BodyHeadHornF.__tablename__: b.BodyHeadHornF,
            b.BodyHeadHornN.__tablename__: b.BodyHeadHornN,
            b.BodyHeadTuskS.__tablename__: b.BodyHeadTuskS,
            b.BodyLimpsArmL.__tablename__: b.BodyLimpsArmL,
            b.BodyLimpsHandS.__tablename__: b.BodyLimpsHandS,
            b.BodyLimpsHandclawS.__tablename__: b.BodyLimpsHandclawS,
            b.BodyLimpsLegL.__tablename__: b.BodyLimpsLegL,
            b.BodyLimpsFootS.__tablename__: b.BodyLimpsFootS,
            b.BodyLimpsFootclawS.__tablename__: b.BodyLimpsFootclawS,
            b.BodyLimpsFootT.__tablename__: b.BodyLimpsFootT,
        }
        self.bodypart = [self.bodyTorso, self.bodyHead, self.bodyLimbs]

    def __insertEntry(self, tclass: b.Base, context: list, session) -> None:
        """populates the newly created table with context
        """
        for item in context:
            table = tclass(item)
            session.add(table)

    def checkDB(self) -> None:
        """calls the DB to check if DB was already created, if not calls a creator
        """
        session = self.db.getSession()
        for part in self.bodypart:
            for key, value in part().items():
                tableClass = self.baseTable[key]
                if not self.db.checkTable(tableClass):
                    self.db.createTable(tableClass)
                    self.__insertEntry(tableClass, value, session)
        session.commit()
        session.close()

    def bodyTorso(self) -> dict:
        return {
            b.BodyTorsoSkinC.__tablename__: ['pale', 'peach', 'olive', 'brown', 'black',
                                             'light_green', 'dark_green', 'blue', 'red', 'purple'],
            b.BodyTorsoBodyT.__tablename__: ['strong', 'muscular', 'slender',
                                             'athletic', 'thin', 'slim', 'chubby'],
            b.BodyTorsoBodyS.__tablename__: ['large', 'medium', 'small'],
            b.BodyTorsoTailL.__tablename__: ['short_tail', 'medium_tail', 'long_tail'],
            b.BodyTorsoWingS.__tablename__: ['tiny_w', 'small_w',
                                             'medium_w', 'large_w', 'huge_w']
        }

    def bodyHead(self) -> dict:
        return {
            b.BodyHeadHeadF.__tablename__: ['oval', 'long_h', 'round', 'angular'],
            b.BodyHeadEyeC.__tablename__: ['green_e', 'blue_e', 'brown_h', 'red_h', 'purple_e'],
            b.BodyHeadHairL.__tablename__: ['short', 'chin-length',
                                            'shoulder-length', 'long', 'none'],
            b.BodyHeadHairT.__tablename__: ['smooth', 'curly', 'frizzy'],
            b.BodyHeadHairC.__tablename__: ['brown_h', 'black_h', 'blond_h', 'red_h'],
            b.BodyHeadNoseF.__tablename__: ['crooked', 'small_n', 'tall_n', 'pointed_n'],
            b.BodyHeadChinF.__tablename__: ['energetic_c', 'pointed_c',
                                            'round_c', 'small_c', 'protruding_c'],
            b.BodyHeadEarF.__tablename__: ['sticking_out_e', 'fitting_e',
                                           'pointy_e', 'pointy_ragged_e'],
            b.BodyHeadEarS.__tablename__: ['big_e', 'small_e'],
            b.BodyHeadLipF.__tablename__: ['thin_l', 'balanced_l', 'plump_l',
                                           'thin_upperlip_l', 'thin_lowerlip_l'],
            b.BodyHeadHornS.__tablename__: ['tiny_h', 'small_h',
                                            'medium_h', 'large_h', 'giant_h'],
            b.BodyHeadHornF.__tablename__: ['antlers', 'goat', 'straight', 'curved', 'hooked'],
            b.BodyHeadHornN.__tablename__: ['none', '1', '2', '3', '4'],
            b.BodyHeadTuskS.__tablename__: ['none_t', 'tiny_t', 'small_t',
                                            'medium_t', 'large_t', 'giant_T'],
        }

    def bodyLimbs(self) -> dict:
        return {
            b.BodyLimpsArmL.__tablename__: ['long_l', 'medium_l', 'small_l'],
            b.BodyLimpsHandS.__tablename__: ['huge_l', 'medium_s', 'small_l'],
            b.BodyLimpsHandclawS.__tablename__: ['long', 'medium_c', 'small_c'],
            b.BodyLimpsLegL.__tablename__: ['long_l', 'medium_l', 'small_l'],
            b.BodyLimpsFootS.__tablename__: ['huge_l', 'medium_s', 'small_l'],
            b.BodyLimpsFootclawS.__tablename__: ['long_claw', 'medium_claw', 'small_claw'],
            b.BodyLimpsFootT.__tablename__: ['foot', 'cowhoof', 'elkhoof',
                                             'goathoof', 'lionpaw', 'chicken'],
        }
