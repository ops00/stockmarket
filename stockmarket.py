#!/usr/bin/env python3

import random
import sys
import time
import threading
import os

#create user profile, difficauly 

class Player(object):
	def __init__(self, name, money, loan):
		self.name = name
		self.money = money
		self.loan = loan


class Stock(object):
	
	def __init__(self, name, stockprice, currentOwned):
		self.name = name
		self.stockprice = stockprice
		self.currentOwned = currentOwned
		
	def increase(self, amount):
		self.stockprice += amount
	
	def decrease(self, amount):
		self.stockprice -= amount
		
	def dividend(self, name):
		self.dividendPayment = self.stockprice * self.currentOwned / 25 
		name.money += self.dividendPayment
		
	def totalValue(self):
		net = self.stockprice * self.currentOwned
		return net

		 
def newGame():
	print(colors.Br + "Welcome to a the simple " + colors.sGreen + "(c)onsole based " + colors.sRed +
 "(s)tockmarket game\n" + colors.stClr)

	while True:
		playerOption = "d"
		#playerOption = input("d to start program, q to quit: ")
		#this needs to be made correctly.
		if playerOption != "d":
			sys.exit()
		
		else:
			gameLogic()

			
def buyStock():
	stockList = stockPriceList.stockList
	print(colors.sBlue + "options:")
	print(colors.Br + " | ".join(map(str,stockList)) + colors.stClr)
		
	try:
		whatStockToBuy = eval(input("What stock to" + colors.sGreen + " buy?" + colors.stClr + "\n:")) #better way to do than eval?
		if whatStockToBuy.stockprice > 0:
			print("One share of " + colors.Br + whatStockToBuy.name + colors.stClr +
			 " is currently priced at", whatStockToBuy.stockprice, "$")
			
			howManyToBuy = int(input("How many would you want to buy? \n:"))
			totalprice = (howManyToBuy * int(whatStockToBuy.stockprice))
			print("Total price of purchase:" + colors.sRed, totalprice, "$" + colors.stClr)
	
			areYouSure = input("Confirm buy, " + colors.sGreen + "(y)es " + colors.stClr + "or " +
			 colors.sRed + "(n)o" + colors.stClr + "\n:" )
		
			if totalprice > joe.money:
				print(colors.sRed + "You dont have the cash!" + colors.stClr)
				pass
	
			else:	
				if areYouSure == "y":
					joe.money -= totalprice
					print("Bought " + colors.Br + whatStockToBuy.name + colors.stClr + " stock for at total price of" +
					 colors.sRed, totalprice, "$" + colors.stClr)
					whatStockToBuy.currentOwned += howManyToBuy
		
				else:
					pass
		else:
			print(colors.Br + whatStockToBuy.name + colors.stClr + " is currently " + colors.sRed + "negative" +
			 colors.stClr + ", wait until it is positive to buy. Price:", whatStockToBuy.stockprice)
			pass	
			
	except (ValueError, NameError, AttributeError, SyntaxError): #need to actually check for wrong stock name in a correct way.
		print(colors.sRed + "Please put in a valid stock name." + colors.stClr)
		pass

		
def buyStockFast(first, second):
	whatStockToBuy = first
	howManyToBuy = second
		
	try:
		if whatStockToBuy.stockprice > 0:
			totalprice = (howManyToBuy * int(whatStockToBuy.stockprice))

			if totalprice > joe.money:
				print(colors.sRed + "You dont have the cash!" + colors.stClr)
				pass

			else:	
				joe.money -= totalprice
				print("Bought " + colors.Br + whatStockToBuy.name + colors.stClr + " stock for at total price of" +
				 colors.sRed, totalprice, "$" + colors.stClr)
				whatStockToBuy.currentOwned += howManyToBuy
		
		else:
			print(colors.Br + whatStockToBuy.name + colors.stClr + " is currently " + colors.sRed + "negative" +
			 colors.stClr + ", wait until it is positive to buy. Price:", whatStockToBuy.stockprice)
			pass
			
	except ValueError:
		print(colors.sRed + "Please put in valid info" + colors.stClr)	

