# I have a dictionary like tmpDict = {'ONE':{'TWO':{'THREE':10}}}
#
# Do we have any other way to access THREE's value other than doing
# tmpDict['ONE']['TWO']['THREE']?
# 
# {'dict1': {'innerkey': 'value'}}
# my code | wilhelm code
#### form of ####
#
# 0 : {'number'    : '2',
#      'name'      : 'K\'un, The Receptive',
#      'above'     : 'EARTH, the receptive',
#      'below'     : 'EARTH, the receptive',
#      'judgement' : 'THE RECEPTIVE brings about sublime success,\n'
#                    'Furthering through the perseverance of a mare.\n'
#               	 'If the superior man undertakes something and tries to lead,\n'
#               	 'He goes astray;\n'
#               	 'But if he follows, he finds guidance.\n'
#               	 'It is favorable to find friends in the west and south,\n'
#               	 'To forego friends in the east and north.\n'
#               	 'Quiet perseverance brings good fortune.',
#      'image'     : 'The earth\'s condition is receptive devotion.\n'
#               	 'Thus the superior man who has breadth of character\n'
#               	 'Carries the outer world.'},
#
#
# MOUNTAIN, keeping still
# HEAVEN, the creative
# LAKE, the joyous
# hexIndex[hexCode]['number']
#

