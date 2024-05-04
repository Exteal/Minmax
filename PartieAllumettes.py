from Allumettes import Allumettes
from StrategieGrundy import StrategieGrundy
from ConfigurationAllumettes import ConfigurationAllumettes
from CoupAllumettes import CoupAllumettes
from StrategieMinMax import StrategieMinMax
from StrategieGrundyOpti import StrategieGrundyOpti

from random import randint
from time import perf_counter as pc
from copy import deepcopy

def test_coups_1():
    partie = Allumettes()


    cg = ConfigurationAllumettes([3, 3, 2], 3)
    #cg.jouer_coup(CoupMorpion(1, 0, 0))

    # cg.jouer_coup(CoupMorpion(2, 2, 2))
    # cg.jouer_coup(CoupMorpion(1, 2, 0))

    # cg.jouer_coup(CoupMorpion(2, 1, 1))
    # cg.jouer_coup(CoupMorpion(1, 2, 1))
    # cg.jouer_coup(CoupMorpion(2, 0, 2))
    # cg.jouer_coup(CoupMorpion(1, 2, 2))


    # cg.jouer_coup(CoupMorpion(2, 0, 1))


    partie.jouerPartie(cg, StrategieMinMax, 15)

def test_coups_2():
    """rotation a 45° fait apparaitre un probleme"""

    partie = Allumettes()

    cg = ConfigurationAllumettes([3, 3, 2], 3)
   

    partie.jouerPartie(cg, StrategieGrundyOpti)


# def test_coups_3():
#     partie = Allumettes()

#     cg = ConfigurationMorpion()
#     cg.jouer_coup(CoupMorpion(1, 2, 0))
#     cg.jouer_coup(CoupMorpion(2, 0, 0))
#     cg.jouer_coup(CoupMorpion(1, 1, 1))
#     cg.jouer_coup(CoupMorpion(2, 0, 2))
#     cg.jouer_coup(CoupMorpion(1, 0, 1))
#     partie.jouerPartie(cg, StartegieMinMax, 100)



def comparasion_methodes(cols, maxallu):
    
    partie = Allumettes()
    groupes = []

    for _ in range(cols):
        groupes.append(randint(1, maxallu))

    
    cg = ConfigurationAllumettes(groupes, len(groupes))
    times = {}
    strats = [StrategieMinMax, StrategieGrundy, StrategieGrundyOpti]
    copies = [deepcopy(cg) for _ in strats]
    args = [15, copies[1], None]
    
    
   


    times[cg] = {}
    
    print("conf  ", cg)


    for idx, strat in enumerate(strats):
        print("debut ", strat)

        now = pc()

        partie.jouerPartie(copies[idx], strat, args[idx])

        later = pc()
        
        #print(times[cg])
        times[cg][strat] = later - now


    
    return times


comp = comparasion_methodes(3, 5)
print(comp)
