# tic_tac_toe/game/models.py
from django.db import models

class Game(models.Model):
    # Define your model fields here
    board = models.JSONField(default=lambda: [['' for _ in range(3)] for _ in range(3)])
    turn = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, blank=True, null=True)
    
    def make_move(self, row, col):
        if self.board[row][col] == '' and self.winner is None:
            self.board[row][col] = self.turn
            self.check_winner()
            self.turn = 'O' if self.turn == 'X' else 'X'
            self.save()

    def reset(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.turn = 'X'
        self.winner = None
        self.save()

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                self.winner = row[0]
                return
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                self.winner = self.board[0][col]
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.winner = self.board[0][0]
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.winner = self.board[0][2]
            return
        if all(cell != '' for row in self.board for cell in row):
            self.winner = 'Draw'

    def get_board(self):
        return self.board

    def get_current_turn(self):
        return self.turn

    def is_draw(self):
        return self.winner == 'Draw'
