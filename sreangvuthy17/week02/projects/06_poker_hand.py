"""
                                        PROJECT 06: Best Poker Hand

    Description:    In this program, you will write a function that take two strings(player_one and player_two) in parameter that will represent two poker player hands and then return the result as a string:
                    - Player One WIN​ (if the player_one win) 
                    - Player Two WIN​ (if the player_two win) 
                    - Tie​ (if the result is equal)
                    The first character is the value of the card:  2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce) 
                    The second character represents the suit:  S(pades), H(earts), D(iamonds), C(lubs) 
                    Each card will be separated with a space The order of the card in the hands does not matter 
                        Example of hand: ​“AH KH QH JH TH” 
                    This hand correspond to Ace, King, Queen, Jack and Ten of HEART. This is a royal flush. ( The best hand in Poker ) 
                    If the two players got the same rank, you will return Tie. 
                    In the ‘real Poker’ if two player got same rank (for example: two pair of Aces VS two pair of Kings: the Aces will win) 
                    
                    If you are able to do as the ‘real Poker’ ranking, ​you will get bonus points for this project​. 
                    Make sure that you do it for all the hands and you are sure that you understand the rules! ​If you are not sure, please ask first else your program will not be valid. 
                    
                    Also you will have to name your project 06_poker_real.py if you do the BONUS. Else you will name it 06_poker_hand.py 
 
                                    More information about Poker Ranking: https://en.wikipedia.org/wiki/List_of_poker_hands 
 
 
    Requirements :  ● Program must be named : ​06_poker_hand.py​ and saved into​ week02/projects 
                    ● Your function must be called ​poker_hand(player_one, player_two) 

    Hint :  ❖ string split  
            ❖ loop 
            ❖ array/list  
            ❖ make sure you understand the rules before starting your algorithms.
 
    Output : 
            Example 01: 
            poker_hand(“AH KH QH JH TH”, “AS KS TS 2H 3H”) 
            >> Player 1 WIN 
            
            Example 02: 
            poker_hand(“AH KS QS JS TH”, “8S 8H 8D 8C 2H”) 
            >> Player 2 WIN  
 
            Example 03: 
            poker_hand(“AH KS QH JH TH”, “AS KH QC JC TC”) 
            >> Tie
 
 
                        Explanation​: (don’t print this part in your program) 
 
                        -   Example 01 : Player 1 WIN 
                            Royal Flush [Player One] > No Pair [Player Two] 
 
                        -   Example 02 : Player 2 WIN 
                            Straight [Player One] < Four of a Kind [Player Two] 
 
                        -   Example 03 : Tie 
                            Straight [Player One] == Straight [Player Two] 
 
"""

# Find if card contain same suit.
def flush(cards):
    return len([card for card in cards.split(" ") if cards[1] == card[1]]) == 5

# Find kind of card return 1 for one pair, 2 for two pair, 3 for Three of kind, 4 for Full house, 6 for Four of kind
def kind(cards):
    count = 0
    for num in range(0, 14,3):
        for num1 in range(num, 12,3):
            if cards[num] == cards[num1+3]:
                count += 1
    return count

# Find Card is Straight Or Not
def straight(cards):
    # Create Order of card
    order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    # Assign Card to order
    order_cards = [ card[0] for x in order for card in cards.split(" ") if x == card[0]]
    # Compare if Each order of card same or not
    return [order.index(order_cards[num]) for num in range(0, 5)] == [x for x in range(order.index(order_cards[0]), order.index(order_cards[0])+5)]

# Give rank if card base on poker hand ranking chart
def ranking(cards):
    # It is Flush and Straight and Contain the the Letter A mean it from T to A so it royal flush
    if flush(cards) and straight(cards) and cards.__contains__("A"):
        return 10
    # If it is Flush and Straight it is straight Flush
    elif flush(cards) and straight(cards):
        return 9
    # When kind is 6 it is four of kind
    elif kind(cards) == 6:
        return 8
    # WHen kind is 4 it is Full house
    elif kind(cards) == 4:
        return 7
    # Call flush to check if it is flush or not
    elif flush(cards):
        return 6
    # Call straight to check if it is straight or not
    elif straight(cards):
        return 5
    # When Kind is 3 it is three of kind
    elif kind(cards) == 3 :
        return 4
    # When kind is 2 it is two pair
    elif kind(cards) == 2:
        return 3
    # When kind is 1 it is one pair
    elif kind(cards) == 1:
        return 2
    # When None of above it is no pair
    else:
        return 1

# Defining poker_hand() that take (player_one, player_two) parameter/augument
def poker_hand(player_one,player_two):
    print('poker_hand("' + player_one + '", "' + player_two + '")')
    if ranking(player_one) > ranking(player_two):
        print(">> Player 1 WIN")
        return ">> Player 1 WIN"
    elif ranking(player_one) == ranking(player_two):
        print(">> Tie")
        return ">> Tie"
    else:
        print(">> Player 2 WIN")
        return ">> Player 2 WIN"

# call poker_hand() function/method with passing string into parameters/auguments
poker_hand("AH KH QH JH TH", "AS KS TS 2H 3H")
poker_hand("AH KS QS JS TH", "8S 8H 8D 8C 2H")
poker_hand("AH KS QH JH TH", "AS KH QC JC TC")
