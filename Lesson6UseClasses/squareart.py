import turtle

def window_properties():
    window = turtle.Screen()
    window.bgcolor("yellow")


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    

def draw_art():
    jim = turtle.Turtle()
    jim.color("green")
    jim.shape("square")
    jim.speed(20)
    
    count = 0
    travel_square = 36

    while(count < travel_square):
        print("Jim moved forward "+str(count+1)+" time!")
        print("Jim turned right "+str(count+1)+" time!")
        draw_square(jim)
        jim.right(10)
        
        count = count + 1
    

        
window_properties()
draw_art() 
