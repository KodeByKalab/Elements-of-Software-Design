#  File: Poker.py

#  Description:



from math import tanh
import random
import sys

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12
        
        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck (object):
    # constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        for i in range (num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card (rank, suit)
                    self.deck.append (card)

    # shuffle the deck
    def shuffle (self):
        random.shuffle (self.deck)

    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
    # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards
        
        # create empty hand for each player and add to all hands
        for i in range(num_players):
            hand = []
            self.all_hands.append(hand)

        # deal cards round robin
        for i in range (self.numCards_in_Hand):
            for j in range(len(self.all_hands)):
                self.all_hands[j].append (self.deck.deal())

    # simulate the play of poker
    def play (self):
        # sort the hands of each player and print
        for i in range (len(self.all_hands)):
            sorted_hand = sorted (self.all_hands[i], reverse = True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str (card) + ' '
            print ('Player ' + str(i + 1) + ': ' + hand_str)
        print()

        # determine the type of each hand and print
        hand_type = []	# create a list to store type of hand
        hand_points = []	# create a list to store points for hand

        for hand in self.all_hands:
            royal = self.is_royal(hand)
            if (royal != (0,'')):
                hand_points.append(royal[0])
                hand_type.append(royal[1])
                continue
            straight_flush = self.is_straight_flush(hand)
            if (straight_flush != (0,'')):
                hand_points.append(straight_flush[0])
                hand_type.append(straight_flush[1])
                continue
            four_of_kind = self.is_four_kind(hand)
            if (four_of_kind != (0,'')):
                hand_points.append(four_of_kind[0])
                hand_type.append(four_of_kind[1])
                continue
            full_house = self.is_full_house(hand)
            if (full_house != (0,'')):
                hand_points.append(full_house[0])
                hand_type.append(full_house[1])
                continue
            flush = self.is_flush(hand)
            if (flush != (0,'')):
                hand_points.append(flush[0])
                hand_type.append(flush[1])
                continue
            straight = self.is_straight(hand)
            if (straight != (0,'')):
                hand_points.append(straight[0])
                hand_type.append(straight[1])
                continue
            three_of_kind = self.is_three_kind(hand)
            if (three_of_kind != (0,'')):
                hand_points.append(three_of_kind[0])
                hand_type.append(three_of_kind[1])
                continue
            two_pair = self.is_two_pair(hand)
            if (two_pair != (0,'')):
                hand_points.append(two_pair[0])
                hand_type.append(two_pair[1])
                continue
            one_pair = self.is_one_pair(hand)
            if (one_pair != (0,'')):
                hand_points.append(one_pair[0])
                hand_type.append(one_pair[1])
                continue
            high_card = self.is_high_card(hand)
            hand_points.append(high_card[0])
            hand_type.append(high_card[1])

        player_num = 0
        for type in hand_type:
            print('Player ' + str(player_num + 1) + ': ' + type)
            player_num += 1
        
        # determine winner and print
        max_points = 0
        winners = []
        player = 1
        for points in hand_points:
            if points == max_points:
                winners.append(player)
            if points > max_points:
                winners = []
                max_points = points
                winners.append(player)
            player += 1

        if len(winners) > 1:
            for winner in winners:
                print('Player ' + str(winner) + ' ties.')
        else:
            print('Player ' + str(winners[0]) + ' wins.')
         
        
    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        
        if (not same_suit):
            return 0, ''
            
        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)
            
        if (not rank_order):
            return 0, ''
            
        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        
        return points, 'Royal Flush'

    def is_straight_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''
            
        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[0].rank-i)
        
        if (not rank_order):
            return 0, ''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'


    def is_four_kind (self, hand):
        four_kind = False
        four_rank = 0
        for i in range(len(hand) - 3):
            temp_rank = hand[i].rank
            if (temp_rank == hand[i+1].rank == hand[i+2].rank == hand[i+3].rank):
                four_kind = True
                four_rank = temp_rank
                break
        
        if (not four_kind):
            return 0, ''

        # get remaining rank
        other_rank = 0
        if (hand[0].rank != four_rank):
            other_rank = hand[0].rank
        else:
            other_rank = hand[4].rank

        points = 8 * 15 ** 5 + (four_rank) * 15 ** 4 + (four_rank) * 15 ** 3
        points = points + (four_rank) * 15 ** 2 + (four_rank) * 15 ** 1
        points = points + (other_rank)

        return points, 'Four of a Kind'

    def is_full_house (self, hand):
        three_in = False
        three_rank = 0
        for i in range(len(hand) - 2):
            temp_rank = hand[i].rank
            if (temp_rank == hand[i+1].rank == hand[i+2].rank):
                three_in = True
                three_rank = temp_rank
                break
        
        if (not three_in):
            return 0, ''

        # pop out the 3 same rank cards
        i = 0
        hand_copy = hand.copy()
        while i < len(hand_copy):
            if (hand_copy[i].rank == three_rank):
                hand_copy.pop(i)
            else:
                i += 1

        # check if remaining 2 match ranks
        two_in = False
        if (hand_copy[0].rank == hand_copy[1].rank):
            two_in = True
        
        if (not two_in):
            return 0, ''

        points = 7 * 15 ** 5 + (three_rank) * 15 ** 4 + (three_rank) * 15 ** 3
        points = points + (three_rank) * 15 ** 2 + (hand_copy[0].rank) * 15 ** 1
        points = points + (hand_copy[1].rank)

        return points, 'Full House'


    def is_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'

    def is_straight (self, hand):
        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[0].rank-i)
        
        if (not rank_order):
            return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    def is_three_kind (self, hand):
        three_kind = False
        three_rank = 0
        for i in range(len(hand) - 2):
            temp_rank = hand[i].rank
            if (temp_rank == hand[i+1].rank == hand[i+2].rank):
                three_kind = True
                three_rank = temp_rank
                break
        
        if (not three_kind):
            return 0, ''

        other_ranks = [] 
        for i in range(len(hand)):
            if (hand[i].rank != three_rank):
                other_ranks.append(hand[i].rank)

        points = 4 * 15 ** 5 + (three_rank) * 15 ** 4 + (three_rank) * 15 ** 3
        points = points + (three_rank) * 15 ** 2 + (other_ranks[0]) * 15 ** 1
        points = points + (other_ranks[1])

        return points, 'Three of a Kind'

    def is_two_pair (self, hand):
        two_1_in = False
        two_1_rank = 0
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i+1].rank):
                two_1_in = True
                two_1_rank = hand[i].rank
                break
        
        if (not two_1_in):
            return 0, ''

        # pop out the first 2 same rank cards -> hand will have 3 cards left
        i = 0
        hand_copy = hand.copy()
        while i < len(hand_copy):
            if (hand_copy[i].rank == two_1_rank):
                hand_copy.pop(i)
            else:
                i += 1

        # check for second pair
        two_2_in = False
        two_2_rank = 0
        if ((hand_copy[0].rank == hand_copy[1].rank) or (hand_copy[1].rank == hand_copy[2].rank)):
            two_2_in = True
            two_2_rank = hand_copy[1].rank
        
        if (not two_2_in):
            return 0, ''

        # get remaining rank
        other_rank = 0
        if (hand_copy[0].rank != two_2_rank):
            other_rank = hand_copy[0].rank
        else:
            other_rank = hand_copy[2].rank
        
        points = 3 * 15 ** 5 + (two_1_rank) * 15 ** 4 + (two_1_rank) * 15 ** 3
        points = points + (two_2_rank) * 15 ** 2 + (two_2_rank) * 15 ** 1
        points = points + (other_rank)

        return points, 'Two Pair'


    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair (self, hand):
        one_pair = False
        one_rank = 0
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                one_rank = hand[i].rank
                break
        if (not one_pair):
            return 0, ''
            
        i = 0
        hand_copy = hand.copy()
        while i < len(hand_copy):
            if (hand_copy[i].rank == one_rank):
                hand_copy.pop(i)
            else:
                i += 1

        points = 2 * 15 ** 5 + (one_rank) * 15 ** 4 + (one_rank) * 15 ** 3
        points = points + (hand_copy[0].rank) * 15 ** 2 + (hand_copy[1].rank) * 15 ** 1
        points = points + (hand_copy[2].rank)
        
        return points, 'One Pair'

    def is_high_card (self, hand):
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'High Card'

def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int (line)
    if (num_players < 2) or (num_players > 6):
        return

    print('Number of players: {}\n'.format(str(num_players)))
    # create the Poker object
    game = Poker (num_players)

    # play the game
    game.play()

if __name__ == "__main__":
    main()
