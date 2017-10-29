###################################################
# Classes pt 1
###################################################

# 1. For this set of practice exercises, we will walk you through the creation
# of a Tile class suitable for use in your week five mini-project, Memory. This
# class will model the logical behavior of cards/tiles used in Memory. Our goal
# in walking through this design will be to understand the syntactic structure
# of a Python class in detail as well as the logic that goes into designing a
# useful class.

import simplegui

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100

# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # definition of getter for number
    def get_number(self):
        return self.number

    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed

    # expose the tile
    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    # string method for tiles
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return inside_hor and inside_vert


# define event handlers
def mouseclick(pos):
    if tile1.is_selected(pos):
        tile1.hide_tile()
    if tile2.is_selected(pos):
        tile2.expose_tile()

# draw handler
def draw(canvas):
    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

# create two tiles
tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])

# get things rolling
frame.start()

###################################################
# Classes pt 2
###################################################

# 1. Before proceeding to the task of implementing Memory using the Tile class
# that we developed in Week 6a, your job is to complete couple of pairs of
# exercises in which we implement and then use some simple classes. As your
# first task, implement a Person class which has the fields first_name,
# last_name and birth_year. This class should include the methods: __init__
# which takes strings for the two name fields and an integer for the year of
# birth, full_name returns the full name for a person as a string, which is the
# first name followed by a space, followed by the last name, age which takes the
# current year as input and returns the age in years of the person (Don't worry
# about days and months here, just return the difference of the two years.), and
# __str__ returns a string that includes the first name and last name of the
# person as well as their year of birth.

class Person:
    def __init__(self, first, last, year):
        self.first = first
        self.last = last
        self.year = year

    def full_name(self):
        return self.first + ' ' + self.last

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.year)

# 2. Write a function average_age that takes a list of Person objects along with
# the current year and returns the average age of the people in the list.
# Remember that average_age should only use the methods defined in the Person
# class. (The body of average_age should not access the fields in a Person
# object directly.)

def average_age(person_list, current_year):
    total_ages = 0.0
    for person in person_list:
        total_ages += person.age(current_year)
    return total_ages / len(person_list)

# 3. Implement a Student class which has the fields person (Person object),
# password (string), and projects (list of strings). (Note that class uses
# another class, just as in Blackjack.) Complete the following methods.

class Student:
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.person = person
        self.pwd = pwd
        self.projects = []

    # use the full_name method for Person
    def get_name(self):
        return self.person.full_name()

    def check_password(self, pwd):
        return self.pwd == pwd

    def get_projects(self):
        return self.projects

    def add_project(self, project):
        self.projects.append(project)

# 4. Write a function assign that takes a list of Student objects, a student
# full name, a password, and a project as parameters. This function should
# search the list of students for students whose name and password match the
# supplied information. When a match is found, the function checks the student's
# current list of projects for the supplied project. If the project does not
# already exist in the list, the function adds the project to the list. Remember
# to use only methods for the Student class to manipulate Student objects.

def assign(students, name, pwd, project):
    for student in students:
        if student.get_name() == name and student.check_password(pwd):
            if project not in student.get_projects():
                student.add_project(project)
