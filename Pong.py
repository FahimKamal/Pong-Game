"""
Pong Game
Date: 10.01.2020
"""
import turtle
import winsound

# Creating the window
window = turtle.Screen()
# Set the title
window.title("Pong Game by Fahim")
# Set the background color
window.bgcolor("black")
# Set the screen size
window.setup(width=800, height=600)
# Let the user manually update the screen
window.tracer()

# Score
score_a = 0
score_b = 0

score_write = turtle.Turtle()
score_write.speed(0)
score_write.color("White")
score_write.penup()
score_write.hideturtle()
score_write.goto(0, 260)
score_write.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font= ('Courier', 24, 'normal'))


#       Paddle A
paddle_a = turtle.Turtle()
# Speed of the animation of the paddle
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# Set the size of the paddle Default is(20x20)
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
# Set the default position of the paddle
paddle_a.goto(-390, 0)

#       Paddle B
paddle_b = turtle.Turtle()
# Speed of the animation of the paddle
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
# Set the size of the paddle Default is(20x20)
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
# Set the default position of the paddle
paddle_b.goto(380, 0)

#       Ball
ball = turtle.Turtle()
# Speed of the animation of the paddle
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
# Set the default position of the paddle
ball.goto(0, 0)
# Every time the ball moves by 2 pixels
ball.dx = 4
ball.dy = -4


#       Functions
def paddle_a_up():
    """Function will be used to move the paddle_a up"""
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    """Function will be used to move the paddle_a down"""
    paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    """Function will be used to move the paddle_b up"""
    paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    """Function will be used to move the paddle_b down"""
    paddle_b.sety(paddle_b.ycor() - 20)


# Key board binding
# Take input from keyboard
window.listen()
# When press 'w' paddle_a goes up
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_up, 'W')
# When press 's' padd_a goes down
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_a_down, 'S')
# When press 'Up' paddle_b goes up
window.onkeypress(paddle_b_up, 'Up')
# When press 'Down' padd_b goes down
window.onkeypress(paddle_b_down, 'Down')

# Main game loop
# Every-time the loop runs the window updates
while True:
    window.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        # When ball hits the top border
        ball.sety(290)
        ball.dy *= -1
        # Plays a sound of ball bounce
        winsound.PlaySound('ball_bounce.wav', winsound.SND_ASYNC)
    if ball.ycor() < -290:
        # When ball hits the bottom border
        ball.sety(-290)
        ball.dy *= -1
        # Plays a sound of ball bounce
        winsound.PlaySound('ball_bounce.wav', winsound.SND_ASYNC)
    if ball.xcor() > 390:
        # When ball hits the right border
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_write.clear()
        score_write.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'normal'))
    if ball.xcor() < -390:
        # when ball hits the left border
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_write.clear()
        score_write.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'normal'))

    # Paddle and ball collisions
    if ball.xcor() > 370 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        # Collision with paddle_b on the right side
        ball.dx *= -1
        # Plays a sound of ball bounce
        winsound.PlaySound('ball_bounce.wav', winsound.SND_ASYNC)
    if ball.xcor() < -380 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        # Collision with paddle_a on the left side
        ball.dx *= -1
        # Plays a sound of ball bounce
        winsound.PlaySound('ball_bounce.wav', winsound.SND_ASYNC)
