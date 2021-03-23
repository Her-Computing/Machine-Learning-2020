from random import randint
#starting values
money = 1000
print("Your starting money is: 1000 dollars. \n\nIf you predict the number correctly, your money be multiplied by 50. Otherwise, you will lose the money you betted.")
#generate random number

while money > 25:
    computerGeneratedNumber = int(randint(0,49))
    #asking user for number and bet
    numberChosen = input("\nChoose a number between 0 and 49: ")
    numberChosen = int(numberChosen)
    #validating if number is legal
    while numberChosen > 49 or numberChosen < 0:
      print("\nYour guess was illegal! Try again!")
      numberChosen = input("\nChoose a number between 0 and 49: ")
      numberChosen = int(numberChosen)
    moneyAtStake = input("How much money would you like to bet? ")
    moneyAtStake = int(moneyAtStake)   
    #checking if bet is legal
    if moneyAtStake < money:
      print("\nThe wheel is spinning...")
      for i in range (0,5,1):
        print("...")
    while moneyAtStake > money or moneyAtStake < 0:
      print("Your bet is too big! Bet another value: ")
      moneyAtStake = input("How much money would you like to bet? ")
      moneyAtStake = int(moneyAtStake)   
    #sequence for determining new money
    if numberChosen == computerGeneratedNumber:
      money = moneyAtStake * 50 + money
      print("Computer number: ", computerGeneratedNumber)
      print("\nYou guessed correctly! Your money is now: "+str(money))
    elif numberChosen + 5 >= computerGeneratedNumber > numberChosen or  numberChosen - 5 <= computerGeneratedNumber < numberChosen:
      money = moneyAtStake * 10 + money
      print("Computer number: ", computerGeneratedNumber)
      print("\nYour guess was close! Your money is now: "+str(money))
    else:
      money -= moneyAtStake
      print("Computer number: ", computerGeneratedNumber)
      print("\nYour guess was wrong. Your money s now: "+ str(money))
    #checking if player is running out of money
    if money <= 25:
      print("\nYou are running out of money! You have lost!!")
      break