# Blackjack CLI (Command Line Interface) – Python Implementation

A simple command-line Blackjack game written in Python, focused on **teaching programming concepts** and helping beginners understand **code flow**, **conditional logic**, and **basic data structures**. This isn't just a game—it's a way to **learn how to think like a programmer**.

---

## 🧠 Core Concepts Used

- **Dictionaries** for mapping card values.
- **Lists** for maintaining player and dealer hands.
- **Functions** to modularize logic.
- **Loops** for continuous gameplay (`while`).
- **Conditionals** (`if`, `else`) for decision-making.
- **User input handling** using `input()`.
- **Score evaluation logic**, including Ace adjustments.

---

## 🗂️ File Structure

blackjack/
├── blackjack.py # Main game logic
└── README.md # Documentation and code explanation


---

## 🎮 How the Game Works (Code Flow)

### Step 1: Card Value Definitions

A dictionary `card_values` is used to map cards like `'2'` to `2`, `'J'` to `10`, and `'A'` to `11` by default. Ace logic is adjusted later.

```python
card_values = {
    "2": 2, ..., "A": 11
}

```
### Step 2: Function – calculate_score(cards: list)

Calculates total score from the card list, handling Aces as either 11 or 1 depending on total value.

```python

    def calculate_score(cards):
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
```


### Step 3: Initial Card Draw

    Player and Dealer are each dealt 2 cards.

    Dealer's second card is hidden.

    Player is shown both their cards but not the score (to mimic real gameplay).


```python
    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]

```


### Step 4: Player Turn – Hit or Stand

    Player is repeatedly asked whether to Hit (draw another card) or Stand (end their turn).

    Every time they hit, the new card is added, and the cards are displayed.

    If an Ace is drawn, the player chooses whether to count it as 1 or 11.

```python

if new_card == 'A':
    value = input("Choose value for Ace (1 or 11): ")

```

### Step 5: Dealer Turn (after player stands)

    Dealer draws until their score is at least 17 (standard rule).

    Aces are auto-adjusted here—no input.

```python
while calculate_score(dealer_cards) < 17:
    dealer_cards.append(draw_card())

```




### Step 6: Final Result

Once both turns are done:

    Scores are compared

    Winner is decided and shown with both hands revealed

```python
if player_score > 21:
    print("You busted. Dealer wins.")
elif dealer_score > 21 or player_score > dealer_score:
    print("You win!")

```



