hexIndex = {0 : {'number'    : '2',
                 'name'      : 'K\'un, The Receptive',
                 'above'     : 'EARTH, the receptive',
                 'below'     : 'EARTH, the receptive',
                 'judgement' : 'THE RECEPTIVE brings about sublime success,\n'
                               'Furthering through the perseverance of a mare.\n'
                 	           'If the superior man undertakes something and tries to lead,\n'
               	               'He goes astray;\n'
                          	   'But if he follows, he finds guidance.\n'
                          	   'It is favorable to find friends in the west and south,\n'
                          	   'To forego friends in the east and north.\n'
                          	   'Quiet perseverance brings good fortune.',
                 'image'     : 'The earth\'s condition is receptive devotion.\n'
                        	   'Thus the superior man who has breadth of character\n'
               	               'Carries the outer world.'},
            1 : {'number'    : 24,
                 'name'      : 'Fu, Return (The Turning Point)',
                 'above'     : 'EARTH, the receptive',
                 'below'     : 'THUNDER, the arousing',
                 'judgement' : 'RETURN. Success.\n'
                          	   'Going out and coming in without error.\n'
                          	   'Friends come without blame.\n'
                          	   'To and fro goes the way.\n'
                          	   'On the seventh day comes return.\n'
                          	   'It furthers one to have somewhere to go.',
                 'image'     : 'Thunder within the earth:\n'
                          	   'The image of THE TURNING POINT.\n'
                          	   'Thus the kings of antiquity closed the passes\n'
                          	   'At the time of solstice.\n'
                          	   'Merchants and strangers did not go about,\n'
                          	   'And the ruler\n'
                          	   'Did not travel through the provinces.'},
            2 :  {'number' : 7,
                  'name'   : 'Shih, The Army',
                  'above'  : 'EARTH, the receptive',
                  'below'  : 'WATER, the abysmal'},
            3 :  {'number' : 19,
                  'name'   : 'Lin, Approach'},
            4 :  {'number' : 15,
                  'name'   : 'Ch\'ien, Modesty'},
            5 :  {'number' : 36,
                  'name'   : 'Ming I, Darkening of the Light'},
            6 :  {'number' : 46,
                  'name'   : 'Sheng, Pushing Upward'},
            7 :  {'number' : 11,
                  'name'   : 'T\'ai, Peace'},
            8 :  {'number' : 16,
                  'name'   : 'Yu, Enthusiasm'},
            9 :  {'number' : 51,
                  'name'   : 'Chen, The Arousing (Shock, Thunder)'},
            10 : {'number' : 40,
                  'name'   : 'Hsieh, Deliverance'},
            11 : {'number' : 54,
                  'name'   : 'Kuei Mei, The Marrying Maiden'},
            12 : {'number' : 62,
                  'name'   : 'Hsiao Kuo, Preponderance of the Small'},
            13 : {'number' : 55,
                  'name'   : 'Feng, Abundance (Fullness)'},
            14 : {'number' : 32,
                  'name'   : 'Heng, Duration'},
            15 : {'number' : 34,
                  'name'   : 'Ta Chuang, The Power of the Great'},
            16 : {'number' : 8,
                  'name'   : 'Pi, Holding Together (Union)'},
            17 : {'number' : 3,
                  'name'   : 'Chun, Difficulty at the Beginning'},
            18 : {'number' : 29,
                  'name'   : 'K\'an, The Abysmal (Water)'},
            19 : {'number' : 60,
                  'name'   : 'Chieh, Limitation'},
            20 : {'number' : 39,
                  'name'   : 'Chien, Obstruction'},
            21 : {'number' : 63,
                  'name'   : 'Chi Chi, After Completion'},
            22 : {'number' : 48,
                  'name'   : 'Ching, The Well'},
            23 : {'number' : 5,
                  'name'   : 'Hsu, Waiting (Nourishment)'},
            24 : {'number' : 45,
                  'name'   : 'Ts\'ui, Gathering Together (Massing)'},
            25 : {'number' : 17,
                  'name'   : 'Sui, Following'},
            26 : {'number' : 47,
                  'name'   : 'K\'un, Oppression (Exhaustion)'},
            27 : {'number' : 58,
                  'name'   : 'Tui, The Joyous (Lake)'},
            28 : {'number' : 31,
                  'name'   : 'Hsien, Influence (Wooing)'},
            29 : {'number' : 49,
                  'name'   : 'Ko, Revolution (Molting)'},
            30 : {'number' : 28,
                  'name'   : 'Ta Kuo, Preponderance of the Great'},
            31 : {'number' : 43,
                  'name'   : 'Kuai, Break-Through (Resoluteness)'},
            32 : {'number' : 23,
                  'name'   : 'Po, Splitting Apart'},
            33 : {'number' : 27,
                  'name'   : 'I, Corners of the Mouth (Nourishment)'},
            34 : {'number' : 4,
                  'name'   : 'Meng, Youthful Folly'},
            35 : {'number' : 41,
                  'name'   : 'I, Increase'},
            36 : {'number' : 52,
                  'name'   : 'Ken, Keeping Still (Mountain)'},
            37 : {'number' : 22,
                  'name'   : 'Pi, Grace'},
            38 : {'number' : 18,
                  'name'   : 'Ku, Work on What Has Been Spoiled (Decay)'},
            39 : {'number' : 26,
                  'name'   : 'Ta Ch\'u, The Taming Power of the Great'},
            40 : {'number' : 35,
                  'name'   : 'Chin, Progress'},
            41 : {'number' : 21,
                  'name'   : 'Shih Ho, Biting Through'},
            42 : {'number' : 64,
                  'name'   : 'Wei Chi, Before Completion'},
            43 : {'number' : 38,
                  'name'   : 'K\'uei, Opposition'},
            44 : {'number' : 56,
                  'name'   : 'Lu, The Wanderer'},
            45 : {'number' : 30,
                  'name'   : 'Li, The Clinging (Fire)'},
            46 : {'number' : 50,
                  'name'   : 'Ting, The Cauldron'},
            47 : {'number' : 14,
                  'name'   : 'Ta Yu, Possession in Great Measure'},
            48 : {'number' : 20,
                  'name'   : 'Kuan, Completion (View)'},
            49 : {'number' : 42,
                  'name'   : 'I, Increase'},
            50 : {'number' : 59,
                  'name'   : 'Huan, Dispersion (Dissolusion)'},
            51 : {'number' : 61,
                  'name'   : 'Chung Fu, Inner Truth'},
            52 : {'number' : 53,
                  'name'   : 'Chien, Development (Gradual Progress)'},
            53 : {'number' : 37,
                  'name'   : 'Chia Jen, The Family (The Clan)'},
            54 : {'number' : 57,
                  'name'   : 'Sun, The Gentle (The Penetrating, Wind)'},
            55 : {'number' : 9,
                  'name'   : 'Hsiao Chu, The Taming Power of the Small'},
            56 : {'number' : 12,
                  'name'   : 'P\'i, Standstill (Stagnation)'},
            57 : {'number' : 25,
                  'name'   : 'Wu Wang, Innocence (The Unexpected)'},
            58 : {'number' : 6,
                  'name'   : 'Sung, Conflict'},
            59 : {'number' : 10,
                  'name'   : 'Lu, Treading (Conduct)'},
            60 : {'number' : 33,
                  'name'   : 'Tun, Retreat'},
            61 : {'number' : 13,
                  'name'   : 'T\'ung Jen, Fellowship with Men'},
            62 : {'number' : 44,
                  'name'   : 'Kou, Coming to Meet'},
            63 : {'number' : 1,
                  'name'   : 'Ch\'ien, The Creative'}
           }
