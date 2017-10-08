# "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
tries = 0
wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """
    Turn an integer representing the number of tenths
    of a second into a string like "0:00.1", with
    additional zeroes in place as necessary.
    """

    # create the minute section of the string
    minutes = t // 600
    formatted_string = str(minutes) + ":"

    seconds = t - (minutes * 600)

    # if we need preceeding zeros for the seconds,
    # add them here
    if seconds < 10:
        formatted_string += '00' + str(seconds)
    elif seconds < 100:
        formatted_string += '0' + str(seconds)
    else:
        formatted_string += str(seconds)

    # we're not using floats for this exercise, so
    # insert a '.' symbol before the final digit in
    # the string to show the last tenth of a second
    last_digit = formatted_string[-1]
    formatted_string = formatted_string[:-1] + '.' + last_digit

    return formatted_string

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global tries

    if timer.is_running():
        print "Timer is already running."
    else:
        timer.start()
        tries += 1

def stop():
    global wins

    if timer.is_running():
        timer.stop()

        if time % 10 == 0:
            wins += 1
    else:
        print "Timer is already stopped."

def reset():
    """
    Stop the timer if it's running, and reset the game
    state ready for a new game.
    """
    global time
    global tries
    global wins

    if timer.is_running():
        timer.stop()

    time = 0
    tries = 0
    wins = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time

    # this game only runs up to a max time of 10:00.0
    if time < 6000:
        time += 1
    else:
        print "Time's up! Resetting game..."
        reset()

# define draw handler
def draw(canvas):
    canvas.draw_text(str(wins) + '/' + str(tries), [150,30], 30, "red", "sans-serif")
    canvas.draw_text(format(time), [45,90], 40, "white", "sans-serif")

# create frame and timer
frame = simplegui.create_frame("Stopwatch: The Game", 200, 150)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
