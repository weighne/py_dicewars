import random
import numpy as np

pm = np.array([+1,-1])

map = [['A,5','B,2','A,2'],
       ['B,3','A,2','B,5'],
       ['B,2','A,3','B,2']]

def neighbor_check(a_coord, b_coord):
    print(int(b_coord.split(',')[0])+pm.all())
    if a_coord == b_coord:
        print("Identical Coords!")
    else:
        if int(a_coord.split(',')[0]) == int(b_coord.split(',')[0])+pm.all() or int(a_coord.split(',')[0]) == int(b_coord.split(',')[0]):
            print("x okay")
            if int(a_coord.split(',')[1]) == int(b_coord.split(',')[1])+pm.all() or int(a_coord.split(',')[1]) == int(b_coord.split(',')[1]):
                return True
            else:
                return False
        else:
            return False


def dice_roll(num):
    # roll a six sided die X number of times and add it up
    sum = 0
    for x in range(int(num)):
        roll = random.randint(1,6)
        # print(f'{x}: {roll}')
        sum += roll
    return sum


def fight(attack, defend):
    attack_roll = dice_roll(attack)
    defend_roll = dice_roll(defend)
    print(f'attack roll: {attack_roll}')
    print(f'defend roll: {defend_roll}')

    if attack_roll >= defend_roll:
        defend = 0
        attack = attack
    else:
        attack = 1
        defend = defend

    return attack, defend


def get_stats(coords):
    # get character and stat from map coordinates
    char = (map[int(coords.split(',')[0].strip())][int(coords.split(',')[1].strip())]).split(',')[0]
    stat = (map[int(coords.split(',')[0].strip())][int(coords.split(',')[1].strip())]).split(',')[1]
    # print(f'stat: {char} -- {stat}')
    return str(char), int(stat)


def update_board(attack, defend, attacker, defender):
    # update board spaces baased on outcome of battle
    if attack > defend:
        map[int(attacker.split(',')[0].strip())][int(attacker.split(',')[1].strip())] = f'{attack_char},1'
        map[int(defender.split(',')[0].strip())][int(defender.split(',')[1].strip())] = f'{attack_char},{attack_stat-1}'
    elif attack == defend:
        map[int(attacker.split(',')[0].strip())][int(attacker.split(',')[1].strip())] = f'{attack_char},1'
        map[int(defender.split(',')[0].strip())][int(defender.split(',')[1].strip())] = f'{defend_char},1'
    elif attack < defend:
        map[int(attacker.split(',')[0].strip())][int(attacker.split(',')[1].strip())] = f'{attack_char},1'
        map[int(defender.split(',')[0].strip())][int(defender.split(',')[1].strip())] = f'{defend_char},{defend_stat}'
    for x in map:
        print(x)


if __name__ == '__main__':
    valid = True
    while valid == True:
        for x in map:
            print(x)

        attacker = input('Choose attacker coords (x, y): ')
        defender = input('Choose defender coords (x, y): ')
        attack_char, attack_stat = get_stats(attacker)
        defend_char, defend_stat = get_stats(defender)
        neighbors = neighbor_check(attacker, defender)
        print(neighbors)
        if neighbors == True:
            attack, defend = fight(attack_stat, defend_stat)
            update_board(attack, defend, attacker, defender)
        else:
            continue
