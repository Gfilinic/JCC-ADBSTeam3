import pygame as p
import Game

p.init()
WIDTH=HEIGHT=512
DIMENSIONS=8
SqSize= HEIGHT // DIMENSIONS    
Max_FPS=10
Models={}


def loadModels():
    chessPieces=['wP','wR','wN','wB','wK','wQ','bP','bR','bN','bB','bK','bQ']
    for piece in chessPieces:
        Models[piece]=p.transform.scale(p.image.load("BackEnd\Models\\"+piece+".png"),(SqSize,SqSize)) 

def drawSquares(screen):
    colors=[p.Color("light gray"),p.Color("crimson")]
    for row in range(DIMENSIONS):
        for column in range(DIMENSIONS):
            color=colors[((row+column)%2)]
            p.draw.rect(screen,color,p.Rect(column*SqSize,row*SqSize,SqSize,SqSize)) 

def drawPieces(screen,board):
    for row in range(DIMENSIONS):
        for column in range(DIMENSIONS):
            piece=board[row][column]
            if piece != '__':
                screen.blit(Models[piece],p.Rect(column*SqSize,row*SqSize,SqSize,SqSize))    

def drawBoard(screen,boardState):
    drawSquares(screen)
    drawPieces(screen,boardState.board)

def setUpScreen():
    screen=p.display.set_mode((WIDTH,HEIGHT))
    screen.fill(p.Color("white"))
    return screen


    

def main():
    screen=setUpScreen()
    clock=p.time.Clock()
    boardState=Game.BoardState()
    loadModels()
    active=True
    selectedSquare=()
    playerClicks=[]
    while active:
       for e in p.event.get():
        if e.type==p.QUIT:
            active=False
        elif e.type==p.MOUSEBUTTONDOWN:
            location=p.mouse.get_pos()
            selectedColumn=location[0]//SqSize
            selectedRow=location[1]//SqSize
            
            if selectedSquare==(selectedRow,selectedColumn):
                selectedSquare=()
                playerClicks=[]
            else:
                selectedSquare=(selectedRow,selectedColumn)
                playerClicks.append(selectedSquare)

            if len(playerClicks)==2:
                move = Game.Movement(playerClicks[0],playerClicks[1],boardState.board)
                print(move.getChessNotation())
                boardState.makeMove(move)
                selectedSquare=()
                playerClicks=[]


        drawBoard(screen,boardState)
        clock.tick(Max_FPS)
        p.display.flip()
    
if __name__=="__main__":
    main()