def sellStock():
	stockList = stockPriceList.stockList
	print(colors.sBlue + "options:")
	print(colors.Br + " | ".join(map(str,stockList)) + colors.stClr)

	try:
		whatStockToSell = eval(input("What stock to" + colors.sRed + " sell?" + colors.stClr + "\n:"))
		howManyDoYouHave = whatStockToSell.currentOwned
		playerChosenStock = whatStockToSell.stockprice
		if playerChosenStock > 20:
			if howManyDoYouHave <= 0:
				print(colors.sRed + "You dont own any shares of " + colors.Br + whatStockToSell.name + colors.stClr)
				pass
			
			else:	
				print("One share of " + colors.Br + whatStockToSell.name +
				 colors.stClr + " is currently priced at: ", playerChosenStock, "$")
				print("You currently have" + colors.Br, howManyDoYouHave, colors.stClr + "shares")
				howManyToSell = int(input("How many shares would you like to sell? \n:")) 
				totalprice = (howManyToSell * int(playerChosenStock))
				print("Total sum of sale: " + colors.sGreen, totalprice, "$" + colors.stClr) 
				
				areYouSure = input("Confirm sale, " + colors.sGreen + "(y)es " + colors.stClr + "or " + colors.sRed +
				 "(n)o" + colors.stClr + "\n:")

				if howManyToSell > howManyDoYouHave:
					print("You don't have that many, you have" + colors.Br, assetsNow, colors.stClr + "shares of " +
					 colors.Br + whatStockToSell.name + colors.stClr)
					pass
	
				else:
					if areYouSure == "y":
						joe.money += totalprice
						print("Sold " + colors.Br + whatStockToSell.name + colors.stClr + " stock for a total price of" +
						 colors.sGreen, totalprice, "$" + colors.stClr)
						whatStockToSell.currentOwned -= howManyToSell
	
					else:
						pass
						
		else:
			print(colors.sRed + "The goverment has put a hold on " + colors.Br + whatStockToSell.name + 
			colors.sRed + " please wait until the stock reaches " + colors.sGreen + "20 $" + 
			colors.sRed + " a share to sell. Price:" + colors.Br, playerChosenStock, colors.stClr + "$")
					
	except (ValueError, NameError, AttributeError, SyntaxError): #need to actually check for wrong stock name in a correct way.
		print(colors.sRed + "Please put in valid info." + colors.stClr)
		pass
		
def sellStockFast(first, second):
	stockList = stockPriceList.stockList
	whatStockToSell = first
	howManyToSell = second
	
	try:
		howManyDoYouHave = whatStockToSell.currentOwned
		playerChosenStock = whatStockToSell.stockprice
		if playerChosenStock > 20:
			if howManyDoYouHave <= 0:
				print(colors.sRed + "You dont own any shares of " + colors.Br + whatStockToSell + colors.stClr)
				pass
				
			else:	
				totalprice = (int(howManyToSell) * int(playerChosenStock))
				if int(howManyToSell) > howManyDoYouHave:
					print("You don't have that many, you have" + colors.Br, assetsNow, colors.stClr + "shares of " +
					 colors.Br + whatStockToSell.name + colors.stClr)
					pass
	
				else:
					joe.money += totalprice
					print("Sold " + colors.Br + whatStockToSell.name + colors.stClr + " stock for a total price of" +
					colors.sGreen, totalprice, "$" + colors.stClr)
					whatStockToSell.currentOwned -= howManyToSell 
			
		else:
			print(colors.sRed + "The goverment has put a hold on " + colors.Br + whatStockToSell.name + 
			colors.sRed + " please wait until the stock reaches " + colors.sGreen + "20 $" + 
			colors.sRed + " a share to sell. Price:" + colors.Br, playerChosenStock, colors.stClr + "$")
				
	except ValueError: #need to actually check for wrong stock name in better way.
		print(colors.sRed + "Please put in valid info." + colors.stClr)
		pass
	
		
