from IntTranslator import integerTranslate

def fractionBinary(numerator, denominator):
  whole = False
  i = 1
  array = []
  while whole == False:
    fraction = int(numerator)/int(denominator)
    fraction = fraction * (2**i)
    if fraction.is_integer() == True:
      whole = True
      array.append(i)
      num = int(integerTranslate(array))
      print(num/(10**i))

    i += 1

  

  
  
