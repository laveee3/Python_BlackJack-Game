import random
import time

print("BlackJack Card Game    - python program  - Lavanya_E  June 9")

class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        if self.value < 11:
            print('{} of {}'.format(self.value, self.suit))
        elif self.value == 11:
            print('J of {}'.format(self.suit))
        elif self.value == 12:
            print('Q of {}'.format(self.suit))
        elif self.value == 13:
            print('K of {}'.format(self.suit))
        else:
            print('Ace of {}'.format(self.suit))

    def card_value(self):
        if self.value < 11:
            return(self.value)
        elif self.value in (11,12,13):
            return(10)
        else:
            return(11)

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for shoe in range(6):
            for s in ["Spades", "Diamonds", "Hearts", "Clubs"]:
                for v in range(2, 15):
                    self.cards.append(Card(s, v))
                    #print('{} of {}'.format(v, s))

    def show(self):
        # c is a single card object, accessing the show() method from the Card class
        for c in self.cards:
            c.show()

    def shuffle(self):
        # Fisher-Yates shuffle algorithm (which is what random.shuffle uses!)
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self #see note below

    def showHand(self):
        #card is a single card object, accessing the show() method from the Card class
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

    def hand_value(self):
        num_aces = 0
        total_cd_val = 0
        for card in self.hand:
            total_cd_val +=card.card_value()
            if card.value == 14:
                num_aces += 1

        while num_aces > 0:
            if total_cd_val > 21:
                total_cd_val -= 10
                num_aces -= 1
            else:
                break
        return(total_cd_val)


num_games = int(input("Enter number of games (>0):"))
games = num_games
start_time = time.time()
win_times_P = 0
win_times_Dlr = 0
winning_hands = []
while (num_games):
    # Creating the deck of cards and followed by shuffling it

    print("GAMES remaining :" + str(num_games) + '\n')
    # Creating the deck of cards and followed by shuffling it
    deck1 = Deck()
    deck1.shuffle()
    #deck1.show()

    player = Participant("Player")
    dealer = Participant("Dealer")

    def first_two_deals():
        for member in (player, dealer):
            member.draw(deck1)
            print(f'\nThe cards in {member.name}\'s hand:')
            member.showHand()
     #       print(member.name)

    first_two_deals()

    while(player.hand_value() < 16):
        player.draw(deck1)
        print(f'\nThe {len(player.hand)} cards in {player.name}\'s hand:')
        player.showHand()
        #dealer.draw(deck1)
        print("the new Hand value of player is ", player.hand_value())

    if player.hand_value() == 21 and dealer.hand_value() < 21:
        print("\n----PLAYER WINS-----")
        win_times_P += 1
    elif player.hand_value() > 21:
        print("\n----DEALER WINS-----")
        win_times_Dlr += 1
    elif player.hand_value() in (16, 17, 18, 19, 20):
        print("\n->Player says STAY")
        while (dealer.hand_value() < 16):
            print("\n*** Dealer took a card")
            dealer.draw(deck1)
            print("the new Hand value of dealer is ", dealer.hand_value())
        print("----------------------------------------------------")
        dealer.showHand()
        print("Hand value of dealer is ", dealer.hand_value())
        if dealer.hand_value() == 21 and player.hand_value() < 21:
            print("\n----DEALER WINS-----")
            win_times_Dlr += 1
        elif dealer.hand_value() > 21:
            #dealer.showHand()
            print("\n----PLAYER WINS-----")
            win_times_P += 1
        elif dealer.hand_value() in (16,17, 18, 19, 20):
            if dealer.hand_value() > player.hand_value():
                print("\n----DEALER WINS-----")
                win_times_Dlr += 1
            elif dealer.hand_value() == player.hand_value():
                print("\n---- No ONE  WINS-----")
            else:
                print("\n----PLAYER WINS-----")
                win_times_P += 1
        else:
            print(" the end")
    else:
        print(" the end")

    num_games -= 1
print("--- Run time is %s seconds ---" % (time.time() - start_time))
print("The number of times Player won",win_times_P)
print("The number of times Dealer won",win_times_Dlr)
print("The player percentage of winning", (win_times_P/games)*100, "%")