def loans():
	networthCalc()
	playerMoney = joe.money
	currentLoan = joe.loan
	net = networthCalc.totalnet
	maximumLoan = (net - currentLoan) 
	
	try:
		playerAnswer = input("Would you like to" + colors.sRed + " (t)ake " + colors.stClr + "a loan or" +
		 colors.sGreen + " (p)ay " + colors.stClr + "back a loan? \n:")	
		if playerAnswer == "t":
			if maximumLoan > 0:
				print("You currently qualify for a loan of: ", maximumLoan, "$")
				howMuchLoanDoesCuWant = int(input("How much would you like to loan? \n:"))
	
				if howMuchLoanDoesCuWant > maximumLoan:
					joe.loan += maximumLoan
					joe.money += maximumLoan
					print(colors.sGreen + "Maximum loan approved." + colors.stClr)
					
				else:
					joe.loan += howMuchLoanDoesCuWant
					joe.money += howMuchLoanDoesCuWant
					print(colors.sGreen + "Loan approved." + colors.stClr)
					
			else:
				print(colors.sRed + "You currently don't qualify for a loan, raise your net worth." + colors.stClr) 
				pass
				
		elif playerAnswer == "p": 
			if currentLoan == 0:
				print(colors.sRed + "You dont have a loan." + colors.stClr)
				
			else:
				print("Your current loan outstanding is" + colors.sRed, currentLoan, "$" + colors.stClr)
				playerChoice = int(input("How much would you like to pay back? \n:"))
				if playerChoice > currentLoan:
					print(colors.sRed + "You dont owe that much money" + colors.stClr) 
					
					if playerChoice < playerMoney: 
						playerChoicePayFullBack = input("Would you like to pay back the full loan? " + colors.sGreen + "(y)es " +
						 colors.stClr + "or " + colors.sRed + "(n)o" + colors.stClr + "\n:")
						 
						if playerChoicePayFullBack == "y":
								joe.money -= currentLoan
								joe.loan = 0
								print(colors.sGreen + "Payment succesful." + colors.stClr)
								
						else:
							pass	
							
					else:
						pass
						
				else:
					joe.money -= playerChoice
					joe.loan -= playerChoice
					print(colors.sGreen + "Payment succesful." + colors.stClr)
					
		else:
			print(colors.sRed + "Check your typing." + colors.stClr)
			pass
	
	except (ValueError):
		print(colors.sRed + "Please put in valid information." + colors.stClr)
	
	
def interest():
	while True:
		currentLoan = joe.loan
		if currentLoan == 0:
			time.sleep(60)
			pass
			
		else:
			interest = (currentLoan / 2000) #needs better calculation, needs to be percentage based and random.
			joe.money -= interest
			joe.loan -= interest
			time.sleep(2)
			pass


def dividends():
	x = joe
	
	while True:
		aapl.dividend(x)
		goog.dividend(x)
		lnx.dividend(x)
		a.dividend(x)
		c.dividend(x)
		hog.dividend(x)
		hpq.dividend(x)
		intc.dividend(x)
		ko.dividend(x)
		luv.dividend(x)
		mmm.dividend(x)
		msft.dividend(x)
		t.dividend(x)
		tgt.dividend(x)
		txn.dividend(x)
		wmt.dividend(x)
		time.sleep(120)
	
		
def showPlayerAssets():
	networthCalc()
	print(colors.Br + " aapl:" + colors.stClr , aapl.currentOwned, "\n",
		colors.Br + "goog:" + colors.stClr , goog.currentOwned, "\n",
		colors.Br + "lnx: " + colors.stClr , lnx.currentOwned, "\n",
		colors.Br + "a:   " + colors.stClr , a.currentOwned, "\n",
		colors.Br + "c:   " + colors.stClr , c.currentOwned, "\n",
		colors.Br + "hog: " + colors.stClr , hog.currentOwned, "\n",
		colors.Br + "hpq: " + colors.stClr , hpq.currentOwned, "\n",
		colors.Br + "intc:" + colors.stClr , intc.currentOwned, "\n",
		colors.Br + "ko:  " + colors.stClr , ko.currentOwned, "\n",
		colors.Br + "luv: " + colors.stClr , luv.currentOwned, "\n",
		colors.Br + "mmm: " + colors.stClr , mmm.currentOwned, "\n",
		colors.Br + "msft:" + colors.stClr , msft.currentOwned, "\n",
		colors.Br + "t:   " + colors.stClr , t.currentOwned, "\n",
		colors.Br + "tgt: " + colors.stClr , tgt.currentOwned, "\n",
		colors.Br + "txn: " + colors.stClr , txn.currentOwned, "\n",
		colors.Br + "wmt: " + colors.stClr , wmt.currentOwned, "\n","\n",
		colors.sGreen + "cash:" + colors.stClr , joe.money, "$", "\n",
		colors.sYellow + "loan:" + colors.stClr , joe.loan, "$", "\n",
		colors.sMagenta + "Total networth:" + colors.stClr, networthCalc.totalnet , "$", "\n",
		colors.sCyan + "All assets" + colors.stClr, networthCalc.total , "$", "\n",) 
		
		#color change based on performance x ammount of time, only show stock owned
		
		
