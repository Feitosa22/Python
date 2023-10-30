# player = {
#     "nome": "Guilherme",
#     "level": 1,
#     "hp": 100,
#     "mana": 20,
#     "exp": 0,
#     "dano": 5,
#     "velocidade_ataque": 0.8,
# }

# npcs = [
# {"nome": "baby_drag", "dano": 2, "hp": 50, "exp": 20, "velocidade_ataque": 0.5},
# {"nome": "drag", "dano": 5, "hp": 100, "exp": 35, "velocidade_ataque": 1},
# {"nome": "drag_lord", "dano": 10, "hp": 200, "exp": 50, "velocidade_ataque": 1.5},
# {"nome": "demon", "dano": 50, "hp": 800, "exp": 100, "velocidade_ataque": 2},
# {"nome": "oblesc", "dano": 200, "hp": 5000, "exp": 600, "velocidade_ataque": 0.5},
# ]

# - Dia 1 - Tempo de Estudo 


import os

player = {"nome": "Python", "x": 0, "y": 0}
grid_size = {"x": 10, "y": 5}

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def andar(direcao):
    moves = {
        "d": (1, 0), 
        "a": (-1, 0), 
        "w": (0, -1), 
        "s": (0, 1)}
    if direcao in moves:
        new_x = player["x"] + moves[direcao][0]
        new_y = player["y"] + moves[direcao][1]

        if 0 <= new_x < grid_size["x"]:
            player["x"] = new_x
        if 0 <= new_y < grid_size["y"]:
            player["y"] = new_y

def print_grid():
    for y in range(grid_size["y"]):
        for x in range(grid_size["x"]):
            if player['x'] == x and player['y'] == y:
                print("X", end="")
            else:
                print("-", end="")
        print() 

while True:
    clear_screen()
    print("----------------------------------")
    print_grid()
    print("----------------------------------")

    direcao = input("Próxima direção (w, s, d, a, q para sair): ").lower()
    if direcao == "q":
        break
    andar(direcao)
