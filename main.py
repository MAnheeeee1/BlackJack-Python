import random
import art

player_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_decide_winner = False

def draw_card(card_deck, amount_of_card):
    for card in range(amount_of_card):
        card_deck.append(random.choice(cards))

def calculate_score(card_deck):
    total_point = sum(card_deck)
    if 11 in card_deck and total_point > 21:
        total_point -= 10
    return total_point

# First round of the game
play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(art.logo)
draw_card(player_cards, 2)
player_score = calculate_score(player_cards)
draw_card(computer_cards, 2)
computer_first_card = computer_cards[0]
print(f"Your cards: {player_cards}, current score: {player_score}")
print(f"Computer's first card: {computer_first_card}")

# Loop that asks the player if he/she wants to draw another card
while not should_decide_winner:
    draw_card_request = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_card_request == "y":
        draw_card(player_cards, 1)
        player_score = calculate_score(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        if player_score > 21:
            print("You went over. You lose.")
            should_decide_winner = True
    else:
        should_decide_winner = True
while sum(computer_cards) < 17 and player_score < 22:
    print("The sum of card computure, is under 17\nIt will draw a new card!")
    draw_card(computer_cards, 1)
    print(f"The computure draw {computer_cards[-1]} point")
# Decide the winner
player_final_score = calculate_score(player_cards)
computer_final_score = calculate_score(computer_cards)

if computer_final_score > 21:
    print(f"Your score: {player_final_score}")
    print(f"Computure score: {computer_final_score}")
    print("You have won, the computre point is over 21")
elif player_final_score > computer_final_score:
    print(f"Your score: {player_final_score}")
    print(f"Computure score: {computer_final_score}")
    print("You have won")
else:
    print(f"Your score: {player_final_score}")
    print(f"Computure score: {computer_final_score}")
    print("Computure has won")
print(player_cards)
print(computer_cards)
