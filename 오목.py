import tkinter as tk
from tkinter import messagebox
import random

BOARD_SIZE = 15
CELL_SIZE = 40
MARGIN = 30
STONE_RADIUS = 15

EMPTY = " "
PLAYER_X = "X"  
PLAYER_O = "O"  

class Gomoku:
    def __init__(self, root):
        self.root = root
        self.root.title("오목 🎯 (사람 vs AI)")
        self.difficulty = tk.StringVar(value="Normal")  

        
        self.canvas = tk.Canvas(root,
                                width=BOARD_SIZE*CELL_SIZE + MARGIN*2,
                                height=BOARD_SIZE*CELL_SIZE + MARGIN*2,
                                bg="burlywood3")
        self.canvas.pack()

        
        frame = tk.Frame(root)
        frame.pack(pady=5)
        tk.Label(frame, text="난이도 🎚️").pack(side="left", padx=5)
        for level in ["Easy", "Normal", "Hard"]:
            tk.Radiobutton(frame, text=level, variable=self.difficulty, value=level).pack(side="left")

        self.canvas.bind("<Button-1>", self.handle_click)
        self.reset_game()

    def reset_game(self):
        self.board = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.current = PLAYER_X  
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
       
        for i in range(BOARD_SIZE):
            x = MARGIN + i*CELL_SIZE
            self.canvas.create_line(MARGIN, x, MARGIN + (BOARD_SIZE-1)*CELL_SIZE, x)
            self.canvas.create_line(x, MARGIN, x, MARGIN + (BOARD_SIZE-1)*CELL_SIZE)
        
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] != EMPTY:
                    self.draw_stone(i, j, self.board[i][j])

    def draw_stone(self, x, y, player):
        cx = MARGIN + x*CELL_SIZE
        cy = MARGIN + y*CELL_SIZE
        color = "black" if player == PLAYER_X else "white"
        self.canvas.create_oval(cx-STONE_RADIUS, cy-STONE_RADIUS,
                                cx+STONE_RADIUS, cy+STONE_RADIUS,
                                fill=color, outline="black")

    def handle_click(self, event):
        if self.current != PLAYER_X:
            return

        x = round((event.x - MARGIN) / CELL_SIZE)
        y = round((event.y - MARGIN) / CELL_SIZE)

        if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and self.board[x][y] == EMPTY:
            self.board[x][y] = PLAYER_X
            self.draw_board()
            if self.check_winner(PLAYER_X):
                messagebox.showinfo("결과", "🎉 당신이 이겼습니다!")
                self.ask_restart()
                return

            self.current = PLAYER_O
            self.root.after(500, self.ai_turn)

    def ai_turn(self):
        move = self.find_best_move()
        if move:
            x, y = move
            self.board[x][y] = PLAYER_O
            self.draw_board()
            if self.check_winner(PLAYER_O):
                messagebox.showinfo("결과", "😈 컴퓨터가 이겼습니다!")
                self.ask_restart()
                return
        self.current = PLAYER_X

    def find_best_move(self):
        difficulty = self.difficulty.get()
        best_score = -float('inf')
        best_move = None

        
        if difficulty == "Easy" and random.random() < 0.3:
            return random.choice(self.available_moves())

        for x, y in self.available_moves():
        
            self.board[x][y] = PLAYER_O
            attack_score = self.evaluate_position(PLAYER_O, x, y)
        
            self.board[x][y] = PLAYER_X
            defense_score = self.evaluate_position(PLAYER_X, x, y)
            self.board[x][y] = EMPTY

           
            if difficulty == "Hard":
                total_score = attack_score * 1.2 + defense_score * 1.1
            elif difficulty == "Normal":
                total_score = attack_score + defense_score * 0.9
            else:  
                total_score = attack_score + defense_score * 0.7

            if total_score > best_score:
                best_score = total_score
                best_move = (x, y)

        return best_move

    def available_moves(self):
        return [(x, y) for x in range(BOARD_SIZE) for y in range(BOARD_SIZE)
                if self.board[x][y] == EMPTY]

    def evaluate_position(self, player, x, y):
        """해당 위치의 점수를 계산 (패턴 기반)"""
        directions = [(1,0),(0,1),(1,1),(1,-1)]
        score = 0
        opponent = PLAYER_X if player == PLAYER_O else PLAYER_O

        for dx, dy in directions:
            count, block = 1, 0

           
            nx, ny = x + dx, y + dy
            while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[nx][ny] == player:
                count += 1
                nx += dx
                ny += dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[nx][ny] == opponent:
                block += 1

           
            nx, ny = x - dx, y - dy
            while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[nx][ny] == player:
                count += 1
                nx -= dx
                ny -= dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[nx][ny] == opponent:
                block += 1

            
            if count >= 5:
                score += 100000
            elif count == 4:
                score += 10000 if block == 0 else 5000
            elif count == 3:
                score += 1000 if block == 0 else 200
            elif count == 2:
                score += 100 if block == 0 else 30

        return score

    def check_winner(self, player):
        directions = [(1,0),(0,1),(1,1),(1,-1)]
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.board[x][y] == player:
                    for dx, dy in directions:
                        count = 1
                        nx, ny = x + dx, y + dy
                        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[nx][ny] == player:
                            count += 1
                            nx += dx
                            ny += dy
                        if count >= 5:
                            return True
        return False

    def ask_restart(self):
        again = messagebox.askyesno("다시 시작?", "게임을 다시 시작하시겠습니까?")
        if again:
            self.reset_game()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    Gomoku(root)
    root.mainloop()
