class Card:
    def __init__(self, value, suit):
        self.value = str(value)
        self.suit = str(suit)
        self.score = 0

    def __str__(self):
        return '('+self.value+' '+self.suit+')'

    def getScore(self):
        if self.value == 'A':
            self.score += 1
        elif '2' <= self.value <= '9':
            self.score += int(self.value)
        else:
            self.score += 10
        return self.score
    
    def sum(self, other):
        return (self.score + other.score)%10

    def __lt__(self, rhs):
        board = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        board_suit = ['club','diamond','heart','spade']
        return (board.index(self.value),board_suit.index(self.suit)) < (board.index(rhs.value),board_suit.index(rhs.suit))

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
     print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
     print(cards[i])