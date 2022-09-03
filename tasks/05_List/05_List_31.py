cards = input().split(" ")
operations = input()

def cut(cards):
  card_length = len(cards)
  left_pile = cards[:card_length // 2]
  right_pile = cards[card_length // 2:]

  return right_pile + left_pile

def shuffle(cards):
  card_length = len(cards)
  left_pile = cards[:card_length // 2]
  right_pile = cards[card_length // 2:]

  combined_pile = []

  for a, b in zip(left_pile, right_pile):
    combined_pile.append(a)
    combined_pile.append(b)

  return combined_pile

for operation in operations:
  if (operation == "C"):
    cards = cut(cards)
  elif (operation == "S"):
    cards = shuffle(cards)

print(" ".join(cards))