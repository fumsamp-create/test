import random
morse = { "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",}


list = ["code", "bit", "list", "soul", "next"]
answers = []
def morse_encode(word):
    encode_word = ""
    for letter in word:
      letter_code = morse[letter]
      encode_word = encode_word + letter_code
    return encode_word

def get_word(list):
  return random.choice(list)

def print_statisctics(answers):
  all = len(answers)
  right_ans = answers.count(True)
  wrong_ans = answers.count(False)

  return f"Всего задач {all}, верно решего {right_ans}, неверно решено{wrong_ans}"
print("Сегодня мы потренеруемся с морзянкой!")
input("Нажмите Enter для продолжения")

for question in range(5):
  random_word = get_word(list)
  coded_word = morse_encode(random_word)
  print(f"слово - {coded_word}")
  user_input = input("Ваш ответ\n")
  if user_input == random_word:
    print("Верный ответ!")
    answers.append(True)
  else:
    print(f"неверный ответ!, правильно будет - {random_word}")
    answers.append(False)
print_statisctics(answers)
