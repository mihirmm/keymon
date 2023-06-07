# import colorama
from colorama import init, Fore, Back, Style

init()

WILD_ANIMATION = ['XX                            \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n', 'XX                            \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n', 'XXXXXXXXXXXXXXXXXXXXXX        \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                            XX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n                             X\n        XXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXX                          X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXX      X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nX                            X\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                      XXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX                           XX\nX  XXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXX                XX\nXX                          XX\nXX                          XX\nXX                          XX\nXX                          XX\nXX                          XX\nXX                          XX\nXX                          XX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXX                         XXX\nXX                         XXX\nXX                         XXX\nXX                         XXX\nXX                          XX\nXX                          XX\nXX                          XX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXX                         XXX\nXX                         XXX\nXX                         XXX\nXX                         XXX\nXX                         XXX\nXX                         XXX\nXX        XXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXX                  XXX\nXXX                        XXX\nXXX                        XXX\nXXX                        XXX\nXXX                        XXX\nXXX                        XXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXX                       XXXX\nXXX                       XXXX\nXXX                        XXX\nXXX                        XXX\nXXX                        XXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXX                       XXXX\nXXX                       XXXX\nXXX                       XXXX\nXXX                       XXXX\nXXX      XXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXX            XXXX\nXXXX                      XXXX\nXXXX                      XXXX\nXXXX                      XXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXX                     XXXXX\nXXXX                     XXXXX\nXXXX                XXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXX                  XXXXX\nXXXXX                    XXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXX                  XXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n']

