def stringTranslate(array):
  i = 0
  original = array
  binarystring = []
  while i < len(array):
    binary = ""
    while array[i] > 0:
      binary = str(array[i] % 2) + binary
      array[i] = array[i]//2

    binarystring.append(str(binary))
    i += 1

  return(binarystring)

