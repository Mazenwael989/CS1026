#Done By: Mazen Baioumy
#create country class
class Country :
    #Create constructor and instance variable
    #Set Objects with Specified Data (Country, Population, Area, Continent)
    def __init__(self, name = "", population = 0, area = 0, continent = ""):
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent
    #Gives the Name of Country
    def Getnameofcountry(self):
        return self._name
    #Gives Population
    def GetthePopulation(self):
        return self._population
    #Gives Area
    def findarea(self):
        return self._area
    #Gives Continent
    def getContinent(self):
        return self._continent
    #Clears Instance Variables
    def clear(self):
        self._name = ""
        self._population = 0
        self._area = 0
        self._continent = ""
    #set methods for setters and getters
    #Set Specified Population
    def setPopulation(self, pop):
        self._population = pop
    #Set Specified Area
    def setArea(self, area):
        self._area = area
    #Set Specified Continent
    def setContinent(self, cont):
        self._continent = cont
    #Calculate Population Density
    def getPopDensity(self):
        if self._area > 0:
            popDensity = round(self._population / self._area, 2)
        else:
            return 0
        return popDensity
    #Returns to two Decimal Places and string

    #create string reperesentation for class
    #Format  Country based on size, population, and area
    def __repr__(self):
        return(self._name + "(pop:" + str(self._population) + ", size:" + str(self._area) + ") in " + self._continent)
    def outFile(self, countryObject, popDensity):
        _str = countryObject.Getnameofcountry() + "|" + countryObject.getContinent() + "|" + str(countryObject.gGetthePopulation()) + "|" + \
            str(countryObject.findarea()) + "|" + str(popDensity)
        return _str

