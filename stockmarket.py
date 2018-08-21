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
		#this needs to be made correctly.
		if playerOption != "d":
			sys.exit()
		else:
			
			gameLogic()
			
 


def playerStatus():
	playerStatus.playerMoney = 10000
	playerStatus.playerLoan = 0
	

def buyStock():
	stockList = stockPrice.stockList
	print(colors.sBlue + "options:")
	print(colors.Br + " | ".join(map(str,stockList)) + colors.stClr)
	whatStockToBuy = input("What stock to" + colors.sGreen + " buy?" + colors.stClr + "\n:")
	
	
	if whatStockToBuy in stockList:
		
		try:
			playerChosenStock = getattr(stockPrice, whatStockToBuy)
			if playerChosenStock > 0:
				print("One share of " + colors.Br + whatStockToBuy + colors.stClr + " is currently priced at", playerChosenStock, "$")
		
		
				howManyToBuy = int(input("How many would you want to buy? \n:"))
				totalprice = (howManyToBuy * int(playerChosenStock))
				assetsNow = getattr(showAssets, whatStockToBuy)
				print("Total price of purchase:" + colors.sRed, totalprice, "$" + colors.stClr)
	
				areYouSure = input("Confirm buy, " + colors.sGreen + "(y)es " + colors.stClr + "or " + colors.sRed + "(n)o" + colors.stClr + "\n:" )
		
				if totalprice > playerStatus.playerMoney:
					print(colors.sRed + "You dont have the cash!" + colors.stClr)
					pass
	
				else:	
					if areYouSure == "y":
						playerStatus.playerMoney -= totalprice
						print("Bought " + colors.Br + whatStockToBuy + colors.stClr + " stock for at total price of" + colors.sRed, totalprice, "$" + colors.stClr)
						assetsNew = (assetsNow + int(howManyToBuy))
						setattr(showAssets, whatStockToBuy, assetsNew) 
		
					else:
						pass
			else:
				print(colors.Br + whatStockToBuy + colors.stClr + " is currently " + colors.sRed + "negative" + colors.stClr + ", wait until it is positive to buy. Price:", playerChosenStock)
				pass
		except ValueError:
			pass
		
		

	else:
		print(colors.sRed + "Please put in a valid stock name." + colors.stClr)
	
def sellStock():
	stockList = stockPrice.stockList
	print(colors.sBlue + "options:")
	print(colors.Br + " | ".join(map(str,stockList)) + colors.stClr)
	whatStockToSell = input("What stock to" + colors.sRed + " sell?" + colors.stClr + "\n:")
	stockList = stockPrice.stockList
	
	
	if whatStockToSell in stockList:
		try:
			howManyDoYouHave = getattr(showAssets, whatStockToSell)
			playerChosenStock = getattr(stockPrice, whatStockToSell)
			if playerChosenStock > 20:
				if howManyDoYouHave <= 0:
					print(colors.sRed + "You dont own any shares of " + colors.Br + whatStockToSell + colors.stClr)
					pass
				else:	
					print("One share of " + colors.Br + whatStockToSell + colors.stClr + " is currently priced at: ", playerChosenStock, "$")
					print("You currently have" + colors.Br, howManyDoYouHave, colors.stClr + "shares")
					howManyToSell = int(input("How many shares would you like to sell? \n:")) 
					totalprice = (howManyToSell * int(playerChosenStock))
					assetsNow = getattr(showAssets, whatStockToSell)
					print("Total sum of sale: " + colors.sGreen, totalprice, "$" + colors.stClr) 
	
					areYouSure = input("Confirm sale, " + colors.sGreen + "(y)es " + colors.stClr + "or " + colors.sRed + "(n)o" + colors.stClr + "\n:")
	
					if howManyToSell > assetsNow:
						print("You don't have that many, you have" + colors.Br, assetsNow, colors.stClr + "shares of " + colors.Br + whatStockToSell + colors.stClr)
						pass
	
					else:
						if areYouSure == "y":
							playerStatus.playerMoney += totalprice
							print("Sold " + colors.Br + whatStockToSell + colors.stClr + " stock for a total price of" + colors.sGreen, totalprice, "$" + colors.stClr)
							assetsNew = (assetsNow - int(howManyToSell))
							setattr(showAssets, whatStockToSell, assetsNew)
		
						else:
							pass
			else:
				print(colors.sRed + "The goverment has put a hold on " + colors.Br + whatStockToSell + 
				colors.sRed + " please wait until the stock reaches " + colors.sGreen + "20 $" + 
				colors.sRed + " a share to sell. Price:" + colors.Br, playerChosenStock, colors.stClr + "$")
				
		except ValueError:
			print(colors.sRed + "Please put in a number." + colors.stClr)
			pass
	else:
		print(colors.sRed + "Please put in a valid stock name." + colors.stClr)
		pass
			
