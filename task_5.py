def say_hello(name):
    msg = 'Hello, ' + name + '. How are you?'
    return msg
print(say_hello('bootcamp prep'))

def check_number(num):
    if (num > 0):
        return 'positive'
    elif (num < 0):
        return 'negative'
    else:
        return 'zero'
print(check_number(5))

def fizz_buzz_1(max):
  for i in range(0, max):
    if (i % 3 == 0 and i % 5 != 0):
      print(i)
    elif (i % 5 == 0 and i % 3 != 0):
      print(i)

fizz_buzz_1(20)

def even_caps(sentence):
    new_sentence = ""
    for i in range(0, len(sentence)):
        char = sentence[i]
        if (i % 2 == 0):
            capital_char = char.upper()
            new_sentence += capital_char
        else:
            new_sentence += char
    return new_sentence

print(even_caps("Hello World"))