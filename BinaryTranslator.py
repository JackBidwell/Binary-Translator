from ConvertDecimal import fractionBinary
from AlphabetLocation import letLocation
from IntTranslator import integerTranslate
from StringTranslator import stringTranslate
from PrintString import PrintString

binarystring = []

type = input("WELCOME TO BINARY TRANSLATOR WOULD YOU LIKE TO TRANSLATE A NUMBER (1) OR A STRING (2): ")
userInput = []

if type == "1":
  translate = input("WHAT NUMBER WOULD YOU LIKE TO TRANSLATE: ")
  original = input
  userInput.append(int(translate))
  integerTranslate(userInput)
elif type =="2":
  translate = input("WHAT STRING WOULD YOU LIKE TO TRANSLATE: ")
  original = translate
  translate = letLocation(translate)
  binarystring = stringTranslate(translate)
  PrintString(original, binarystring)
  
  


