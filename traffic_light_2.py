import turtle # tess becomes a traffic light

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black","darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# when the machine changes state, we change tess' position and
# her fillcolor

# this variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:      # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:        # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:       # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def red_key():
    '''Fill tess with red when key pressed'''
    tess.fillcolor("red")

def green_key():
    '''Fill tess with green when key pressed'''
    tess.fillcolor("green")

def blue_key():
    '''Fill tess with blue when key pressed'''
    tess.fillcolor("blue")


penwidth = tess.shapesize()[2]
def increase_width():
    '''Increase tess pen width'''
    global penwidth
    if penwidth < 20: # If 20 do nothing
        penwidth = penwidth + 1
    tess.shapesize(outline = penwidth)

def decrease_width():
    '''Decrease tess pen width'''
    global penwidth
    if penwidth > 1: # If 1 do nothing
        penwidth = penwidth - 1
    tess.shapesize(outline = penwidth)

turtlesize = tess.shapesize()[0]
def increase_size():
    '''Increase tess size'''
    global turtlesize
    if turtlesize < 20: # If 20 do nothing
        turtlesize = turtlesize + 1
    tess.shapesize(turtlesize)

def decrease_size():
    '''Decrease tess size'''
    global turtlesize
    if turtlesize > 1: # If 20 do nothing
        turtlesize = turtlesize - 1
    tess.shapesize(turtlesize)

timer = 1 # In seconds
def increase_timer():
    '''Increase timer of the traffic light'''
    global timer
    if timer < 5:
        timer = timer + .25

def decrease_timer():
    '''Increase timer of the traffic light'''
    global timer
    if timer > .25:
        timer = timer - .25
    

def loop_advance_state_machine():
    '''Handle the loop to call advance_state_machine to change the color of the traffic light'''
    global timer
    advance_state_machine()
    wn.ontimer(loop_advance_state_machine, int(timer*1000))

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

# Handlers on keys
wn.onkey(red_key, "r")
wn.onkey(green_key, "g")
wn.onkey(blue_key, "b")
wn.onkey(increase_width, "plus") # To increase width with +
wn.onkey(decrease_width, "minus") # To increase width with -
wn.onkey(increase_size, "asterisk") # To increase size with *
wn.onkey(decrease_size, "slash") # To increase width with /
wn.onkey(increase_timer, "w") # To increase the timer with w
wn.onkey(decrease_timer, "s") # To increase the timer with s

# Timer to automatically change the traffic light
wn.ontimer(loop_advance_state_machine, 1000)

wn.listen()     # Listen for events
wn.mainloop()