import turtle
import random

def draw_branch(t, length, depth, angle_range=(20, 45), shrink=0.75):
    if depth <= 0 or length < 3:
        # Рисуем "листья" на концах
        t.dot(4, random.choice(["lime", "yellow", "orange", "red"]))
        return

    # Случайный цвет ствола/ветви (от тёмно-коричневого до зелёного)
    r = max(100, int(139 - depth * 8))  # коричневый → зелёный
    g = max(60, int(60 + depth * 15))
    b = 40
    t.color(r, g, b)

    # Толщина линии зависит от глубины
    t.width(max(1, depth // 2))

    # Рисуем текущую ветвь
    t.forward(length)

    # Случайные углы для левой и правой ветвей
    angle1 = random.uniform(*angle_range)
    angle2 = random.uniform(*angle_range)

    # Левая ветвь
    t.left(angle1)
    draw_branch(t, length * shrink, depth - 1, angle_range, shrink)

    # Правая ветвь
    t.right(angle1 + angle2)
    draw_branch(t, length * shrink, depth - 1, angle_range, shrink)

    # Возвращаемся назад
    t.left(angle2)
    t.backward(length)

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)
screen.title("Большое случайное дерево")

# Черепашка
t = turtle.Turtle()
t.speed(0)
t.left(90)  # Направление вверх

# Позиционируем внизу по центру
t.penup()
t.goto(0, -250)
t.pendown()

# Случайные параметры для разнообразия
initial_length = random.randint(100, 140)
max_depth = random.randint(8, 11)          # Больше уровней = больше ветвей
angle_min = random.randint(15, 25)
angle_max = random.randint(30, 50)
shrink_factor = random.uniform(0.65, 0.78)

# Рисуем дерево
draw_branch(t, initial_length, max_depth, (angle_min, angle_max), shrink_factor)

t.hideturtle()
screen.exitonclick()