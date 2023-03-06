from math import inf
from copy import deepcopy

player_hp = 50
player_armor = 0
player_mana = 500

boss_hp = 71
boss_dmg = 10

#mana cost, damage, heal, armor, mana gain, length
magic_missile = [53, 4, 0, 0, 0, 1]
drain = [73, 2, 2, 0, 0, 1]
shield = [113, 0, 0, 7, 0, 6]
poison = [173, 3, 0, 0, 0, 6]
recharge = [229, 0, 0, 0, 101, 5]

spells = [magic_missile, drain, shield, poison, recharge]

def sim_battle(spell, player_hp, player_armor, current_mana, boss_hp, boss_dmg, mana_spent, effects, win_cost, visited_states):
    visited_states.append((player_hp, boss_hp, current_mana, effects))

    if effects:
        for effect in effects.copy():
            effects.remove(effect)
            boss_hp -= effect[1]
            player_armor += effect[3]
            current_mana += effect[4]
            effect[5] -= 1
            if effect[5] > 0:
                effects.append(effect)
    if boss_hp <= 0:
        win_cost.append(mana_spent)
        return

    if spell[0:5] in [effect[0:5] for effect in effects]:
        return
    current_mana -= spell[0]
    mana_spent += spell[0]
    if current_mana <= 0 or mana_spent >= min(win_cost):
        return
    if spell[5] > 1:
        effects.append(spell.copy())
    else:
        boss_hp -= spell[1]
        player_hp += spell[2]

    if effects:
        for effect in effects.copy():
            effects.remove(effect)
            boss_hp -= effect[1]
            player_armor += effect[3]
            current_mana += effect[4]
            effect[5] -= 1
            if effect[5] > 0:
                effects.append(effect)
    if boss_hp <= 0:
        win_cost.append(mana_spent)
        return
    
    if boss_dmg - player_armor <= 0:
        player_hp -= 1
    else:
        player_hp -= boss_dmg - player_armor
    if player_hp <= 0:
        return
    
    for spell in spells:
        sim_battle(spell.copy(), player_hp, player_armor, current_mana, boss_hp, boss_dmg, mana_spent, deepcopy(effects), win_cost, visited_states)

mana_spent = 0
effects = []
win_cost = [inf]
visited_states = []
for spell in spells:
    sim_battle(spell.copy(), player_hp, player_armor, player_mana, boss_hp, boss_dmg, mana_spent, effects, win_cost, visited_states)

print(min(win_cost))