def showMarket():
	showMarket.index = (aapl.stockprice + goog.stockprice + lnx.stockprice + a.stockprice +
	c.stockprice + hog.stockprice + hpq.stockprice + intc.stockprice + ko.stockprice + luv.stockprice +
	mmm.stockprice + msft.stockprice + t.stockprice + tgt.stockprice + txn.stockprice + wmt.stockprice)
	
	print(colors.Br + " aapl:" + colors.stClr , aapl.stockprice, "$", "\n",
		colors.Br + "goog:" + colors.stClr , goog.stockprice, "$", "\n",
		colors.Br + "lnx: " + colors.stClr , lnx.stockprice, "$", "\n",
		colors.Br + "a:   " + colors.stClr , a.stockprice, "$", "\n",
		colors.Br + "c:   " + colors.stClr , c.stockprice, "$", "\n",
		colors.Br + "hog: " + colors.stClr , hog.stockprice, "$", "\n",
		colors.Br + "hpq: " + colors.stClr , hpq.stockprice, "$", "\n",
		colors.Br + "intc:" + colors.stClr , intc.stockprice, "$", "\n",
		colors.Br + "ko:  " + colors.stClr , ko.stockprice, "$", "\n",
		colors.Br + "luv: " + colors.stClr , luv.stockprice, "$", "\n",
		colors.Br + "mmm: " + colors.stClr , mmm.stockprice, "$", "\n",
		colors.Br + "msft:" + colors.stClr , msft.stockprice, "$", "\n",
		colors.Br + "t:   " + colors.stClr , t.stockprice, "$", "\n",
		colors.Br + "tgt: " + colors.stClr , tgt.stockprice, "$", "\n",
		colors.Br + "txn: " + colors.stClr , txn.stockprice, "$", "\n",
		colors.Br + "wmt: " + colors.stClr , wmt.stockprice, "$","\n""\n",
		colors.sCyan + "market index:" + colors.stClr, showMarket.index, "\n")
	
		#color change in share price based on up/down in x ammount of time,
		# also percentage change in x ammount of time
		

def networthCalc():
	x = joe
	
	s1 = aapl.totalValue()
	s2 = goog.totalValue()
	s3 = lnx.totalValue()
	s4 = a.totalValue()
	s5 = c.totalValue()
	s6 = hog.totalValue()
	s7 = hpq.totalValue()
	s8 = intc.totalValue()
	s9 = ko.totalValue()
	s10 = luv.totalValue()
	s11 = mmm.totalValue()
	s12 = msft.totalValue()
	s13 = t.totalValue()
	s14 = tgt.totalValue()
	s15 = txn.totalValue()
	s16 = wmt.totalValue()
	
	networthCalc.totalnet = (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 
	+ s10 + s11 + s12 + s13 + s14 + s15 + s16 + x.money - x.loan)
	
	networthCalc.total = networthCalc.totalnet + x.loan
	
	
def stockPriceList():	
	stockPriceList.stockList = ["aapl", "goog", "lnx", "a", "c", "hog", "hpq",
	 "intc", "ko", "luv", "mmm", "msft", "t", "tgt", "txn", "wmt"]


def marketSwing():
	#fix this mess
	marketSwing.directionOfMarket = random.randint(1,6)
	marketSwing.directionOfMarket1 = random.randint(1,6)
	marketSwing.directionOfMarket2 = random.randint(1,6)
	marketSwing.directionOfMarket3 = random.randint(1,6)
	marketSwing.directionOfMarket4 = random.randint(1,6)
	marketSwing.directionOfMarket5 = random.randint(1,6)
	marketSwing.directionOfMarket6 = random.randint(1,6)
	marketSwing.directionOfMarket7 = random.randint(1,6)
	marketSwing.directionOfMarket8 = random.randint(1,6)
	marketSwing.directionOfMarket9 = random.randint(1,6)
	marketSwing.directionOfMarket10 = random.randint(1,6)
	marketSwing.directionOfMarket11 = random.randint(1,6)
	marketSwing.directionOfMarket12 = random.randint(1,6)
	marketSwing.directionOfMarket13 = random.randint(1,6)
	marketSwing.directionOfMarket14 = random.randint(1,6)
	marketSwing.directionOfMarket15 = random.randint(1,6)
		
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
	
