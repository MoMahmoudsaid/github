import turtle
     
wind = turtle.Screen()
wind.title(' M.M.S.M Game ')
wind.bgcolor('black')
wind.setup(width=800,height=600)
wind.tracer(0)

m1 = turtle.Turtle()
m1.speed(0)
m1.shape("square")
m1.color("green")
m1.shapesize(stretch_wid=7,stretch_len=.5)
m1.penup()
m1.goto(-350,0)                                  

m2 = turtle.Turtle()
m2.speed(0)
m2.shape("square")
m2.color("red")
m2.shapesize(stretch_wid=7,stretch_len=.5)
m2.penup()
m2.goto(350,0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

def m1_up():
    y = m1.ycor()
    y +=20
    m1.sety(y)

score1=0                                                                                                             
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player1 : {}  Player2 : {}".format(score1,score2) ,font=(10),align="center")
  

def m1_down():
    y = m1.ycor()
    y -=20
    m1.sety(y)

def m2_up():
    y = m2.ycor()
    y +=20
    m2.sety(y)

def m2_down():
    y =  m2.ycor()
    y -= 20
    m2.sety(y)





wind.listen() 
wind.onkeypress(m2_up,"w")
wind.onkeypress(m2_down,"s")

wind.onkeypress(m1_up,"Up")
wind.onkeypress(m1_down,"Down")





while True:
    wind.update()   
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dy *= -1
        score1 += 1

        score.clear()
        score.write("Player1 : {}  Player2 : {}".format(score1,score2) ,font=(10),align="center")
     
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dy *= -1
        score2 += 1
        score.clear()
        score.write("Player1 : {}  Player2 : {}".format(score1,score2) ,font=(10),align="center")

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < m2.ycor() + 70 and ball.ycor() > m2.ycor() - 70):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() >- 350) and (ball.ycor() < m1.ycor() + 70 and ball.ycor() > m1.ycor() - 70):
        ball.setx(-340)
        ball.dx *= -1
