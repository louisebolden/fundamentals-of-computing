###################################################
# Mouse and list methods
###################################################

# 1. For each mouse click, print the position of the mouse click to the console.

import simplegui

WIDTH = 300
HEIGHT = 200

# Handlers for keydown and keyup
def click_1(pos):
    print "Mouse click at " + str(pos)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Exercise", 300, 200)
frame.set_mouseclick_handler(click_1)

# Start the frame animation
frame.start()

# 2. Modify the program template below so that clicking inside any of the three displayed circles prints the color of the clicked circle to the console. Hint: Use the supplied function dist to compute the distance between the center of each circle and the mouse click.

import math

# define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click_2(pos):
    print pos
    if dist(pos, RED_POS) <= RADIUS:
        print "Red"
    if dist(pos, GREEN_POS) <= RADIUS:
        print "Green"
    if dist(pos, BLUE_POS) <= RADIUS:
        print "Blue"


# define draw
def draw_1(canvas):
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")

# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click_2)
frame.set_draw_handler(draw_1)

# start frame
frame.start()

# 3. Write a function day_to_number(day) that takes the supplied global list day_list and returns the position of the given day in that list. You can either use the Docs to locate the appropriate list method or write a for loop to implement this function.

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number(day):
    return day_list.index(day)

# 4. Write a function string_list_join(string_list) that takes a list of strings as input and returns a single string that is the concatenation of the strings in the list. We recommend using a for loop to implement this function.

def string_list_join(string_list):
    full_string = ""
    for string in string_list:
        full_string += string
    return full_string

# 5. Complete the given program template to produce a program that fills the canvas with a 10x10 grid of touching balls of the given size. You should use two for loops, one nested inside the other, placed in the draw handler.

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS

# define draw
def draw_2(canvas):
    pos = [BALL_RADIUS,BALL_RADIUS]
    for num in range(1,11):
        # draw a circle in top-left
        canvas.draw_circle(pos, BALL_RADIUS, 1, "white")

        for num2 in range(1,10):
            # move down
            pos[1] += (BALL_RADIUS * 2)
            # draw another circle
            canvas.draw_circle(pos, BALL_RADIUS, 1, "white")
            # (and repeat 9 times)

        # reset Y pos ready to draw next top circle
        pos[1] = BALL_RADIUS

        # move across to put next top circle in correct place
        pos[0] += (BALL_RADIUS * 2)

# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw_2)

# start frame
frame.start()

# 6. Challenge: Write a program that draws a polyline (an open polygon) based on a sequence of mouse clicks. The first click should create a point. Subsequent clicks should add a new segment to the polyline. You should include a “Clear” button that deletes the polyline and restarts the drawing process.

polyline = []

# define mouseclick handler
def click_3(pos):
    polyline.append(pos)

# button to clear canvas
def clear():
    global polyline
    polyline = []

# define draw
def draw_3(canvas):
    if len(polyline) > 0:
        canvas.draw_polyline(polyline, 2, 'White')

# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click_3)
frame.set_draw_handler(draw_3)
frame.add_button("Clear", clear)

# start frame
frame.start()

###################################################
# Dictionaries and images
###################################################

# 1. Create a dictionary day_to_number that converts the days of the week "Sunday", "Monday", … into the numbers 0, 1, …, respectively.

day_to_number = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
}

# 2. Create dictionary for name_lookup that, when you lookup the keys "Joe", "Scott", "John", and "Stephen", you get the values "Warren", "Rixner", "Greiner", and "Wong", respectively.

name_lookup = {
    "Joe": "Warren",
    "Scott": "Rixner",
    "John": "Greiner",
    "Stephen": "Wong"
}

# 3. Debug the program template below so that the resulting program draws the supplied image on the canvas.

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")
test_image_size = [135, 164]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]

# draw handler
def draw_4(canvas):
    canvas.draw_image(test_image,
                      test_image_center,
                      test_image_size,
                      test_image_center,
                      test_image_size)

# create frame and register draw handler
frame = simplegui.create_frame("Test image", test_image_size[0], test_image_size[1])
frame.set_draw_handler(draw_4)

# start frame
frame.start()

# 4. Load this image of an asteroid, and draw the image centered at the last mouse click. Prior to any mouse clicks, the image should be drawn in the middle of the canvas. The image size is 95×93 pixels.

# global constants
WIDTH = 400
HEIGHT = 300
image_center = [WIDTH/2, HEIGHT/2]

# load test image
image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')

# mouseclick handler
def click(pos):
    global image_center
    image_center = list(pos)

# draw handler
def draw_5(canvas):
    canvas.draw_image(image,
                      (95 / 2, 93 / 2),
                      (95, 93),
                      (image_center),
                      (95, 93)
                     )

# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw_5)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