def stockPriceChange(first, second):
	#and this mess
	direction = first
	stock = second
	timeToChange = 1
		
	while True:
		directionOfMarkets = getattr(marketSwing, direction)
		time.sleep(timeToChange)
		if directionOfMarkets == 1:
			timeToChange = random.randint(1,10)
			randomnumber = random.randint(1,5)
			stock.increase(randomnumber)
		elif directionOfMarkets == 2:
			timeToChange = random.randint(1,3)
			randomnumber = random.randint(1,7)
			stock.increase(randomnumber)
		elif directionOfMarkets == 3:
			timeToChange = random.randint(1,2)
			randomnumber = random.randint(1,10)
			stock.increase(randomnumber)
		elif directionOfMarkets == 4:
			timeToChange = random.randint(1,10)
			randomnumber = random.randint(1,2)
			stock.decrease(randomnumber)
		elif directionOfMarkets == 5:
			timeToChange = random.randint(1,3)
			randomnumber = random.randint(1,5)
			stock.decrease(randomnumber)
		else:
			timoToChange = random.randint(1,2)
			randomnumber = random.randint(1,7)
			stock.decrease(randomnumber)

def randomEvents():
	while True:
		time.sleep(30)
		stocklist = [aapl, goog, lnx, a, c, hog, hpq, intc, ko, luv, mmm, msft, t, tgt, txn, wmt]
		
		rs = random.randint(0,6)
				
		event = random.randint(1,8)
		poslist = ["releases a new product, its a hit", "profit statement over expections",
		 "product well received", "stock is on fire", "frenzy",
		  "CEO: 'The future looks bright for us'",
		   "CEO: 'Our profits are higher than ever before'"]
		   
		neglist = ["product complere failure", "stock plumets",
		 "ceo fired", "stock in downward spiral",
		  "customer information has been hacked, stock price down",
		   "profit statement a dissapointment", "product has critical design flaw"]
		   
		if event == 1:
			stocklist[rs].stockprice += 100
			rpp = random.randint(0,6)
			print(colors.sYellow + "//NEWS: " + colors.sGreen + stocklist[rs].name + " " + poslist[rpp] + colors.stClr)
			
		elif event == 2:
			stocklist[rs].stockprice += 200
			rpp = random.randint(0,6)
			print(colors.sYellow + "//NEWS: " + colors.sGreen + stocklist[rs].name + " " + poslist[rpp] + colors.stClr)
			
		elif event == 3:
			stocklist[rs].stockprice -= 100
			rpp = random.randint(0,6)
			print(colors.sYellow + "//NEWS: " + colors.sRed + stocklist[rs].name + " " + neglist[rpp] + colors.stClr)
		
		elif event == 4:
			stocklist[rs].stockprice -= 200
			rpp = random.randint(0,6)
			print(colors.sYellow + "//NEWS: " + colors.sRed + stocklist[rs].name + " " + neglist[rpp] + colors.stClr)
			
		else:
			pass
	


def helper():
	print("You move around the game by typing the letter in lowercase that \
is inside a parenthesis.\n \nAs an example: '(b)uy' type b to get to the buy page. \
\n \nWhen buying and selling stock, use lowercase and the stock names shown on\
the buy/sell \nscreen.\n \nExample: To buy Apple stock just type aapl in the buy screen.\n \n\
Some time after you have taken a loan you will automaticaly start paying it back.\
\nYou also pay interest 0,2% , this happens every 2 seconds.\nEvery 120 seconds companies pay dividends 3-5%.\n \n\
There are also some commands to make the gameplay faster. \nYou can see them by typing (cmd) command\
\n \nThe game is based fully in python.\
\n \n// version 0.1.2 //  \n \n \n \n ")

def helperCmd():
	print("You can type fast commands, try (bb) for fast buy and (ss) for fast sale. \nAfter you type bb a prompt opens up : \
\ntype stock name and number of shares to buy.\n \nExample :aapl 10 to buy 10 shares of Apple. The sale happens the same way. \n \nBe careful, there is no confirmation. \n")


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
	playerChoice = input(colors.sGreen + "(b)uy stock, " + colors.sRed + "(s)ell stock, " + colors.sBlue 
	+ "show (a)ssets, " + colors.sMagenta + "show (m)arket, " + colors.sYellow + "(l)oans, " + colors.sCyan +
	"(h)elp " + colors.stClr + "or (q)uit\n: ")
	
		
	if playerChoice == "b":
		buyStock()
		print("Your current money:"+ colors.sGreen , joe.money, "$" + colors.stClr)
	elif playerChoice == "bb":
		try:
			playerChosenS, playerChosenA = input("\n:").split()
			buyStockFast(eval(playerChosenS), eval(playerChosenA))
		except (ValueError, NameError, SyntaxError, AttributeError): #needs a better way
			print("type cmd if you need help with fast command options")
			#buy maximum shares as fast option?
	elif playerChoice == "s":
		sellStock()
		print("Your current money:" + colors.sGreen , joe.money, "$" + colors.stClr)
	elif playerChoice == "ss":
		try:
			playerChosenS, playerChosenA = input("\n:").split()
			sellStockFast(eval(playerChosenS), eval(playerChosenA))
		except (ValueError, NameError, SyntaxError, AttributeError): #needs a better way
			print("type cmd if you need help with fast command options")
			#sell all shares you own as another fast option?
	elif playerChoice == "a":
		showPlayerAssets()
	elif playerChoice == "m":
		showMarket()
	elif playerChoice == "l":
		loans()
		#create maximum loan fast option/command
		#create pay back maximum loan fast option
	elif playerChoice == "h":
		helper()
	elif playerChoice == "cmd":
		helperCmd()
	elif playerChoice == "q":
		os._exit(0)
	else:
		print("Please chose a valid option, type h for help.")

