card_value = ['3', '4', '5', '6', '7', '8',
              '9', '10', 'J', 'Q', 'K', 'A', '2']
card_suit = ['club', 'diamond', 'heart', 'spade']


class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

    def __str__(self) -> str:
        return "({} {})".format(self.value, self.suit)

    def next1(self):
        next_value = card_value[(card_value.index(self.value) + 1) % 13]
        next_suite = card_suit[(card_suit.index(self.suit) + 1) % 4]
        if (next_suite == 'club'):
            return Card(next_value, next_suite)
        else:
            return Card(self.value, next_suite)

    def next2(self):
        next_value = card_value[(card_value.index(self.value) + 1) % 13]
        next_suite = card_suit[(card_suit.index(self.suit) + 1) % 4]
        if (next_suite == 'club'):
            self.value = next_value
            self.suit = next_suite
        else:
            self.suit = next_suite


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
