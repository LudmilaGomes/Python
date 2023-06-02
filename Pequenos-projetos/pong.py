'''

Jogo em Python usando Turtle
Jogo: Pong
Tutorial: https://www.youtube.com/watch?v=XGf2GcyHPhc

'''

import turtle
import time     # importamos o módule time para poder utilizar time.sleep()

# Criamos uma variável 'wind' referente à janela do jogo
wind = turtle.Screen()              # cria a janela
wind.title("Pong Game")             # título da janela
wind.bgcolor("red")                 # cor de fundo (background)
wind.setup(width=800, height=600)   # tamanho da janela (largura, altura)
wind.tracer(0)                      # ON ou OFF; delay para a atualização dos desenhos; se não fizermos isso, as coisas vão rodar de forma mais lenta

# Pontuação
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # cria um objeto do Turtle do módulo turtle
paddle_a.speed(0)           # velocidade da animação
paddle_a.shape("square")    # forma do paddle_a: um quadrado
# por definição, o quadrado criado tem 20 pixels por 20 pixels; então, vamos mudar a forma
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")     # cor do 'paddle_a'
paddle_a.penup()            # garante que o objeto que se movimenta criado não irá desenhar nada na janela
paddle_a.goto(-350, 0)      # coordenadas do 'paddle_a' nos eixos X e Y

# Paddle B
paddle_b = turtle.Turtle()  # cria um objeto do Turtle do módulo turtle
paddle_b.speed(0)           # velocidade da animação
paddle_b.shape("square")    # forma do paddle_a: um quadrado
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")     # cor do 'paddle_a'
paddle_b.penup()            # garante que o objeto que se movimenta criado não irá desenhar nada na janela
paddle_b.goto(350, 0)      # coordenadas do 'paddle_a' nos eixos X e Y

# Bola
ball = turtle.Turtle()  # cria um objeto do Turtle do módulo turtle
ball.speed(0)           # velocidade da animação
ball.shape("square")    # forma do paddle_a: um círculo
# por definição, o quadrado criado tem 20 pixels por 20 pixels
ball.color("white")     # cor do 'paddle_a'
ball.penup()            # garante que o objeto que se movimenta criado não irá desenhar nada na janela
ball.goto(0, 0)         # coordenadas do 'paddle_a' nos eixos X e Y
# separamos o movimento da bola em movimento em X e movimento em Y; toda vez que a bola se move, é de 2 pixels em 2
ball.dx = 2
ball.dy = -2

# Vamos desenhar a pontuação dos jogadores na tela
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: {}   ||   player B: {}".format(score_a, score_b), align="center", font=("Arial", 18, "normal"))

# Funções 
def paddle_a_up():
    y = paddle_a.ycor()     # retorna a coordenada Y do objeto
    y += 20                 # incrementados 20 à variável 'y' (up)
    paddle_a.sety(y)        # setamos o novo valor y (já incrementado) como a coordenada Y do 'paddle_a'

def paddle_a_down():
    y = paddle_a.ycor()     # retorna a coordenada Y do objeto
    y -= 20                 # incrementados 20 à variável 'y' (up)
    paddle_a.sety(y)        # setamos o novo valor y (já incrementado) como a coordenada Y do 'paddle_a'

def paddle_b_up():
    y = paddle_b.ycor()     # retorna a coordenada Y do objeto
    y += 20                 # incrementados 20 à variável 'y' (up)
    paddle_b.sety(y)        # setamos o novo valor y (já incrementado) como a coordenada Y do 'paddle_b'

def paddle_b_down():
    y = paddle_b.ycor()     # retorna a coordenada Y do objeto
    y -= 20                 # incrementados 20 à variável 'y' (up)
    paddle_b.sety(y)        # setamos o novo valor y (já incrementado) como a coordenada Y do 'paddle_b'

# Relacionar o movimento up e down ao teclado
wind.listen()                       # manda o programa a captar inputs do teclado
wind.onkeypress(paddle_a_up, "w")   # a tecla "W" é relacionada à função 'paddle_a_up'
wind.onkeypress(paddle_a_down, "s") # a tecla "S" é relacionada à função 'paddle_a_down'
wind.onkeypress(paddle_b_up, "Up")   # a tecla "W" é relacionada à função 'paddle_a_up'
wind.onkeypress(paddle_b_down, "Down") # a tecla "S" é relacionada à função 'paddle_a_down'

# Main game loop
while 1:
    time.sleep(1/120)   # a velocidade da bola era muito rápida; com 'time.sleep()', podemos ter um controle melhor dessa velocidade
    wind.update()

    # movimento da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # checagem de ultrapassagem das bordas em X e Y
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   # revertemos a direção da bola

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   # revertemos a direção da bola

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1   # revertemos a direção da bola
        score_a += 1
        pen.clear()
        pen.write("player A: {}   ||   player B: {}".format(score_a, score_b), align="center", font=("Arial", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1   # revertemos a direção da bola
        score_b += 1
        pen.clear()
        pen.write("player A: {}   ||   player B: {}".format(score_a, score_b), align="center", font=("Arial", 18, "normal"))
    
    # colisão da bola com paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1   # revertemos a direção da bola

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1   # revertemos a direção da bola