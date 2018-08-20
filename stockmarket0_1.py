#!/usr/bin/env python3

import random
import sys
import time
import threading
import os

def newGame():
	while True:
		playerOption = "d"
		#playerOption = input("d for action, q to quit: ")
		if playerOption != "d":
			sys.exit()
		else:
			
			gameLogic()
			

def playerStatus():
	playerStatus.playerMoney = 10000
	playerStatus.playerLoan = 0
	

def buyStock():
	stockList = stockPrice.stockList
	print("options:")
	print(" | ".join(map(str,stockList)))
	whatStockToBuy = input("What stock to buy? \n:")
	
	
	if whatStockToBuy in stockList:
		
		try:
			playerChosenStock = getattr(stockPrice, whatStockToBuy)
			if playerChosenStock > 0:
				print("One share of " + whatStockToBuy + " is currently priced at", playerChosenStock, "$")
		
		
				howManyToBuy = int(input("How many would you want to buy? \n:"))
				totalprice = (howManyToBuy * int(playerChosenStock))
				assetsNow = getattr(showAssets, whatStockToBuy)
				print("Total price of purchase:",totalprice, "$")
	
				areYouSure = input("Confirm buy, (y)es or (n)o \n:")
		
				if totalprice > playerStatus.playerMoney:
					print("You dont have the cash!")
					pass
	
				else:	
					if areYouSure == "y":
						playerStatus.playerMoney -= totalprice
						print("Bought " + whatStockToBuy + " stock for at total price of", totalprice, "$")
						assetsNew = (assetsNow + int(howManyToBuy))
						setattr(showAssets, whatStockToBuy, assetsNew) 
		
					else:
						pass
			else:
				print(whatStockToBuy + " is currently negative, wait until it is positive to buy. Price:", playerChosenStock)
				pass
		except ValueError:
			pass
		
		

	else:
		print("Please put in a valid stock name.")
	
def sellStock():
	stockList = stockPrice.stockList
	print("Options:")
	print(" | ".join(map(str,stockList)))
	whatStockToSell = input("What stock to sell? \n:")
	stockList = stockPrice.stockList
	howManyDoYouHave = getattr(showAssets, whatStockToSell)
	
	if whatStockToSell in stockList:
		try:
			playerChosenStock = getattr(stockPrice, whatStockToSell)
			if playerChosenStock > 20:
				print("One share of " + whatStockToSell + " is currently priced at: ", playerChosenStock, "$")
				print("You currently have", howManyDoYouHave, "shares")
				howManyToSell = int(input("How many shares would you like to sell? \n:"))
				totalprice = (howManyToSell * int(playerChosenStock))
				assetsNow = getattr(showAssets, whatStockToSell)
				print("Total sum of sale: ", totalprice, "$") 
	
				areYouSure = input("Confirm sale, (y)es or (n)o \n:")
	
				if howManyToSell > assetsNow:
					print("You don't have that many, you have", assetsNow, "shares of " + whatStockToSell)
					pass
	
				else:
					if areYouSure == "y":
						playerStatus.playerMoney += totalprice
						print("Sold " + whatStockToSell + " stock for a total price of", totalprice, "$")
						assetsNew = (assetsNow - int(howManyToSell))
						setattr(showAssets, whatStockToSell, assetsNew)
		
					else:
						pass
			else:
				print("The goverment has put a hold on " + whatStockToSell + " please wait until the stock reaches 20 $ a share to sell. Price:", playerChosenStock, "$")
		except ValueError:
			print("Please put in a number.")
			pass
	else:
		print("Please put in a valid stock name.")
		pass
			
