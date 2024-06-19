# Translate number to Binary with looping remainder



translate = input("What would you like to translate: ")
type = input("Would you like to translate a number(1) or a word(2)")
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetposition = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]


if type == "1":
  num = int(translate)
elif type == "2":
  num = []
  i = 0
  while i < len(translate):
    j = 0
    while j < len(alphabet):
      if translate[i] == alphabet[j]:
        num.append(alphabetposition[j])
      j += 1

print(num)


    

# binary = ""
# while num > 0:
#   binary = str(num % 2) + binary
#   num = num//2

# print(binary)
  