MOVES_INFO = {
 "pound": {
  "type": "normal",
  "power": 40,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "karate-chop": {
  "type": "fighting",
  "power": 50,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "double-slap": {
  "type": "normal",
  "power": 15,
  "pp": 10,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "comet-punch": {
  "type": "normal",
  "power": 18,
  "pp": 15,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "mega-punch": {
  "type": "normal",
  "power": 80,
  "pp": 20,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "pay-day": {
  "type": "normal",
  "power": 40,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "fire-punch": {
  "type": "fire",
  "power": 75,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "ice-punch": {
  "type": "ice",
  "power": 75,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "thunder-punch": {
  "type": "electric",
  "power": 75,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "scratch": {
  "type": "normal",
  "power": 40,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "vice-grip": {
  "type": "normal",
  "power": 55,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "guillotine": {
  "type": "normal",
  "power": None,
  "pp": 5,
  "accuracy": 30,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "razor-wind": {
  "type": "normal",
  "power": 80,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "swords-dance": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": 2,
   "defense": None
  },
 },
 "cut": {
  "type": "normal",
  "power": 50,
  "pp": 30,
  "accuracy": 95,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "gust": {
  "type": "flying",
  "power": 40,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "wing-attack": {
  "type": "flying",
  "power": 60,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "whirlwind": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "fly": {
  "type": "flying",
  "power": 90,
  "pp": 15,
  "accuracy": 95,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "bind": {
  "type": "normal",
  "power": 15,
  "pp": 20,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "slam": {
  "type": "normal",
  "power": 80,
  "pp": 20,
  "accuracy": 75,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "vine-whip": {
  "type": "grass",
  "power": 45,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "stomp": {
  "type": "normal",
  "power": 65,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "double-kick": {
  "type": "fighting",
  "power": 30,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "mega-kick": {
  "type": "normal",
  "power": 120,
  "pp": 5,
  "accuracy": 75,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "jump-kick": {
  "type": "fighting",
  "power": 100,
  "pp": 10,
  "accuracy": 95,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "rolling-kick": {
  "type": "fighting",
  "power": 60,
  "pp": 15,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "sand-attack": {
  "type": "ground",
  "power": None,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "headbutt": {
  "type": "normal",
  "power": 70,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "horn-attack": {
  "type": "normal",
  "power": 65,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "fury-attack": {
  "type": "normal",
  "power": 15,
  "pp": 20,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "horn-drill": {
  "type": "normal",
  "power": None,
  "pp": 5,
  "accuracy": 30,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "tackle": {
  "type": "normal",
  "power": 40,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "body-slam": {
  "type": "normal",
  "power": 85,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "wrap": {
  "type": "normal",
  "power": 15,
  "pp": 20,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "take-down": {
  "type": "normal",
  "power": 90,
  "pp": 20,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "thrash": {
  "type": "normal",
  "power": 120,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "double-edge": {
  "type": "normal",
  "power": 120,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "tail-whip": {
  "type": "normal",
  "power": None,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": -1
  },
 },
 "poison-sting": {
  "type": "poison",
  "power": 15,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "twineedle": {
  "type": "bug",
  "power": 25,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "pin-missile": {
  "type": "bug",
  "power": 25,
  "pp": 20,
  "accuracy": 95,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "leer": {
  "type": "normal",
  "power": None,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": -1
  },
 },
 "bite": {
  "type": "dark",
  "power": 60,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "growl": {
  "type": "normal",
  "power": None,
  "pp": 40,
  "accuracy": 100,
  "buffs": {
   "attack": -1,
   "defense": None
  },
 },
 "roar": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "sing": {
  "type": "normal",
  "power": None,
  "pp": 15,
  "accuracy": 55,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "supersonic": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": 55,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "sonic-boom": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "disable": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "acid": {
  "type": "poison",
  "power": 40,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "ember": {
  "type": "fire",
  "power": 40,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "flamethrower": {
  "type": "fire",
  "power": 90,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "mist": {
  "type": "ice",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "water-gun": {
  "type": "water",
  "power": 40,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "hydro-pump": {
  "type": "water",
  "power": 110,
  "pp": 5,
  "accuracy": 80,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "surf": {
  "type": "water",
  "power": 90,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "ice-beam": {
  "type": "ice",
  "power": 90,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "blizzard": {
  "type": "ice",
  "power": 110,
  "pp": 5,
  "accuracy": 70,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "psybeam": {
  "type": "psychic",
  "power": 65,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "bubble-beam": {
  "type": "water",
  "power": 65,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "aurora-beam": {
  "type": "ice",
  "power": 65,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": -1,
   "defense": None
  },
 },
 "hyper-beam": {
  "type": "normal",
  "power": 150,
  "pp": 5,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "peck": {
  "type": "flying",
  "power": 35,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "drill-peck": {
  "type": "flying",
  "power": 80,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "submission": {
  "type": "fighting",
  "power": 80,
  "pp": 20,
  "accuracy": 80,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "low-kick": {
  "type": "fighting",
  "power": None,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "counter": {
  "type": "fighting",
  "power": None,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "seismic-toss": {
  "type": "fighting",
  "power": None,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "strength": {
  "type": "normal",
  "power": 80,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "absorb": {
  "type": "grass",
  "power": 20,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "mega-drain": {
  "type": "grass",
  "power": 40,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "leech-seed": {
  "type": "grass",
  "power": 40,
  "pp": 10,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "growth": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": 1,
   "defense": None
  },
 },
 "razor-leaf": {
  "type": "grass",
  "power": 55,
  "pp": 25,
  "accuracy": 95,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "solar-beam": {
  "type": "grass",
  "power": 120,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "poison-powder": {
  "type": "poison",
  "power": None,
  "pp": 35,
  "accuracy": 75,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "stun-spore": {
  "type": "grass",
  "power": None,
  "pp": 30,
  "accuracy": 75,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "sleep-powder": {
  "type": "grass",
  "power": None,
  "pp": 15,
  "accuracy": 75,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "petal-dance": {
  "type": "grass",
  "power": 120,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "string-shot": {
  "type": "bug",
  "power": None,
  "pp": 40,
  "accuracy": 95,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "dragon-rage": {
  "type": "dragon",
  "power": None,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "fire-spin": {
  "type": "fire",
  "power": 35,
  "pp": 15,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "thunder-shock": {
  "type": "electric",
  "power": 40,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "thunderbolt": {
  "type": "electric",
  "power": 90,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "thunder-wave": {
  "type": "electric",
  "power": None,
  "pp": 20,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "thunder": {
  "type": "electric",
  "power": 110,
  "pp": 10,
  "accuracy": 70,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "rock-throw": {
  "type": "rock",
  "power": 50,
  "pp": 15,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "earthquake": {
  "type": "ground",
  "power": 100,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "fissure": {
  "type": "ground",
  "power": None,
  "pp": 5,
  "accuracy": 30,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "dig": {
  "type": "ground",
  "power": 80,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "toxic": {
  "type": "poison",
  "power": None,
  "pp": 10,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "confusion": {
  "type": "psychic",
  "power": 50,
  "pp": 25,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "psychic": {
  "type": "psychic",
  "power": 90,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "hypnosis": {
  "type": "psychic",
  "power": None,
  "pp": 20,
  "accuracy": 60,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "meditate": {
  "type": "psychic",
  "power": None,
  "pp": 40,
  "accuracy": None,
  "buffs": {
   "attack": 1,
   "defense": None
  },
 },
 "agility": {
  "type": "psychic",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "quick-attack": {
  "type": "normal",
  "power": 40,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "rage": {
  "type": "normal",
  "power": 20,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "teleport": {
  "type": "psychic",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "night-shade": {
  "type": "ghost",
  "power": None,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "mimic": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "screech": {
  "type": "normal",
  "power": None,
  "pp": 40,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": -2
  },
 },
 "double-team": {
  "type": "normal",
  "power": None,
  "pp": 15,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "recover": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "harden": {
  "type": "normal",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": 1
  },
 },
 "minimize": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "smokescreen": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "confuse-ray": {
  "type": "ghost",
  "power": None,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "withdraw": {
  "type": "water",
  "power": None,
  "pp": 40,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": 1
  },
 },
 "defense-curl": {
  "type": "normal",
  "power": None,
  "pp": 40,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": 1
  },
 },
 "barrier": {
  "type": "psychic",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": 2
  },
 },
 "light-screen": {
  "type": "psychic",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "haze": {
  "type": "ice",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "reflect": {
  "type": "psychic",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "focus-energy": {
  "type": "normal",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "bide": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "metronome": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "mirror-move": {
  "type": "flying",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "self-destruct": {
  "type": "normal",
  "power": 200,
  "pp": 5,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "egg-bomb": {
  "type": "normal",
  "power": 100,
  "pp": 10,
  "accuracy": 75,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "lick": {
  "type": "ghost",
  "power": 30,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "smog": {
  "type": "poison",
  "power": 30,
  "pp": 20,
  "accuracy": 70,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "sludge": {
  "type": "poison",
  "power": 65,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "bone-club": {
  "type": "ground",
  "power": 65,
  "pp": 20,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "fire-blast": {
  "type": "fire",
  "power": 110,
  "pp": 5,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "waterfall": {
  "type": "water",
  "power": 80,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "clamp": {
  "type": "water",
  "power": 35,
  "pp": 15,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "swift": {
  "type": "normal",
  "power": 60,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "skull-bash": {
  "type": "normal",
  "power": 130,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "spike-cannon": {
  "type": "normal",
  "power": 20,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "constrict": {
  "type": "normal",
  "power": 10,
  "pp": 35,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "amnesia": {
  "type": "psychic",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "kinesis": {
  "type": "psychic",
  "power": None,
  "pp": 15,
  "accuracy": 80,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "soft-boiled": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "high-jump-kick": {
  "type": "fighting",
  "power": 130,
  "pp": 10,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "glare": {
  "type": "normal",
  "power": None,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "dream-eater": {
  "type": "psychic",
  "power": 100,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "poison-gas": {
  "type": "poison",
  "power": None,
  "pp": 40,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "barrage": {
  "type": "normal",
  "power": 15,
  "pp": 20,
  "accuracy": 85,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "leech-life": {
  "type": "bug",
  "power": 80,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "lovely-kiss": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": 75,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "sky-attack": {
  "type": "flying",
  "power": 140,
  "pp": 5,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "transform": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "bubble": {
  "type": "water",
  "power": 40,
  "pp": 30,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "dizzy-punch": {
  "type": "normal",
  "power": 70,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "spore": {
  "type": "grass",
  "power": None,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "flash": {
  "type": "normal",
  "power": None,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "psywave": {
  "type": "psychic",
  "power": None,
  "pp": 15,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "splash": {
  "type": "normal",
  "power": None,
  "pp": 40,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "acid-armor": {
  "type": "poison",
  "power": None,
  "pp": 20,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": 2
  },
 },
 "crabhammer": {
  "type": "water",
  "power": 100,
  "pp": 10,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "explosion": {
  "type": "normal",
  "power": 250,
  "pp": 5,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "fury-swipes": {
  "type": "normal",
  "power": 18,
  "pp": 15,
  "accuracy": 80,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "bonemerang": {
  "type": "ground",
  "power": 50,
  "pp": 10,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "rest": {
  "type": "psychic",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "rock-slide": {
  "type": "rock",
  "power": 75,
  "pp": 10,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "hyper-fang": {
  "type": "normal",
  "power": 80,
  "pp": 15,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "sharpen": {
  "type": "normal",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": 1,
   "defense": None
  },
 },
 "conversion": {
  "type": "normal",
  "power": None,
  "pp": 30,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "tri-attack": {
  "type": "normal",
  "power": 80,
  "pp": 10,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "super-fang": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": 90,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "slash": {
  "type": "normal",
  "power": 70,
  "pp": 20,
  "accuracy": 100,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "substitute": {
  "type": "normal",
  "power": None,
  "pp": 10,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "struggle": {
  "type": "normal",
  "power": 50,
  "pp": 1,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 },
 "poop-throw": {
  "type": "ground",
  "power": 60,
  "pp": 1,
  "accuracy": None,
  "buffs": {
   "attack": None,
   "defense": None
  },
 }
}

POKEMON_INFO = {
 "bulbasaur": {
  "evolution_chain": [("bulbasaur", 16, "ivysaur"),
                      ("ivysaur", 32, "venusaur")],
  "starting_moves": ["tackle", "growl", "leech-seed"],
  "learned_moves": [
   ("vine-whip", 13),
   ("leech-seed", 7),
   ("growth", 34),
   ("razor-leaf", 27),
   ("solar-beam", 48),
   ("poison-powder", 20),
   ("sleep-powder", 41),
  ],
  "types": ["grass", "poison"],
  "base_health":
  45,
  "catch_rate":
  45,
 },
 "ivysaur": {
  "evolution_chain": [("bulbasaur", 16, "ivysaur"),
                      ("ivysaur", 32, "venusaur")],
  "starting_moves": ["tackle", "growl", "leech-seed"],
  "learned_moves": [
   ("vine-whip", 13),
   ("growth", 38),
   ("razor-leaf", 30),
   ("solar-beam", 54),
   ("poison-powder", 22),
   ("sleep-powder", 46),
  ],
  "types": ["grass", "poison"],
  "base_health":
  60,
  "catch_rate":
  45,
 },
 "venusaur": {
  "evolution_chain": [("bulbasaur", 16, "ivysaur"),
                      ("ivysaur", 32, "venusaur")],
  "starting_moves": ["vine-whip", "tackle", "growl", "leech-seed", "amnesia"],
  "learned_moves": [
   ("growth", 43),
   ("razor-leaf", 30),
   ("solar-beam", 65),
   ("poison-powder", 22),
   ("sleep-powder", 55),
   ("petal-dance", 32),
  ],
  "types": ["grass", "poison"],
  "base_health":
  80,
  "catch_rate":
  45,
 },
 "charmander": {
  "evolution_chain": [
   ("charmander", 16, "charmeleon"),
   ("charmeleon", 36, "charizard"),
  ],
  "starting_moves": ["scratch", "growl", "ember"],
  "learned_moves": [
   ("leer", 15),
   ("ember", 9),
   ("flamethrower", 38),
   ("fire-spin", 46),
   ("rage", 22),
   ("smokescreen", 13),
   ("fury-swipes", 18),
   ("slash", 30),
  ],
  "types": ["fire"],
  "base_health":
  39,
  "catch_rate":
  45,
 },
 "charmeleon": {
  "evolution_chain": [
   ("charmander", 16, "charmeleon"),
   ("charmeleon", 36, "charizard"),
  ],
  "starting_moves": ["scratch", "growl", "ember"],
  "learned_moves": [
   ("leer", 15),
   ("flamethrower", 42),
   ("fire-spin", 56),
   ("rage", 24),
   ("smokescreen", 13),
   ("fury-swipes", 20),
   ("slash", 33),
  ],
  "types": ["fire"],
  "base_health":
  58,
  "catch_rate":
  45,
 },
 "charizard": {
  "evolution_chain": [
   ("charmander", 16, "charmeleon"),
   ("charmeleon", 36, "charizard"),
  ],
  "starting_moves": ["scratch", "leer", "growl", "ember", "smokescreen"],
  "learned_moves": [
   ("wing-attack", 36),
   ("flamethrower", 46),
   ("fire-spin", 55),
   ("rage", 24),
   ("fury-swipes", 20),
   ("slash", 36),
  ],
  "types": ["fire", "flying"],
  "base_health":
  78,
  "catch_rate":
  45,
 },
 "squirtle": {
  "evolution_chain": [
   ("squirtle", 16, "wartortle"),
   ("wartortle", 36, "blastoise"),
  ],
  "starting_moves": ["tackle", "tail-whip", "bubble"],
  "learned_moves": [
   ("bite", 22),
   ("water-gun", 15),
   ("hydro-pump", 42),
   ("withdraw", 28),
   ("skull-bash", 35),
   ("bubble", 8),
  ],
  "types": ["water"],
  "base_health":
  44,
  "catch_rate":
  45,
 },
 "wartortle": {
  "evolution_chain": [
   ("squirtle", 16, "wartortle"),
   ("wartortle", 36, "blastoise"),
  ],
  "starting_moves": ["tackle", "tail-whip", "bubble"],
  "learned_moves": [
   ("bite", 24),
   ("water-gun", 15),
   ("hydro-pump", 47),
   ("withdraw", 31),
   ("skull-bash", 39),
  ],
  "types": ["water"],
  "base_health":
  59,
  "catch_rate":
  45,
 },
 "blastoise": {
  "evolution_chain": [
   ("squirtle", 16, "wartortle"),
   ("wartortle", 36, "blastoise"),
  ],
  "starting_moves": ["tackle", "tail-whip", "water-gun", "bubble"],
  "learned_moves": [
   ("bite", 24),
   ("hydro-pump", 52),
   ("withdraw", 31),
   ("skull-bash", 42),
  ],
  "types": ["water"],
  "base_health":
  79,
  "catch_rate":
  45,
 },
 "caterpie": {
  "evolution_chain": [("caterpie", 7, "metapod"),
                      ("metapod", 10, "butterfree")],
  "starting_moves": ["tackle", "string-shot"],
  "learned_moves": [],
  "types": ["bug"],
  "base_health": 45,
  "catch_rate": 255,
 },
 "metapod": {
  "evolution_chain": [("caterpie", 7, "metapod"),
                      ("metapod", 10, "butterfree")],
  "starting_moves": ["harden"],
  "learned_moves": [],
  "types": ["bug"],
  "base_health": 50,
  "catch_rate": 120,
 },
 "butterfree": {
  "evolution_chain": [("caterpie", 7, "metapod"),
                      ("metapod", 10, "butterfree")],
  "starting_moves": ["tackle", "confusion", "harden"],
  "learned_moves": [
   ("gust", 28),
   ("whirlwind", 26),
   ("supersonic", 21),
   ("psybeam", 32),
   ("poison-powder", 15),
   ("stun-spore", 16),
   ("sleep-powder", 17),
  ],
  "types": ["bug", "flying"],
  "base_health":
  60,
  "catch_rate":
  45,
 },
 "weedle": {
  "evolution_chain": [("weedle", 7, "kakuna"), ("kakuna", 10, "beedrill")],
  "starting_moves": ["poison-sting", "string-shot"],
  "learned_moves": [],
  "types": ["bug", "poison"],
  "base_health": 40,
  "catch_rate": 255,
 },
 "kakuna": {
  "evolution_chain": [("weedle", 7, "kakuna"), ("kakuna", 10, "beedrill")],
  "starting_moves": ["harden"],
  "learned_moves": [],
  "types": ["bug", "poison"],
  "base_health": 45,
  "catch_rate": 120,
 },
 "beedrill": {
  "evolution_chain": [("weedle", 7, "kakuna"), ("kakuna", 10, "beedrill")],
  "starting_moves": ["fury-attack", "peck"],
  "learned_moves": [
   ("twineedle", 20),
   ("pin-missile", 30),
   ("agility", 35),
   ("rage", 25),
   ("focus-energy", 16),
  ],
  "types": ["bug", "poison"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "pidgey": {
  "evolution_chain": [("pidgey", 18, "pidgeotto"),
                      ("pidgeotto", 36, "pidgeot")],
  "starting_moves": ["gust", "tackle"],
  "learned_moves": [
   ("wing-attack", 28),
   ("whirlwind", 19),
   ("sand-attack", 5),
   ("agility", 36),
   ("quick-attack", 12),
   ("mirror-move", 44),
  ],
  "types": ["normal", "flying"],
  "base_health":
  40,
  "catch_rate":
  255,
 },
 "pidgeotto": {
  "evolution_chain": [("pidgey", 18, "pidgeotto"),
                      ("pidgeotto", 36, "pidgeot")],
  "starting_moves": ["gust", "sand-attack", "tackle"],
  "learned_moves": [
   ("wing-attack", 31),
   ("whirlwind", 21),
   ("agility", 40),
   ("quick-attack", 12),
   ("mirror-move", 49),
  ],
  "types": ["normal", "flying"],
  "base_health":
  63,
  "catch_rate":
  120,
 },
 "pidgeot": {
  "evolution_chain": [("pidgey", 18, "pidgeotto"),
                      ("pidgeotto", 36, "pidgeot")],
  "starting_moves": ["gust", "sand-attack", "tackle", "quick-attack"],
  "learned_moves": [
   ("wing-attack", 31),
   ("whirlwind", 21),
   ("agility", 44),
   ("mirror-move", 54),
  ],
  "types": ["normal", "flying"],
  "base_health":
  83,
  "catch_rate":
  45,
 },
 "rattata": {
  "evolution_chain": [("rattata", 20, "raticate"),
                      ("rattata", 20, "raticate")],
  "starting_moves": ["tackle", "tail-whip"],
  "learned_moves": [
   ("quick-attack", 7),
   ("focus-energy", 23),
   ("hyper-fang", 14),
   ("super-fang", 34),
  ],
  "types": ["normal"],
  "base_health":
  30,
  "catch_rate":
  255,
 },
 "raticate": {
  "evolution_chain": [("rattata", 20, "raticate"),
                      ("rattata", 20, "raticate")],
  "starting_moves": [
   "swords-dance",
   "tackle",
   "tail-whip",
   "quick-attack",
   "fury-swipes",
  ],
  "learned_moves": [
   ("bite", 10),
   ("focus-energy", 27),
   ("hyper-fang", 14),
   ("super-fang", 41),
  ],
  "types": ["normal"],
  "base_health":
  55,
  "catch_rate":
  127,
 },
 "spearow": {
  "evolution_chain": [("spearow", 20, "fearow")],
  "starting_moves": ["growl", "peck"],
  "learned_moves": [
   ("fury-attack", 15),
   ("leer", 9),
   ("drill-peck", 29),
   ("agility", 36),
   ("focus-energy", 29),
   ("mirror-move", 22),
  ],
  "types": ["normal", "flying"],
  "base_health":
  40,
  "catch_rate":
  255,
 },
 "fearow": {
  "evolution_chain": [("spearow", 20, "fearow")],
  "starting_moves": ["leer", "growl", "peck", "quick-attack"],
  "learned_moves": [
   ("fury-attack", 15),
   ("drill-peck", 34),
   ("agility", 43),
   ("focus-energy", 32),
   ("mirror-move", 25),
  ],
  "types": ["normal", "flying"],
  "base_health":
  65,
  "catch_rate":
  90,
 },
 "ekans": {
  "evolution_chain": [("ekans", 22, "arbok")],
  "starting_moves": ["wrap", "leer"],
  "learned_moves": [
   ("poison-sting", 10),
   ("bite", 17),
   ("acid", 38),
   ("screech", 31),
   ("haze", 43),
   ("glare", 24),
  ],
  "types": ["poison"],
  "base_health":
  35,
  "catch_rate":
  255,
 },
 "arbok": {
  "evolution_chain": [("ekans", 22, "arbok")],
  "starting_moves": ["wrap", "poison-sting", "leer"],
  "learned_moves": [
   ("slam", 36),
   ("bite", 17),
   ("acid", 47),
   ("screech", 36),
   ("haze", 51),
   ("glare", 27),
  ],
  "types": ["poison"],
  "base_health":
  60,
  "catch_rate":
  90,
 },
 "pikachu": {
  "evolution_chain": [("pichu", None, "pikachu")],
  "starting_moves": ["growl", "thunder-shock"],
  "learned_moves": [
   ("slam", 20),
   ("double-kick", 9),
   ("tail-whip", 6),
   ("thunder-wave", 9),
   ("thunder", 43),
   ("agility", 33),
   ("quick-attack", 16),
   ("light-screen", 50),
   ("swift", 26),
  ],
  "types": ["electric"],
  "base_health":
  35,
  "catch_rate":
  190,
 },
 "raichu": {
  "evolution_chain": [("pichu", None, "pikachu")],
  "starting_moves": [
   "slam",
   "tail-whip",
   "growl",
   "thunder-shock",
   "thunder-wave",
   "agility",
   "quick-attack",
  ],
  "learned_moves": [],
  "types": ["electric"],
  "base_health":
  60,
  "catch_rate":
  75,
 },
 "sandshrew": {
  "evolution_chain": [("sandshrew", 22, "sandslash")],
  "starting_moves": ["scratch"],
  "learned_moves": [
   ("sand-attack", 10),
   ("poison-sting", 24),
   ("agility", 27),
   ("defense-curl", 6),
   ("swift", 31),
   ("fury-swipes", 38),
   ("slash", 17),
  ],
  "types": ["ground"],
  "base_health":
  50,
  "catch_rate":
  255,
 },
 "sandslash": {
  "evolution_chain": [("sandshrew", 22, "sandslash")],
  "starting_moves": ["scratch", "sand-attack", "defense-curl"],
  "learned_moves": [
   ("poison-sting", 27),
   ("swift", 36),
   ("fury-swipes", 47),
   ("slash", 17),
  ],
  "types": ["ground"],
  "base_health":
  75,
  "catch_rate":
  90,
 },
 "nidoran-f": {
  "evolution_chain": [("nidoran-f", 16, "nidorina")],
  "starting_moves": ["tackle", "growl"],
  "learned_moves": [
   ("scratch", 8),
   ("double-kick", 43),
   ("tail-whip", 21),
   ("poison-sting", 14),
   ("bite", 29),
   ("fury-swipes", 36),
  ],
  "types": ["poison"],
  "base_health":
  55,
  "catch_rate":
  235,
 },
 "nidorina": {
  "evolution_chain": [("nidoran-f", 16, "nidorina")],
  "starting_moves": ["scratch", "tackle", "growl"],
  "learned_moves": [
   ("double-kick", 50),
   ("tail-whip", 23),
   ("poison-sting", 14),
   ("bite", 32),
   ("fury-swipes", 41),
  ],
  "types": ["poison"],
  "base_health":
  70,
  "catch_rate":
  120,
 },
 "nidoqueen": {
  "evolution_chain": [("nidoran-f", 16, "nidorina")],
  "starting_moves": [
   "scratch",
   "tackle",
   "body-slam",
   "tail-whip",
   "bite",
   "growl",
   "supersonic",
   "fury-swipes",
  ],
  "learned_moves": [("double-kick", 12), ("poison-sting", 14)],
  "types": ["poison", "ground"],
  "base_health":
  90,
  "catch_rate":
  45,
 },
 "nidoran-m": {
  "evolution_chain": [("nidoran-m", 16, "nidorino")],
  "starting_moves": ["tackle", "leer", "peck"],
  "learned_moves": [
   ("double-kick", 43),
   ("horn-attack", 8),
   ("fury-attack", 29),
   ("horn-drill", 36),
   ("poison-sting", 14),
   ("focus-energy", 21),
  ],
  "types": ["poison"],
  "base_health":
  46,
  "catch_rate":
  235,
 },
 "nidorino": {
  "evolution_chain": [("nidoran-m", 16, "nidorino")],
  "starting_moves": ["horn-attack", "tackle", "leer", "peck"],
  "learned_moves": [
   ("double-kick", 50),
   ("fury-attack", 32),
   ("horn-drill", 41),
   ("poison-sting", 14),
   ("focus-energy", 23),
  ],
  "types": ["poison"],
  "base_health":
  61,
  "catch_rate":
  120,
 },
 "nidoking": {
  "evolution_chain": [("nidoran-m", 16, "nidorino")],
  "starting_moves": [
   "horn-attack",
   "fury-attack",
   "tackle",
   "thrash",
   "poison-sting",
   "leer",
   "supersonic",
   "peck",
   "focus-energy",
  ],
  "learned_moves": [("double-kick", 12)],
  "types": ["poison", "ground"],
  "base_health":
  81,
  "catch_rate":
  45,
 },
 "clefairy": {
  "evolution_chain": [("cleffa", None, "clefairy")],
  "starting_moves": ["pound", "growl", "splash"],
  "learned_moves": [
   ("double-slap", 18),
   ("sing", 13),
   ("minimize", 24),
   ("defense-curl", 39),
   ("light-screen", 48),
   ("metronome", 31),
   ("amnesia", 16),
  ],
  "types": ["fairy"],
  "base_health":
  70,
  "catch_rate":
  150,
 },
 "clefable": {
  "evolution_chain": [("cleffa", None, "clefairy")],
  "starting_moves": [
   "pound",
   "double-slap",
   "growl",
   "sing",
   "minimize",
   "metronome",
   "splash",
  ],
  "learned_moves": [],
  "types": ["fairy"],
  "base_health":
  95,
  "catch_rate":
  25,
 },
 "vulpix": {
  "evolution_chain": [],
  "starting_moves": ["tackle", "tail-whip", "ember"],
  "learned_moves": [
   ("roar", 21),
   ("flamethrower", 35),
   ("fire-spin", 42),
   ("quick-attack", 16),
   ("confuse-ray", 28),
  ],
  "types": ["fire"],
  "base_health":
  38,
  "catch_rate":
  190,
 },
 "ninetales": {
  "evolution_chain": [],
  "starting_moves": [
   "tackle",
   "tail-whip",
   "roar",
   "disable",
   "ember",
   "hypnosis",
   "quick-attack",
   "confuse-ray",
  ],
  "learned_moves": [("fire-spin", 43)],
  "types": ["fire"],
  "base_health":
  73,
  "catch_rate":
  75,
 },
 "jigglypuff": {
  "evolution_chain": [("igglybuff", None, "jigglypuff")],
  "starting_moves": ["sing", "pound"],
  "learned_moves": [
   ("pound", 9),
   ("double-slap", 24),
   ("body-slam", 34),
   ("double-edge", 39),
   ("disable", 14),
   ("defense-curl", 19),
   ("rest", 29),
  ],
  "types": ["normal", "fairy"],
  "base_health":
  115,
  "catch_rate":
  170,
 },
 "wigglytuff": {
  "evolution_chain": [("igglybuff", None, "jigglypuff")],
  "starting_moves": [
   "pound",
   "double-slap",
   "sing",
   "disable",
   "minimize",
   "defense-curl",
   "pound",
  ],
  "learned_moves": [],
  "types": ["normal", "fairy"],
  "base_health":
  140,
  "catch_rate":
  50,
 },
 "zubat": {
  "evolution_chain": [("zubat", 22, "golbat"), ("golbat", None, "crobat")],
  "starting_moves": ["absorb", "leech-life"],
  "learned_moves": [
   ("wing-attack", 28),
   ("bite", 15),
   ("supersonic", 10),
   ("confuse-ray", 21),
   ("haze", 36),
  ],
  "types": ["poison", "flying"],
  "base_health":
  40,
  "catch_rate":
  255,
 },
 "golbat": {
  "evolution_chain": [("zubat", 22, "golbat"), ("golbat", None, "crobat")],
  "starting_moves":
  ["bite", "absorb", "quick-attack", "screech", "leech-life"],
  "learned_moves": [
   ("wing-attack", 32),
   ("supersonic", 10),
   ("confuse-ray", 21),
   ("haze", 43),
  ],
  "types": ["poison", "flying"],
  "base_health":
  75,
  "catch_rate":
  90,
 },
 "oddish": {
  "evolution_chain": [("oddish", 21, "gloom")],
  "starting_moves": ["absorb", "growth"],
  "learned_moves": [
   ("acid", 24),
   ("solar-beam", 46),
   ("poison-powder", 15),
   ("stun-spore", 17),
   ("sleep-powder", 19),
   ("petal-dance", 33),
  ],
  "types": ["grass", "poison"],
  "base_health":
  45,
  "catch_rate":
  255,
 },
 "gloom": {
  "evolution_chain": [("oddish", 21, "gloom")],
  "starting_moves": ["absorb", "growth", "poison-powder", "stun-spore"],
  "learned_moves": [
   ("acid", 28),
   ("razor-leaf", 18),
   ("solar-beam", 52),
   ("sleep-powder", 19),
   ("petal-dance", 38),
  ],
  "types": ["grass", "poison"],
  "base_health":
  60,
  "catch_rate":
  120,
 },
 "vileplume": {
  "evolution_chain": [("oddish", 21, "gloom")],
  "starting_moves": [
   "acid",
   "absorb",
   "growth",
   "stun-spore",
   "sleep-powder",
   "petal-dance",
  ],
  "learned_moves": [("poison-powder", 15)],
  "types": ["grass", "poison"],
  "base_health":
  75,
  "catch_rate":
  45,
 },
 "paras": {
  "evolution_chain": [("paras", 24, "parasect")],
  "starting_moves": ["scratch"],
  "learned_moves": [
   ("absorb", 11),
   ("growth", 41),
   ("poison-powder", 13),
   ("stun-spore", 13),
   ("sleep-powder", 2),
   ("leech-life", 20),
   ("spore", 27),
   ("fury-swipes", 15),
   ("slash", 34),
  ],
  "types": ["bug", "grass"],
  "base_health":
  35,
  "catch_rate":
  190,
 },
 "parasect": {
  "evolution_chain": [("paras", 24, "parasect")],
  "starting_moves": [
   "scratch",
   "absorb",
   "leech-seed",
   "poison-powder",
   "stun-spore",
   "sleep-powder",
   "screech",
   "leech-life",
  ],
  "learned_moves": [
   ("growth", 48),
   ("spore", 30),
   ("fury-swipes", 15),
   ("slash", 39),
  ],
  "types": ["bug", "grass"],
  "base_health":
  60,
  "catch_rate":
  75,
 },
 "venonat": {
  "evolution_chain": [("venonat", 31, "venomoth")],
  "starting_moves": ["tackle", "disable"],
  "learned_moves": [
   ("supersonic", 11),
   ("psybeam", 35),
   ("poison-powder", 24),
   ("stun-spore", 30),
   ("sleep-powder", 38),
   ("confusion", 19),
   ("psychic", 43),
   ("leech-life", 27),
  ],
  "types": ["bug", "poison"],
  "base_health":
  60,
  "catch_rate":
  190,
 },
 "venomoth": {
  "evolution_chain": [("venonat", 31, "venomoth")],
  "starting_moves": [
   "tackle",
   "supersonic",
   "disable",
   "poison-powder",
   "confusion",
   "agility",
   "screech",
   "leech-life",
  ],
  "learned_moves": [
   ("gust", 31),
   ("psybeam", 38),
   ("stun-spore", 30),
   ("sleep-powder", 43),
   ("psychic", 50),
  ],
  "types": ["bug", "poison"],
  "base_health":
  70,
  "catch_rate":
  75,
 },
 "diglett": {
  "evolution_chain": [("diglett", 26, "dugtrio")],
  "starting_moves": ["scratch"],
  "learned_moves": [
   ("sand-attack", 24),
   ("growl", 15),
   ("earthquake", 40),
   ("dig", 19),
   ("agility", 12),
   ("fury-swipes", 21),
   ("slash", 31),
  ],
  "types": ["ground"],
  "base_health":
  10,
  "catch_rate":
  255,
 },
 "dugtrio": {
  "evolution_chain": [("diglett", 26, "dugtrio")],
  "starting_moves": [
   "scratch",
   "growl",
   "dig",
   "agility",
   "screech",
   "tri-attack",
  ],
  "learned_moves": [
   ("sand-attack", 24),
   ("earthquake", 47),
   ("fury-swipes", 21),
   ("slash", 35),
  ],
  "types": ["ground"],
  "base_health":
  35,
  "catch_rate":
  50,
 },
 "meowth": {
  "evolution_chain": [
   ("meowth", 28, "persian"),
   ("meowth", None, "persian"),
   ("meowth", 28, "perrserker"),
  ],
  "starting_moves": ["scratch", "growl"],
  "learned_moves": [
   ("pay-day", 17),
   ("bite", 12),
   ("screech", 24),
   ("fury-swipes", 33),
   ("slash", 44),
  ],
  "types": ["normal"],
  "base_health":
  40,
  "catch_rate":
  255,
 },
 "persian": {
  "evolution_chain": [
   ("meowth", 28, "persian"),
   ("meowth", None, "persian"),
   ("meowth", 28, "perrserker"),
  ],
  "starting_moves": [
   "scratch",
   "bite",
   "growl",
   "hypnosis",
   "screech",
   "amnesia",
  ],
  "learned_moves": [("pay-day", 17), ("fury-swipes", 37), ("slash", 51)],
  "types": ["normal"],
  "base_health":
  65,
  "catch_rate":
  90,
 },
 "psyduck": {
  "evolution_chain": [("psyduck", 33, "golduck")],
  "starting_moves": ["scratch"],
  "learned_moves": [
   ("tail-whip", 28),
   ("disable", 31),
   ("hydro-pump", 52),
   ("confusion", 36),
   ("screech", 23),
   ("amnesia", 44),
   ("fury-swipes", 43),
  ],
  "types": ["water"],
  "base_health":
  50,
  "catch_rate":
  190,
 },
 "golduck": {
  "evolution_chain": [("psyduck", 33, "golduck")],
  "starting_moves": ["scratch", "tail-whip", "disable"],
  "learned_moves": [
   ("hydro-pump", 59),
   ("psybeam", 27),
   ("confusion", 39),
   ("screech", 23),
   ("amnesia", 50),
   ("fury-swipes", 48),
  ],
  "types": ["water"],
  "base_health":
  80,
  "catch_rate":
  75,
 },
 "mankey": {
  "evolution_chain": [("mankey", 28, "primeape")],
  "starting_moves": ["scratch", "leer", "poop-throw"],
  "learned_moves": [
   ("karate-chop", 15),
   ("thrash", 39),
   ("low-kick", 9),
   ("seismic-toss", 33),
   ("screech", 45),
   ("focus-energy", 27),
   ("fury-swipes", 21),
  ],
  "types": ["fighting"],
  "base_health":
  40,
  "catch_rate":
  190,
 },
 "primeape": {
  "evolution_chain": [("mankey", 28, "primeape")],
  "starting_moves":
  ["karate-chop", "scratch", "poop-throw", "low-kick", "leer", "fury-swipes"],
  "learned_moves": [
   ("thrash", 46),
   ("seismic-toss", 37),
   ("screech", 45),
   ("focus-energy", 27),
  ],
  "types": ["fighting"],
  "base_health":
  65,
  "catch_rate":
  75,
 },
 "growlithe": {
  "evolution_chain": [],
  "starting_moves": ["bite", "roar"],
  "learned_moves": [
   ("take-down", 30),
   ("leer", 23),
   ("ember", 18),
   ("flamethrower", 50),
   ("agility", 39),
  ],
  "types": ["fire"],
  "base_health":
  55,
  "catch_rate":
  190,
 },
 "arcanine": {
  "evolution_chain": [],
  "starting_moves": ["take-down", "leer", "bite", "roar", "ember", "agility"],
  "learned_moves": [],
  "types": ["fire"],
  "base_health": 90,
  "catch_rate": 75,
 },
 "poliwag": {
  "evolution_chain": [("poliwag", 25, "poliwhirl")],
  "starting_moves": ["bubble"],
  "learned_moves": [
   ("pound", 4),
   ("double-slap", 25),
   ("body-slam", 31),
   ("water-gun", 19),
   ("hydro-pump", 45),
   ("low-kick", 26),
   ("hypnosis", 16),
   ("amnesia", 38),
  ],
  "types": ["water"],
  "base_health":
  40,
  "catch_rate":
  255,
 },
 "poliwhirl": {
  "evolution_chain": [("poliwag", 25, "poliwhirl")],
  "starting_moves": ["pound", "water-gun", "hypnosis", "bubble"],
  "learned_moves": [
   ("double-slap", 26),
   ("body-slam", 33),
   ("hydro-pump", 49),
   ("low-kick", 30),
   ("amnesia", 41),
  ],
  "types": ["water"],
  "base_health":
  65,
  "catch_rate":
  120,
 },
 "poliwrath": {
  "evolution_chain": [("poliwag", 25, "poliwhirl")],
  "starting_moves": [
   "pound",
   "double-slap",
   "body-slam",
   "mist",
   "water-gun",
   "hydro-pump",
   "hypnosis",
   "haze",
   "bubble",
  ],
  "learned_moves": [],
  "types": ["water", "fighting"],
  "base_health":
  90,
  "catch_rate":
  45,
 },
 "abra": {
  "evolution_chain": [("abra", 16, "kadabra")],
  "starting_moves": ["teleport"],
  "learned_moves": [],
  "types": ["psychic"],
  "base_health": 25,
  "catch_rate": 200,
 },
 "kadabra": {
  "evolution_chain": [("abra", 16, "kadabra")],
  "starting_moves": ["disable", "confusion", "teleport", "kinesis"],
  "learned_moves": [
   ("psybeam", 27),
   ("psychic", 38),
   ("night-shade", 19),
   ("recover", 31),
   ("reflect", 42),
  ],
  "types": ["psychic"],
  "base_health":
  40,
  "catch_rate":
  100,
 },
 "alakazam": {
  "evolution_chain": [("abra", 16, "kadabra")],
  "starting_moves": ["disable", "confusion", "teleport", "barrier", "kinesis"],
  "learned_moves": [
   ("psybeam", 27),
   ("psychic", 38),
   ("night-shade", 19),
   ("recover", 31),
   ("reflect", 42),
  ],
  "types": ["psychic"],
  "base_health":
  55,
  "catch_rate":
  50,
 },
 "machop": {
  "evolution_chain": [("machop", 28, "machoke")],
  "starting_moves": ["karate-chop"],
  "learned_moves": [
   ("leer", 25),
   ("submission", 46),
   ("low-kick", 20),
   ("seismic-toss", 39),
   ("focus-energy", 32),
  ],
  "types": ["fighting"],
  "base_health":
  70,
  "catch_rate":
  180,
 },
 "machoke": {
  "evolution_chain": [("machop", 28, "machoke")],
  "starting_moves": ["karate-chop", "leer", "low-kick"],
  "learned_moves": [
   ("submission", 52),
   ("seismic-toss", 44),
   ("focus-energy", 36),
  ],
  "types": ["fighting"],
  "base_health":
  80,
  "catch_rate":
  90,
 },
 "machamp": {
  "evolution_chain": [("machop", 28, "machoke")],
  "starting_moves": ["karate-chop", "leer", "low-kick"],
  "learned_moves": [
   ("submission", 52),
   ("seismic-toss", 44),
   ("focus-energy", 36),
  ],
  "types": ["fighting"],
  "base_health":
  90,
  "catch_rate":
  45,
 },
 "bellsprout": {
  "evolution_chain": [("bellsprout", 21, "weepinbell")],
  "starting_moves": ["vine-whip", "growth"],
  "learned_moves": [
   ("slam", 42),
   ("wrap", 13),
   ("acid", 26),
   ("razor-leaf", 33),
   ("poison-powder", 15),
   ("stun-spore", 21),
   ("sleep-powder", 18),
  ],
  "types": ["grass", "poison"],
  "base_health":
  50,
  "catch_rate":
  255,
 },
 "weepinbell": {
  "evolution_chain": [("bellsprout", 21, "weepinbell")],
  "starting_moves": ["vine-whip", "wrap", "growth"],
  "learned_moves": [
   ("slam", 49),
   ("acid", 29),
   ("razor-leaf", 38),
   ("poison-powder", 15),
   ("stun-spore", 23),
   ("sleep-powder", 18),
  ],
  "types": ["grass", "poison"],
  "base_health":
  65,
  "catch_rate":
  120,
 },
 "victreebel": {
  "evolution_chain": [("bellsprout", 21, "weepinbell")],
  "starting_moves": [
   "vine-whip",
   "acid",
   "growth",
   "razor-leaf",
   "stun-spore",
   "sleep-powder",
   "leech-life",
  ],
  "learned_moves": [("wrap", 13), ("poison-powder", 15)],
  "types": ["grass", "poison"],
  "base_health":
  80,
  "catch_rate":
  45,
 },
 "tentacool": {
  "evolution_chain": [("tentacool", 30, "tentacruel")],
  "starting_moves": ["acid"],
  "learned_moves": [
   ("wrap", 13),
   ("poison-sting", 18),
   ("supersonic", 7),
   ("water-gun", 22),
   ("hydro-pump", 48),
   ("screech", 40),
   ("barrier", 33),
   ("constrict", 27),
   ("acid-armor", 32),
  ],
  "types": ["water", "poison"],
  "base_health":
  40,
  "catch_rate":
  190,
 },
 "tentacruel": {
  "evolution_chain": [("tentacool", 30, "tentacruel")],
  "starting_moves": ["wrap", "supersonic", "acid", "haze"],
  "learned_moves": [
   ("poison-sting", 18),
   ("water-gun", 22),
   ("hydro-pump", 50),
   ("screech", 43),
   ("barrier", 35),
   ("constrict", 27),
   ("acid-armor", 34),
  ],
  "types": ["water", "poison"],
  "base_health":
  80,
  "catch_rate":
  60,
 },
 "geodude": {
  "evolution_chain": [("geodude", 25, "graveler")],
  "starting_moves": ["tackle"],
  "learned_moves": [
   ("sand-attack", 3),
   ("rock-throw", 16),
   ("earthquake", 31),
   ("harden", 26),
   ("defense-curl", 11),
   ("self-destruct", 21),
   ("explosion", 36),
  ],
  "types": ["rock", "ground"],
  "base_health":
  40,
  "catch_rate":
  255,
 },
 "graveler": {
  "evolution_chain": [("geodude", 25, "graveler")],
  "starting_moves": ["sand-attack", "tackle", "defense-curl"],
  "learned_moves": [
   ("rock-throw", 16),
   ("earthquake", 36),
   ("harden", 29),
   ("self-destruct", 21),
   ("explosion", 43),
  ],
  "types": ["rock", "ground"],
  "base_health":
  55,
  "catch_rate":
  120,
 },
 "golem": {
  "evolution_chain": [("geodude", 25, "graveler")],
  "starting_moves": ["sand-attack", "tackle", "defense-curl"],
  "learned_moves": [
   ("rock-throw", 16),
   ("earthquake", 36),
   ("harden", 29),
   ("self-destruct", 21),
   ("explosion", 43),
  ],
  "types": ["rock", "ground"],
  "base_health":
  80,
  "catch_rate":
  45,
 },
 "ponyta": {
  "evolution_chain": [("ponyta", 40, "rapidash")],
  "starting_moves": ["tackle", "ember"],
  "learned_moves": [
   ("stomp", 32),
   ("take-down", 43),
   ("tail-whip", 30),
   ("growl", 35),
   ("fire-spin", 39),
   ("agility", 48),
  ],
  "types": ["fire"],
  "base_health":
  50,
  "catch_rate":
  190,
 },
 "rapidash": {
  "evolution_chain": [("ponyta", 40, "rapidash")],
  "starting_moves": [
   "stomp",
   "tackle",
   "tail-whip",
   "growl",
   "ember",
   "hypnosis",
   "quick-attack",
  ],
  "learned_moves": [
   ("double-kick", 15),
   ("fury-attack", 40),
   ("take-down", 47),
   ("fire-spin", 39),
   ("agility", 55),
  ],
  "types": ["fire"],
  "base_health":
  65,
  "catch_rate":
  60,
 },
 "slowpoke": {
  "evolution_chain": [("slowpoke", 37, "slowbro")],
  "starting_moves": ["tackle", "confusion"],
  "learned_moves": [
   ("headbutt", 22),
   ("growl", 27),
   ("disable", 18),
   ("water-gun", 33),
   ("psychic", 48),
   ("amnesia", 40),
  ],
  "types": ["water", "psychic"],
  "base_health":
  90,
  "catch_rate":
  190,
 },
 "slowbro": {
  "evolution_chain": [("slowpoke", 37, "slowbro")],
  "starting_moves": ["stomp", "headbutt", "tackle", "disable", "confusion"],
  "learned_moves": [
   ("growl", 27),
   ("water-gun", 33),
   ("psychic", 55),
   ("withdraw", 37),
   ("amnesia", 44),
  ],
  "types": ["water", "psychic"],
  "base_health":
  95,
  "catch_rate":
  75,
 },
 "magnemite": {
  "evolution_chain": [
   ("magnemite", 30, "magneton"),
   ("magneton", None, "magnezone"),
   ("magneton", None, "magnezone"),
   ("magneton", None, "magnezone"),
   ("magneton", None, "magnezone"),
  ],
  "starting_moves": ["tackle"],
  "learned_moves": [
   ("supersonic", 29),
   ("sonic-boom", 21),
   ("thunder-shock", 25),
   ("thunder-wave", 35),
   ("screech", 47),
   ("swift", 41),
  ],
  "types": ["electric", "steel"],
  "base_health":
  25,
  "catch_rate":
  190,
 },
 "magneton": {
  "evolution_chain": [
   ("magnemite", 30, "magneton"),
   ("magneton", None, "magnezone"),
   ("magneton", None, "magnezone"),
   ("magneton", None, "magnezone"),
   ("magneton", None, "magnezone"),
  ],
  "starting_moves": ["tackle", "sonic-boom", "thunder-shock"],
  "learned_moves": [
   ("supersonic", 29),
   ("thunder-wave", 38),
   ("screech", 54),
   ("swift", 46),
   ("tri-attack", 35),
  ],
  "types": ["electric", "steel"],
  "base_health":
  50,
  "catch_rate":
  60,
 },
 "farfetchd": {
  "evolution_chain": [],
  "starting_moves": ["sand-attack", "peck"],
  "learned_moves": [
   ("swords-dance", 23),
   ("fury-attack", 15),
   ("leer", 7),
   ("razor-leaf", 13),
   ("agility", 31),
   ("focus-energy", 4),
   ("slash", 39),
  ],
  "types": ["normal", "flying"],
  "base_health":
  52,
  "catch_rate":
  45,
 },
 "doduo": {
  "evolution_chain": [("doduo", 31, "dodrio")],
  "starting_moves": ["peck"],
  "learned_moves": [
   ("swords-dance", 36),
   ("jump-kick", 40),
   ("fury-attack", 24),
   ("thrash", 50),
   ("growl", 20),
   ("drill-peck", 30),
   ("agility", 44),
   ("rage", 36),
   ("tri-attack", 40),
  ],
  "types": ["normal", "flying"],
  "base_health":
  35,
  "catch_rate":
  190,
 },
 "dodrio": {
  "evolution_chain": [("doduo", 31, "dodrio")],
  "starting_moves": [
   "fury-attack",
   "growl",
   "supersonic",
   "peck",
   "quick-attack",
   "mirror-move",
  ],
  "learned_moves": [
   ("swords-dance", 38),
   ("jump-kick", 43),
   ("thrash", 60),
   ("drill-peck", 30),
   ("agility", 51),
   ("rage", 39),
   ("tri-attack", 45),
  ],
  "types": ["normal", "flying"],
  "base_health":
  60,
  "catch_rate":
  45,
 },
 "seel": {
  "evolution_chain": [("seel", 34, "dewgong")],
  "starting_moves": ["headbutt"],
  "learned_moves": [
   ("take-down", 45),
   ("growl", 30),
   ("ice-beam", 50),
   ("aurora-beam", 35),
   ("rest", 40),
  ],
  "types": ["water"],
  "base_health":
  65,
  "catch_rate":
  190,
 },
 "dewgong": {
  "evolution_chain": [("seel", 34, "dewgong")],
  "starting_moves": ["headbutt", "growl", "aurora-beam"],
  "learned_moves": [("take-down", 50), ("ice-beam", 56), ("rest", 44)],
  "types": ["water", "ice"],
  "base_health": 90,
  "catch_rate": 75,
 },
 "grimer": {
  "evolution_chain": [("grimer", 38, "muk")],
  "starting_moves": ["pound", "disable", "pound"],
  "learned_moves": [
   ("screech", 48),
   ("harden", 42),
   ("minimize", 33),
   ("sludge", 37),
   ("poison-gas", 30),
   ("acid-armor", 55),
  ],
  "types": ["poison"],
  "base_health":
  80,
  "catch_rate":
  190,
 },
 "muk": {
  "evolution_chain": [("grimer", 38, "muk")],
  "starting_moves": ["pound", "disable", "haze", "poison-gas", "pound"],
  "learned_moves": [
   ("screech", 53),
   ("harden", 45),
   ("minimize", 33),
   ("sludge", 37),
   ("acid-armor", 60),
  ],
  "types": ["poison"],
  "base_health":
  105,
  "catch_rate":
  75,
 },
 "shellder": {
  "evolution_chain": [],
  "starting_moves": ["tackle", "withdraw"],
  "learned_moves": [
   ("leer", 39),
   ("supersonic", 18),
   ("hydro-pump", 61),
   ("ice-beam", 50),
   ("aurora-beam", 30),
   ("clamp", 23),
  ],
  "types": ["water"],
  "base_health":
  30,
  "catch_rate":
  190,
 },
 "cloyster": {
  "evolution_chain": [],
  "starting_moves": [
   "tackle",
   "twineedle",
   "leer",
   "supersonic",
   "hydro-pump",
   "aurora-beam",
   "withdraw",
   "barrier",
   "clamp",
  ],
  "learned_moves": [("spike-cannon", 50)],
  "types": ["water", "ice"],
  "base_health":
  50,
  "catch_rate":
  60,
 },
 "gastly": {
  "evolution_chain": [("gastly", 25, "haunter")],
  "starting_moves": ["night-shade", "confuse-ray", "lick"],
  "learned_moves": [("hypnosis", 27), ("dream-eater", 35), ("poison-gas", 7)],
  "types": ["ghost", "poison"],
  "base_health": 30,
  "catch_rate": 190,
 },
 "haunter": {
  "evolution_chain": [("gastly", 25, "haunter")],
  "starting_moves": ["night-shade", "confuse-ray", "lick", "smog"],
  "learned_moves": [("hypnosis", 29), ("dream-eater", 38), ("poison-gas", 7)],
  "types": ["ghost", "poison"],
  "base_health": 45,
  "catch_rate": 90,
 },
 "gengar": {
  "evolution_chain": [("gastly", 25, "haunter")],
  "starting_moves": [
   "disable",
   "night-shade",
   "confuse-ray",
   "haze",
   "lick",
   "smog",
  ],
  "learned_moves": [("hypnosis", 29), ("dream-eater", 38), ("poison-gas", 7)],
  "types": ["ghost", "poison"],
  "base_health":
  60,
  "catch_rate":
  45,
 },
 "onix": {
  "evolution_chain": [],
  "starting_moves": ["tackle", "screech"],
  "learned_moves": [
   ("bind", 15),
   ("slam", 33),
   ("rock-throw", 19),
   ("rage", 25),
   ("harden", 43),
  ],
  "types": ["rock", "ground"],
  "base_health":
  35,
  "catch_rate":
  45,
 },
 "drowzee": {
  "evolution_chain": [("drowzee", 26, "hypno")],
  "starting_moves": ["pound", "hypnosis", "pound"],
  "learned_moves": [
   ("headbutt", 24),
   ("disable", 12),
   ("psybeam", 26),
   ("confusion", 17),
   ("psychic", 32),
   ("meditate", 37),
   ("poison-gas", 29),
  ],
  "types": ["psychic"],
  "base_health":
  60,
  "catch_rate":
  190,
 },
 "hypno": {
  "evolution_chain": [("drowzee", 26, "hypno")],
  "starting_moves": [
   "pound",
   "disable",
   "confusion",
   "hypnosis",
   "barrier",
   "pound",
  ],
  "learned_moves": [
   ("headbutt", 24),
   ("psybeam", 28),
   ("psychic", 37),
   ("meditate", 43),
   ("poison-gas", 33),
  ],
  "types": ["psychic"],
  "base_health":
  85,
  "catch_rate":
  75,
 },
 "krabby": {
  "evolution_chain": [("krabby", 28, "kingler")],
  "starting_moves": ["leer", "bubble"],
  "learned_moves": [
   ("vice-grip", 20),
   ("guillotine", 25),
   ("stomp", 30),
   ("harden", 40),
   ("crabhammer", 35),
  ],
  "types": ["water"],
  "base_health":
  30,
  "catch_rate":
  225,
 },
 "kingler": {
  "evolution_chain": [("krabby", 28, "kingler")],
  "starting_moves": ["vice-grip", "leer", "agility", "amnesia", "bubble"],
  "learned_moves": [
   ("guillotine", 25),
   ("slam", 44),
   ("stomp", 34),
   ("harden", 49),
   ("crabhammer", 42),
  ],
  "types": ["water"],
  "base_health":
  55,
  "catch_rate":
  60,
 },
 "voltorb": {
  "evolution_chain": [("voltorb", 30, "electrode")],
  "starting_moves": ["tackle", "screech"],
  "learned_moves": [
   ("sonic-boom", 17),
   ("thunder-shock", 9),
   ("light-screen", 29),
   ("self-destruct", 22),
   ("swift", 36),
   ("explosion", 43),
  ],
  "types": ["electric"],
  "base_health":
  40,
  "catch_rate":
  190,
 },
 "electrode": {
  "evolution_chain": [("voltorb", 30, "electrode")],
  "starting_moves": ["tackle", "sonic-boom", "thunder-shock", "screech"],
  "learned_moves": [
   ("light-screen", 29),
   ("self-destruct", 22),
   ("swift", 40),
   ("explosion", 50),
  ],
  "types": ["electric"],
  "base_health":
  60,
  "catch_rate":
  60,
 },
 "exeggcute": {
  "evolution_chain": [],
  "starting_moves": ["absorb", "hypnosis", "barrage"],
  "learned_moves": [
   ("psybeam", 27),
   ("leech-seed", 28),
   ("solar-beam", 42),
   ("poison-powder", 37),
   ("stun-spore", 32),
   ("sleep-powder", 48),
   ("confusion", 19),
   ("reflect", 25),
  ],
  "types": ["grass", "psychic"],
  "base_health":
  60,
  "catch_rate":
  90,
 },
 "exeggutor": {
  "evolution_chain": [],
  "starting_moves": [
   "absorb",
   "leech-seed",
   "stun-spore",
   "confusion",
   "hypnosis",
   "barrage",
  ],
  "learned_moves": [("stomp", 28)],
  "types": ["grass", "psychic"],
  "base_health":
  95,
  "catch_rate":
  45,
 },
 "cubone": {
  "evolution_chain": [("cubone", 28, "marowak"), ("cubone", 28, "marowak")],
  "starting_moves": ["growl", "bone-club"],
  "learned_moves": [
   ("headbutt", 18),
   ("thrash", 38),
   ("tail-whip", 13),
   ("leer", 25),
   ("rage", 46),
   ("focus-energy", 31),
   ("bonemerang", 43),
  ],
  "types": ["ground"],
  "base_health":
  50,
  "catch_rate":
  190,
 },
 "marowak": {
  "evolution_chain": [("cubone", 28, "marowak"), ("cubone", 28, "marowak")],
  "starting_moves": [
   "tail-whip",
   "leer",
   "growl",
   "screech",
   "focus-energy",
   "bone-club",
  ],
  "learned_moves": [
   ("headbutt", 18),
   ("thrash", 41),
   ("rage", 55),
   ("bonemerang", 48),
  ],
  "types": ["ground"],
  "base_health":
  60,
  "catch_rate":
  75,
 },
 "hitmonlee": {
  "evolution_chain": [
   ("tyrogue", 20, "hitmonlee"),
   ("tyrogue", 20, "hitmonchan"),
   ("tyrogue", 20, "hitmontop"),
  ],
  "starting_moves": ["double-kick", "tackle", "meditate"],
  "learned_moves": [
   ("mega-kick", 53),
   ("jump-kick", 38),
   ("rolling-kick", 33),
   ("focus-energy", 43),
   ("high-jump-kick", 48),
  ],
  "types": ["fighting"],
  "base_health":
  50,
  "catch_rate":
  45,
 },
 "hitmonchan": {
  "evolution_chain": [
   ("tyrogue", 20, "hitmonlee"),
   ("tyrogue", 20, "hitmonchan"),
   ("tyrogue", 20, "hitmontop"),
  ],
  "starting_moves": ["comet-punch", "tackle", "agility"],
  "learned_moves": [
   ("mega-punch", 48),
   ("fire-punch", 33),
   ("ice-punch", 38),
   ("thunder-punch", 43),
   ("leer", 5),
   ("counter", 53),
   ("focus-energy", 35),
   ("dizzy-punch", 25),
  ],
  "types": ["fighting"],
  "base_health":
  50,
  "catch_rate":
  45,
 },
 "lickitung": {
  "evolution_chain": [("lickitung", None, "lickilicky")],
  "starting_moves": ["wrap", "supersonic", "lick"],
  "learned_moves": [
   ("slam", 31),
   ("stomp", 7),
   ("disable", 15),
   ("acid", 10),
   ("screech", 39),
   ("defense-curl", 23),
  ],
  "types": ["normal"],
  "base_health":
  90,
  "catch_rate":
  45,
 },
 "koffing": {
  "evolution_chain": [("koffing", 35, "weezing")],
  "starting_moves": ["tackle", "smog", "poison-gas"],
  "learned_moves": [
   ("smokescreen", 37),
   ("haze", 45),
   ("self-destruct", 40),
   ("sludge", 32),
   ("explosion", 48),
  ],
  "types": ["poison"],
  "base_health":
  40,
  "catch_rate":
  190,
 },
 "weezing": {
  "evolution_chain": [("koffing", 35, "weezing")],
  "starting_moves": [
   "tackle",
   "psybeam",
   "screech",
   "smog",
   "sludge",
   "poison-gas",
  ],
  "learned_moves": [
   ("smokescreen", 39),
   ("haze", 49),
   ("self-destruct", 43),
   ("explosion", 53),
  ],
  "types": ["poison"],
  "base_health":
  65,
  "catch_rate":
  60,
 },
 "rhyhorn": {
  "evolution_chain": [("rhyhorn", 42, "rhydon")],
  "starting_moves": ["sand-attack", "horn-attack", "tackle"],
  "learned_moves": [
   ("stomp", 30),
   ("fury-attack", 40),
   ("horn-drill", 45),
   ("take-down", 55),
   ("tail-whip", 35),
   ("leer", 50),
   ("rock-throw", 19),
  ],
  "types": ["ground", "rock"],
  "base_health":
  80,
  "catch_rate":
  120,
 },
 "rhydon": {
  "evolution_chain": [("rhyhorn", 42, "rhydon")],
  "starting_moves": [
   "stomp",
   "sand-attack",
   "horn-attack",
   "fury-attack",
   "tackle",
   "tail-whip",
  ],
  "learned_moves": [
   ("horn-drill", 48),
   ("take-down", 64),
   ("leer", 55),
   ("rock-throw", 19),
  ],
  "types": ["ground", "rock"],
  "base_health":
  105,
  "catch_rate":
  60,
 },
 "chansey": {
  "evolution_chain": [("happiny", None, "chansey"),
                      ("chansey", None, "blissey")],
  "starting_moves": ["pound", "double-slap", "tail-whip", "pound"],
  "learned_moves": [
   ("double-edge", 54),
   ("growl", 30),
   ("sing", 24),
   ("minimize", 38),
   ("defense-curl", 44),
   ("light-screen", 48),
  ],
  "types": ["normal"],
  "base_health":
  250,
  "catch_rate":
  30,
 },
 "tangela": {
  "evolution_chain": [("tangela", None, "tangrowth")],
  "starting_moves": ["bind", "constrict"],
  "learned_moves": [
   ("slam", 45),
   ("vine-whip", 29),
   ("absorb", 29),
   ("growth", 49),
   ("poison-powder", 32),
   ("stun-spore", 36),
   ("sleep-powder", 39),
  ],
  "types": ["grass"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "kangaskhan": {
  "evolution_chain": [],
  "starting_moves": ["pound", "comet-punch", "rage"],
  "learned_moves": [
   ("mega-punch", 36),
   ("tail-whip", 31),
   ("leer", 41),
   ("bite", 26),
   ("growl", 4),
   ("dizzy-punch", 46),
  ],
  "types": ["normal"],
  "base_health":
  105,
  "catch_rate":
  45,
 },
 "horsea": {
  "evolution_chain": [("horsea", 32, "seadra")],
  "starting_moves": ["bubble"],
  "learned_moves": [
   ("leer", 24),
   ("water-gun", 30),
   ("hydro-pump", 45),
   ("agility", 37),
   ("smokescreen", 19),
   ("focus-energy", 14),
  ],
  "types": ["water"],
  "base_health":
  30,
  "catch_rate":
  225,
 },
 "seadra": {
  "evolution_chain": [("horsea", 32, "seadra")],
  "starting_moves": ["disable", "smokescreen", "bubble"],
  "learned_moves": [
   ("leer", 24),
   ("water-gun", 30),
   ("hydro-pump", 52),
   ("agility", 41),
   ("focus-energy", 14),
  ],
  "types": ["water"],
  "base_health":
  55,
  "catch_rate":
  75,
 },
 "goldeen": {
  "evolution_chain": [("goldeen", 33, "seaking")],
  "starting_moves": ["tail-whip", "peck"],
  "learned_moves": [
   ("horn-attack", 24),
   ("fury-attack", 30),
   ("horn-drill", 45),
   ("supersonic", 19),
   ("agility", 54),
   ("quick-attack", 10),
   ("waterfall", 37),
  ],
  "types": ["water"],
  "base_health":
  45,
  "catch_rate":
  225,
 },
 "seaking": {
  "evolution_chain": [("goldeen", 33, "seaking")],
  "starting_moves": [
   "tail-whip",
   "supersonic",
   "psybeam",
   "peck",
   "quick-attack",
  ],
  "learned_moves": [
   ("horn-attack", 24),
   ("fury-attack", 30),
   ("horn-drill", 48),
   ("agility", 54),
   ("waterfall", 39),
  ],
  "types": ["water"],
  "base_health":
  80,
  "catch_rate":
  60,
 },
 "staryu": {
  "evolution_chain": [],
  "starting_moves": ["tackle"],
  "learned_moves": [
   ("water-gun", 17),
   ("hydro-pump", 47),
   ("psybeam", 24),
   ("recover", 27),
   ("harden", 22),
   ("minimize", 37),
   ("confuse-ray", 40),
   ("light-screen", 42),
   ("swift", 32),
  ],
  "types": ["water"],
  "base_health":
  30,
  "catch_rate":
  225,
 },
 "starmie": {
  "evolution_chain": [],
  "starting_moves": [
   "tackle",
   "water-gun",
   "hydro-pump",
   "psybeam",
   "recover",
   "harden",
   "minimize",
  ],
  "learned_moves": [("confuse-ray", 37)],
  "types": ["water", "psychic"],
  "base_health":
  60,
  "catch_rate":
  60,
 },
 "mr-mime": {
  "evolution_chain": [("mime-jr", None, "mr-mime"),
                      ("mr-mime", 42, "mr-rime")],
  "starting_moves": ["pound", "confusion", "barrier"],
  "learned_moves": [
   ("double-slap", 31),
   ("psybeam", 36),
   ("meditate", 39),
   ("light-screen", 23),
   ("substitute", 47),
  ],
  "types": ["psychic", "fairy"],
  "base_health":
  40,
  "catch_rate":
  45,
 },
 "scyther": {
  "evolution_chain": [],
  "starting_moves": ["quick-attack"],
  "learned_moves": [
   ("swords-dance", 35),
   ("wing-attack", 50),
   ("leer", 17),
   ("agility", 42),
   ("double-team", 24),
   ("focus-energy", 20),
   ("slash", 29),
  ],
  "types": ["bug", "flying"],
  "base_health":
  70,
  "catch_rate":
  45,
 },
 "jynx": {
  "evolution_chain": [("smoochum", 30, "jynx")],
  "starting_moves": ["pound", "lovely-kiss"],
  "learned_moves": [
   ("double-slap", 23),
   ("ice-punch", 31),
   ("body-slam", 39),
   ("thrash", 47),
   ("sing", 20),
   ("blizzard", 58),
   ("confusion", 12),
   ("screech", 18),
   ("lick", 18),
  ],
  "types": ["ice", "psychic"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "electabuzz": {
  "evolution_chain": [("elekid", 30, "electabuzz")],
  "starting_moves": ["leer", "quick-attack"],
  "learned_moves": [
   ("thunder-punch", 42),
   ("low-kick", 10),
   ("thunder-shock", 34),
   ("thunder", 54),
   ("screech", 37),
   ("light-screen", 49),
  ],
  "types": ["electric"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "magmar": {
  "evolution_chain": [("magby", 30, "magmar")],
  "starting_moves": ["ember"],
  "learned_moves": [
   ("fire-punch", 43),
   ("leer", 36),
   ("flamethrower", 55),
   ("fire-spin", 19),
   ("smokescreen", 48),
   ("confuse-ray", 39),
   ("smog", 52),
  ],
  "types": ["fire"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "pinsir": {
  "evolution_chain": [],
  "starting_moves": ["vice-grip"],
  "learned_moves": [
   ("guillotine", 30),
   ("swords-dance", 54),
   ("bind", 21),
   ("thrash", 35),
   ("seismic-toss", 25),
   ("harden", 43),
   ("focus-energy", 36),
   ("slash", 49),
  ],
  "types": ["bug"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "tauros": {
  "evolution_chain": [],
  "starting_moves": ["tackle"],
  "learned_moves": [
   ("stomp", 21),
   ("horn-attack", 13),
   ("take-down", 51),
   ("thrash", 43),
   ("tail-whip", 28),
   ("leer", 35),
   ("rage", 44),
   ("focus-energy", 38),
  ],
  "types": ["normal"],
  "base_health":
  75,
  "catch_rate":
  45,
 },
 "magikarp": {
  "evolution_chain": [("magikarp", 20, "gyarados")],
  "starting_moves": ["splash"],
  "learned_moves": [("tackle", 15)],
  "types": ["water"],
  "base_health": 20,
  "catch_rate": 255,
 },
 "gyarados": {
  "evolution_chain": [("magikarp", 20, "gyarados")],
  "starting_moves": [
   "bind",
   "tackle",
   "thrash",
   "leer",
   "bite",
   "hydro-pump",
   "dragon-rage",
   "splash",
  ],
  "learned_moves": [("hyper-beam", 52)],
  "types": ["water", "flying"],
  "base_health":
  95,
  "catch_rate":
  45,
 },
 "lapras": {
  "evolution_chain": [],
  "starting_moves": ["growl", "water-gun"],
  "learned_moves": [
   ("body-slam", 25),
   ("sing", 16),
   ("mist", 20),
   ("hydro-pump", 46),
   ("ice-beam", 38),
   ("confuse-ray", 31),
  ],
  "types": ["water", "ice"],
  "base_health":
  130,
  "catch_rate":
  45,
 },
 "ditto": {
  "evolution_chain": [],
  "starting_moves": ["transform"],
  "learned_moves": [],
  "types": ["normal"],
  "base_health": 48,
  "catch_rate": 35,
 },
 "eevee": {
  "evolution_chain": [
   ("eevee", None, "espeon"),
   ("eevee", None, "umbreon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "sylveon"),
   ("eevee", None, "sylveon"),
  ],
  "starting_moves": ["sand-attack", "tackle"],
  "learned_moves": [
   ("double-kick", 10),
   ("take-down", 45),
   ("tail-whip", 31),
   ("bite", 37),
   ("growl", 16),
   ("quick-attack", 27),
   ("focus-energy", 36),
  ],
  "types": ["normal"],
  "base_health":
  55,
  "catch_rate":
  45,
 },
 "vaporeon": {
  "evolution_chain": [
   ("eevee", None, "espeon"),
   ("eevee", None, "umbreon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "sylveon"),
   ("eevee", None, "sylveon"),
  ],
  "starting_moves": [
   "sand-attack",
   "tackle",
   "growl",
   "water-gun",
   "quick-attack",
  ],
  "learned_moves": [
   ("double-kick", 10),
   ("tail-whip", 37),
   ("bite", 40),
   ("mist", 48),
   ("hydro-pump", 54),
   ("aurora-beam", 36),
   ("haze", 44),
   ("acid-armor", 42),
  ],
  "types": ["water"],
  "base_health":
  130,
  "catch_rate":
  45,
 },
 "jolteon": {
  "evolution_chain": [
   ("eevee", None, "espeon"),
   ("eevee", None, "umbreon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "sylveon"),
   ("eevee", None, "sylveon"),
  ],
  "starting_moves": [
   "sand-attack",
   "tackle",
   "bite",
   "growl",
   "thunder-shock",
   "quick-attack",
  ],
  "learned_moves": [
   ("double-kick", 42),
   ("tail-whip", 37),
   ("pin-missile", 48),
   ("thunder-wave", 40),
   ("thunder", 54),
   ("agility", 44),
  ],
  "types": ["electric"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "flareon": {
  "evolution_chain": [
   ("eevee", None, "espeon"),
   ("eevee", None, "umbreon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "leafeon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "glaceon"),
   ("eevee", None, "sylveon"),
   ("eevee", None, "sylveon"),
  ],
  "starting_moves":
  ["sand-attack", "tackle", "growl", "ember", "quick-attack"],
  "learned_moves": [
   ("double-kick", 10),
   ("tail-whip", 37),
   ("leer", 42),
   ("bite", 40),
   ("flamethrower", 54),
   ("fire-spin", 44),
   ("rage", 48),
   ("focus-energy", 24),
   ("smog", 42),
  ],
  "types": ["fire"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "porygon": {
  "evolution_chain": [],
  "starting_moves": ["tackle", "sharpen", "conversion"],
  "learned_moves": [
   ("psybeam", 23),
   ("thunder-shock", 15),
   ("agility", 35),
   ("recover", 28),
   ("barrier", 18),
   ("tri-attack", 42),
  ],
  "types": ["normal"],
  "base_health":
  65,
  "catch_rate":
  45,
 },
 "omanyte": {
  "evolution_chain": [("omanyte", 40, "omastar")],
  "starting_moves": ["water-gun", "withdraw", "constrict"],
  "learned_moves": [
   ("sand-attack", 10),
   ("horn-attack", 34),
   ("leer", 39),
   ("bite", 13),
   ("hydro-pump", 53),
   ("rock-throw", 26),
   ("spike-cannon", 46),
  ],
  "types": ["rock", "water"],
  "base_health":
  35,
  "catch_rate":
  45,
 },
 "omastar": {
  "evolution_chain": [("omanyte", 40, "omastar")],
  "starting_moves": [
   "sand-attack",
   "horn-attack",
   "bite",
   "supersonic",
   "water-gun",
   "withdraw",
   "constrict",
  ],
  "learned_moves": [
   ("leer", 39),
   ("hydro-pump", 49),
   ("rock-throw", 26),
   ("spike-cannon", 44),
  ],
  "types": ["rock", "water"],
  "base_health":
  70,
  "catch_rate":
  45,
 },
 "kabuto": {
  "evolution_chain": [("kabuto", 40, "kabutops")],
  "starting_moves": ["scratch", "harden"],
  "learned_moves": [
   ("sand-attack", 28),
   ("leer", 44),
   ("hydro-pump", 49),
   ("absorb", 34),
   ("mega-drain", 46),
   ("rock-throw", 30),
   ("leech-life", 48),
   ("slash", 39),
  ],
  "types": ["rock", "water"],
  "base_health":
  30,
  "catch_rate":
  45,
 },
 "kabutops": {
  "evolution_chain": [("kabuto", 40, "kabutops")],
  "starting_moves": ["scratch", "absorb", "screech", "harden", "confuse-ray"],
  "learned_moves": [
   ("sand-attack", 28),
   ("leer", 46),
   ("hydro-pump", 53),
   ("mega-drain", 51),
   ("rock-throw", 30),
   ("leech-life", 54),
   ("slash", 39),
  ],
  "types": ["rock", "water"],
  "base_health":
  60,
  "catch_rate":
  45,
 },
 "aerodactyl": {
  "evolution_chain": [],
  "starting_moves": ["wing-attack", "agility"],
  "learned_moves": [
   ("take-down", 45),
   ("bite", 38),
   ("supersonic", 33),
   ("hyper-beam", 54),
   ("rock-throw", 21),
  ],
  "types": ["rock", "flying"],
  "base_health":
  80,
  "catch_rate":
  45,
 },
 "snorlax": {
  "evolution_chain": [("munchlax", None, "snorlax")],
  "starting_moves": ["headbutt", "tackle", "amnesia", "rest"],
  "learned_moves": [
   ("body-slam", 35),
   ("double-edge", 48),
   ("bite", 16),
   ("hyper-beam", 56),
   ("screech", 39),
   ("harden", 41),
   ("defense-curl", 15),
  ],
  "types": ["normal"],
  "base_health":
  160,
  "catch_rate":
  25,
 },
 "articuno": {
  "evolution_chain": [],
  "starting_moves": ["gust", "ice-beam", "peck"],
  "learned_moves": [
   ("leer", 16),
   ("mist", 60),
   ("blizzard", 51),
   ("agility", 55),
   ("haze", 60),
  ],
  "types": ["ice", "flying"],
  "base_health":
  90,
  "catch_rate":
  3,
 },
 "zapdos": {
  "evolution_chain": [],
  "starting_moves": ["peck", "drill-peck", "thunder-shock"],
  "learned_moves": [
   ("leer", 16),
   ("thunder", 51),
   ("agility", 55),
   ("light-screen", 60),
  ],
  "types": ["electric", "flying"],
  "base_health":
  90,
  "catch_rate":
  3,
 },
 "moltres": {
  "evolution_chain": [],
  "starting_moves": ["gust", "wing-attack", "ember", "peck", "fire-spin"],
  "learned_moves": [
   ("leer", 51),
   ("flamethrower", 49),
   ("solar-beam", 71),
   ("agility", 55),
   ("sky-attack", 60),
  ],
  "types": ["fire", "flying"],
  "base_health":
  90,
  "catch_rate":
  3,
 },
 "dratini": {
  "evolution_chain": [
   ("dratini", 30, "dragonair"),
   ("dragonair", 55, "dragonite"),
  ],
  "starting_moves": ["wrap", "leer"],
  "learned_moves": [
   ("slam", 30),
   ("hyper-beam", 50),
   ("dragon-rage", 40),
   ("thunder-wave", 10),
   ("agility", 20),
  ],
  "types": ["dragon"],
  "base_health":
  41,
  "catch_rate":
  45,
 },
 "dragonair": {
  "evolution_chain": [
   ("dratini", 30, "dragonair"),
   ("dragonair", 55, "dragonite"),
  ],
  "starting_moves": ["wrap", "leer", "thunder-wave"],
  "learned_moves": [
   ("slam", 35),
   ("hyper-beam", 55),
   ("dragon-rage", 45),
   ("agility", 20),
  ],
  "types": ["dragon"],
  "base_health":
  61,
  "catch_rate":
  45,
 },
 "dragonite": {
  "evolution_chain": [
   ("dratini", 30, "dragonair"),
   ("dragonair", 55, "dragonite"),
  ],
  "starting_moves": ["wrap", "leer", "mist", "thunder-wave", "agility"],
  "learned_moves": [
   ("wing-attack", 55),
   ("slam", 35),
   ("hyper-beam", 60),
   ("dragon-rage", 45),
  ],
  "types": ["dragon", "flying"],
  "base_health":
  91,
  "catch_rate":
  45,
 },
 "mewtwo": {
  "evolution_chain": [],
  "starting_moves":
  ["disable", "confusion", "psychic", "confuse-ray", "swift"],
  "learned_moves": [
   ("mist", 75),
   ("psybeam", 22),
   ("agility", 88),
   ("recover", 70),
   ("barrier", 63),
   ("amnesia", 81),
  ],
  "types": ["psychic"],
  "base_health":
  106,
  "catch_rate":
  3,
 },
 "mew": {
  "evolution_chain": [],
  "starting_moves": ["pound", "confusion", "pound"],
  "learned_moves": [
   ("mega-punch", 20),
   ("psychic", 40),
   ("barrier", 40),
   ("metronome", 30),
   ("amnesia", 60),
   ("transform", 10),
  ],
  "types": ["psychic"],
  "base_health":
  100,
  "catch_rate":
  45,
 },
}

POKEMON_NAMES = []
for name, value in POKEMON_INFO.items():
	POKEMON_NAMES.append(name)

type_colors = {
 "normal": Fore.WHITE,
 "fire": Fore.RED,
 "water": Fore.CYAN,
 "grass": Fore.GREEN,
 "electric": Fore.YELLOW,
 "ice": Fore.CYAN,
 "fighting": Fore.LIGHTRED_EX,
 "poison": Fore.MAGENTA,
 "ground": Fore.YELLOW,
 "flying": Fore.LIGHTCYAN_EX,
 "psychic": Fore.LIGHTMAGENTA_EX,
 "bug": Fore.LIGHTGREEN_EX,
 "rock": Fore.YELLOW,
 "ghost": Fore.LIGHTMAGENTA_EX,
 "dragon": Fore.BLUE,
 "dark": Fore.LIGHTBLACK_EX,
 "steel": Fore.LIGHTWHITE_EX,
 "fairy": Fore.LIGHTMAGENTA_EX,
}

# pokemon_base_healths = {
#     "pikachu": 35,
#     "bulbasaur": 45,
#     "charmander": 39,
#     "squirtle": 44,
#     "ralts": 28,
#     "jigglypuff": 115,
#     "geodude": 40,
#     "gastly": 30,
#     "machop": 70,
#     "abra": 25,
#     "pidgey": 40,
#     "rattata": 46,
#     "oddish": 45,
#     "growlithe": 55,
#     "poliwhirl": 65,
#     "lugia": 106,
#     "magikarp": 20,
#     "vulpix": 38,
#     "diglett": 10,
#     "psyduck": 50,
#     "slowpoke": 90,
#     "shellder": 30,
#     "mankey": 40,
#     "kabuto": 30,
#     "omanyte": 35,
#     "dratini": 41,
#     "drowzee": 60,
#     "ekans": 35,
#     "sandshrew": 50,
#     "articuno": 90,
#     "moltres": 90,
#     "zapdos": 90
# }

# grass_spawn_rates = {
#     "pikachu": 10,
#     "bulbasaur": 0,
#     "charmander": 0,
#     "squirtle": 0,
#     "ralts": 5,
#     "jigglypuff": 9,
#     "geodude": 12,
#     "gastly": 11,
#     "machop": 13,
#     "abra": 14,
#     "pidgey": 35,
#     "rattata": 33,
#     "oddish": 30,
#     "growlithe": 19,
#     "poliwhirl": 7,
#     "lugia": 1,
#     "magikarp": 9,
#     "vulpix": 12,
#     "diglett": 10,
#     "psyduck": 7,
#     "slowpoke": 7,
#     "shellder": 7,
#     "mankey": 7,
#     "kabuto": 10,
#     "omanyte": 10,
#     "dratini": 10,
#     "drowzee": 9,
#     "ekans": 8,
#     "sandshrew": 8,
#     "articuno": 1,
#     "moltres": 1,
#     "zapdos": 1
# }

# # pokemon_types = {
# #     "pikachu": ["electric"],
# #     "bulbasaur": ["grass", "poison"],
# #     "charmander": ["fire"],
# #     "squirtle": ["water"],
# #     "ralts": ["psychic", "fairy"],
# #     "jigglypuff": ["normal", "fairy"],
# #     "geodude": ["rock", "ground"],
# #     "gastly": ["ghost", "poison"],
# #     "machop": ["fighting"],
# #     "abra": ["psychic"],
# #     "pidgey": ["normal", "flying"],
# #     "rattata": ["normal"],
# #     "oddish": ["grass", "poison"],
# #     "growlithe": ["fire"],
# #     "poliwhirl": ["water"],
# #     "lugia": ["psychic", "flying"],
# #     "magikarp": ["water"],
# #     "vulpix": ["fire"],
# #     "diglett": ["ground"],
# #     "psyduck": ["water"],
# #     "slowpoke": ["water", "psychic"],
# #     "shellder": ["water"],
# #     "mankey": ["fighting"],
# #     "kabuto": ["rock", "water"],
# #     "omanyte": ["rock", "water"],
# #     "dratini": ["dragon"],
# #     "drowzee": ["psychic"],
# #     "ekans": ["poison"],
# #     "sandshrew": ["ground"],
# #     "articuno": ["ice", "flying"],
# #     "moltres": ["fire", "flying"],
# #     "zapdos": ["electric", "flying"],
# # }

# # region_pokemon_default_moves = {
# #     "bulbasaur": ["tackle", "growl", "leech seed", "vine whip"],
# #     "charmander": ["scratch", "growl", "ember", "smokescreen"],
# #     "squirtle": ["tackle", "tail whip", "squirt everywhere", "withdraw"],
# #     "pikachu": ["thundershock", "growl", "tail whip", "quick attack"],
# #     "ralts": ["growl", "confusion", "double team", "teleport"],
# #     "jigglypuff": ["sing", "pound", "disable", "defense curl"],
# #     "geodude": ["tackle", "defense curl", "rock throw", "magnitude"],
# #     "gastly": ["hypnosis", "lick", "spite", "curse"],
# #     "machop": ["low kick", "leer", "karate chop", "focus energy"],
# #     "abra": ["teleport", "kinesis", "confusion", "disable"],
# #     "pidgey": ["tackle", "gust", "bite", "growl"],
# #     "rattata": ["tackle", "tail whip", "growl", "bite"],
# #     "oddish": ["absorb", "sweet scent", "acid", "moonlight"],
# #     "growlithe": ["bite", "roar", "ember", "leer"],
# #     "poliwhirl": ["water gun", "double slap", "hypnosis", "bubblebeam"],
# #     "lugia": ["aeroblast", "punishment", "ancient power", "hydro pump"],
# #     "magikarp": ["splash", "tackle"],
# #     "vulpix": ["ember", "tail whip", "roar", "quick attack"],
# #     "diglett": ["scratch", "growl", "dig", "sand attack"],
# #     "psyduck": ["scratch", "tail whip", "water gun", "confusion"],
# #     "slowpoke": ["curse", "yawn", "tackle", "water gun"],
# #     "shellder": ["tackle", "withdraw", "icicle spear", "supersonic"],
# #     "mankey": ["scratch", "throw poop", "karate chop", "focus energy"],
# #     "kabuto": ["scratch", "harden", "absorb", "ancient power"],
# #     "omanyte": ["constrict", "withdraw", "bite", "water gun"],
# #     "dratini": ["wrap", "leer", "thunder wave", "twister"],
# #     "drowzee": ["pound", "hypnosis", "disable", "confusion"],
# #     "ekans": ["wrap", "leer", "poison sting", "bite"],
# #     "sandshrew": ["scratch", "defense curl", "sand attack", "poison sting"],
# #     "articuno": ["peck", "ice beam", "agility", "reflect"],
# #     "moltres": ["wing attack", "flamethrower", "agility", "safeguard"],
# #     "zapdos": ["thunder shock", "drill peck", "agility", "light screen"],
# # }

# moves_data = {
#     "tackle": {"type": "normal", "damage": 40, "pp": 35, "defense_buff": 1.0},
#     "bite": {"type": "dark", "damage": 30, "pp": 35, "defense_buff": 1.0},
#     "vine whip": {"type": "grass", "damage": 45, "pp": 25, "defense_buff": 1.0},
#     "ember": {"type": "fire", "damage": 40, "pp": 25, "defense_buff": 1.0},
#     "squirt everywhere": {"type": "water", "damage": 40, "pp": 25, "defense_buff": 1.0},
#     "confusion": {"type": "psychic", "damage": 50, "pp": 25, "defense_buff": 1.0},
#     "sing": {"type": "normal", "damage": 0, "pp": 15, "defense_buff": 1.0},
#     "rock throw": {"type": "rock", "damage": 50, "pp": 15, "defense_buff": 1.0},
#     "lick": {"type": "ghost", "damage": 30, "pp": 30, "defense_buff": 1.0},
#     "karate chop": {"type": "fighting", "damage": 50, "pp": 25, "defense_buff": 1.0},
#     "teleport": {"type": "psychic", "damage": 0, "pp": 20, "defense_buff": 1.0},
#     "growl": {"type": "normal", "damage": 0, "pp": 40, "defense_buff": 1.05},
#     "quick attack": {"type": "normal", "damage": 40, "pp": 30, "defense_buff": 1.0},
#     "scratch": {"type": "normal", "damage": 40, "pp": 35, "defense_buff": 1.0},
#     "smokescreen": {"type": "normal", "damage": 0, "pp": 20, "defense_buff": 1.05},
#     "leech seed": {"type": "grass", "damage": 0, "pp": 10, "defense_buff": 1.05},
#     "pound": {"type": "normal", "damage": 40, "pp": 35, "defense_buff": 1.0},
#     "disable": {"type": "normal", "damage": 0, "pp": 20, "defense_buff": 1.05},
#     "defense curl": {"type": "normal", "damage": 0, "pp": 40, "defense_buff": 1.05},
#     "magnitude": {"type": "ground", "damage": 60, "pp": 30, "defense_buff": 1.0},
#     "hypnosis": {"type": "psychic", "damage": 0, "pp": 20, "defense_buff": 1.05},
#     "spite": {"type": "ghost", "damage": 0, "pp": 10, "defense_buff": 1.05},
#     "curse": {"type": "ghost", "damage": 0, "pp": 10, "defense_buff": 1.05},
#     "low kick": {"type": "fighting", "damage": 50, "pp": 20, "defense_buff": 1.0},
#     "leer": {"type": "normal", "damage": 0, "pp": 30, "defense_buff": 1.05},
#     "focus energy": {"type": "normal", "damage": 0, "pp": 30, "defense_buff": 1.0},
#     "kinesis": {"type": "psychic", "damage": 0, "pp": 15, "defense_buff": 1.05},
#     "withdraw": {"type": "water", "damage": 0, "pp": 40, "defense_buff": 1.0},
#     "thundershock": {"type": "electric", "damage": 40, "pp": 30, "defense_buff": 1.0},
#     "double team": {"type": "normal", "damage": 0, "pp": 15, "defense_buff": 1.0},
#     "gust": {"type": "flying", "damage": 40, "pp": 35, "defense_buff": 1.0},
#     "tail whip": {"type": "normal", "damage": 0, "pp": 30, "defense_buff": 1.05},
#     "absorb": {"type": "grass", "damage": 20, "pp": 25, "defense_buff": 1.0},
#     "sweet scent": {"type": "normal", "damage": 0, "pp": 20, "defense_buff": 1.05},
#     "acid": {"type": "poison", "damage": 40, "pp": 30, "defense_buff": 1.0},
#     "moonlight": {"type": "fairy", "damage": 0, "pp": 5, "defense_buff": 1.0},
#     "roar": {"type": "normal", "damage": 0, "pp": 20, "defense_buff": 1.0},
#     "water gun": {"type": "water", "damage": 40, "pp": 25, "defense_buff": 1.0},
#     "double slap": {"type": "normal", "damage": 15, "pp": 10, "defense_buff": 1.0},
#     "bubblebeam": {"type": "water", "damage": 65, "pp": 20, "defense_buff": 1.0},
#     "aeroblast": {"type": "flying", "damage": 100, "pp": 5, "defense_buff": 1.0},
#     "punishment": {"type": "dark", "damage": 60, "pp": 5, "defense_buff": 1.0},
#     "ancient power": {"type": "rock", "damage": 60, "pp": 5, "defense_buff": 1.0},
#     "hydro pump": {"type": "water", "damage": 110, "pp": 5, "defense_buff": 1.0},
#     "splash": {"type": "water", "damage": 0, "pp": 40, "defense_buff": 1.0},
#     "sand attack": {"type": "ground", "damage": 0, "pp": 15, "defense_buff": 1.0},
#     "supersonic": {"type": "normal", "damage": 0, "pp": 20, "defense_buff": 1.0},
#     "icicle spear": {"type": "ice", "damage": 25, "pp": 30, "defense_buff": 1.0},
#     "yawn": {"type": "normal", "damage": 0, "pp": 30, "defense_buff": 1.05},
#     "harden": {"type": "normal", "damage": 0, "pp": 30, "defense_buff": 1.0},
#     "agility": {"type": "psychic", "damage": 0, "pp": 30, "defense_buff": 1.0},
#     "thunder shock": {"type": "electric", "damage": 40, "pp": 30, "defense_buff": 1.0},
#     "peck": {"type": "flying", "damage": 35, "pp": 35, "defense_buff": 1.0},
#     "flamethrower": {"type": "fire", "damage": 90, "pp": 15, "defense_buff": 1.0},
#     "constrict": {"type": "normal", "damage": 10, "pp": 35, "defense_buff": 1.0},
#     "reflect": {"type": "psychic", "damage": 0, "pp": 20, "defense_buff": 1.0},
#     "wrap": {"type": "normal", "damage": 15, "pp": 20, "defense_buff": 1.0},
#     "poison sting": {"type": "poison", "damage": 15, "pp": 35, "defense_buff": 1.0},
#     "light screen": {"type": "psychic", "damage": 0, "pp": 30, "defense_buff": 1.0},
#     "wing attack": {"type": "flying", "damage": 60, "pp": 35, "defense_buff": 1.0},
#     "thunder wave": {"type": "electric", "damage": 0, "pp": 20, "defense_buff": 1.0},
#     "twister": {"type": "dragon", "damage": 40, "pp": 20, "defense_buff": 1.0},
#     "safeguard": {"type": "normal", "damage": 0, "pp": 25, "defense_buff": 1.0},
#     "drill peck": {"type": "flying", "damage": 80, "pp": 20, "defense_buff": 1.0},
#     "dig": {"type": "ground", "damage": 80, "pp": 10, "defense_buff": 1.0},
#     "ice beam": {"type": "ice", "damage": 90, "pp": 10, "defense_buff": 1.0},
#     "throw poop": {"type": "ice", "damage": 200, "pp": 10, "defense_buff": 1.0}

# }

# code used to make sure i didnt miss any moves
"""
def find_missing_moves():
	m1 = set()
	m2 = set()
	for pokemon, moves in region_pokemon_default_moves.items():
		for move in moves:
			m1.add(move)
	for mm, val in moves_data.items():
		m2.add(mm)

	return m1-m2

missing_moves = find_missing_moves()
print(missing_moves)

find_missing_moves()
"""

# pokemon_evolutions = {
#     "charmander": {16: "charmeleon", 36: "charizard"},
#     "squirtle": {16: "wartortle", 36: "blastoise"},
#     "ralts": {20: "kirlia", 30: "gardevoir"},
#     "jigglypuff": {22: "wigglytuff"},
#     "geodude": {25: "graveler", 35: "golem"},
#     "gastly": {25: "haunter", 35: "gengar"},
#     "machop": {28: "machoke", 40: "machamp"},
#     "abra": {16: "kadabra", 36: "alakazam"},
#     "pidgey": {18: "pidgeotto", 36: "pidgeot"},
#     "rattata": {20: "raticate"},
#     "oddish": {21: "gloom"},
#     "growlithe": {30: "arcanine"},
#     "poliwhirl": {25: "poliwrath"},
#     "magikarp": {20: "gyarados"},
#     "vulpix": {30: "ninetales"},
#     "diglett": {26: "dugtrio"},
#     "psyduck": {33: "golduck"},
#     "slowpoke": {37: "slowbro"},
#     "shellder": {28: "cloyster"},
#     "mankey": {28: "primeape"},
#     "pikachu": {22: "raichu"},
#     "ekans": {22: "arbok"},
#     "sandshrew": {22: "sandslash"},
#     "bulbasaur": {16: "ivysaur", 32: "venusaur"},
#     "drowzee": {26: "hypno"},
#     "kabuto": {40: "kabutops"},
#     "omanyte": {40: "omastar"},
#     "dratini": {30: "dragonair", 55: "dragonite"},
#     "articuno": {},
#     "zapdos": {},
#     "moltres": {},
#     "lugia": {},
# }

# got the numbers online


def calculate_effectiveness(move_type, target_types):
	effectiveness_chart = {
	 "normal": {
	  "rock": 0.5,
	  "ghost": 0,
	  "steel": 0.5
	 },
	 "fighting": {
	  "normal": 2,
	  "flying": 0.5,
	  "poison": 0.5,
	  "rock": 2,
	  "bug": 0.5,
	  "ghost": 0,
	  "steel": 2,
	  "psychic": 0.5,
	  "ice": 2,
	  "dark": 2,
	  "fairy": 0.5,
	 },
	 "flying": {
	  "fighting": 2,
	  "rock": 0.5,
	  "bug": 2,
	  "steel": 0.5,
	  "grass": 2,
	  "electric": 0.5,
	 },
	 "poison": {
	  "poison": 0.5,
	  "ground": 0.5,
	  "rock": 0.5,
	  "ghost": 0.5,
	  "steel": 0,
	  "grass": 2,
	  "fairy": 2,
	 },
	 "ground": {
	  "flying": 0,
	  "poison": 2,
	  "rock": 2,
	  "bug": 0.5,
	  "steel": 2,
	  "fire": 2,
	  "grass": 0.5,
	  "electric": 2,
	 },
	 "rock": {
	  "fighting": 0.5,
	  "flying": 2,
	  "ground": 0.5,
	  "bug": 2,
	  "steel": 0.5,
	  "fire": 2,
	  "ice": 2,
	 },
	 "bug": {
	  "fighting": 0.5,
	  "flying": 0.5,
	  "poison": 0.5,
	  "ghost": 0.5,
	  "steel": 0.5,
	  "fire": 0.5,
	  "grass": 2,
	  "psychic": 2,
	  "dark": 2,
	  "fairy": 0.5,
	 },
	 "ghost": {
	  "normal": 0,
	  "ghost": 2,
	  "psychic": 2,
	  "dark": 0.5
	 },
	 "steel": {
	  "rock": 2,
	  "steel": 0.5,
	  "fire": 0.5,
	  "water": 0.5,
	  "electric": 0.5,
	  "ice": 2,
	  "fairy": 2,
	 },
	 "fire": {
	  "rock": 0.5,
	  "bug": 2,
	  "steel": 2,
	  "fire": 0.5,
	  "water": 0.5,
	  "grass": 2,
	  "ice": 2,
	  "dragon": 0.5,
	 },
	 "water": {
	  "ground": 2,
	  "rock": 2,
	  "fire": 2,
	  "water": 0.5,
	  "grass": 0.5,
	  "dragon": 0.5,
	 },
	 "grass": {
	  "flying": 0.5,
	  "poison": 0.5,
	  "ground": 2,
	  "rock": 2,
	  "bug": 0.5,
	  "steel": 0.5,
	  "fire": 0.5,
	  "water": 2,
	  "grass": 0.5,
	  "dragon": 0.5,
	 },
	 "electric": {
	  "flying": 2,
	  "ground": 0,
	  "water": 2,
	  "grass": 0.5,
	  "electric": 0.5,
	  "dragon": 0.5,
	 },
	 "psychic": {
	  "fighting": 2,
	  "poison": 2,
	  "steel": 0.5,
	  "psychic": 0.5,
	  "dark": 0,
	 },
	 "ice": {
	  "flying": 2,
	  "ground": 2,
	  "steel": 0.5,
	  "fire": 0.5,
	  "water": 0.5,
	  "grass": 2,
	  "ice": 0.5,
	  "dragon": 2,
	 },
	 "dragon": {
	  "steel": 0.5,
	  "dragon": 2,
	  "fairy": 0
	 },
	 "dark": {
	  "fighting": 0.5,
	  "ghost": 2,
	  "psychic": 2,
	  "dark": 0.5,
	  "fairy": 0.5
	 },
	 "fairy": {
	  "fighting": 2,
	  "poison": 0.5,
	  "steel": 0.5,
	  "fire": 0.5,
	  "dragon": 2,
	  "dark": 2,
	 },
	}
	effectivenesses = []
	for target_type in target_types:
		try:
			effectivenesses.append(effectiveness_chart[move_type][target_type])
		except:
			pass
	effectiveness=1
	for value in effectivenesses:
		effectiveness *= value
	
	return effectiveness

"""
New and improved code
"""
"""
import requests

def get_gen_one_moves():
  moves = []
  url = "https://pokeapi.co/api/v2/generation/1"
  
  response = requests.get(url)
  if response.status_code == 200:
    generation_data = response.json()
    moves_url = generation_data['moves']
    
    for move_url in moves_url:
      move_data = requests.get(move_url['url']).json()
      
      move_name = move_data['name']
      move_type = move_data['type']['name']
      move_power = move_data['power']
      move_pp = move_data['pp']
      move_accuracy = move_data['accuracy']
      
      # Get additional information if available
      move_buffs = {
        'attack': None,
        'defense': None
      }
      
      if 'stat_changes' in move_data:
        for stat_change in move_data['stat_changes']:
          if stat_change['stat']['name'] == 'attack':
            move_buffs['attack'] = stat_change['change']
          elif stat_change['stat']['name'] == 'defense':
            move_buffs['defense'] = stat_change['change']
      
      move_info = {
        'name': move_name,
        'type': move_type,
        'power': move_power,
        'pp': move_pp,
        'accuracy': move_accuracy,
        'buffs': move_buffs
      }
      
      if move_info["power"] or move_info["buffs"]["attack"] or move_info["buffs"]["attack"]:
        moves.append(move_info)
      
    return moves
  else:
    print("Failed to retrieve move data. Error:", response.status_code)

MOVES = get_gen_one_moves()

MOVE_NAMES = []
for move in MOVES:
  MOVE_NAMES.append(move['name'])


def get_gen_one_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    response = requests.get(url)
    data = response.json()

    gen_one_pokemon = []

    for result in data["results"]:
        pokemon_url = result["url"]
        pokemon_data = requests.get(pokemon_url).json()

        name = pokemon_data["name"]
        evolves_to = {}
        starting_moves = []
        learned_moves = []
        types = []
        base_health = 0
        catch_rate = 0

        if "species" in pokemon_data:
            species_url = pokemon_data["species"]["url"]
            species_data = requests.get(species_url).json()

            if "evolution_chain" in species_data:
                evolution_chain_url = species_data["evolution_chain"]["url"]
                evolution_chain_data = requests.get(evolution_chain_url).json()

                evolves_to = find_pokemon_evolutions(evolution_chain_data)

            base_health = pokemon_data["stats"][0]["base_stat"]

            for flavor_text in species_data["flavor_text_entries"]:
                if flavor_text["language"]["name"] == "en":
                    catch_rate = species_data["capture_rate"]
                    break

        for move in pokemon_data["moves"]:
            if move["version_group_details"][0]["level_learned_at"] == 1:
                if move["move"]["name"] in MOVE_NAMES:
                    starting_moves.append(move["move"]["name"])
            elif move["version_group_details"][0]["level_learned_at"] == 0:
                pass
            else:
                if move["move"]["name"] in MOVE_NAMES:
                    learned_moves.append((move["move"]["name"], move["version_group_details"][0]["level_learned_at"]))

        for type_entry in pokemon_data["types"]:
            types.append(type_entry["type"]["name"])

        gen_one_pokemon.append({
            "name": name,
            "evolution_chain": evolves_to,
            "starting_moves": starting_moves,
            "learned_moves": learned_moves,
            "types": types,
            "base_health": base_health,
            "catch_rate": catch_rate
        })

    return gen_one_pokemon

def find_pokemon_evolutions(pokemon_json):
  evolutions = []
  chain = pokemon_json.get("chain")
  
  def extract_evolutions(chain, parent_species_name=None):
    species = chain.get("species")
    evolution_details = chain.get("evolution_details")
    
    if evolution_details:
      for evolution in evolution_details:
        min_level = evolution.get("min_level")
        trigger = evolution.get("trigger")
        if trigger and trigger.get("name") == "level-up":
          evolutions.append((parent_species_name, min_level, species["name"]))
    
    evolves_to = chain.get("evolves_to")
    if evolves_to:
      for evolution in evolves_to:
        extract_evolutions(evolution, species["name"])
  
  extract_evolutions(chain)
  return evolutions

print(MOVES)
print("\n")
POKEMON_INFO = get_gen_one_pokemon()
print(POKEMON_INFO)

# print(".")
# m1=set()
# m2=set()
# for pokemon in POKEMON_INFO:
#   for move in pokemon["starting_moves"]:
#     m1.add(move)
#   for move, level in pokemon["learned_moves"]:
#     m1.add(move)

# # print(".")
# # for move in get_gen_one_moves():
# #   m2.add(move["name"])
# for name in MOVE_NAMES:
#   m2.add(name)

# print("OVERLAP")
# print(m1-m2)
"""



"""
This is the old code i used to get some of the pokemon data
I used a RESTful api for pokemon
"""
# import requests
#
# pokemon_ids = [25, 1, 4, 7, 280, 39, 74, 92, 66, 63]
#
# pokemon_base_healths = {}
#
# for pokemon_id in pokemon_ids:
# 	 url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
#
# 	 response = requests.get(url)
# 	 if response.status_code == 200:
# 		 pokemon_data = response.json()
#
# 		 # extract name
# 		 name = pokemon_data['name']
#
# 		 # extract base HP stat
# 		 base_hp = pokemon_data['stats'][0]['base_stat']
#
# 		 # print("Name:", name)
# 		 # print("Base HP:", base_hp)
# 		 pokemon_base_healths[name] = base_hp
#
# 		 # print("---------------------------------------")
# 	 else:
# 		 print("api failed")
#
# print(pokemon_base_healths)
