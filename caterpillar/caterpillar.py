import turtle as t
import random


t.bgcolor("yellow")


caterpillar=t.Turtle()
caterpillar.shape("square")
caterpillar.color("red")
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

caterpillar_2=t.Turtle()
caterpillar_2.shape("square")
caterpillar_2.color("blue")
caterpillar_2.speed(0)
caterpillar_2.penup()
caterpillar_2.hideturtle()

leaf=t.Turtle()
leaf_shape=((0,0), (14,2), (18,6), (20,20), (6,18), (2, 14))
t.register_shape("leaf", leaf_shape)
leaf.shape("leaf")
leaf.color("green")
leaf.speed(0)
leaf.penup()
leaf.hideturtle()

apple=t.Turtle()
apple.shape("circle")
apple.color("red")
apple.speed(0)
apple.penup()
apple.hideturtle()

game_started=False
text_turtle=t.Turtle()
text_turtle.write("Нажмите ПРОБЕЛ, чтобы начать игру", align="center", font=("Arial", 16, "bold"))
text_turtle.hideturtle()

score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

score_turtle2=t.Turtle()
score_turtle2.hideturtle()
score_turtle2.speed(0)

def outside_window():
    left_wall=-t.window_width()/2
    right_wall=t.window_width()/2
    top_wall=t.window_height()/2
    bottom_wall=-t.window_height()/2
    (x,y)=caterpillar.pos()
    (x1,y1)=caterpillar_2.pos()
    outside=(x<left_wall or x>right_wall or y<bottom_wall or y>top_wall) or (x1<left_wall or x1>right_wall or y1<bottom_wall or y1>top_wall)
    return outside
    
def game_over():
    
    caterpillar.color("yellow")
    caterpillar_2.color("yellow")
    leaf.color("yellow")
    t.penup()
    t.hideturtle()
   

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x=t.window_width()/2 - 60
    y=t.window_height()/2 - 60
    score_turtle.setpos(x, y)
    score_turtle.color("red")
    score_turtle.write(str(current_score),align="center", font=("Arial", 40, "bold"))

def display_score2(current_score):
    score_turtle2.clear()
    score_turtle2.penup()
    x=-t.window_width()/2 +60
    y=t.window_height()/2-60
    score_turtle2.setpos(x,y)
    score_turtle2.color("blue")
    score_turtle2.write(str(current_score),align="center", font=("Arial", 40, "bold"))
    
def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-t.window_width()//2,t.window_width()//2))
    leaf.sety(random.randint(-t.window_height()//2,t.window_height()//2))
    leaf.st()

def show_apple():
    apple.st()
    
def place_apple():
    apple.ht()
    apple.setx(random.randint(-t.window_width()//2,t.window_width()//2))
    apple.sety(random.randint(-t.window_height()//2,t.window_height()//2))
    t.ontimer(show_apple, 5000)
    

def start_game():
    global game_started, time
    if game_started:
        return
    game_started=True
    score=0
    score1=0
    text_turtle.clear()
    caterpillar_2_speed=2
    caterpillar_2_length=3
    caterpillar_2.shapesize(1,caterpillar_2_length, 1)
    caterpillar_2.showturtle()
    
    caterpillar_speed=2
    caterpillar_length=3
    caterpillar.shapesize(1,caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    display_score2(score1)
    
    place_apple()
    place_leaf()
    while True:
        caterpillar.forward(caterpillar_speed)
        caterpillar_2.forward(caterpillar_2_speed)
        if caterpillar.distance(leaf) <20:
      
            place_leaf()
           
            caterpillar_length+=1
            caterpillar.shapesize(1, caterpillar_length, 1)
            if caterpillar_speed>1:
                caterpillar_speed-=0.5
            score+=5
            display_score(score)
        if caterpillar_2.distance(leaf) <20:
            
            place_leaf()
            caterpillar_2_length+=1
            caterpillar_2.shapesize(1, caterpillar_2_length, 1)
            if caterpillar_2_speed>1:
                caterpillar_2_speed-=0.5
            score1+=5
            display_score2(score1)

        if caterpillar.distance(apple) <20:
            place_apple()
           
            if caterpillar_length>1:
                caterpillar_length-=1
                caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed+=1
            score+=10
            display_score(score)
        if caterpillar_2.distance(apple) <20:
            place_apple()
            if caterpillar_2_length>1:
                caterpillar_2_length-=1
                caterpillar_2.shapesize(1, caterpillar_2_length, 1)
            caterpillar_2_speed+=1
            score1+=10
            display_score2(score1)
        if outside_window():
            game_over()
            t.color('red')
            if score>score1:
                t.color('red')
                t.write("Конец игры. Победа игрока 2", align="center", font=("Arial", 30, "normal"))
            elif score1>score:
                t.color('blue')
                t.write("Конец игры. Победа игрока 1", align="center", font=("Arial", 30, "normal"))
            else:
                t.color('black')
                t.write("Конец игры. Ничья", align="center", font=("Arial", 30, "normal"))
            break

def move_up():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(270)
def move_right():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(0)
def move_left():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(180)

        
def move_up_2():
    if caterpillar_2.heading()==0 or caterpillar_2.heading()==180:
        caterpillar_2.setheading(90)
def move_down_2():
    if caterpillar_2.heading()==0 or caterpillar_2.heading()==180:
        caterpillar_2.setheading(270)
def move_right_2():
    if caterpillar_2.heading()==90 or caterpillar_2.heading()==270:
        caterpillar_2.setheading(0)
def move_left_2():
    if caterpillar_2.heading()==90 or caterpillar_2.heading()==270:
        caterpillar_2.setheading(180)
    
    
t.onkey(start_game, "space")
t.onkey(move_up, "Up")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")
t.onkey(move_left, "Left")

t.onkey(move_up_2, "w")
t.onkey(move_down_2, "s")
t.onkey(move_right_2, "d")
t.onkey(move_left_2, "a")

t.listen()
t.mainloop()
