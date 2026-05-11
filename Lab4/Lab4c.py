import math
import turtle


def draw_rectangle(length,height,color):
    stripe = height /13 
    t = turtle.Turtle()
    t.speed(100)
    for i in range(13):
        if i % 2 == 0:
            t.fillcolor("red")
        else:
            t.fillcolor("white")
        t.begin_fill()
        t.forward(length)
        t.left(90)
        t.forward(stripe)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(stripe)
        t.left(90)
        t.end_fill()
        t.penup()
        t.goto(0, -(i+1)*stripe)
        t.pendown()
    if color == "red":
        t.penup()
        t.goto(0, stripe)
        t.pendown()

def draw_star(size):
    hoist = size / 0.0616
    canton_w = 1.9 * hoist * 2 / 5
    canton_h = hoist * 7 / 13
    stripe = hoist / 13

    E = canton_h / 10        
    G = canton_w / 12       
    K = stripe * 4 / 5     
    circumradius = K / 2     
    inner_radius = circumradius * math.sin(math.radians(18)) / math.sin(math.radians(54))
    
    t = turtle.Turtle()
    t.speed(100)
    t.hideturtle()

    t.penup()
    t.goto(0, stripe)
    t.setheading(0)
    t.pendown()
    t.fillcolor("blue")
    t.pencolor("blue")
    t.begin_fill()
    for length in [canton_w, canton_h, canton_w, canton_h]:
        t.forward(length)
        t.right(90)
    t.end_fill()

    for row in range(10):
        cols = 6 if row % 2 == 0 else 5
        x_offset = G if row % 2 == 0 else G * 2

        for col in range(cols):
            sx = x_offset + col * G * 2
            sy = stripe - (E * (row + 0.5))

            t.penup()
            t.goto(sx, sy)
            t.setheading(90)  
            t.pendown()
            t.fillcolor("white")
            t.pencolor("white")
            t.begin_fill()
            for i in range(5):
               
                angle = 90 + i * 72
                ox = sx + circumradius * math.cos(math.radians(angle))
                oy = sy + circumradius * math.sin(math.radians(angle))
                inner_angle = angle + 36
                ix = sx + inner_radius * math.cos(math.radians(inner_angle))
                iy = sy + inner_radius * math.sin(math.radians(inner_angle))
                t.penup()
                if i == 0:
                    t.goto(ox, oy)
                    t.pendown()
                else:
                    t.goto(ox, oy)
                t.goto(ix, iy)
            ox = sx + circumradius * math.cos(math.radians(90))
            oy = sy + circumradius * math.sin(math.radians(90))
            t.goto(ox, oy)
            t.end_fill()


def draw_flag(height):
    draw_rectangle(1.9*height, height, "red")
    draw_star(0.0616*height)


a = int(input("Enter the height of the flag: "))
draw_flag(a)
turtle.done()

    