def loans():
	playerMoney1 = playerStatus.playerMoney
	currentLoan = playerStatus.playerLoan
	maximumLoan = ((playerMoney1 * 2) - currentLoan*4)
	
	try:
		playerAnswer = input("Would you like to (t)ake a loan or (p)ay back a loan? \n:")	
		if playerAnswer == "t":
			if maximumLoan > 0:
				print("You currently qualify for a loan of: ", maximumLoan, "$")
				howMuchLoanDoesCuWant = int(input("How much would you like to loan? \n:"))
	
		
				if howMuchLoanDoesCuWant > maximumLoan:
					newLoan3 = int(currentLoan + maximumLoan)
					newCash3 = int(playerMoney1 + maximumLoan)
					setattr(playerStatus, "playerLoan", newLoan3)
					setattr(playerStatus, "playerMoney", newCash3)
					print("Maximum loan approved.")
				else:
					newLoan = int(currentLoan + howMuchLoanDoesCuWant)
					newCash = int(playerMoney1 + howMuchLoanDoesCuWant)
					setattr(playerStatus, "playerLoan", newLoan)
					setattr(playerStatus, "playerMoney", newCash)
					print("Loan approved.")
			else:
				print("You currently don't qualify for a loan, raise your net worth.")
				pass
		elif playerAnswer == "p":
			print("Your current loan outstanding is ", currentLoan, "$")
			playerChoice = int(input("How much would you like to pay back? \n:"))
			if playerChoice > currentLoan:
				print("You dont owe that much money") 
				if playerChoice < playerMoney1:
					playerChoice2 = input("Would you like to pay back the full loan? (y)es or (n)o \n:")
					if playerChoice2 == "y":
							newLoan2 = 0
							newCash2 = int(playerMoney1 - currentLoan)
							setattr(playerStatus, "playerLoan", newLoan2)
							setattr(playerStatus, "playerMoney", newCash2)
							print("Payment succesful.")
					else:
						pass	
				else:
					pass
			else:
				newLoan1 = int(currentLoan - playerChoice)
				newCash1 = int(playerMoney1 - playerChoice)
				setattr(playerStatus, "playerLoan", newLoan1)
				setattr(playerStatus, "playerMoney", newCash1)
				print("Payment succesful.")
		else:
			print("Error 1L, you can continue to play the game.")
			pass
	
	except (ValueError):
		print("Please put in valid information.")
	
	
def interest():
	
	while True:
		currentLoan = playerStatus.playerLoan 
		playerMoney1 = playerStatus.playerMoney
		holderInput = "y"
		
		if currentLoan == 0:
			time.sleep(60)
			pass
		else:
			interest = (currentLoan / 2000)
			newCash = int(playerMoney1 - interest)
			newLoan = int(currentLoan - interest)
			setattr(playerStatus, "playerMoney", newCash)
			setattr(playerStatus, "playerLoan" , newLoan)
			time.sleep(2)
			pass
			
def showAssets():
	showAssets.aapl = 0
	showAssets.goog = 0
	showAssets.lnx = 0
	showAssets.a = 0
	showAssets.c = 0
	showAssets.hog = 0
	showAssets.hpq = 0
	showAssets.intc = 0
	showAssets.ko = 0
	showAssets.luv = 0
	showAssets.mmm = 0
	showAssets.msft = 0
	showAssets.t = 0
	showAssets.tgt = 0
	showAssets.txn = 0
	showAssets.wmt = 0

	
def stockPrice():
	stockPrice.aapl = 200
	stockPrice.goog = 200
	stockPrice.lnx = 200
	stockPrice.a = 200
	stockPrice.c = 200
	stockPrice.hog = 200
	stockPrice.hpq = 200
	stockPrice.intc = 200
	stockPrice.ko = 200
	stockPrice.luv = 200
	stockPrice.mmm = 200
	stockPrice.msft = 200
	stockPrice.t = 200
	stockPrice.tgt = 200
	stockPrice.txn = 200
	stockPrice.wmt = 200
	
	stockPrice.stockList = ["aapl", "goog", "lnx", "a", "c", "hog", "hpq", "intc", "ko", "luv", "mmm", "msft", "t", "tgt", "txn", "wmt"]

