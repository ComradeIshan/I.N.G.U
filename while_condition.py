#i = 1
#while i <= 5:
 #   print('*' * i)
  #  i = i + 1
#print("Done")
#Guessing game -

Attempts = 0
correct_number = 9
limit = 3
while Attempts < limit:
    guess = int(input("Guess your number: "))
    Attempts = Attempts + 1
    if guess == correct_number:
        print("You win")
        break
else:
    print("Fail")



