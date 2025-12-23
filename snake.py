from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "#F5BFD9"
FOOD_COLOR = "red"
BACK_GROUND = "BLACK"


#
class Snake :
    def __init__(self) :
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.square = []
        for i in range (0,BODY_PARTS):
            self.coordinates.append([0,0])
        for X,Y in self.coordinates :
            square = canvas.create_rectangle(X,Y,X+SPACE_SIZE,Y+SPACE_SIZE,fill=SNAKE_COLOR,)
            self.square.append(square)

class Food :
    def __init__(self) :
        X = random.randint(0,(GAME_WIDTH//SPACE_SIZE)-1)*SPACE_SIZE
        Y = random.randint(0,(GAME_HEIGHT//SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates = [X,Y]
        canvas.create_oval(X,Y,X+SPACE_SIZE,Y+SPACE_SIZE,fill=FOOD_COLOR,tags="food")

def next_turn(snake,food):
    X,Y = snake.coordinates[0]
    if direction == 'up':
        Y-=SPACE_SIZE
    elif direction == 'down':
        Y+=SPACE_SIZE
    elif direction == 'left':
        X-=SPACE_SIZE
    elif direction == 'right':
        X+=SPACE_SIZE
        
    snake.coordinates.insert(0,(X,Y))

    square = canvas.create_rectangle(X,Y,X+SPACE_SIZE,Y+SPACE_SIZE,fill = SNAKE_COLOR)
    snake.square.insert(0,square)

    if X == food.coordinates[0] and Y == food.coordinates[1]:
        global score

        score += 1

        label.config(text='score : {}'.format(score))
        canvas.delete("food")
        food = Food()
    else :
        del snake.coordinates[-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1]

    if check_collisions (snake):
        game_over()

    else : 
        window.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    X,Y = snake.coordinates[0]
    if X < 0 or X >= GAME_WIDTH:
        return True
    elif Y < 0 or Y >= GAME_HEIGHT:
        return True
    for BODY_PARTS in snake.coordinates[1:]:
        if X == BODY_PARTS[0] and Y == BODY_PARTS[1]:
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text="GAME OVER", font=("InkFree",70),fill= "red",tags="game over")
    #canvas.create_text(350,350,text="GAME OVER", font=("InkFree",70),fill= "red",tags="game over")

window = Tk()
window.title("snake game")
window.resizable(False,False)

score = 0
direction = "down"
label = Label(window,text="score : {}".format(score),font=("InkFree",10))
label.pack()

canvas = Canvas(window,bg=BACK_GROUND,width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

X = int((screen_width/2) - (window_width/2))
Y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{X}+{Y}")
window.bind('<Left>',lambda event : change_direction('left'))
window.bind('<Right>',lambda event : change_direction('right'))
window.bind('<Up>',lambda event : change_direction('up'))
window.bind('<Down>',lambda event : change_direction('down'))

snake = Snake()
food = Food() 
next_turn(snake,food)

window.mainloop()