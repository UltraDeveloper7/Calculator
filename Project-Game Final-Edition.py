import turtle
import random
import time
import winsound
import math

t = 6
k = 20
s = 0

###########################Classes and Functions#########################

######Classes
class Create_Objects(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()


class Message(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.speed(0)
        self.penup()
        self.hideturtle()


#Function for Main Screen
def Start_Game():
    global Game_State
    Game_State = "Game"
#Function for Instruction Screen       
def Instructions():
    global Game_State
    Game_State = "Instructions"
#Function for End Screen    
def End_Game():
    global Game_State
    Game_State = "Game - Over"



#Function for Paused Screen
is_paused = False
def toggle_pause():
    global is_paused
    global Game_State
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
    Game_State = "Paused"


#Function for Quit Screen
def Quit():
    global running
    running = False


#Making the player move
def move_right():                                       #whenever i call this function: player.xcor -> (player.xcor + 20) and the player moves to the new coordinates 
    x = player.xcor()                
    x += playerspeed
    if x > 350:
        x = 350
    player.setx(x)


def move_left():                                        #whenever i call this function : player.xcor -> (player.xcor - 20) and the player moves to the new coordinates
    x = player.xcor()
    x -= playerspeed
    if x < -350:
        x = -350
    player.setx(x)

###Check for collision(comet,laser)
def collide(comet1, comet2):
    distance = math.sqrt((comet1.xcor() - comet2.xcor())**2 + (comet1.ycor() - comet2.ycor())**2)
    if  1 <= distance <= 80 :
        return True
    else:
        return False

def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate = "fire"
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        # Move bullet right above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


#Making the arrows move
def ball1_move():
    if ball1.direction == "down":
        y = ball1.ycor()                                #y--> variable that contains the current arrow y coordinates 
        ball1.sety(y - t)                               #every time this function is called (all the time: every time it goes into the loop) arrow1 moves to the new coordinates  


def ball2_move():
    if ball2.direction == "down":
        y = ball2.ycor()
        ball2.sety(y - t)



#Set up the player
player = Create_Objects()
turtle.register_shape("player.gif")
player.color("green") 
player.speed(10)                                         # animation speed of the turtle module
player.shape("player.gif")
player.shapesize(stretch_wid=2, stretch_len=2)
player.goto(0, -280)
player.left(90)
playerspeed = 25

#Set up the Bullets
bullet = Create_Objects()
turtle.register_shape("Lazer.gif")
bullet.shape("Lazer.gif")
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.goto(0,-400)
bullet.hideturtle()
bulletspeed=20


#Set up the balls
balls = []
turtle.register_shape("ball.gif")
first_time = True
for _i  in range(2):
    ball = Create_Objects()
    ball.color("red")
    ball.shape("ball.gif")
    ball.shapesize(stretch_wid=2,stretch_len=2)
    ball.speed =  2
    ball.right(90)
    if first_time:
        first_time = False
        ball.goto(random.randint(-40,280),250)
    else:
        ball.goto(random.randint(-280,40),250)
    ball.direction = "down"
    balls.append(ball)
ball1, ball2 = balls


#Indication that the bullet is ready to fire
bulletstate= "ready"


###############################Screen update############################

#Set up the screen
Screen_Width = 1000
Screen_Height = 800
wn = turtle.Screen()
wn.title("The Ultimate Python Game")
wn.bgcolor("black")
wn.setup(Screen_Width + 80, Screen_Height + 40)
wn.cv._rootwindow.resizable(False, False)
wn.tracer(0)                                            # turns off screen updates and makes the turtle go as fast as possible
BorderPen = turtle.Turtle()
BorderPen.speed(0)
BorderPen.color("white")
BorderPen.penup()
BorderPen.setposition(-500,400)
BorderPen.pendown()
BorderPen.pensize(3)
BorderPen.fd(1000)
BorderPen.rt(90)
BorderPen.fd(800)
BorderPen.rt(90)
BorderPen.fd(1000)
BorderPen.rt(90)
BorderPen.fd(800)
BorderPen.hideturtle()

#Comet crash
comet=0
comet_pen = turtle.Turtle()
comet_pen.speed(0)
comet_pen.color("lightblue")
comet_pen.up()
comet_pen.setposition(-470,360)
cometstring = "Comet: {}". format(comet)
comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))
comet_pen.hideturtle()


