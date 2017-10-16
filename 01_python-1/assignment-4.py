# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [2, 2]
paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    rand_1 = float(random.randrange(120, 240)) / 60
    rand_2 = float(random.randrange(60, 180)) / 60

    if direction == "LEFT":
        ball_vel = [-rand_1, -rand_1]
    elif direction == "RIGHT":
        ball_vel = [rand_2, -rand_2]

# define event handlers
def new_game():
    # Reset the game ready to start fresh
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]

    # random direction for ball start
    rand = random.randrange(1, 3)
    if rand == 1:
        spawn_ball("LEFT")
    else:
        spawn_ball("RIGHT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # if ball hits a gutter, the opposite player gets a
    # point and the ball respawns
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        # if ball hits right paddle, it bounces & speeds up
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            ball_vel[0] = -(ball_vel[0] + (ball_vel[0] * 0.1))
            ball_vel[1] = ball_vel[1] + (ball_vel[1] * 0.1)
        # but if player1 missed, player1 gets point & ball respawns
        else:
            score1 += 1
            spawn_ball("LEFT")
    elif ball_pos[0] <= (0 + PAD_WIDTH + BALL_RADIUS):
        # if ball hits left paddle, it bounces & speeds up
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            ball_vel[0] = -(ball_vel[0] + (ball_vel[0] * 0.1))
            ball_vel[1] = ball_vel[1] + (ball_vel[1] * 0.1)
        # but if player1 missed, player2 gets point & ball respawns
        else:
            score2 += 1
            spawn_ball("RIGHT")

    # if ball hits the top or bottom 'wall', it bounces
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] <= (0 + BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "white")

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos >= 0 and paddle1_vel[1] < 0) or ((paddle1_pos + PAD_HEIGHT) <= HEIGHT and paddle1_vel[1] > 0):
        paddle1_pos += paddle1_vel[1]

    if (paddle2_pos >= 0 and paddle2_vel[1] < 0) or ((paddle2_pos + PAD_HEIGHT) <= HEIGHT and paddle2_vel[1] > 0):
        paddle2_pos += paddle2_vel[1]

    # draw paddles
    canvas.draw_line(
            [0 + HALF_PAD_WIDTH, paddle1_pos],
            [0 + HALF_PAD_WIDTH, PAD_HEIGHT + paddle1_pos], PAD_WIDTH, "white")
    canvas.draw_line(
            [WIDTH - HALF_PAD_WIDTH, paddle2_pos],
            [WIDTH - HALF_PAD_WIDTH, PAD_HEIGHT + paddle2_pos], PAD_WIDTH, "white")

    # draw scores
    canvas.draw_text(str(score1), (50, 50), 40, "white")
    canvas.draw_text(str(score2), (350, 50), 40, "white")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 3
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -3
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 3

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Restart", new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