def marketSwing():
	marketSwing.directionOfMarket = 1
	marketSwing.directionOfMarket1 = 1
	marketSwing.directionOfMarket2 = 1
	marketSwing.directionOfMarket3 = 1
	marketSwing.directionOfMarket4 = 1
	marketSwing.directionOfMarket5 = 1
	marketSwing.directionOfMarket6 = 1
	marketSwing.directionOfMarket7 = 1
	marketSwing.directionOfMarket8 = 1
	marketSwing.directionOfMarket9 = 1
	marketSwing.directionOfMarket10 = 1
	marketSwing.directionOfMarket11 = 1
	marketSwing.directionOfMarket12 = 1
	marketSwing.directionOfMarket13 = 1
	marketSwing.directionOfMarket14 = 1
	marketSwing.directionOfMarket15 = 1
	
	
	while True:
		holderInput = "y"
		
			
		if holderInput == "y":
			randomChoice = random.randint(1,16)
			timeToChange = 1
			
			# debug change time print(timeToChange, " seconds info next market change")
			time.sleep(timeToChange)
				
			if randomChoice == 1:
				marketSwing.directionOfMarket = random.randint(1,6)	
				#print(marketSwing.directionOfMarket, marketSwing.directionOfMarket1, marketSwing.directionOfMarket2)
			elif randomChoice == 2:
				marketSwing.directionOfMarket1 = random.randint(1,6)
				#print(marketSwing.directionOfMarket, marketSwing.directionOfMarket1, marketSwing.directionOfMarket2)
			elif randomChoice == 3:
				marketSwing.directionOfMarket2 = random.randint(1,6)
				#print(marketSwing.directionOfMarket, marketSwing.directionOfMarket1, marketSwing.directionOfMarket2)
			elif randomChoice == 4:
				marketSwing.directionOfMarket3 = random.randint(1,6)
			elif randomChoice == 5:
				marketSwing.directionOfMarket4 = random.randint(1,6)
			elif randomChoice == 6:
				marketSwing.directionOfMarket5 = random.randint(1,6)
			elif randomChoice == 7:
				marketSwing.directionOfMarket6 = random.randint(1,6)
			elif randomChoice == 8:
				marketSwing.directionOfMarket7 = random.randint(1,6)
			elif randomChoice == 9:
				marketSwing.directionOfMarket8 = random.randint(1,6)
			elif randomChoice == 10:
				marketSwing.directionOfMarket9 = random.randint(1,6)
			elif randomChoice == 11:
				marketSwing.directionOfMarket10 = random.randint(1,6)
			elif randomChoice == 12:
				marketSwing.directionOfMarket11 = random.randint(1,6)
			elif randomChoice == 13:
				marketSwing.directionOfMarket12 = random.randint(1,6)
			elif randomChoice == 14:
				marketSwing.directionOfMarket13 = random.randint(1,6)
			elif randomChoice == 15:
				marketSwing.directionOfMarket14 = random.randint(1,6)
			elif randomChoice == 16:
				marketSwing.directionOfMarket15 = random.randint(1,6)					
			else:
				pass
				
		else:
			pass	
	
def stockPriceChange(first, second, third, four):
	direction = first
	timeToChange = 1
	stockPriceName = second
	stockNameText = third
	stockNameTextStr = four
	
	while True:
		priceNow = getattr(stockPrice, stockNameTextStr)
		directionOfMarkets = getattr(marketSwing, direction)
		time.sleep(timeToChange)
		if directionOfMarkets == 1:
			timeToChange = random.randint(1,10)
			randomnumber = random.randint(1,5)
			priceNew = (priceNow + randomnumber)
			setattr(stockPrice, stockNameTextStr, priceNew)
		elif directionOfMarkets == 2:
			timeToChange = random.randint(1,3)
			randomnumber = random.randint(1,7)
			priceNew = (priceNow + randomnumber)
			setattr(stockPrice, stockNameTextStr, priceNew)
		elif directionOfMarkets == 3:
			timeToChange = random.randint(1,2)
			randomnumber = random.randint(1,10)
			priceNew = (priceNow + randomnumber)
			setattr(stockPrice, stockNameTextStr, priceNew)
		elif directionOfMarkets == 4:
			timeToChange = random.randint(1,10)
			randomnumber = random.randint(1,2)
			priceNew = (priceNow - randomnumber)
			setattr(stockPrice, stockNameTextStr, priceNew)
		elif directionOfMarkets == 5:
			timeToChange = random.randint(1,3)
			randomnumber = random.randint(1,5)
			priceNew = (priceNow - randomnumber)
			setattr(stockPrice, stockNameTextStr, priceNew)
		else:
			timoToChange = random.randint(1,2)
			randomnumber = random.randint(1,7)
			priceNew = (priceNow - randomnumber)
			setattr(stockPrice, stockNameTextStr, priceNew)

