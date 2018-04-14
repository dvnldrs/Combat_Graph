import matplotlib.pyplot as plt
from random import *


def graph_damage(armor_class, dodge, attack_rating, weapon_damage):
    Y = []
    X = []

    for a in range (0, 50):
        X.append(a)
        Y.append(0)

    for x in range(0, 10000):
        Y[combat_roll(armor_class, dodge, attack_rating, weapon_damage)]+= 1

    plt.bar(X,Y)
    plt.title('Combat Damage Distribution')
    plt.show()


def combat_roll(armor_class, dodge, attack_rating, weapon_damage):
    if dodge_check(dodge):
        return 0
    froll = randint(1, 10)
    sroll = randint(2, 10)
    roll = froll + sroll
    base_damage = calculate_base_damage(roll, attack_rating, armor_class, weapon_damage)

    if roll == 1:
        return 0

    if roll == 20:
        base_damage = calculate_crit_damage(attack_rating, weapon_damage)

    if base_damage < 0:
        return 0

    return int(base_damage)


def calculate_crit_damage(attack_rating, weapon_damage):
    return int((20 * attack_rating) + weapon_damage)


def calculate_base_damage(roll, attack_rating, armor_class, weapon_damage):

    attack = (attack_rating * roll) + weapon_damage
    damage = attack - armor_class
    return damage


def dodge_check(dodge):
    dodge_success = randint(1, 100) <= dodge
    return dodge_success


defender_armorclass = 0
defender_dodge = 30

warrior_attackrating = 1
warrior_weapondamage = 10

monk_attackrating = 2
monk_weapondamage = 1

while True:
    inp = input('input attacker or type stop: ')
    if inp == 'warrior':
        graph_damage(defender_armorclass, defender_dodge, warrior_attackrating, warrior_weapondamage)
    elif inp == 'monk':
        graph_damage(defender_armorclass, defender_dodge, monk_attackrating, monk_weapondamage)
    elif inp == 'stop':
        exit()
    else:
        print('what is that?')

#graph_damage(defender_armorclass, defender_dodge, attacker_attackrating, attacker_weapondamage)







