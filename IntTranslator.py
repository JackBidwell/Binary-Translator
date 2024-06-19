def integerTranslate(array):
  original = array[0]
  negative = False
  binarystring = []
  i = 0
  while i < len(array):
    binary = ""
    if array[i] < 0:
      array[i] *= -1
      negative = True
    while array[i] > 0:
      binary = str(array[i] % 2) + binary
      array[i] = array[i]//2
    binarystring.append(str(binary))
    i += 1

    if negative == True:
      print("Your number "+ str(original) + " in binary is -" + str(binarystring[0]))
    else:
      print("Your number "+ str(original) + " in binary is " + str(binarystring[0]))

