## Создайте программу для игры в ""Крестики-нолики"".

board = [ "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def Board(board):
    print("+---+---+---+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---+---+---+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---+---+---+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---+---+---+")

def Input(player):
    value = False
    while not value:
        playerPos = input(f"Игрок {player} ходит на клетку ")
        try:
            playerPos = int(playerPos)
        except:
            print("Некорректный ввод ")
            continue
        if playerPos >= 1 and playerPos <= 9:
            if str((board[playerPos - 1]) not in "XO"):
                board[playerPos - 1] = player
                value = True
            else:
                print("Эта клетка занята ")
        else:
            print("Введите число от 1 до 9 ")
        
def Win(board):
    winPos = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in winPos:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def Main(board):
    count = 0
    win = False
    while not win:
        Board(board)
        if count % 2 == 0:
            Input("X")
        else:
            Input("O")
        count += 1
        if count > 4:
            temp = Win(board)
            if temp:
                print(f"    {temp} победил ")
                win = True
                break
        if count == 9:
            print("    Ничья ")
            break
    Board(board)

Main(board)