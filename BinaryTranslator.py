from ConvertDecimal import fractionBinary
from AlphabetLocation import letLocation
from IntTranslator import integerTranslate
from StringTranslator import stringTranslate
from PrintString import PrintString

binarystring = []

type = input("WELCOME TO BINARY TRANSLATOR WOULD YOU LIKE TO TRANSLATE A NUMBER (1) OR A STRING (2): ")
userInput = []

if type == "1":
  isFraction = input("ARE YOU GOING TO BE TRANSLATING A FRACTION? (Y/N): ")
  if isFraction.lower() == "y":
    numerator = input("WHAT IS THE NUMERATOR?: ")
    demoninator =  input("WHAT IS THE DENOMINATOR?: ")
    fractionBinary(numerator, demoninator)
  elif isFraction.lower() == "n":
    translate = input("WHAT NUMBER WOULD YOU LIKE TO TRANSLATE: ")
    original = input
    userInput.append(int(translate))
    print(integerTranslate(userInput))
elif type =="2":
  translate = input("WHAT STRING WOULD YOU LIKE TO TRANSLATE: ")
  original = translate
  translate = letLocation(translate)
  binarystring = stringTranslate(translate)
  PrintString(original, binarystring)
  
  