def loans():
	networthCalc()
	playerMoney1 = playerStatus.playerMoney
	currentLoan = playerStatus.playerLoan
	maximumLoan = ((networthCalc.totalnet * 2) - currentLoan * 2)
	
	try:
		playerAnswer = input("Would you like to" + colors.sRed + " (t)ake " + colors.stClr + "a loan or" + colors.sGreen + " (p)ay " + colors.stClr + "back a loan? \n:")	
		if playerAnswer == "t":
			if maximumLoan > 0:
				print("You currently qualify for a loan of: ", maximumLoan, "$")
				howMuchLoanDoesCuWant = int(input("How much would you like to loan? \n:"))
	
		
				if howMuchLoanDoesCuWant > maximumLoan:
					newLoan3 = int(currentLoan + maximumLoan)
					newCash3 = int(playerMoney1 + maximumLoan)
					setattr(playerStatus, "playerLoan", newLoan3)
					setattr(playerStatus, "playerMoney", newCash3)
					print(colors.sGreen + "Maximum loan approved." + colors.stClr)
				else:
					newLoan = int(currentLoan + howMuchLoanDoesCuWant)
					newCash = int(playerMoney1 + howMuchLoanDoesCuWant)
					setattr(playerStatus, "playerLoan", newLoan)
					setattr(playerStatus, "playerMoney", newCash)
					print(colors.sGreen + "Loan approved." + colors.stClr)
			else:
				print(colors.sRed + "You currently don't qualify for a loan, raise your net worth." + colors.stClr) #need to calculate networth in showPlayerAssets.
				pass
		elif playerAnswer == "p": 
			if currentLoan == 0:
				print(colors.sRed + "You dont have a loan." + colors.stClr)
			else:
				print("Your current loan outstanding is" + colors.sRed, currentLoan, "$" + colors.stClr)
				playerChoice = int(input("How much would you like to pay back? \n:"))
				if playerChoice > currentLoan:
					print(colors.sRed + "You dont owe that much money" + colors.stClr) 
					if playerChoice < playerMoney1: 
						playerChoice2 = input("Would you like to pay back the full loan? " + colors.sGreen + "(y)es " + colors.stClr + "or " + colors.sRed + "(n)o" + colors.stClr + "\n:")
						if playerChoice2 == "y":
								newLoan2 = 0
								newCash2 = int(playerMoney1 - currentLoan)
								setattr(playerStatus, "playerLoan", newLoan2)
								setattr(playerStatus, "playerMoney", newCash2)
								print(colors.sGreen + "Payment succesful." + colors.stClr)
						else:
							pass	
					else:
						pass
				else:
					newLoan1 = int(currentLoan - playerChoice)
					newCash1 = int(playerMoney1 - playerChoice)
					setattr(playerStatus, "playerLoan", newLoan1)
					setattr(playerStatus, "playerMoney", newCash1)
					print(colors.sGreen + "Payment succesful." + colors.stClr)
		else:
			print(colors.sRed + "Check your typing." + colors.stClr)
			pass
	
	except (ValueError):
		print(colors.sRed + "Please put in valid information." + colors.stClr)
	
	
def interest():
	
	while True:
		currentLoan = playerStatus.playerLoan 
		playerMoney1 = playerStatus.playerMoney
		
		if currentLoan == 0:
			time.sleep(60)
			pass
		else:
			interest = (currentLoan / 2000) #needs better calculation, needs to be percentage based and random.
			newCash = int(playerMoney1 - interest)
			newLoan = int(currentLoan - interest)
			setattr(playerStatus, "playerMoney", newCash)
			setattr(playerStatus, "playerLoan" , newLoan)
			time.sleep(2)
			pass


def dividends():
	print("Nothing here yet")
		


def news():
	print("Nothing here yet")
		
