import pygame
import os
from abc import ABC, abstractmethod

#pygame display setup
WIDTH, HEIGHT = 800,800
ROWS, COLS = 8,8
SQUARE = WIDTH/ROWS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption('chess')

#colors
WHITE = (200,200,200)
BLACK = (25,25,25)

#import piece pics
BP_IMG = pygame.image.load(os.path.join('images', 'bp.png'))
WP_IMG = pygame.image.load(os.path.join('images', 'wp.png'))
BR_IMG = pygame.image.load(os.path.join('images', 'br.png'))
WR_IMG = pygame.image.load(os.path.join('images', 'wr.png'))
BN_IMG = pygame.image.load(os.path.join('images', 'bn.png'))
WN_IMG = pygame.image.load(os.path.join('images', 'wn.png'))
BB_IMG = pygame.image.load(os.path.join('images', 'bb.png'))
WB_IMG = pygame.image.load(os.path.join('images', 'wb.png'))
BQ_IMG = pygame.image.load(os.path.join('images', 'bq.png'))
WQ_IMG = pygame.image.load(os.path.join('images', 'wq.png'))
BK_IMG = pygame.image.load(os.path.join('images', 'bk.png'))
WK_IMG = pygame.image.load(os.path.join('images', 'wk.png'))

#Board array
BOARD = [[None for i in range(COLS)] for j in range(ROWS)]


