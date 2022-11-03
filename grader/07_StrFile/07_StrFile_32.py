def eight_characters(password: str):
  error_msg = "Less than 8 characters"
  less_than_eight = False

  if (len(password) >= 8):
    less_than_eight = True

  if (not less_than_eight): print(error_msg)
  return less_than_eight

def no_lowercase(password: str):
  error_msg = "No lowercase letters"
  has_lowercase = False

  for character in password:
    if (character.islower()):
      has_lowercase = True

  if (not has_lowercase): print(error_msg)
  return has_lowercase

def no_uppercase(password: str):
  error_msg = "No uppercase letters"
  has_uppercase = False

  for character in password:
    if (character.isupper()):
      has_uppercase = True

  if (not has_uppercase): print(error_msg)
  return has_uppercase

def no_numbers(password: str):
  error_msg = "No numbers"
  has_number = False

  for character in password:
    if (character.isnumeric()):
      has_number = True

  if (not has_number): print(error_msg)
  return has_number

def no_symbols(password: str):
  error_msg = "No symbols"

  special_characters = "\'!@#$%^&*()-+?_=,<>/\""
  
  has_symbol = False

  for character in password:
    if (character in special_characters):
      has_symbol = True

  if (not has_symbol): print(error_msg)
  return has_symbol

def repetition(password: str):
  error_msg = "Character repetition"
  no_repetition = True

  for i in range(len(password)):
    phrase = password[i:i+4]
    if (len(phrase) == 4):
      phrase_ascii = [ord(c) for c in phrase]
      phrase_avg = sum(phrase_ascii) // len(phrase_ascii)
      if (phrase_avg == phrase_ascii[0] and phrase_avg == phrase_ascii[1] and phrase_avg == phrase_ascii[2] and phrase_avg == phrase_ascii[3]):
        no_repetition = False

  if (not no_repetition): print(error_msg)
  return no_repetition

def number_sequence(password: str):
  error_msg = "Number sequence"

  sequence = "01234567890"

  no_sequence = True

  for i in range(len(password)):
    if (password[i].isnumeric()):
      numbers = password[i:i+4]
      if (len(numbers) == 4 and (numbers in sequence or numbers in sequence[::-1])):
        no_sequence = False

  if (not no_sequence): print(error_msg)
  return no_sequence

def letter_sequence(password: str):
  error_msg = "Letter sequence"

  sequence = "abcdefghijklmnopqrstuvwxyz"

  no_sequence = True

  for i in range(len(password)):
    phrase = password[i:i+4].lower()
    if (len(phrase) == 4 and (phrase in sequence or phrase in sequence[::-1])):
      no_sequence = False

  if (not no_sequence): print(error_msg)
  return no_sequence

def keyboard_pattern(password: str):
  error_msg = "Keyboard pattern"

  sequence = "!@#$%^&*()_+qwertyuiopasdfghjklzxcvbnm"

  no_sequence = True

  for i in range(len(password)):
    phrase = password[i:i+4].lower()
    if (len(phrase) == 4 and (phrase in sequence or phrase in sequence[::-1])):
      no_sequence = False

  if (not no_sequence): print(error_msg)
  return no_sequence


def main():
  user_password = input()

  results = []

  results.append(eight_characters(user_password))
  results.append(no_lowercase(user_password))
  results.append(no_uppercase(user_password))
  results.append(no_numbers(user_password))
  results.append(no_symbols(user_password))
  results.append(repetition(user_password))
  results.append(number_sequence(user_password))
  results.append(letter_sequence(user_password))
  results.append(keyboard_pattern(user_password))

  i = 0
  is_pass = True

  while (i < len(results)):
    if (not results[i]):
      is_pass = False
    i+=1

  if (is_pass): print("OK")

main()