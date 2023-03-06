from itertools import combinations

player_hp = 100
player_dmg = 0
player_armor = 0

boss_hp = 103
boss_dmg = 9
boss_armor = 2

player_stats = [player_hp, player_dmg, player_armor]
boss_stats = [boss_hp, boss_dmg, boss_armor]

#cost, dmg, armor
dagger = [8,4,0]
shortsword = [10,5,0]
warhammer = [25,6,0]
longsword = [40,7,0]
greataxe = [74,8,0]
weapons = [dagger, shortsword, warhammer, longsword, greataxe]

no_armor = [0,0,0]
leather = [13,0,1]
chainmail = [31,0,2]
splintmail = [53,0,3]
bandedmail = [75,0,4]
platemail = [102,0,5]
armors = [no_armor, leather, chainmail, splintmail, bandedmail, platemail]

no_ring1 = [0,0,0]
no_ring2 = [0,0,0]
dmg1 = [25,1,0]
dmg2 = [50,2,0]
dmg3 = [100,3,0]
def1 = [20,0,1]
def2 = [40,0,2]
def3 = [80,0,3]
rings = [no_ring1, no_ring2, def1, dmg1, def2, dmg2, def3, dmg3]

def sim_battle(player_stats, boss_stats):
    player_hp, player_dmg, player_armor = player_stats
    boss_hp, boss_dmg, boss_armor = boss_stats
    while True:
        if player_dmg > boss_armor:
            boss_hp -= (player_dmg - boss_armor)
        else:
            boss_hp -= 1
        if boss_hp <= 0:
            won = True
            break
        if boss_dmg > player_armor:
            player_hp -= (boss_dmg - player_armor)
        else:
            player_hp -= 1
        if player_hp <= 0:
            won = False
            break
    return won

min_cost = 1000
min_gear = []

max_cost = 0
max_gear = []
for weapon in combinations(weapons,1):
    for armor in combinations(armors,1):
        for ring in combinations(rings,2):
            cost = weapon[0][0] + armor[0][0]
            for r in ring:
                cost += r[0]
            player_stats[1] = weapon[0][1]
            player_stats[2] = armor[0][2]
            for r in ring:
                player_stats[1] += r[1]
                player_stats[2] += r[2]
            if sim_battle(player_stats, boss_stats) and cost < min_cost:
                min_cost = cost
                min_gear = [weapon, armor, ring]
            elif not sim_battle(player_stats, boss_stats) and cost > max_cost:
                max_cost = cost
                max_gear = [weapon, armor, ring]

print(f"The least amount of gold you can spend to still win the fight is: {min_cost}, with weapon: {min_gear[0]}, armor: {min_gear[1]} and rings: {min_gear[2]}")
print(f"The most amount of gold you can spend to still lose the fight is: {max_cost}, with weapon: {max_gear[0]}, armor: {max_gear[1]} and rings: {max_gear[2]}")