def helper():
	print("Welcome to the help page, some things to get you started \n \nYou move around the game by typing the letter in lowercase that is in a parenthes.\n \nAs an example: '(b)uy' type b to get to the buy page. \
	\n \nWhen buying and selling stock, use lowercase and the stock names shown on the buy/sell \nscreen.\n \nExample: To buy Linux stock just type lnx in the buy screen.\n \n\
Some time after you have taken a loan you will automaticaly start paying it back. \nYou also pay interest 0,2% , this might seem low but it happens every 2 seconds. \n \nThe game is based fully in python. \n \n                  // version 0.1 //  \n \n \n \n ")
			
def gameLogic():
	
	playerChoice = input("(b)uy stock, (s)ell stock, show (a)ssets, show (m)arket, (l)oans ,(h)elp or (q)uit to exit\n: ")
		
	if playerChoice == "b":
		buyStock()
		print("Your current money: ",playerStatus.playerMoney, "$")
	elif playerChoice == "s":
		sellStock()
		print("Your current money: ",playerStatus.playerMoney, "$")
	elif playerChoice == "a":
		print(" aapl:", showAssets.aapl, "\n",
		"goog:", showAssets.goog, "\n",
		"lnx: ", showAssets.lnx, "\n",
		"a:   ", showAssets.a, "\n",
		"c:   ", showAssets.c, "\n",
		"hog: ", showAssets.hog, "\n",
		"hpq: ", showAssets.hpq, "\n",
		"intc:", showAssets.intc, "\n",
		"ko:  ", showAssets.ko, "\n",
		"luv: ", showAssets.luv, "\n",
		"mmm: ", showAssets.mmm, "\n",
		"msft:", showAssets.msft, "\n",
		"t:   ", showAssets.t, "\n",
		"tgt: ", showAssets.tgt, "\n",
		"txn: ", showAssets.txn, "\n",
		"wmt: ", showAssets.wmt, "\n","\n", 
		"cash:", playerStatus.playerMoney, "$", "\n",
		"loan:", playerStatus.playerLoan, "$") 
		
		
	elif playerChoice == "m":
		print(" aapl:", stockPrice.aapl, "$", "\n",
		"goog:", stockPrice.goog, "$", "\n",
		"lnx: ", stockPrice.lnx, "$", "\n",
		"a:   ", stockPrice.a, "$", "\n",
		"c:   ", stockPrice.c, "$", "\n",
		"hog: ", stockPrice.hog, "$", "\n",
		"hpq: ", stockPrice.hpq, "$", "\n",
		"intc:", stockPrice.intc, "$", "\n",
		"ko:  ", stockPrice.ko, "$", "\n",
		"luv: ", stockPrice.luv, "$", "\n",
		"mmm: ", stockPrice.mmm, "$", "\n",
		"msft:",stockPrice.msft, "$", "\n",
		"t:   ", stockPrice.t, "$", "\n",
		"tgt: ", stockPrice.tgt, "$", "\n",
		"txn: ", stockPrice.txn, "$", "\n",
		"wmt: ", stockPrice.wmt, "$", "\n")
	elif playerChoice == "l":
		loans()
	elif playerChoice == "h":
		helper()
	elif playerChoice == "q":
		os._exit(0)
	else:
		print("Please chose a valid option, type h for help.")



