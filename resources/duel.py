import curses
import time
import random

def duel(stdscr):
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)    # Vida inimigo
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Vida player
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Texto
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Hit
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Obstáculo

    altura, largura = stdscr.getmaxyx()

    player_x = largura // 2 - 15
    player_y = altura - 4

    enemy_x = largura // 2 + 15
    enemy_y = altura - 4

    player_health = 200
    enemy_health = 200

    alcance = 5

    player_jumping = False
    player_jump_peak = player_y - 3

    enemy_jumping = False
    enemy_jump_peak = enemy_y - 3

    obstaculos = []
    # Plataforma chão
    for x in range(2, largura - 2):
        obstaculos.append((x, altura - 3))
    # Blocos no chão
    for x in range(player_x + 3, player_x + 7):
        obstaculos.append((x, altura - 4))
        obstaculos.append((x, altura - 5))
    for x in range(enemy_x - 7, enemy_x - 3):
        obstaculos.append((x, altura - 4))
        obstaculos.append((x, altura - 5))
    # Plataforma alta central
    for x in range(largura // 2 - 5, largura // 2 + 5):
        obstaculos.append((x, altura - 7))
    # Blocos laterais
    for x in range(10, 14):
        obstaculos.append((x, altura - 6))
        obstaculos.append((x, altura - 7))
        obstaculos.append((x, altura - 8))
    for x in range(largura - 14, largura - 10):
        obstaculos.append((x, altura - 6))
        obstaculos.append((x, altura - 7))
        obstaculos.append((x, altura - 8))

    def pode_mover(x, y):
        if x < 2 or x > largura - 6:
            return False
        if y < altura - 10:
            return False
        if (x, y) in obstaculos and y >= altura - 4:
            return False
        return True

    turno_player = True
    hit_animation = 0
    hit_animation_enemy = 0

    while True:
        stdscr.clear()

        for x in range(2, largura - 2):
            stdscr.addch(altura - 2, x, "_", curses.color_pair(3))

        for (ox, oy) in obstaculos:
            stdscr.addch(oy, ox, "#", curses.color_pair(5))

        draw_bar(stdscr, 1, 2, player_health, 10, 20, 2, "Player")
        draw_bar(stdscr, 2, 2, enemy_health, 10, 20, 1, "Enemy")

        draw_player(stdscr, player_x, player_y, hit_animation > 0)
        draw_enemy(stdscr, enemy_x, enemy_y, hit_animation_enemy > 0)

        if turno_player:
            stdscr.addstr(altura - 1, 2, "Seu turno: ← → ↑ (pular), Espaço para atacar, Q para sair", curses.color_pair(3))
        else:
            stdscr.addstr(altura - 1, 2, "Turno do inimigo...", curses.color_pair(3))

        stdscr.refresh()

        if enemy_health <= 0:
            stdscr.addstr(altura // 2, (largura // 2) - 5, "VOCÊ VENCEU!", curses.color_pair(2))
            stdscr.refresh()
            stdscr.getch()
            break
        if player_health <= 0:
            stdscr.addstr(altura // 2, (largura // 2) - 5, "VOCÊ PERDEU!", curses.color_pair(1))
            stdscr.refresh()
            stdscr.getch()
            break

        if turno_player:
            stdscr.timeout(-1)  # Espera indefinidamente pela tecla
            tecla = stdscr.getch()

            if tecla == curses.KEY_LEFT:
                if pode_mover(player_x - 1, player_y):
                    player_x -= 1
            elif tecla == curses.KEY_RIGHT:
                if pode_mover(player_x + 1, player_y):
                    player_x += 1
            elif tecla == curses.KEY_UP:
                if not player_jumping and player_y >= altura - 4:
                    player_jumping = True
            elif tecla == ord(" "):
                if abs(player_x - enemy_x) <= alcance and abs(player_y - enemy_y) <= 1:
                    dano = random.randint(1, 20)  # d20
                    animate_attack(stdscr, player_x + 5, player_y - 1, enemy_x, enemy_y - 1)
                    enemy_health -= dano
                    hit_animation_enemy = 2
                    if enemy_health < 0:
                        enemy_health = 0
                turno_player = False
            elif tecla == ord("q"):
                break
            else:
                continue

            # Atualiza pulo player
            if player_jumping:
                player_y -= 1
                if player_y <= player_jump_peak:
                    player_jumping = False
            else:
                if player_y < altura - 4:
                    player_y += 1

        else:
            # Turno do inimigo: movimenta até conseguir atacar
            time.sleep(0.4)

            distancia = abs(enemy_x - player_x)
            altura_dif = abs(enemy_y - player_y)

            if distancia > alcance or altura_dif > 1:
                # Tenta se mover em direção ao player (prioriza movimento horizontal)
                if enemy_x > player_x and pode_mover(enemy_x - 1, enemy_y):
                    enemy_x -= 1
                elif enemy_x < player_x and pode_mover(enemy_x + 1, enemy_y):
                    enemy_x += 1
                else:
                    # Tenta pular se estiver preso e pode subir
                    if not enemy_jumping and enemy_y >= altura - 4:
                        enemy_jumping = True
            else:
                dano = random.randint(1, 20)  # d20 inimigo
                animate_attack(stdscr, enemy_x - 1, enemy_y - 1, player_x, player_y - 1)
                player_health -= dano
                hit_animation = 2
                if player_health < 0:
                    player_health = 0
                turno_player = True  # depois que ataca, passa turno pro player

            # Atualiza pulo inimigo
            if enemy_jumping:
                enemy_y -= 1
                if enemy_y <= enemy_jump_peak:
                    enemy_jumping = False
            else:
                if enemy_y < altura - 4:
                    enemy_y += 1

        if hit_animation > 0:
            hit_animation -= 1
        if hit_animation_enemy > 0:
            hit_animation_enemy -= 1


def draw_player(stdscr, x, y, hit=False):
    color = curses.color_pair(4) if hit else curses.color_pair(2)
    stdscr.addstr(y - 2, x, r" \O/ ", color)
    stdscr.addstr(y - 1, x, r"  |  ", color)
    stdscr.addstr(y,     x, r" / \ ", color)

def draw_enemy(stdscr, x, y, hit=False):
    color = curses.color_pair(4) if hit else curses.color_pair(1)
    stdscr.addstr(y - 2, x, r" [X] ", color)
    stdscr.addstr(y - 1, x, r" /|\ ", color)
    stdscr.addstr(y,     x, r" / \ ", color)

def animate_attack(stdscr, x_from, y_from, x_to, y_to):
    caminho = range(x_from, x_to) if x_from < x_to else range(x_from, x_to, -1)
    for x in caminho:
        stdscr.addstr(y_from, x, "*", curses.color_pair(4))
        stdscr.refresh()
        time.sleep(0.02)
        stdscr.addstr(y_from, x, " ")
    stdscr.refresh()

def draw_bar(stdscr, y, x, current, maximum, length, color_pair, label=""):
    filled = int((current / maximum) * length)
    bar = "█" * filled + "-" * (length - filled)
    stdscr.addstr(y, x, f"{label} [{bar}] {current}/{maximum}", curses.color_pair(color_pair))

if __name__ == "__main__":
    curses.wrapper(duel)
