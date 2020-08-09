import numpy as np


class Game:
    def __init__(self):
        self.current_state = [[], [], []]
        self.moves = 0
        self.score = 0
        self.now = 0
        self.initialize_game()
        self.Lx = 2
        self.Ly = 0


    # random initialization values between -1 to 1
    def initialize_game(self):
        for j in range(3):
            list = np.random.randint(-1, 2, 3)
            for i in list:
                self.current_state[j].append(list[i])

    def draw_board(self):
        for i in range(3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def get_input(self, move, score):
        self.moves = move
        self.score = score
        self.score -= self.current_state[self.Lx][self.Ly]

    def north(self, x, y):
        self.now = self.current_state[x - 1][y]
        self.current_state[x][y] = np.random.randint(-1, 2, 1)
        self.moves -= 1
        self.score -= self.now
        return "up", x - 1, y

    def south(self, x, y):
        self.now = self.current_state[x + 1][y]
        self.current_state[x][y] = np.random.randint(-1, 2, 1)
        self.moves -= 1
        self.score -= self.now
        return "down", x + 1, y

    def west(self, x, y):
        self.now = self.current_state[x][y - 1]
        self.current_state[x][y] = np.random.randint(-1, 2, 1)
        self.moves -= 1
        self.score -= self.now
        return "left", x, y - 1

    def east(self, x, y):
        self.now = self.current_state[x][y + 1]
        self.current_state[x][y] = np.random.randint(-1, 2, 1)
        self.moves -= 1
        self.score -= self.now
        return "right", x, y + 1

    def is_valid_move(self, x, y):
        if x > 2 or y > 2 or x < 0 or y < 0:
            return False
        else:
            return True

    def minimax(self, move, newLx, newLy):
        bestmove = "end"
        Lx = 2
        Ly = 0
        if self.moves == 0 and self.score == 0:
            return "end"
        else:
            # for m in range(self.moves):
            #     for i in range(0, 3):
            #         for j in range(0, 3):

            if self.is_valid_move(newLx - 1, newLy):
                if ((self.is_valid_move(newLx, newLy+1) and (self.current_state[newLx - 1][newLy] >= self.current_state[newLx][newLy + 1]))
                        or (self.is_valid_move(newLx, newLy-1) and (self.current_state[newLx - 1][newLy] >= self.current_state[newLx][newLy - 1]))
                        or (self.is_valid_move(newLx+1, newLy) and (self.current_state[newLx - 1][newLy] >= self.current_state[newLx + 1][newLy]))):
                    bestmove, Lx, Ly = self.north(newLx, newLy)
                    self.minimax(bestmove, Lx, Ly)

            elif self.is_valid_move(newLx + 1, newLy):
                if ((self.is_valid_move(newLx+1, newLy) and (self.current_state[newLx + 1][newLy] >= self.current_state[newLx][newLy + 1]))
                        or (self.is_valid_move(newLx, newLy-1) and (self.current_state[newLx + 1][newLy] >= self.current_state[newLx][newLy - 1]))
                        or (self.is_valid_move(newLx-1, newLy) and (self.current_state[newLx + 1][newLy] >= self.current_state[newLx - 1][newLy]))):
                    bestmove, Lx, Ly = self.south(newLx, newLy)
                    self.minimax(bestmove, Lx, Ly)

            elif self.is_valid_move(newLx, newLy + 1):
                if ((self.is_valid_move(newLx+1, newLy) and (self.current_state[newLx][newLy + 1] >= self.current_state[newLx + 1][newLy]))
                        or (self.is_valid_move(newLx, newLy-1) and (self.current_state[newLx][newLy + 1] >= self.current_state[newLx][newLy - 1]))
                        or (self.is_valid_move(newLx-1, newLy) and (self.current_state[newLx][newLy + 1] >= self.current_state[newLx - 1][newLy]))):
                    bestmove, Lx, Ly = self.east(newLx, newLy)
                    self.minimax(bestmove, Lx, Ly)

            elif self.is_valid_move(newLx, newLy - 1):
                bestmove, Lx, Ly = self.west(newLx, newLy)
                self.minimax(bestmove, Lx, Ly)
        return bestmove, Lx, Ly

    def start(self):
        print("Welcome to Modified add the number game \n    let's start \n")
        x = 2
        y = 0
        moves=""
        numofmoves = int(input("Enter No. moves: "))
        score = int(input("Enter Score: "))
        self.draw_board()
        self.get_input(numofmoves, score)
        while True:
            if numofmoves > 0:
                moves, x, y = self.minimax("", x, y)
                print(moves, self.Lx, self.Ly, "\n", numofmoves, score)
                self.draw_board()
                if moves == "end" and score <= 0:
                    print("Modified Add the number game has been solved!!!")
                    return
                elif moves == "end" and score > 0 and numofmoves == 0:
                    print("Can't be solved !!!")
                    return
                numofmoves -= 1
                score -= self.now
            else:
                return


g = Game()
g.start()