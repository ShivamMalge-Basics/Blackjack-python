import random

# Setup deck and card values
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4  # Standard 52-card deck
random.shuffle(deck)  # Shuffle the deck

# Assign values to each card; Aces handled separately during score calculation
card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10,
    "A": 11  # Aces start as 11, but will be adjusted
}

# Function to deal one card from the deck
def deal_card():
    return deck.pop()

# Function to calculate the total score of a hand
def calculate_score(cards, is_player=True):
    score = 0
    aces = 0  # Count the number of Aces
    values = []

    for card in cards:
        if card == "A":
            aces += 1
            if is_player:
                # Let player choose value of Ace manually
                while True:
                    try:
                        user_choice = int(input(f"You got an Ace! Choose value for Ace (1 or 11): "))
                        if user_choice in [1, 11]:
                            values.append(user_choice)
                            break
                    except:
                        pass
                continue  # Skip default scoring for Ace
        values.append(card_values[card])  # Add value of other cards

    score = sum(values)

    if not is_player:
        # Dealer logic: Convert Ace from 11 to 1 if score exceeds 21
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

    return score

# ------------------------- Game Starts Here -------------------------

# Deal 2 cards to player and dealer each
player_cards = [deal_card(), deal_card()]
dealer_cards = [deal_card(), deal_card()]

# Show initial hands
print(f"\nYour cards: {player_cards}")
print(f"Dealer's revealed card: {dealer_cards[0]}")
print("Dealer's second card is hidden.\n")

# --------- Player's Turn ---------
while True:
    player_score = calculate_score(player_cards, is_player=True)
    print(f"Your current score: {player_score}")
    
    if player_score > 21:
        print("You busted! Dealer wins.")
        exit()

    # Ask player to Hit or Stand
    move = input("Do you want to Hit or Stand? (h/s): ").strip().lower()
    if move == 'h':
        new_card = deal_card()
        player_cards.append(new_card)
        print(f"You drew: {new_card}")
    elif move == 's':
        break  # End player's turn

# --------- Dealer's Turn ---------
print(f"\nDealer's full hand: {dealer_cards}")
dealer_score = calculate_score(dealer_cards, is_player=False)
print(f"Dealer's score: {dealer_score}")

# Dealer keeps drawing until reaching 17 or more
while dealer_score < 17:
    new_card = deal_card()
    dealer_cards.append(new_card)
    print(f"Dealer draws: {new_card}")
    dealer_score = calculate_score(dealer_cards, is_player=False)
    print(f"Dealer's new score: {dealer_score}")

# --------- Determine Winner ---------
print(f"\nFinal Scores - You: {player_score} | Dealer: {dealer_score}")
if dealer_score > 21 or player_score > dealer_score:
    print("You win!")
elif player_score < dealer_score:
    print("Dealer wins!")
else:
    print("It's a draw!")

        