class Piece(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def is_valid(self):
        pass

    def draw(self, WIN):
        WIN.blit(self.img, (self.col * SQUARE + 20, self.row * SQUARE + 20))

class Pawn(Piece):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.hasMoved = False
        self.img = BP_IMG if color == 'b' else WP_IMG
        self.letter = 'p'

    def is_valid(self, newPos):
        curPos = (self.row, self.col)
        if BOARD[newPos[0]][newPos[1]]:
            if self.color == 'b':
                if (newPos[0] - 1 == curPos[0]) and (newPos[1] - 1 == curPos[1] or newPos[1] + 1 == curPos[1]):
                    return True
            else:
                if (newPos[0] + 1 == curPos[0]) and (newPos[1] - 1 == curPos[1] or newPos[1] + 1 == curPos[1]):
                    return True
        else:
            if self.color == 'b':
                if self.hasMoved:
                    if newPos[0] - 1 == curPos[0]:
                        return True
                else:
                    if newPos[0] - 1 == curPos[0] or newPos[0] - 2 == curPos[0]:
                        return True
            else:
                if self.hasMoved:
                    if newPos[0] + 1 == curPos[0]:
                        return True
                else:
                    if newPos[0] + 1 == curPos[0] or newPos[0] + 2 == curPos[0]:
                        return True
        return False
        

    def draw(self, WIN):
        super().draw(WIN)

class Rook(Piece):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.hasMoved = False
        self.img = BR_IMG if color == 'b' else WR_IMG
        self.letter = 'r'

    def is_valid(self, newPos):
        curPos = (self.row, self.col)
        if curPos[0] == newPos[0]:
            if curPos[1] > newPos[1]:
                for j in range(newPos[1] + 1, curPos[1]):
                    if BOARD[curPos[0]][j]:
                        return False
                return True
            else:
                for j in range(curPos[1] + 1, newPos[1]):
                    if BOARD[curPos[0]][j]:
                        return False
                return True
        elif curPos[1] == newPos[1]:
            if curPos[0] > newPos[0]:
                for i in range(newPos[0] + 1, curPos[0]):
                    if BOARD[i][curPos[1]]:
                        return False
                return True
            else:
                for i in range(curPos[0] + 1, newPos[0]):
                    if BOARD[i][curPos[1]]:
                        return False
                return True
            
        return False

    def draw(self, WIN):
        super().draw(WIN)

class Knight(Piece):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.hasMoved = False
        self.img = BN_IMG if color == 'b' else WN_IMG
        self.letter = 'n'

    def is_valid(self, newPos):
        pass

    def draw(self, WIN):
        super().draw(WIN)

class Bishop(Piece):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.hasMoved = False
        self.img = BB_IMG if color == 'b' else WB_IMG
        self.letter = 'b'

    def is_valid(self, newPos):
        pass

    def draw(self, WIN):
        super().draw(WIN)

class King(Piece):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.hasMoved = False
        self.img = BK_IMG if color == 'b' else WK_IMG
        self.letter = 'k'

    def is_valid(self, newPos):
        pass

    def draw(self, WIN):
        super().draw(WIN)

class Queen(Piece):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.hasMoved = False
        self.img = BQ_IMG if color == 'b' else WQ_IMG
        self.letter = 'q'

    def is_valid(self, newPos):
        pass

    def draw(self, WIN):
        super().draw(WIN)


#make all pieces in starting position and add them to the board
def make_pieces():
    #black
    for j in range(COLS):
        BOARD[1][j] = Pawn(1 , j, 'b')

    BOARD[0][0] = Rook(0 , 0, 'b')
    BOARD[0][7] = Rook(0 , 7, 'b')

    BOARD[0][1] = Bishop(0 , 1, 'b')
    BOARD[0][6] = Bishop(0 , 6, 'b')

    BOARD[0][2] = Knight(0 , 2, 'b')
    BOARD[0][5] = Knight(0 , 5, 'b')

    BOARD[0][3] = Queen(0 , 3, 'b')

    BOARD[0][4] = King(0 , 4, 'b')

    #white
    for j in range(COLS):
        BOARD[6][j] = Pawn(6 , j, 'w')

    BOARD[7][0] = Rook(7 , 0, 'w')
    BOARD[7][7] = Rook(7 , 7, 'w')

    BOARD[7][1] = Bishop(7 , 1, 'w')
    BOARD[7][6] = Bishop(7 , 6, 'w')

    BOARD[7][2] = Knight(7 , 2, 'w')
    BOARD[7][5] = Knight(7 , 5, 'w')

    BOARD[7][4] = Queen(7 , 4, 'w')

    BOARD[7][3] = King(7 , 3, 'w')

#draws chess board onto screen
def draw_board():
    WIN.fill(WHITE)
    alt = 0
    for row in range(ROWS):
        for col in range(COLS):
            if (col + alt) % 2 == 0:
                pygame.draw.rect(WIN, WHITE, (row * SQUARE, col * SQUARE, SQUARE, SQUARE))
            else:
                pygame.draw.rect(WIN, BLACK, (row * SQUARE, col * SQUARE, SQUARE, SQUARE))
        alt += 1

def draw_pieces():
    for i in range(ROWS):
        for j in range(COLS):
            if BOARD[i][j]:
                #print(i, j)
                BOARD[i][j].draw(WIN)

def calculate_square(pos):
    col = int(pos[0] / 100)
    row = int(pos[1] / 100)
    return (row, col)

def print_board():
    for i in range(ROWS):
        print()
        for j in range(COLS):
            if BOARD[i][j]:
                print(BOARD[i][j].letter, end = " ")
            else:
                print(0, end = " ")

def move(pos1, pos2):
    square1 = calculate_square(pos1)
    square2 = calculate_square(pos2)
    moving_piece = BOARD[square1[0]][square1[1]]
    captured_piece = BOARD[square2[0]][square2[1]]
    if moving_piece:
        print(square1, square2)
        print_board()
        if moving_piece.is_valid(square2):
            moving_piece.hasMoved = True
            moving_piece.row = square2[0]
            moving_piece.col = square2[1]
            BOARD[square1[0]][square1[1]] = None
            BOARD[square2[0]][square2[1]] = moving_piece

def main():
    clock = pygame.time.Clock()
    running = True
    make_pieces()
    click1 = None
    click2 = None

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not click1:
                    click1 = pos
                else:
                    click2 = pos
                if click1 and click2:
                    move(click1, click2)
                    click1 = None
                    click2 = None

        draw_board()
        draw_pieces()
        pygame.display.update()
        


    pygame.quit()
if __name__ == '__main__':
    main()