import turtle
import math
import time
import random

# Configuração da tela
screen = turtle.Screen()
screen.bgcolor("#0d0d1a")
screen.title("❤️ Surpresa")

# Tartaruga do coração
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

# Tartaruga do texto
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

# Tartaruga do fundo
bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.penup()

# Tartaruga do botão
button = turtle.Turtle()
button.hideturtle()
button.penup()


# Fundo com estrelas
def draw_background_stars():
    bg.color("white")
    for _ in range(80):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        bg.goto(x, y)
        bg.dot(random.randint(2, 4))


# Função do coração
def heart(scale, color):
    t.color(color)
    t.begin_fill()
    for i in range(360):
        x = scale * 16 * math.sin(math.radians(i))**3
        y = scale * (
            13 * math.cos(math.radians(i))
            - 5 * math.cos(2 * math.radians(i))
            - 2 * math.cos(3 * math.radians(i))
            - math.cos(4 * math.radians(i))
        )
        t.goto(x, y)
    t.end_fill()


# Texto máquina de escrever
def typewriter(text, x, y):
    text_turtle.goto(x, y)
    text_turtle.color("white")
    for i in range(len(text)):
        text_turtle.clear()
        text_turtle.write(
            text[:i+1],
            align="center",
            font=("Segoe UI", 20, "bold")
        )
        time.sleep(0.05)


# Função que inicia a animação
def start_animation(x, y):
    button.clear()

    # Desenha o fundo
    draw_background_stars()

    # Desenha os corações rapidamente
    for s in range(18, 13, -1):
        t.penup()
        t.goto(0, -10)
        t.pendown()
        heart(s, "#330000")
        time.sleep(0.1)  # tempo reduzido

    # Coração principal
    t.penup()
    t.goto(0, -10)
    t.pendown()
    heart(14, "#ff1a1a")

    # Texto no centro
    typewriter("Feliz Valentine's Day ❤️", 0, -10)


# Desenha o botão
def draw_button():
    button.goto(0, -50)
    button.color("white")
    button.write(
        "Clique aqui para começar ❤️",
        align="center",
        font=("Segoe UI", 18, "bold")
    )


draw_button()

# Evento de clique
screen.onclick(start_animation)

turtle.done()