def showPlayerAssets():
	networthCalc()
	print(colors.Br + " aapl:" + colors.stClr , showAssets.aapl, "\n",
		colors.Br + "goog:" + colors.stClr , showAssets.goog, "\n",
		colors.Br + "lnx: " + colors.stClr , showAssets.lnx, "\n",
		colors.Br + "a:   " + colors.stClr , showAssets.a, "\n",
		colors.Br + "c:   " + colors.stClr , showAssets.c, "\n",
		colors.Br + "hog: " + colors.stClr , showAssets.hog, "\n",
		colors.Br + "hpq: " + colors.stClr , showAssets.hpq, "\n",
		colors.Br + "intc:" + colors.stClr , showAssets.intc, "\n",
		colors.Br + "ko:  " + colors.stClr , showAssets.ko, "\n",
		colors.Br + "luv: " + colors.stClr , showAssets.luv, "\n",
		colors.Br + "mmm: " + colors.stClr , showAssets.mmm, "\n",
		colors.Br + "msft:" + colors.stClr , showAssets.msft, "\n",
		colors.Br + "t:   " + colors.stClr , showAssets.t, "\n",
		colors.Br + "tgt: " + colors.stClr , showAssets.tgt, "\n",
		colors.Br + "txn: " + colors.stClr , showAssets.txn, "\n",
		colors.Br + "wmt: " + colors.stClr , showAssets.wmt, "\n","\n", 
		colors.sGreen + "cash:" + colors.stClr , playerStatus.playerMoney, "$", "\n",
		colors.sYellow + "loan:" + colors.stClr , playerStatus.playerLoan, "$", "\n",
		colors.sMagenta + "Total networth:" + colors.stClr , networthCalc.totalnet, "$", "\n",
		colors.sCyan + "All assets" + colors.stClr , networthCalc.totalincc, "$", "\n",) 
		
	
		#color change based on performance x ammount of time
		#only show stock owned
		
def showMarket():
	print(colors.Br + " aapl:" + colors.stClr , stockPrice.aapl, "$", "\n",
		colors.Br + "goog:" + colors.stClr , stockPrice.goog, "$", "\n",
		colors.Br + "lnx: " + colors.stClr , stockPrice.lnx, "$", "\n",
		colors.Br + "a:   " + colors.stClr , stockPrice.a, "$", "\n",
		colors.Br + "c:   " + colors.stClr , stockPrice.c, "$", "\n",
		colors.Br + "hog: " + colors.stClr , stockPrice.hog, "$", "\n",
		colors.Br + "hpq: " + colors.stClr , stockPrice.hpq, "$", "\n",
		colors.Br + "intc:" + colors.stClr , stockPrice.intc, "$", "\n",
		colors.Br + "ko:  " + colors.stClr , stockPrice.ko, "$", "\n",
		colors.Br + "luv: " + colors.stClr , stockPrice.luv, "$", "\n",
		colors.Br + "mmm: " + colors.stClr , stockPrice.mmm, "$", "\n",
		colors.Br + "msft:" + colors.stClr ,stockPrice.msft, "$", "\n",
		colors.Br + "t:   " + colors.stClr , stockPrice.t, "$", "\n",
		colors.Br + "tgt: " + colors.stClr , stockPrice.tgt, "$", "\n",
		colors.Br + "txn: " + colors.stClr , stockPrice.txn, "$", "\n",
		colors.Br + "wmt: " + colors.stClr , stockPrice.wmt, "$", "\n")
	
		#color change in share price based on up/down in x ammount of time, also percentage change in x ammount of time

