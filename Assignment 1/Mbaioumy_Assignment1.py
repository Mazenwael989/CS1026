customerName = input("Please Enter Your Name:")
#Input to allow customer to enter his name
beverageType = input("Please Enter The Desired Beverage:")
#customer entering the desried beverage using input
beverageSize = input("Please Enter Beverage size:")
#customer entering size of his specified beverage
Tax = 1.11
#Tax is 1.11 set it to that value

#using if statmenet to allow customer to pick between different selections
if beverageType== "coffee" or beverageType== "c":
#set beverage size with pride then allowing customer to pick addon
    if beverageSize== "large" or beverageSize=="l":
        costOfSize= 3.25
        coffeeAddon = input("Do you want a vanilla, chocolate, or maple, or none:")
#provided price of size of beverage with input allowing user to pick his favorite addon
        if coffeeAddon == "vanilla" or coffeeAddon== "v":
            costOfAddon= 0.25
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a large coffee, with some vanilla flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))
#simple math of addition and multiplication to calculate the cost(occurs for all of them) then a print sentence providing customer name.
#including his favourite flavour and cost rounded to two for cents.
        elif coffeeAddon == "maple" or coffeeAddon== "m":
            costOfAddon = 0.50
            costOfBeverage = (costOfSize + costOfAddon) * Tax
            print("For Mr.{}, a large coffee, with some maple flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))
#These statments allow customer to pick whatever he wants with new info supplied
            
        elif coffeeAddon == "chocolate" or coffeeAddon== "c":
            costOfAddon=0.75
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a large coffee, with chocolate flavour, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif coffeeAddon == "none" or coffeeAddon == "n":
            costOfAddon= 0
            costOfBeverage = (costOfSize)*Tax
            print("For Mr.{}, a large coffee, with no flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        else:
            print("Invalid addon entered please change your information")

    elif beverageSize == "small" or beverageSize== "s":
        costOfSize = 1.50
        coffeeAddon = input("Do you want a vanilla, chocolate, or maple:")

        if coffeeAddon == "vanilla" or coffeeAddon== "v":
            costOfAddon= 0.25
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a small coffee, with some vanilla flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif coffeeAddon == "maple" or coffeeAddon== "m":
            costOfAddon = 0.50
            costOfBeverage = (costOfSize + costOfAddon) * Tax
            print("For Mr.{}, a small coffee, with some maple flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif coffeeAddon == "chocolate" or coffeeAddon== "c":
            costOfAddon=0.75
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a small coffee, with chocolate flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif coffeeAddon== "none" or coffeeAddon== "n":
            costOfAddon= 0
            costOfBeverage = (costOfSize) * Tax
            print("For Mr.{}, a small coffee, with no flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        else:
            print("Invalid addon entered please change your information")

    elif beverageSize == "medium" or "m":
        costOfSize = 2.50
        coffeeAddon = input("Do you want a vanilla, chocolate, or maple:")

        if coffeeAddon == "vanilla" or coffeeAddon== "v":
            costOfAddon= 0.25
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a medium coffee, with some vanilla flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif coffeeAddon == "maple" or coffeeAddon== "m":
            costOfAddon = 0.50
            costOfBeverage = (costOfSize + costOfAddon) * Tax
            print("For Mr.{}, a medium coffee, with some maple flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif coffeeAddon == "chocolate" or coffeeAddon== "c":
            costOfAddon=0.75
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a medium coffee, with chocolate flavour, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif coffeeAddon== "none" or coffeeAddon== "n":
            costOfAddon= 0
            costOfBeverage = (costOfSize) * Tax
            print("For Mr.{}, a medium coffee, no flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        else:
            print("Invalid addon entered please change your information")
# new if statment incase user decides to pick tea instead of coffee

if beverageType== "tea" or beverageType== "t":
#
    if beverageSize== "large" or beverageSize=="l":
        costOfSize= 3.25
        TeaAddon = input("Do you want a lemon, mint,or none:")

        if TeaAddon == "lemon" or TeaAddon== "l":
            costOfAddon= 0.25
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a large tea, with some lemon flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif TeaAddon == "mint" or TeaAddon== "mi":
            costOfAddon = 0.50
            costOfBeverage = (costOfSize + costOfAddon) * Tax
            print("For Mr.{}, a large tea, with some mint flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif TeaAddon == "none" or TeaAddon == "n":
            costOfAddon= 0
            costOfBeverage = (costOfSize)*Tax
            print("For Mr.{}, a large tea, with no flavour, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        else:
            print("Invalid addon entered please change your information")

    elif beverageSize == "small" or beverageSize== "s":
        costOfSize = 1.50
        TeaAddon = input("Do you want lemon, mint or no flavour:")

        if TeaAddon == "lemon" or TeaAddon== "l":
            costOfAddon= 0.25
            costOfBeverage = (costOfSize+costOfAddon) * Tax
            print("For Mr.{}, a small tea, with some lemon, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif TeaAddon == "mint" or TeaAddon== "mi":
            costOfAddon = 0.50
            costOfBeverage = (costOfSize + costOfAddon) * Tax
            print("For Mr.{}, a small tea, with some mint flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif TeaAddon== "none" or TeaAddon== "n":
            costOfAddon= 0
            costOfBeverage = (costOfSize) * Tax
            print("For Mr.{}, a small tea, with no flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        else:
            print("Invalid addon entered please change your information")

    elif beverageSize == "medium" or beverageSize == "m":
        costOfSize = 2.50
        TeaAddon= input("Do you want lemon, mint or no flavour")

        if TeaAddon == "lemon" or TeaAddon== "l":
            costOfAddon=0.25
            costOfBeverage= (costOfSize+costOfAddon)*Tax
            print("For Mr.{}, a medium tea, with some lemon, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif TeaAddon == "mint" or TeaAddon== "mi":
            costOfAddon = 0.50
            costOfBeverage = (costOfSize + costOfAddon) * Tax
            print("For Mr.{}, a medium tea, with some mint flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))

        elif TeaAddon== "none" or TeaAddon== "n":
            costOfAddon= 0
            costOfBeverage = (costOfSize) * Tax
            print("For Mr.{}, a medium tea, with no flavouring, and the cost is: ${}".format(customerName, round(costOfBeverage, 2)))
# else statement for invalid inforamtion not provided
else:
    print("The information entered is not valid(try again)")







