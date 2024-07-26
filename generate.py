import random

coin = random.choice(["heads", "tails"])
print(coin)

from random import choice

coin = choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["jack","queen","king"]
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)

import statistics

print(statistics.mean([100, 90]))









