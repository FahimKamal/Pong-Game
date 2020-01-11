"""
Pong Game (Single Player)
Created by: Fahim Kamal Ahmed
Date: 11.01.2020
"""
import turtle
import winsound

# Setup Screen
window = turtle.Screen()
window.title("Pong Game By Fahim")
window.bgcolor("black")
window.setup(width=450, height=600)
window.tracer()

# Player paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=5, stretch_wid=1)
paddle.penup()
paddle.goto(0,-280)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color("red")
ball.penup()
ball.dx = 4
ball.dy = -4

# Score and Life
score = 0
life = 3
score_show = turtle.Turtle()
score_show.speed(0)
score_show.color('white')
score_show.penup()
score_show.hideturtle()
score_show.goto(0,260)
score_show.write(f"Life: {life}    Score: {score}", align='center', font=('Courier', 24, 'normal'))

# Game Over
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color('red')
game_over.penup()
game_over.hideturtle()


# Functions
def pabble_right():
    paddle.setx(paddle.xcor() + 20)

def paddle_left():
    paddle.setx(paddle.xcor() - 20)

def show_score():
    score_show.clear()
    score_show.write(f"Life: {life}    Score: {score}", align='center', font=('Courier', 24, 'normal'))


# Key binding
window.listen()
window.onkeypress(pabble_right, key='Right')
window.onkeypress(paddle_left, key='Left')


# Main Loop
while True:
    window.update()
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border Check
    if ball.xcor() < -215:
        ball.dx *= -1
    if ball.xcor() > 210:
        ball.dx *= -1
    if ball.ycor() < -280:
        ball.dy *= -1
        life -= 1
        show_score()
        ball.goto(0,0)
    if ball.ycor() > 290:
        ball.dy *= -1

    # Ball paddle collision
    if ball.ycor() < -260 and (paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50):
        ball.dy *= -1
        score += 1
        show_score()

    # Game Over
    if not life:
        game_over.write('GAME OVER', align='center', font=('Courier', 24, 'bold'))
        ball.hideturtle()
        score_show.clear()