print("Welcome to a the simple (c)onsole based (s)tockmarket game\n")
playerStatus()
showAssets()
stockPrice()


n = threading.Thread(name="game", target=newGame, daemon=True)
ms = threading.Thread(name="marketswing", target=marketSwing, daemon=True)

s1 = threading.Thread(name="stockPriceChange", target=stockPriceChange, args=("directionOfMarket", stockPrice.aapl, "AAPL: ", "aapl",), daemon=True)
s2 = threading.Thread(name="stockPriceChange1", target=stockPriceChange, args=("directionOfMarket1", stockPrice.goog, "GOOG: ", "goog",), daemon=True)
s3 = threading.Thread(name="stockPriceChange2", target=stockPriceChange, args=("directionOfMarket2", stockPrice.lnx, "LNX: ", "lnx",), daemon=True)
s4 = threading.Thread(name="stockPriceChange3", target=stockPriceChange, args=("directionOfMarket3", stockPrice.a, "A: ", "a",), daemon=True)
s5 = threading.Thread(name="stockPriceChange4", target=stockPriceChange, args=("directionOfMarket4", stockPrice.c, "C: ", "c",), daemon=True)
s6 = threading.Thread(name="stockPriceChange5", target=stockPriceChange, args=("directionOfMarket5", stockPrice.hog, "HOG: ", "hog",), daemon=True)
s7 = threading.Thread(name="stockPriceChange6", target=stockPriceChange, args=("directionOfMarket6", stockPrice.hpq, "HPQ: ", "hpq",), daemon=True)
s8 = threading.Thread(name="stockPriceChange7", target=stockPriceChange, args=("directionOfMarket7", stockPrice.intc, "INTC: ", "intc",), daemon=True)
s9 = threading.Thread(name="stockPriceChange8", target=stockPriceChange, args=("directionOfMarket8", stockPrice.ko, "KO: ", "ko",), daemon=True)
s10 = threading.Thread(name="stockPriceChange9", target=stockPriceChange, args=("directionOfMarket9", stockPrice.luv, "LUV: ", "luv",), daemon=True)
s11 = threading.Thread(name="stockPriceChange10", target=stockPriceChange, args=("directionOfMarket10", stockPrice.mmm, "MMM: ", "mmm",), daemon=True)
s12 = threading.Thread(name="stockPriceChange11", target=stockPriceChange, args=("directionOfMarket11", stockPrice.msft, "MSFT: ", "msft",), daemon=True)
s13 = threading.Thread(name="stockPriceChange12", target=stockPriceChange, args=("directionOfMarket12", stockPrice.t, "T: ", "t",), daemon=True)
s14 = threading.Thread(name="stockPriceChange13", target=stockPriceChange, args=("directionOfMarket13", stockPrice.tgt, "TGT: ", "tgt",), daemon=True)
s15 = threading.Thread(name="stockPriceChange14", target=stockPriceChange, args=("directionOfMarket14", stockPrice.txn, "TXN: ", "txn",), daemon=True)
s16 = threading.Thread(name="stockPriceChange15", target=stockPriceChange, args=("directionOfMarket15", stockPrice.wmt, "WMT: ", "wmt",), daemon=True)

i = threading.Thread(name="interest", target=interest, daemon = True)

n.start()
ms.start()

s1.start()
s2.start()
s3.start()
s4.start()
s5.start()
s6.start()
s7.start()
s8.start()
s9.start()
s10.start()
s11.start()
s12.start()
s13.start()
s14.start()
s15.start()
s16.start()

i.start()

n.join()
ms.join()

s1.join()
s2.join()
s3.join()
s4.join()
s5.join()
s6.join()
s7.join()
s8.join()
s9.join()
s10.join()
s11.join()
s12.join()
s13.join()
s14.join()
s15.join()
s16.join()

i.join()

