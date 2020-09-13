import turtle
import random
import time
import copy
import winsound


counter = 0
div = 18   #decides the speed of the walls
score = 0
highscore = 0
flag = 0



wn = turtle.Screen()
wn.title("Cave Journey")
wn.bgcolor("black")
wn.setup(width=550, height=550)
wn.tracer(0)

ss = turtle.Turtle()
ss.speed(0)
ss.shape("classic")
ss.shapesize(1, 2)
ss.color("white")
ss.left(90)
ss.penup()
ss.goto(0, -200)

lb = turtle.Turtle()
lb.speed(0)
lb.shape("square")
lb.shapesize(15, 30)
lb.color("white")
lb.left(90)
lb.penup()
lb.goto(-440, -76)

lr = turtle.Turtle()
lr.speed(0)
lr.shape("square")
lr.shapesize(15, 30)
lr.color("white")
lr.left(90)
lr.penup()
lr.goto(440, -76)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-140, 240)

intro = turtle.Turtle()
intro.speed(0)
intro.shape("square")
intro.color("white")
intro.penup()
intro.hideturtle()
intro.goto(0, -50)

kb = turtle.Turtle()
kb.speed(0)
kb.shape("square")
kb.color("green")
kb.penup()
kb.hideturtle()
kb.goto(-150, -200)





def tol():
    n = random.randint(-60, 60)
    return n


def tol2():
    n = random.randint(20, 25)
    return n


def go_left():
    x = ss.xcor()
    ss.setx(x - 10)


def go_right():
    x = ss.xcor()
    ss.setx(x + 10)



wn.listen()
wn.onkeypress(go_left, "z")
wn.onkeypress(go_right, "m")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "Z")
wn.onkeypress(go_right, "M")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_right, "D")


walll = []
wallr = []


while len(wallr) < 20:  # to create a fixed number of walls
    t = tol()
    obsr = turtle.Turtle()
    obsr.color("white")
    obsr.shape("square")
    obsr.penup()
    obsr.shapesize(1.45, 15)
    obsr.goto(200, 1000)
    wallr.append(obsr)

    obsl = turtle.Turtle()
    obsl.color("white")
    obsl.shape("square")
    obsl.penup()
    obsl.shapesize(1.45, 15)
    obsl.goto(-200, 1000)
    walll.append(obsl)






for index in range(20):  # to arrange the walls in the initial page

    y = (index - 11) * 30
    walll[index].sety(y)
    wallr[index].sety(y)

def arrwall():
    for index in range(17):  # if the walls just above gives too less space to move
        t2 = tol2()
        if (walll[index].xcor() - wallr[index + 1].xcor()) > -340:
            wallr[index + 1].setx(wallr[index + 1].xcor() + t2)
        if (wallr[index].xcor() - walll[index + 1].xcor()) < 340:
            walll[index + 1].setx(walll[index + 1].xcor() - t2)
        if (walll[index].xcor() - wallr[index + 2].xcor()) > -340:
            wallr[index + 2].setx(wallr[index + 2].xcor() + t2)
        if (wallr[index].xcor() - walll[index + 2].xcor()) < 340:
            walll[index + 2].setx(walll[index + 2].xcor() - t2)
        if (walll[index].xcor() - wallr[index + 3].xcor()) > -340:
            wallr[index + 3].setx(wallr[index + 3].xcor() + t2)
        if (wallr[index].xcor() - walll[index + 3].xcor()) < 340:
            walll[index + 3].setx(walll[index + 3].xcor() - t2)


def loopwall():
    t = tol()
    wallr[0].goto(200 + t, 240)
    walll[0].goto(-200 + t, 240)
    wallr.append(wallr[0])
    walll.append(walll[0])
    del wallr[0]
    del walll[0]
    for index in range(20):  # to move the walls down
        y = wallr[index].ycor()
        walll[index].sety(y - 30)
        wallr[index].sety(y - 30)


def setwalltozero():
    for index in range(20):
        walll[index].setx(-200)
        wallr[index].setx(200)



while True:

    while flag == 0:
        winsound.PlaySound("Intro", winsound.SND_ASYNC | winsound.SND_ALIAS)
        intro.write("CAVE \nJOURNEY", align="center", font=("BankGothic Md BT", 60, "normal"))
        kb.write("Key Bindings\nMove Left: Z or A\nMove Right: M or D", align="center", font=("BankGothic Md BT", 13, "normal"))
        flag = 1
        time.sleep(7)
        intro.clear()
        kb.clear()





    while flag == 1:

        if counter % div == 0:
            arrwall()

        if counter % div == 0:
            loopwall()
            score += 1
            if score > highscore:
                highscore = copy.copy(score)
            if score % 100 == 0 and div>2:
                div -= 1

        wn.update()

        if ss.xcor() - walll[5].xcor() < 157 or wallr[5].xcor() - ss.xcor() < 157:
            intro.color("red")
            intro.write("CRASHED", align="center", font=("BankGothic Md BT", 70, "normal"))
            time.sleep(3)
            ss.setx(0)
            score = 0
            setwalltozero()
            div = 18
            intro.clear()

        pen.clear()
        pen.write("Score: {}                            High Score: {}".format(score, highscore), align="left", font=("Calibri", 15, "normal"))

        counter += 1































