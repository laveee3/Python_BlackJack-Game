# BlackJack Game using Python

Blackjack is a card-based game played at casinos. The participants in this game do not compete with each other but the dealer assigned by the casino. In this article, we will be creating the Blackjack game between a player and a dealer from scratch, that can be played on the terminal.


Rules of Blackjack
------------------
We will provide a brief set of rules for readers who have never played Blackjack. The magic number for Blackjack is 21. The values for all the cards dealt to a player are added and if the sum exceeds 21, the player busts and loses instantly.

If a player gets an exact 21, the player wins against the dealer. Otherwise, in order to win, the sum of the player’s cards must be more than the sum of the dealer’s cards.

Each face card has a definite value of 10, whereas the ace can be counted as 1 or 11 suitable to the player’s chances of winning. The value of the rest of the cards is defined by their number.


The dealing of the cards in a game of Blackjack is as follows:
---------------------------------------------------------------

A card is dealt to the player facing upwards (visible to everyone).

The dealer deals a card to himself visible to everyone.

Another card is given to the player facing upwards.

The dealer deals a card facing downwards for himself.

The player has to decide whether to stand with the current set of cards or get another card.

If the player decides to hit, another card is dealt.

If the player decides to stand, then the dealer reveals his hidden card.

The dealer does not have the authority to decide whether to hit or stand. The general rule is that the dealer needs to keep hitting more cards if the sum of dealer’s cards is less than 17.

As soon as the sum of dealer’s cards is either 17 or more, the dealer is obliged to stand.

According to the final sum of the cards, the winner is decided.

The programming of the Blackjack game becomes simple as soon as the rules are understood. Creating a terminal-based game from scratch requires three main components: The Game Design, The Game Logic, and Management of Player Interaction.