colors()
stockPriceList()

#make stuff

joe = Player("Joe", 10000, 0)
aapl = Stock("aapl", 200, 0)
goog = Stock("goog", 200, 0)
lnx = Stock("lnx", 200, 0)
a = Stock("a", 200, 0)
c = Stock("c", 200, 0)
hog = Stock("hog", 200, 0)
hpq = Stock("hpq", 200, 0)
intc = Stock("intc", 200, 0)
ko = Stock("ko", 200, 0)
luv = Stock("luv", 200, 0)
mmm = Stock("mmm", 200, 0)
msft = Stock("msft", 200, 0)
t = Stock("t", 200, 0)
tgt = Stock("tgt", 200, 0)
txn = Stock("txn", 200, 0)
wmt = Stock("wmt", 200, 0)



#threads
n = threading.Thread(name="game", target=newGame, daemon=True)
ms = threading.Thread(name="marketswing", target=marketSwing, daemon=True)
div = threading.Thread(name="dividends", target=dividends, daemon=True)
re = threading.Thread(name="randomevent", target=randomEvents, daemon=True)

s1 = threading.Thread(name="stockPriceChange", target=stockPriceChange, args=("directionOfMarket", aapl,), daemon=True)
s2 = threading.Thread(name="stockPriceChange1", target=stockPriceChange, args=("directionOfMarket1", goog,), daemon=True)
s3 = threading.Thread(name="stockPriceChange2", target=stockPriceChange, args=("directionOfMarket2", lnx,), daemon=True)
s4 = threading.Thread(name="stockPriceChange3", target=stockPriceChange, args=("directionOfMarket3", a,), daemon=True)
s5 = threading.Thread(name="stockPriceChange4", target=stockPriceChange, args=("directionOfMarket4", c,), daemon=True)
s6 = threading.Thread(name="stockPriceChange5", target=stockPriceChange, args=("directionOfMarket5", hog,), daemon=True)
s7 = threading.Thread(name="stockPriceChange6", target=stockPriceChange, args=("directionOfMarket6", hpq,), daemon=True)
s8 = threading.Thread(name="stockPriceChange7", target=stockPriceChange, args=("directionOfMarket7", intc,), daemon=True)
s9 = threading.Thread(name="stockPriceChange8", target=stockPriceChange, args=("directionOfMarket8", ko,), daemon=True)
s10 = threading.Thread(name="stockPriceChange9", target=stockPriceChange, args=("directionOfMarket9", luv,), daemon=True)
s11 = threading.Thread(name="stockPriceChange10", target=stockPriceChange, args=("directionOfMarket10", mmm,), daemon=True)
s12 = threading.Thread(name="stockPriceChange11", target=stockPriceChange, args=("directionOfMarket11", msft,), daemon=True)
s13 = threading.Thread(name="stockPriceChange12", target=stockPriceChange, args=("directionOfMarket12", t,), daemon=True)
s14 = threading.Thread(name="stockPriceChange13", target=stockPriceChange, args=("directionOfMarket13", tgt,), daemon=True)
s15 = threading.Thread(name="stockPriceChange14", target=stockPriceChange, args=("directionOfMarket14", txn,), daemon=True)
s16 = threading.Thread(name="stockPriceChange15", target=stockPriceChange, args=("directionOfMarket15", wmt,), daemon=True)

i = threading.Thread(name="interest", target=interest, daemon = True)

n.start()
ms.start()
div.start()
re.start()

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
div.join()
re.join()

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
