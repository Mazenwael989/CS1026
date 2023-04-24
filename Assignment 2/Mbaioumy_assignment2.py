# import the pi for ellipsoid volume from math
from math import pi
#set the list to use them
cubeVolumeList = []
ellipsoidVolumeList = []
pyramidVolumeList = []

#input function to allow user to pick between cube,pyramid,ellipsoid
shapeType = input("Please Enter The Desired shape:")
shapeType = shapeType.lower()
#shape type with .lower allows user to input both uppercase and lowercase shapetypes

#cube function starts with def to calculate volume with return
def cubeVolume(a):
#cu is a which is to the power of 3
    cuVolume = a ** 3
    return cuVolume
#if statement to allow user to determine what the interpeter should run if user pick cube
if shapeType =="cube":
#sidelength is the a float with user input to insert number for sidelength
    sidelength = float(input("Please Enter Cube Side Length:"))
#For calling the list
    cuVolume = cubeVolume(sidelength)
#print with the value of the cube volume rounded to 2 decimal places
    answer = print("The Cube's Volume Is:",round(cuVolume,2))
#This includes cubevolume into the list which is an array
    cubeVolumeList.append(round(cuVolume,2))

#pyramid function starts with def to calculate pyramid volume
def pyramidVolume(b,h):
        pyVolume = 0.3* (b**2)*(h)
        return pyVolume
#the if statement incase pyramid shape is choosen
if shapeType =="pyramid":
    shapeBase = float(input("Please Enter The Base Of Pyramid:"))
    shapeHeight= float(input("Please Enter The Height Of Pyramid:"))
    pyVolume = pyramidVolume (shapeBase,shapeHeight)
    answer1 = print("The Volume Of Pyramid With Specified Base",shapeBase,"Height",shapeHeight,"is",round(pyVolume,2))
    pyVolume = pyramidVolume (shapeBase,shapeHeight)
    pyramidVolumeList.append(round(pyVolume,2))

#function for ellipsoid
def ellipsoidVolume(r1,r2,r3):
    elVolume = 1.3*pi*r1*r2*r3
    return elVolume
#shapeType input for ellipsoid
if shapeType == "ellipsoid":
    firstRadius=float(input("Please Enter The First Radius:"))
    secondRadius=float(input("Please Enter The Second Radius:"))
    thirdRadius=float(input("Please Enter The Third Radius:"))
    elVolume = ellipsoidVolume (firstRadius,secondRadius,thirdRadius)
    qnswer2=print("The Volume Of The Ellipsoid Is:",round(elVolume,2))
# same thing with function and input for ellipsoid and for pyramid repeated with rounding to second decimal place
    ellipsoidVolumeList.append(round(elVolume,2))
if shapeType == "quit":
    print("you have come to the end of your session you didnt enter any values")
else:
    print("Invalid Data Entered Please Retry")
#else with a print function incase invalid input for shape is entered

#while loop that ends when conditions are met

while shapeType != "quit":
    shapeType = input("Please Enter The Shape or quit to end session:")
    shapeType = shapeType.lower()
    if shapeType =="cube":
        shapeVolume = int(input("please enter cube length:"))
        cuVolume = shapeVolume ** 3
        answer = print("the cube volume is:",round(cuVolume,2))
        cubeVolumeList.append(round(cuVolume,2))

    elif shapeType == "pyramid":
        shapeBase = int(input("please enter the base of pyramid:"))
        shapeHeight = int(input("please enter the height of pyramid:"))
        pyVolume = 0.3* (shapeBase**2)*(shapeHeight)
        answer1 = print("The Volume Of Pyramid With Specified Base",shapeBase,"Height",shapeHeight,"is",round(pyVolume,2))
        pyramidVolumeList.append(round(pyVolume,2))
#choosing ellipsoid and input with entering the float

    elif shapeType == "ellipsoid":
        firstRadius=float(input("Please Enter The First Radius:"))
        secondRadius=float(input("Please Enter The Second Radius:"))
        thirdRadius=float(input("Please Enter The Third Radius:"))
        elVolume= 1.3*pi*(firstRadius)*(secondRadius)*(thirdRadius)
        answer=print("The volume of the ellipsoid is:",round(elVolume,2))
        ellipsoidVolumeList.append(round(elVolume,2))
# listing what the values calculated are

    elif shapeType == "quit":
        print("You Have Decided To Leave, Here Are Your Calculated Values")
        print('You have come to the end of the session.')
        print('The volumes calculated for each shape are shown below.')
        print('Cube:', cubeVolumeList)
        print('Pyramid:', pyramidVolumeList)
        print('Ellipsoid:', ellipsoidVolumeList)
    else:
        print("Invalid Data Entry Please Retry")
#else for any invlaid data entry








