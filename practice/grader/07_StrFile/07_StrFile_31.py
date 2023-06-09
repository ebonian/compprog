def validate(dna: str) -> bool:
  dna_char = "ATGCatgc"

  for c in dna:
    if (c not in dna_char):
      return False
  
  return True

def reverse(dna: str) -> str:
  reverse_dna = str.maketrans('ATGCatgc', 'TACGtacg')

  dna = dna.translate(reverse_dna)
  dna = dna[::-1]

  return dna

def frequency(dna: str) -> str:
  count_dna = {}

  for i in range(len(dna)):
    count_dna[dna[i]] = 1 + count_dna.get(dna[i], 0)

  return "A=" + str(count_dna["A"]) + ", T=" + str(count_dna["T"]) + ", G=" + str(count_dna["G"]) + ", C=" + str(count_dna["C"])

def pair(dna: str) -> int:
  search_pair = input()

  count = 0

  for i in range(len(dna)):
    if (search_pair == dna[i:i+2]):
      count += 1

  return count

dna = input()

if (validate(dna)):
  method = input()
  dna = dna.upper()
  if (method == "R"): print(reverse(dna))
  if (method == "F"): print(frequency(dna))
  if (method == "D"): print(pair(dna))
else:
  print("Invalid DNA")