import turtle

def window_properties():
    window = turtle.Screen()
    window.bgcolor("yellow")

def draw_square():
    jim = turtle.Turtle()
    jim.color("green")
    jim.shape("square")
    jim.speed(2)
    
    count = 0
    travel_square = 4

    while(count < travel_square):
        print("Jim moved forward "+str(count+1)+" time!")
        print("Jim turned right "+str(count+1)+" time!")
        jim.forward(200)
        jim.right(90)
        count = count + 1
        
def draw_circle():
    angela = turtle.Turtle()
    angela.shape("circle")
    angela.color("blue")
    
    angela.circle(100)
    print("Angela moved in a circle!")

def draw_triangle():
    suby = turtle.Turtle()
    suby.shape("triangle")
    suby.color("red")

    count = 0
    travel_triangle = 3

    while(count < travel_triangle):
        print("Suby moved forward" +str(count+1)+"time!")
        print("Suby turned right "+str(count+1)+"time!")
        suby.forward(220)
        suby.right(120)
        count = count + 1
         
draw_square()
draw_circle()
draw_triangle()
window_properties()