def networthCalc():
	networthCalc.aapl = getattr(stockPrice, "aapl") * getattr(showAssets, "aapl")
	networthCalc.goog = getattr(stockPrice, "goog") * getattr(showAssets, "goog")
	networthCalc.lnx = getattr(stockPrice, "lnx") * getattr(showAssets, "lnx")
	networthCalc.a = getattr(stockPrice, "a") * getattr(showAssets, "a")
	networthCalc.c = getattr(stockPrice, "c") * getattr(showAssets, "c")
	networthCalc.hog = getattr(stockPrice, "hog") * getattr(showAssets, "hog")
	networthCalc.hpq = getattr(stockPrice, "hpq") * getattr(showAssets, "hpq")
	networthCalc.intc = getattr(stockPrice, "intc") * getattr(showAssets, "intc")
	networthCalc.ko = getattr(stockPrice, "ko") * getattr(showAssets, "ko")
	networthCalc.luv = getattr(stockPrice, "luv") * getattr(showAssets, "luv")
	networthCalc.mmm = getattr(stockPrice, "mmm") * getattr(showAssets, "mmm")
	networthCalc.msft = getattr(stockPrice, "msft") * getattr(showAssets, "msft")
	networthCalc.t = getattr(stockPrice, "t") * getattr(showAssets, "t")
	networthCalc.tgt = getattr(stockPrice, "tgt") * getattr(showAssets, "tgt")
	networthCalc.txn = getattr(stockPrice, "txn") * getattr(showAssets, "txn")
	networthCalc.wmt = getattr(stockPrice, "wmt") * getattr(showAssets, "wmt")
	networthCalc.cash = getattr(playerStatus, "playerMoney")
	networthCalc.credit = getattr(playerStatus, "playerLoan")
	
	networthCalc.totalnet = (networthCalc.aapl + networthCalc.goog + networthCalc.lnx + networthCalc.a +
	networthCalc.c + networthCalc.hog + networthCalc.hpq + networthCalc.intc + networthCalc.ko + networthCalc.luv +
	networthCalc.mmm + networthCalc.msft + networthCalc.t + networthCalc.tgt + networthCalc.txn +	
	networthCalc.wmt + networthCalc.cash - networthCalc.credit)
		
	networthCalc.totalincc = (networthCalc.aapl + networthCalc.goog + networthCalc.lnx + networthCalc.a +
	networthCalc.c + networthCalc.hog + networthCalc.hpq + networthCalc.intc + networthCalc.ko + networthCalc.luv +
	networthCalc.mmm + networthCalc.msft + networthCalc.t + networthCalc.tgt + networthCalc.txn +	
	networthCalc.wmt + networthCalc.cash)
	

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
			
			time.sleep(timeToChange)
				
			if randomChoice == 1:
				marketSwing.directionOfMarket = random.randint(1,6)	
			elif randomChoice == 2:
				marketSwing.directionOfMarket1 = random.randint(1,6)
			elif randomChoice == 3:
				marketSwing.directionOfMarket2 = random.randint(1,6)
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
	print("You move around the game by typing the letter in lowercase that is inside a parenthesis.\n \nAs an example: '(b)uy' type b to get to the buy page. \
	\n \nWhen buying and selling stock, use lowercase and the stock names shown on the buy/sell \nscreen.\n \nExample: To buy Apple stock just type aapl in the buy screen.\n \n\
Some time after you have taken a loan you will automaticaly start paying it back. \nYou also pay interest 0,2% , this happens every 2 seconds. \n \nThe game is based fully in python. \n \n// version 0.1.1 //  \n \n \n \n ")

def colors():
	colors.sGreen = "\033[1;32;40m"
	colors.sRed = "\033[1;31;40m"
	colors.sYellow = "\033[1;33;40m"
	colors.sBlue = "\033[1;34;40m"
	colors.sMagenta = "\033[1;35;40m"
	colors.sCyan = "\033[1;36;40m"
	colors.Br = "\033[1;37;40m"
	colors.stClr = "\033[0;0m"		
			
	
def gameLogic():
	
	playerChoice = input(colors.sGreen + "(b)uy stock, " + colors.sRed + "(s)ell stock, " + colors.sBlue + "show (a)ssets, " + colors.sMagenta + "show (m)arket, " + colors.sYellow + "(l)oans, " + colors.sCyan +  "(h)elp " + colors.stClr + "or (q)uit\n: ")
		
	if playerChoice == "b":
		buyStock()
		print("Your current money: "+ colors.sGreen ,playerStatus.playerMoney, "$" + colors.stClr)
	elif playerChoice == "s":
		sellStock()
		print("Your current money: " + colors.sGreen ,playerStatus.playerMoney, "$" + colors.stClr)
	elif playerChoice == "a":
		showPlayerAssets()
	elif playerChoice == "m":
		showMarket()
	elif playerChoice == "l":
		loans()
	elif playerChoice == "h":
		helper()
	elif playerChoice == "q":
		os._exit(0)
	else:
		print("Please chose a valid option, type h for help.")




colors()
print(colors.Br + "Welcome to a the simple " + colors.sGreen + "(c)onsole based " + colors.sRed + "(s)tockmarket game\n" + colors.stClr)
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

