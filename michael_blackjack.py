#Michael Han, student number 101157504, assignment 3

import random
#calculates user hand's sum
def sumHand(hand):
    #setting sum equal to zero         
    sum = 0
    for i in range (len(hand)):
        #if hand[i] is J
        if hand[i] == 'J':
            
            sum+=10

        #if hand[i] is Q
        elif hand[i] == 'Q':
            
            sum+=10

        #if hand[i] is K
        elif hand[i]=='K':
            sum+=10

        
        #if hand[i] is A
        elif hand[i]=='A':
            sum+=11
            
            
        #if hand [i] is a numbered card
        else:
            sum+=hand[i]

    #if sum is greater than 21
    if sum >21:
        if 'A' in hand:
            #setting counter
            j=0
            #counting for A's, subtracting 10 (making each A value 1) until sum is less than 21
            while sum >21 and j < hand.count('A'):
                sum-=10
                j+=1
            
            return sum 

        else:
            return sum
    #if sum is less than or equal to 21 
    else:
        return sum            

#prints player's hand and sum of player's hand
def displayHand(hand):
    sum = sumHand(hand)
    handDis=""
    for i in range(0,len(hand)):
        handDis += str(hand[i])+" "

    print(f"Your hand: {handDis}  ({sum})")
    
    

#gives player random card from deck
def dealCard():
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    i = random.randrange(0, len(deck))
    #if 1
    if deck[i] == 1:
        card = 'A'
    #if 11
    elif deck[i]==11:
        card = 'J'
    #if 12
    elif deck[i]==12:
        card = 'Q'
    #if 13
    elif deck[i]==13:
        card = 'K'
    #anything else
    else:
        card = deck[i]
    
    return card

#gives player a rank depending on their score
def getRank(score):
    #95 or above
    if score >= 95:
        return "Ace!"
    #less than 95, greater than or equal to 85
    elif score >=85:
        return "King"
    #less than 85, greater than or equal to 75
    elif score >=75:
        return "Queen"  
    #less than 75, greater than or equal to 50
    elif score >=50:
        return "Jack"
    #less than 50, greater than or equal to 25
    elif score >=25:
        return "Commoner"
    #less than 25, greater than -5 (-5 is lowest possible score (100-5*21))
    else:
        return "Noob"

#main function
def main():
    #welcome
    print("Welcome to Michael's Blackjack!")
    #setting score to 100
    score = 100

    #looping for 5 rounds
    for i in range (0, 5):
        #print round number
        print(f"Round {i+1}")
        #print score
        print(f"Score: {score}")
        #setting hand to empty list
        hand = []
        
        #gives user two cards to start
        for i in range (0,2):
            #getting card from dealCard function
            card = dealCard()
            #adding card to hand list
            hand.append(card)

        #printing hand
        displayHand(hand)
        ans=""
        #while user doesn't enter stand and sum is less than 22
        while ans != "stand" and sumHand(hand)<22:
            ans = str(input("Would you like to 'hit' or 'stand': "))
            #if player hits
            if ans == "hit":
                card = dealCard()
                hand.append(card)
                displayHand(hand)
            
        #if the sum of player's hand is less than or equal to 21
        if sumHand(hand)<=21:
            #minus the difference from 21 and the user's hand from score
            score = score - (21 - sumHand(hand))
            print(f"Score: {score}\n\n")

        #if sum of player's hand is more than 21
        else:
            #minus 21 from score
            score -= 21
            print("Busted")
            print(f"Score: {score}\n\n")
    #getting rank
    rank=getRank(score)
    #printing final score and rank
    print(f"Final score: {score}, Rank: {rank}")
    print("Thanks for playing!")

main()