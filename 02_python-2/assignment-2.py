# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = "Hit or stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        result = "Hand contains"
        for card in self.cards:
            result += " " + str(card)
        return result

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        aces = 0
        points = 0
        for card in self.cards:
            rank = card.rank
            points += VALUES[rank]
            if rank == 'A':
                aces += 1
        if aces >= 1 and points + 10 <= 21:
            points += 10
        return points


    def draw(self, canvas, pos):
        card_pos = list(pos)
        for card in self.cards:
            card.draw(canvas, card_pos)
            card_pos[0] += CARD_SIZE[0]

# define deck class
class Deck:
    def __init__(self):
        # store one of each rank and suit of cards in a
        # list called 'cards'
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        # remove the last card from the deck and return
        # it, to mimick the dealer putting that card down
        return self.cards.pop(-1)

    def __str__(self):
        result = "Deck contains"
        for card in self.cards:
            result += " " + str(card)
        return result


# define event handlers for buttons
def deal():
    global deck, player_hand, dealer_hand, outcome, in_play, score

    if in_play:
        outcome = "You forfeited the round and lost one point. New deal?"
        score -= 1
        in_play = False

    else:
        # create a new deck object and shuffle its cards
        deck = Deck()
        deck.shuffle()

        # create hand objects for dealer & player
        dealer_hand = Hand()
        player_hand = Hand()

        # deal 2 cards each to dealer & player
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

        # game is now in play
        outcome = "Hit or stand?"
        in_play = True

def hit():
    global outcome, in_play, score

    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())

        # if busted, assign a message to outcome, update
        # in_play and score
        if player_hand.get_value() > 21:
            outcome = "Player bust! Dealer wins. New deal?"
            in_play = False
            score -= 1

def stand():
    global outcome, score, in_play

    # if hand is in play, repeatedly hit dealer until
    # his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            print 'Dealer ' + str(dealer_hand) + " (" + str(dealer_hand.get_value()) + ")"

        # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21 or player_hand.get_value() > dealer_hand.get_value():
            outcome = "Player wins! New deal?"
            score += 1
        else:
            outcome = "Dealer wins! New deal?"
            score -= 1

        in_play = False

# draw handler
def draw(canvas):
    canvas.draw_text("Let's Play: Blackjack", (10, 50), 50, 'Black')
    canvas.draw_text(outcome, (10, 100), 24, 'Black')

    # draw the dealer's cards, with a label
    canvas.draw_text("Dealer:", (10, 170), 24, 'Black')
    dealer_hand.draw(canvas, (10, 190))

    # cover the dealer's first card while game in play
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (10 + CARD_BACK_CENTER[0], 190 + CARD_BACK_CENTER[1]), CARD_BACK_SIZE)

    # draw the player's cards, with a label
    canvas.draw_text("Player (hand value " + str(player_hand.get_value()) + "):", (10, 350), 24, 'Black')
    player_hand.draw(canvas, (10, 370))

    # draw the current total game score
    canvas.draw_text(score_str(score), (10, 580), 24, 'Black')


    # helper functions
def score_str(score):
    score_str = "Your score is " + str(score)
    if score < -3:
        return score_str + " (it's not your lucky day!)"
    else:
        return score_str


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
