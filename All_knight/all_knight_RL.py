import random

# 盤面の初期化
board = [[False] * 8 for _ in range(8)]

# ナイトの移動可能な方向
moves = [
    (1, 2),
    (2, 1),
    (-1, 2),
    (-2, 1),
    (1, -2),
    (2, -1),
    (-1, -2),
    (-2, -1)
]

# ナイトが移動できるかどうかを判定する関数
def is_valid_move(x, y):
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return False
    return not board[x][y]


# Qテーブルの初期化
Q = {}
for x in range(8):
    for y in range(8):
        Q[(x, y)] = {}
        for dx, dy in moves:
            if is_valid_move(x + dx, y + dy):
                Q[(x, y)][(dx, dy)] = 0

# Q学習のパラメータ
alpha = 0.5
gamma = 0.9
epsilon = 0.1

# ナイトを移動する関数
def move_knight(x, y):
    # ε-greedy法に基づく行動選択
    if random.random() < epsilon:
        dx, dy = random.choice(moves)
    else:
        dx, dy = max(Q[(x, y)], key=Q[(x, y)].get)

    # 移動先の座標
    next_x, next_y = x + dx, y + dy

    # 移動が可能な場合
    if is_valid_move(next_x, next_y):
        # 移動して、ボードにマークする
        board[next_x][next_y] = True

        # Q学習
        max_Q_next = max(Q[(next_x, next_y)].values()) if (next_x, next_y) in Q else 0
        Q[(x, y)][(dx, dy)] += alpha * (1 + gamma * max_Q_next - Q[(x, y)][(dx, dy)])

        return (next_x, next_y)

    # 移動が不可能な場合
    return False

# ゲームのメインループを100回トライアル
for trial in range(100):
    print(f"Trial {trial+1}")
    # 盤面の初期化
    board = [[False] * 8 for _ in range(8)]
    # ナイトの初期位置をランダムに設定
    x, y = random.randint(0, 7), random.randint(0, 7)
    board[x][y] = True
    for i in range(63):
        print(f"Move {i+1}: ({x}, {y})")
        result = move_knight(x, y)
        if not result:
            print("No more moves!")
            break
        x, y = result
    print("Game over!")


