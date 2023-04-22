#Mazen Baioumy Assignment 1
#importing
from random import random
from random import *
#Input sentence so user would enter distance between lines
gridlines = int(input("Please enter the distance between lines(mm):"))
#while loop to keep user from entering wrong info
while gridlines <= 0:
    print("Wrong Value Entered please try again")
    gridlines=int(input("Please enter the distance again:"))
else:
    print("Please continue:")
#input sentence for entering reward
thereward = int(input("Please enter the \"reward\" if the customer wins($):"))
#While loop to check for correct input for reward incase wrong input is entered
while thereward <=0:
    print ("Error Occurred, Please enter a correct value greater than 0")
    thereward = int(input("Please enter the reward again:"))
else:
    print("Here is the probability:")
#Creating probability depending on grid size and distance between lines and where coin might drop
theprobability = round((((gridlines - 2)-28)**2 / (((gridlines - 2)-28)**2 + (gridlines**2 - (gridlines - 28)**2))) * 100)
#setting up counts
wincount = 0
losecount = 0
#count loop
for i in range(1000):
    m = randint(0,100)
    if m <= theprobability:
        wincount = wincount + 1
    else:
        losecount = losecount + 1
#actual = round(wincount / (wincount + losecount) * 100)
#Chance that you earn money based on reward and the probability of not landing on a line
#breakeven
breakeven =round((thereward/2)*((((gridlines - 2)-28)**2 / (((gridlines - 2)-28)**2 + (gridlines**2 - (gridlines - 28)**2))) * 100))
#profit calculation multiply reward with wincount probability and subtract the lose count
profit = (thereward*wincount) - 2*losecount
#if statement incase profit is greater than 0 so winning or less than 0 so losing
if profit >= 0:
    print("For 1000 tosses, you have probability of {}% of winning, and the profit probability of {}%.You won ${}.00!".format(theprobability,breakeven,profit))
else:
    print("For 1000 tosses, you have probability of {}% of winning, and the profit probability of {}%.You lost ${}.00".format(theprobability,breakeven,profit))
#Print sentences connected with probability of lose or win depending on distance and reward
