import turtle 

## short form of movement commands 
# t.rt() instead of t.right()
# t.fd() instead of t.forward()
# t.lt() instead of t.left()
# t.bk() instead of t.backward()

# init screen 
    # not easy to let it run on a codespace 
    # work on this simply locally 
s = turtle.Screen()

# init turtle 
t = turtle.Turtle()

# insert here code to play around 
t.forward(100)
t.right(45)

# click on s to exit 
s.exitonclick()

