from assets.itens import Itens
from player.status import Char
from assets.config import Config
from player.inventory import inventory
from assets.things import clearScreen
import time
import random
from assets.things import typedPrint, DicesAnimation, d20, attackAnimation, magicAttackAnimation
from assets.itens import Spells
from assets.itens import Enemy

def apply_effects(buffs, debuffs, name):
    to_remove = []
    for effect in debuffs:
        debuffs[effect] -= 1
        if debuffs[effect] <= 0:
            to_remove.append(effect)
    for effect in to_remove:
        del debuffs[effect]
        print(f"{name} não está mais com o efeito {effect}.")

    to_remove = []
    for effect in buffs:
        buffs[effect] -= 1
        if buffs[effect] <= 0:
            to_remove.append(effect)
    for effect in to_remove:
        del buffs[effect]
        print(f"{name} não está mais com o buff {effect}.")

def duel(enemy_name):
    # Pega os dados do inimigo
    enemy = Enemy.enemies.get(enemy_name)
    if not enemy:
        print(f"Inimigo {enemy_name} não encontrado!")
        return

    # Extrai os dados
    enemy_hp = enemy["hp"]
    enemy_attack = enemy["attack"]
    enemy_mana = enemy["mana"]
    enemy_spells = enemy["spells"]
    boss = enemy["boss"]
    drop = enemy["drop"]
    player_buffs = {}
    player_debuffs = {}
    enemy_buffs = {}
    enemy_debuffs = {}
    summons = []
    enemy_summons = []

    while Char.health > 0 and enemy_hp > 0:
        clearScreen()
        print(f"{enemy_name} --- {enemy_hp}HP --- {enemy_attack}ATK --- {enemy_mana}MP")
        print(f"{Char.Name} --- {Char.health}HP --- {Char.attack}ATK --- {Char.mana}MP")
        if summons:
            print("Seus invocados:")
            for i, summon in enumerate(summons):
                print(f"  [{i}] {summon['name']} --- {summon['hp']}HP --- {summon['attack']}ATK")

        print("[1] - Atacar")
        print("[2] - Usar magia")

        option = input("Escolha uma opção: ")

        if not option.isdigit():
            clearScreen()
            print("Opção inválida!")
            time.sleep(1)
            continue
        option = int(option)

        # Player stunned check
        if "atordoar" in player_debuffs:
            clearScreen()
            print("Você está atordoado e perdeu o turno!")
            time.sleep(2)
        else:
            if option == 1:
                roll = d20()
                DicesAnimation()
                typedPrint(f"O dado rolou: {roll}", Config.speed)
                time.sleep(1)
                clearScreen()

                damage = Char.attack * roll
                if "reduzir_ataque" in player_debuffs:
                    damage = int(damage * 0.7)

                enemy_hp -= damage
                attackAnimation()
                clearScreen()
                print(f"Você atacou {enemy_name} e causou {damage} de dano!")
                time.sleep(2)

                # Summons attack
                for summon in summons[:]:
                    if enemy_hp <= 0:
                        break
                    summon_damage = summon['attack']
                    enemy_hp -= summon_damage
                    print(f"Seu invocado {summon['name']} atacou e causou {summon_damage} de dano!")
                    time.sleep(1)
                    if enemy_hp <= 0:
                        break

            elif option == 2:
                if Char.mana <= 0 or len(Char.spells) == 0:
                    clearScreen()
                    print("Você não tem mana ou não possui magias!")
                    time.sleep(1)
                    continue

                clearScreen()
                print("Escolha uma magia:")
                for i, spell_name in enumerate(Char.spells):
                    spell = Spells.spells_database[spell_name]
                    cost = spell['custo']
                    dmg_or_heal = spell.get('dano') or spell.get('cura', '')
                    type_str = 'DANO' if spell['tipo'] == 'dano' else 'CURA' if spell['tipo'] == 'cura' else spell['tipo'].upper()
                    print(f"[{i}] - {spell_name} - {cost}MP - {dmg_or_heal} {type_str}")

                spell_option = input("Escolha uma magia: ")

                if not spell_option.isdigit():
                    clearScreen()
                    print("Opção inválida!")
                    time.sleep(1)
                    continue

                spell_option = int(spell_option)
                if spell_option < 0 or spell_option >= len(Char.spells):
                    clearScreen()
                    print("Opção inválida!")
                    time.sleep(1)
                    continue

                spell_name = Char.spells[spell_option]
                spell = Spells.spells_database[spell_name]

                if Char.mana < spell['custo']:
                    clearScreen()
                    print("Mana insuficiente!")
                    time.sleep(1)
                    continue

                Char.mana -= spell['custo']

                # Damage spell
                if spell['tipo'] == "dano":
                    damage = spell['dano']
                    enemy_hp -= damage
                    magicAttackAnimation(spell['ascii'])
                    print(f"Você usou {spell_name} e causou {damage} de dano!")

                    for summon in summons[:]:
                        if enemy_hp <= 0:
                            break
                        summon_damage = summon['attack']
                        enemy_hp -= summon_damage
                        print(f"Seu invocado {summon['name']} atacou e causou {summon_damage} de dano!")
                        time.sleep(1)

                    # Apply debuff if exists and chance
                    if 'efeito' in spell and spell['tipo'] == 'debuff':
                        if random.randint(1,100) <= spell.get('chance', 100):
                            player_debuffs[spell['efeito']] = spell.get('turnos', 1)
                            print(f"{enemy_name} foi afetado pelo debuff {spell['efeito']}!")

                # Buff spell
                elif spell['tipo'] == "buff":
                    player_buffs[spell['efeito']] = spell.get('turnos', 3)
                    magicAttackAnimation(spell['ascii'])
                    print(f"Você ativou o buff {spell['efeito']} por {spell.get('turnos', 3)} turnos!")

                # Debuff spell (like atordoar)
                elif spell['tipo'] == "debuff":
                    enemy_debuffs[spell['efeito']] = spell.get('turnos', 1)
                    magicAttackAnimation(spell['ascii'])
                    print(f"{enemy_name} foi afetado pelo debuff {spell['efeito']} por {spell.get('turnos', 1)} turnos!")

                # Control spell
                elif spell['tipo'] == "controle":
                    enemy_debuffs[spell['efeito']] = spell.get('turnos', 1)
                    magicAttackAnimation(spell['ascii'])
                    print(f"{enemy_name} foi afetado pelo efeito de controle {spell['efeito']}!")

                # Heal spell
                elif spell['tipo'] == "cura":
                    heal = spell['cura']
                    Char.health += heal
                    magicAttackAnimation(spell['ascii'])
                    print(f"Você usou {spell_name} e curou {heal} de vida!")

                # Summon spell
                elif spell['tipo'] == "invocar":
                    for _ in range(spell.get('quantidade', 1)):
                        summon = {
                            'name': spell['invocar'],
                            'hp': 50,  # exemplo, ajuste conforme quiser
                            'attack': 15
                        }
                        summons.append(summon)
                    magicAttackAnimation(spell['ascii'])
                    print(f"Você invocou {spell.get('quantidade',1)} {spell['invocar']}!")

                time.sleep(2)

        # Check if enemy is dead
        if enemy_hp <= 0:
            clearScreen()
            typedPrint(f"{enemy_name} foi derrotado, e {Char.Name} coletou um {drop} de espólio!", Config.speed)
            time.sleep(2)
            inventory.append(drop)
            break

           # --- Enemy turn ---
        clearScreen()
        print(f"Turno de {enemy_name}...")
        time.sleep(1)

        # Apply buffs/debuffs duration reduction
        apply_effects(player_buffs, player_debuffs, Char.Name)
        apply_effects(enemy_buffs, enemy_debuffs, enemy_name)

        # Check if enemy is stunned/atordoado - skip turn
        if "atordoar" in enemy_debuffs:
            print(f"{enemy_name} está atordoado e perdeu o turno!")
            time.sleep(2)
        else:
            if enemy_mana > 0 and len(enemy_spells) > 0:
                enemy_choice = "magia" if boss else random.choice(["ataque", "magia"])
            else:
                enemy_choice = "ataque"

            if enemy_choice == "ataque":
                roll = d20()
                DicesAnimation()
                damage_enemy = enemy_attack * roll
                if "reduzir_ataque" in enemy_debuffs:
                    damage_enemy = int(damage_enemy * 0.7)

                Char.health -= damage_enemy
                print(f"{enemy_name} atacou e causou {damage_enemy} de dano!")
                time.sleep(2)

            elif enemy_choice == "magia":
                spell_name = random.choice(enemy_spells)
                spell = Spells.spells_database[spell_name]

                if enemy_mana >= spell['custo']:
                    enemy_mana -= spell['custo']

                    if spell['tipo'] == "dano":
                        damage = spell['dano']
                        Char.health -= damage
                        print(f"{enemy_name} usou {spell_name} e causou {damage} de dano!")

                    elif spell['tipo'] == "cura":
                        heal = spell['cura']
                        enemy_hp += heal
                        print(f"{enemy_name} usou {spell_name} e curou {heal} de vida!")

                    elif spell['tipo'] == "invocar":
                        for _ in range(spell.get('quantidade', 1)):
                            summon = {
                                'name': spell['invocar'],
                                'hp': 50,
                                'attack': 15
                            }
                            enemy_summons.append(summon)
                        print(f"{enemy_name} invocou {spell.get('quantidade',1)} {spell['invocar']}!")
                    
                    time.sleep(2)
                else:
                    print(f"{enemy_name} tentou usar magia, mas não tem mana suficiente!")
                    time.sleep(1)

        # Enemy summons attack
        for summon in enemy_summons[:]:
            if Char.health <= 0:
                break
            summon_damage = summon['attack']
            Char.health -= summon_damage
            print(f"O invocado {summon['name']} do inimigo atacou e causou {summon_damage} de dano!")
            time.sleep(1)

        # Remove summons mortos (player)
        for summon in summons[:]:
            if summon['hp'] <= 0:
                summons.remove(summon)
                print(f"Seu invocado {summon['name']} morreu.")
                time.sleep(1)

        # Remove summons mortos (enemy)
        for summon in enemy_summons[:]:
            if summon['hp'] <= 0:
                enemy_summons.remove(summon)
                print(f"O invocado {summon['name']} do inimigo morreu.")
                time.sleep(1)

        # Check if player is dead
        if Char.health <= 0:
            clearScreen()
            print("Você foi derrotado...")
            time.sleep(3)
            gameOver(enemy_name)