#Score
lifes = 3
score_board = turtle.Turtle()
score_board.color("white")
score_board.speed(0)
score_board.penup()
score_board.hideturtle()                                #we don't want to see the turtle  
score_board.goto(320,360)
score_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))


#Keyboard bindings                                     #connects a keypress with a function
wn.listen()                                                   #'tell' window to listen for keyboard bindings
wn.onkeypress(move_right,"Right")               #call the move_right function by pressing the Right key
wn.onkeypress(move_left,"Left")                   #call the move_left function by pressing the Left key
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(Start_Game, "S")
wn.onkeypress(Start_Game, "s")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(toggle_pause, "P")
wn.onkeypress(Instructions, "F")
wn.onkeypress(Instructions, "f")
wn.onkeypress(Quit, "Q")
wn.onkeypress(Quit, "q")


##############################Main game loop#########################
Game_Over = False
Victory = False
ball.speed =  2
Game_State = "splash"
running = True
while running :
    if comet != 50:
    
        if lifes > 0:
        
            if not is_paused:
                #First Screen
                if Game_State == "splash":
                    wn.bgpic("splash.gif")
                    player.hideturtle()
                    for b in balls:
                        b.hideturtle()
                    comet_pen.clear()   
                    comet_pen.hideturtle()
                    score_board.hideturtle()
                    score_board.clear()
                    wn.update()
                                 

                #Instructions Screen      
                if Game_State == "Instructions":
                    wn.bgpic("Instructions.gif")
                    player.hideturtle()
                    for b in balls:
                        b.hideturtle()
                    comet_pen.clear()   
                    comet_pen.hideturtle()
                    score_board.hideturtle()
                    score_board.clear()
                    wn.update()
                    
                        
                #Main Screen
                if Game_State == "Game":
                    wn.bgpic("background.gif")
                    player.showturtle()
                    for b in balls:
                        b.showturtle()
                        
                       
                    wn.update()                             #everytime it goes into the loop it updates the screen

                    ball1_move()
                    ball2_move()

                    time.sleep(0.008)              #stops the programme for 0.1s so that i can see the arrow1 (it runs so fast that it disappears immediately


                    if player.xcor() >= 280:
                        player.goto(280,-250)

                    if player.xcor() <= -280:
                        player.goto(-280,-250)

                    #Check collision between bullet and comet
                    if  collide(bullet , ball):
                        winsound.PlaySound("Collision 2.wav", winsound.SND_ASYNC)
                        #Reset bullet
                        bullet.hideturtle()
                        bulletstate="ready"
                        bullet.goto(0,-400)
                        #Reset ball
                        x = random.randint(-200, 200)
                        y = random.randint(100, 250)
                        ball.setposition(x, y)
                        #Update score
                        comet += 1
                        if comet == 0 or comet == 1:
                            comet_pen.color("lightblue")
                            cometstring = "Comet: {}".format(comet)
                            comet_pen.clear()
                            comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))
                        else:
                            comet_pen.color("lightblue")
                            cometstring = "Comets: {}".format(comet)
                            comet_pen.clear()
                            comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))

                     #Move bullet
                    if bulletstate == "fire":
                        y = bullet.ycor()
                        y += bulletspeed
                        bullet.sety(y)

                    #Check bullet΄s position
                    if bullet.ycor() > 150:
                        bullet.hideturtle()
                        bulletstate = "ready"
                        
                        
                    if ball1.ycor() <= -250 and Game_Over == False and Victory == False:
                        ball1.goto(random.randint(-260,30),250)
                        t += 0.05
                        k +=0.1
                        s +=0.5
                        ball.speed += 5

                    if ball2.ycor() <= -250 and Game_Over == False and Victory == False:
                        ball2.goto(random.randint(-30,260),250)
                        t += 0.05
                        k +=0.1
                        s +=0.5
                        ball.speed += 5

                    if ball1.distance(player) < 40 or ball2.distance(player) < 40 or (ball1.distance(player) < 40 and ball2.distance(player) < 40):   #player and ball collisions
                        player.goto(0,-250)
                        winsound.PlaySound("Collision.wav", winsound.SND_ASYNC)
                        ball1.goto(random.randint(-260,30),250)
                        ball2.goto(random.randint(-30,260),250)
                        lifes -= 1
                        ball.speed += -2
                        score_board.clear()
                        score_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))
                        if t > 12 or k > 25:
                           t *= 0.85
                           k *= 0.85

                    if lifes == 1 or lifes == 0:
                        score_board.clear()
                        score_board.color("red")
                        score_board.write("Life: {}".format(lifes), font=("Courier", 24, "normal"))
                  
                elif Game_State == "Game - Over":   
                    wn.bgpic("Game_Over.gif")
                    winsound.PlaySound("Game-Over.wav", winsound.SND_ASYNC)
                    player.hideturtle()
                    bullet.hideturtle()
                    for b in balls:
                        b.hideturtle()
            else:
                #Pause Screen
                if Game_State == "Paused":
                    wn.bgpic("Pause.gif")
                    player.hideturtle()
                    for b in balls:
                        b.hideturtle()
                    wn.update()
                
                
                
        else:
            lifes == 0
            Game_Over = True  
            if Game_Over == True:
                winsound.PlaySound("Game-Over.wav", winsound.SND_ASYNC) 
                wn.bgpic("Game_Over.gif")
                player.hideturtle()
                bullet.hideturtle()
                for b in balls:
                    b.hideturtle()
                comet_pen.clear()   
                comet_pen.hideturtle()
                score_board.hideturtle()
                score_board.clear()
                wn.update()
                message = Message()
                message1 = Message()
                message2 = Message()
                message.goto(0,-80)
                message1.goto(0, -140)
                message2.goto(0, - 200)

                if str(int(s))=='1' or comet == 1 :
                    message.write('Your Score is: {}'.format(str(int(s))), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write("You΄ve crashed {} comet.". format(comet), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write("You could be much better next time!", \
                                    align = "center", font = ("Courier", 25, "normal"))

                elif  20 == comet < 50:
                    message.write("Great job pilot!!", \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write('Your Score is: {} '.format(str(int(s))), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write( "You΄ve crashed {} comets.". format(comet), \
                                    align = "center", font = ("Courier", 45, "normal"))

                elif comet == 0:
                    message.write('Your  Score is: {}'.format(str(int(s))), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write("You didn΄t crash any comet!", \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write("You could be much better next time!", \
                                    align = "center", font = ("Courier", 25, "normal"))
                                 
                else:
                    message.write('Your Score is: {}'.format(str(int(s))),  \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write("You΄ve crashed {} comets.". format(comet), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write("Anyone can be overcomed,so keep practicing!!", \
                                    align = "center", font = ("Courier", 25, "normal"))
                wn.mainloop()

    else:
        #Put comet == 10 for test and only!
        comet == 50
        Victory = True
        if Victory == True:
            winsound.PlaySound("Victory.wav", winsound.SND_ASYNC)      
            wn.bgpic("End.gif")
            message = Message()
            player.hideturtle()
            bullet.hideturtle()
            for b in balls:
                b.hideturtle()
            comet_pen.clear()
            comet_pen.hideturtle()
            score_board.hideturtle()
            score_board.clear()
            wn.update()
            message.write("You Won!!", \
                          align = "center", font = ("Courier", 40, "normal"))
            wn.mainloop()
                
        
#synchronized  with Quit Button      
wn.bye()
