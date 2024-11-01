import turtle
import math

# Функція для малювання фрактала "дерево Піфагора"
def draw_pythagoras_tree(t, length, depth):
    if depth > 0:
        # Малюємо основну гілку
        t.forward(length)
        
        # Зберігаємо поточне положення і кут
        pos = t.position()
        angle = t.heading()
        
        # Малюємо праву гілку
        t.left(45)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
        
        # Повертаємося до початкової позиції і кута
        t.setposition(pos)
        t.setheading(angle)
        
        # Малюємо ліву гілку
        t.right(45)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
        
        # Повертаємося до початкової позиції і кута
        t.setposition(pos)
        t.setheading(angle)
        t.backward(length)

# Основна функція для налаштування і запуску малювання
def start_pythagoras_tree():
    # Запитуємо у користувача рівень рекурсії
    depth = int(input("Введіть рівень рекурсії: "))

    # Налаштовуємо екран turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")

    # Налаштовуємо черепашку
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)  # Починаємо з вертикальної лінії
    t.penup()
    t.goto(0, -screen.window_height() // 3)
    t.pendown()

    # Викликаємо функцію для малювання дерева Піфагора
    draw_pythagoras_tree(t, 100, depth)

    # Завершуємо малювання
    turtle.done()

# Виконання основної функції
if __name__ == "__main__":
    start_pythagoras_tree()
