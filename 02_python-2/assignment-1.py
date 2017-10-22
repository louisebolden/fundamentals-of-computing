# implementation of card game - Memory

import simplegui
import random

# globals
cards = []
exposed = []
state = 0
cached_card_1 = None
cached_card_2 = None
turns = 0

# helper function to initialize globals
def new_game():
    global cards, exposed, state, cached_card_1, cached_card_2, turns

    # set state and clear cached card indices & turns count
    state = 0
    cached_card_1 = None
    cached_card_2 = None
    turns = 0

    # create and shuffle the cards
    cards = list(range(8)) + list(range(8))
    random.shuffle(cards)

    # all cards start out hidden
    exposed = [False for card in cards]

# define event handlers
def mouseclick(pos):
    global state, cached_card_1, cached_card_2, turns

    mouse_x = pos[0]
    card_index = mouse_x // 50 # because cards are 50px wide

    if state == 0: # no cards exposed

        # if clicked-on card was hidden, show it
        if exposed[card_index] == False:
            exposed[card_index] = True
            cached_card_1 = card_index
            turns += 1

        # update state to reflect 1 exposed card
        state = 1

    elif state == 1: # one card exposed

        # if clicked-on card was hidden, show it
        if exposed[card_index] == False:
            exposed[card_index] = True
            cached_card_2 = card_index
            turns += 1

            # update state to reflect 2 exposed cards
            state = 2

    else: # two cards exposed

        # if the cards did not match, hide them
        if cards[cached_card_1] != cards[cached_card_2]:
            exposed[cached_card_1] = False
            exposed[cached_card_2] = False

        # if clicked-on card was hidden, show it
        if exposed[card_index] == False:
            exposed[card_index] = True
            cached_card_1 = card_index
            turns += 1

        # move back to state 1
        state = 1

def draw(canvas):
    # set starting draw positions
    card_pos = [20,60]
    rect_x = 0

    # for each card in the cards list...
    for index, card in enumerate(cards):
        # check whether that card should be visible or not
        is_visible = exposed[index]

        if is_visible:
            # display the card's number
            canvas.draw_text(str(card), card_pos, 20, "white")
        else:
            # draw a hidden card shape
            canvas.draw_polygon([
                [rect_x,0], [rect_x+50,0], [rect_x+50,100], [rect_x,100]
            ], 2, 'Black', 'Green')

        # adjust draw positions to place next card correctly
        card_pos[0] += 50
        rect_x += 50

    # Update the label showing number of turns taken
    label.set_text("Turns = " + str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
