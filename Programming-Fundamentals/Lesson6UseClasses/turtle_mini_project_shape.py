import turtle

def window_properties():
    window = turtle.Screen()
    window.bgcolor("white")

def draw_k(k):
    for i in range(1,2):
        k.left(90)
        k.forward(100)
        k.backward(50)
        k.right(45)
        k.forward(70)
        k.backward(70)
        k.right(80)
        k.forward(75)
     

def draw_bracket(bracket):
    for i in range(1,2):
        bracket.pu()
        bracket.left(35)
        bracket.forward(10)
        bracket.left(90)
        bracket.pd()
        bracket.forward(100)
        bracket.right(90)
        bracket.forward(50)
        bracket.backward(50)
        bracket.right(90)
        bracket.forward(100)
        bracket.left(90)
        bracket.forward(50)

def draw_initials():
    kd = turtle.Turtle()
    kd.color("blue")
    kd.shape("turtle")
    kd.speed(2)
 
    count = 0
    write_initial = 1

    while(count < write_initial):
        print("It's written!")
        draw_k(kd)
        draw_bracket(kd)
        
        count = count + 1


window_properties()
draw_initials()
window.exitonclick()
