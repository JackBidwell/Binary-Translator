# Translate number to Binary with looping remainder


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetposition = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
num = []
binarystring = []
type = input("WELCOME TO BINARY TRANSLATOR WOULD YOU LIKE TO TRANSLATE A NUMBER (1) OR A STRING (2): ")

if type == "1":
  translate = input("WHAT NUMBER WOULD YOU LIKE TO TRANSLATE: ")
  num.append(int(translate))
elif type == "2":
  translate = input("WHAT STRING WOULD YOU LIKE TO TRANSLATE: ")
  num = []
  i = 0
  while i < len(translate):
    j = 0
    while j < len(alphabet):
      if translate[i] == alphabet[j]:
        num.append(alphabetposition[j])
      j += 1
    i += 1

print(num)
finalprint = num[0]
negative = False

i = 0
while i < len(num):
  binary = ""
  if num[i] < 0:
    num[i] *= -1
    negative = True
  while num[i] > 0:
    binary = str(num[i] % 2) + binary
    num[i] = num[i]//2
  
  binarystring.append(str(binary))
  i += 1

if type == "1":
  if negative == True:
    print("Your number "+ str(finalprint) + "in binary is -" + str(binarystring[0]))
  else:
    print("Your number "+ str(finalprint) + "in binary is " + str(binarystring[0]))



  
