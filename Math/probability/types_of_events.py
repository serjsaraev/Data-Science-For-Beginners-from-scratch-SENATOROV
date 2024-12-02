"""Types of events."""

# +
import random

# Certain Event: A tossed coin will fall to the ground (not simulated, as it's trivial).
print("Certain Event: A tossed coin will always fall to the ground.")

# Impossible Event: A coin will not fly upwards infinitely.
print("Impossible Event: A coin cannot fly upwards infinitely.")

# Random Event: Simulating a coin toss
def coin_toss():
    outcomes = ["Heads", "Tails"]
    return random.choice(outcomes)

print(f"Random Event (Coin Toss): {coin_toss()}")

# Random Event: Simulating a dice roll
def dice_roll():
    return random.randint(1, 6)

print(f"Random Event (Dice Roll): {dice_roll()}")

# Random Event: Drawing a card from a shuffled deck
def draw_card():
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck.pop()

print(f"Random Event (Card Draw): {draw_card()}")

# Checking for equally likely events
def is_equally_likely(events):
    probabilities = {event: events.count(event) / len(events) for event in set(events)}
    return len(set(probabilities.values())) == 1

# Example: Simulate 100 dice rolls and check for equal likelihood
dice_results = [dice_roll() for _ in range(100)]
print(f"Dice Roll Results: {dice_results[:10]}...")  # Display the first 10 results
print(f"Are dice rolls equally likely? {is_equally_likely(dice_results)}")

