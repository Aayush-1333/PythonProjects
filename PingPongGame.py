import turtle as t

# === Create screen ===
sc = t.Screen()
sc.title("Block arcade")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

# === Left paddle ===
left_pad = t.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("green")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# === Right paddle ===
right_pad = t.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("green")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# === Ball of circle shape ===
hit_ball = t.Turtle()
hit_ball.speed(50)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# === Initialize the score ===
leftPlayer_score = 0
rightPlayer_score = 0

# === Display the score ===
sketch = t.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left Player: 0    Right Player: 0", align="center", font=("Comic Sans", 24, "normal"))


# ==== Functions to move paddle vertically ====
def paddleA_Up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddleA_Down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def paddleB_Up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def paddleB_Down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# def pause():
#     t.done()


# === Keyboard bindings ===
sc.listen()
sc.onkeypress(paddleA_Up, "w")
sc.onkeypress(paddleA_Down, "s")
sc.onkeypress(paddleB_Up, "Up")
sc.onkeypress(paddleB_Down, "Down")

# === Main Driver Code ===
while leftPlayer_score < 5 and rightPlayer_score < 5:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # === Checking borders ===
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        leftPlayer_score += 1
        sketch.clear()
        sketch.write("Left Player: {}    Right Player: {}".format(leftPlayer_score, rightPlayer_score),
                     align="center", font=("Comic Sans", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        rightPlayer_score += 1
        sketch.clear()
        sketch.write("Left Player: {}   Right Player: {}".format(leftPlayer_score, rightPlayer_score),
                     align="center", font=("Comic Sans", 24, "normal"))

    # ==== Paddle ball collision ====
    if 360 < hit_ball.xcor() < 370 and right_pad.ycor() - 40 < hit_ball.ycor() < right_pad.ycor() + 40:
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if -370 < hit_ball.xcor() < -360 and left_pad.ycor() - 40 < hit_ball.ycor() < left_pad.ycor() + 40:
        hit_ball.setx(-360)
        hit_ball.dx *= -1

# === tracking scores ===
if leftPlayer_score == 5:
    print("Left Player wins!!")

elif rightPlayer_score == 5:
    print("Right Player wins")
