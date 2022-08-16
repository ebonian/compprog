class Card:
    def __init__(self, value, suit):
        self.value = str(value)
        self.suit = str(suit)

    def __str__(self):
        return '('+self.value+' '+self.suit+')'

    def next1(self):
        deck = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','3']
        board_suit = ['club','diamond','heart','spade']
        if self.suit == 'spade': return Card(deck[deck.index(self.value)+1],'club')
        else: return Card(self.value,board_suit[board_suit.index(self.suit)+1])

    def next2(self):
        new = self.next1()
        self.value = new.value
        self.suit = new.suit

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
