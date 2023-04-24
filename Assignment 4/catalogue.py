#Done By: Mazen Baioumy
#Import country class from country python file
from country import Country
#import infinity from math
from math import inf
#create Country Catalogue class
class CountryCatalogue :
    #Create Consturctor
    #Reads in Data from Specified Files
    def __init__(self, _continent = "continent.txt", _data = "data.txt"):
        self._countryCat = []
        #Create a list of Country
        self._cDictionary = dict()
        _continent_file = open(_continent, "r")
        #Open Input file
        _header = _continent_file.readline()

        while _header != "":
            _header = _continent_file.readline()
            _list = _header.rstrip().split(",")
            #This processes the line reading and splitting at(,)

            if _header != "":
                self._cDictionary[_list[0]] = _list[1]
                #Setting The Dictionary from Input File

        _continent_file.close()
        #Closes Input File
        #Opens Input File
        _data_file = open(_data, "r")
        _headr = _data_file.readline()

        while _headr != "":
            _headr = _data_file.readline()

            if _headr != "":
                _list = _headr.rstrip().split("|")
                _cntry = _list[0]
                _pop = _list[1].split(",")
                _population = ""
                _area = _list[2].split(",")
                _area_int = ""

                for i in range(len(_pop)):
                    _population += _pop[i]

                for i in range(len(_area)):
                    _area_int += _area[i]
                    #Below Sets Object

                _country = Country(_cntry, float(_population), float(_area_int), self._cDictionary[_cntry])
                self._countryCat.append(_country)
                #Appends Object to List

        _data_file.close()
        #Closes Input File
    #Function to return object of Specified Country
    #Returns the correct object or nothing at all
    def findCountry(self, country):
        if country != "":
            for i in range(len(self._countryCat)):
                if self._countryCat[i].getName() == country:
                    return self._countryCat[i]
        if country == "":
            return None
    #MFunction to set a new Population of a Specified Country
    def setPopulationOfCountry(self, country, pop):
        for i in range(len(self._countryCat)):
            if self._countryCat[i].getName() == country:
                self._countryCat[i].setPopulation(pop)
                return True
        return False

    #Function to set a new Area of a Specified Country
    def setAreaOfCountry(self, country, area):
        for i in range(len(self._countryCat)):
            if self._countryCat[i].getName() == country:
                self._countryCat[i].setArea(area)
                return True
        return False


    #Adds Country to Catalogue given with country, population, size and area
    def addCountry(self, name, pop, area, cont):
        if name not in self._cDictionary:
            _country = Country(name, pop, area, cont)
            self._countryCat.append(_country)
            self._cDictionary[name] = cont
            return True
        else:
            return False

    #Function That Deletes Country from Catalogue
    def deleteCountry(self, country):
        if country in self._cDictionary:
            self._cDictionary.pop(country)
            for i in range(len(self._countryCat)):
                if self._countryCat[i].getName() == country:
                    self._countryCat.pop(i)
                    return True
        return False

    ##Prints Country Catalogue
    def printCountryCatalogue(self):
        for i in range(len(self._countryCat)):
            print(self._countryCat[i].__repr__())
    #Function to retrieve all countries based on continent
    def getCountriesByContinent(self, cont):
        _list = []
        for i in range(len(self._countryCat)):
            if self._countryCat[i].getContinent() == cont:
                _list.append(self._countryCat[i])
        return _list

    #Function for Sorting Countries In Continent by Population
    def getCountriesByPopulation(self, cont = ""):
        _dict = dict()
        _list = []
        for i in range(len(self._countryCat)):
            if cont == self._countryCat[i].getContinent():
                _dict[self._countryCat[i].getPopulation()] = self._countryCat[i].getName()
            if cont == "":
                _dict[self._countryCat[i].getPopulation()] = self._countryCat[i].getName()
        for key in sorted(_dict):
            _list2 = [str(_dict[key]), key]
            tuple(_list2)
            _list.append(_list2)
            _list.reverse()
        return _list
    #Function for Sorting countries on a Continent by Area
    #Highest to Lowest
    def getCountriesByArea(self, cont = ""):
        _dict = dict()
        _list = []
        for i in range(len(self._countryCat)):
            if cont == self._countryCat[i].getContinent():
                _dict[self._countryCat[i].getArea()] = self._countryCat[i].getName()

            if cont == "":
                _dict[self._countryCat[i].getArea()] = self._countryCat[i].getName()

        for key in sorted(_dict):
            _list2 = [str(_dict[key]), key]
            tuple(_list2)
            _list.append(_list2)

        _list.reverse()
        return _list

    #Function to Find Highest Population Continent in Dataset
    def findMostPopulousContinent(self):
        _dict = dict()
        _max = 0
        _cont = ""

        for key in sorted(self._cDictionary):
            _x = 0
            for i in range(len(self._countryCat)):
                if self._countryCat[i].getContinent() == self._cDictionary[key]:
                    _x += self._countryCat[i].getPopulation()
            if _x > _max:
                if len(_dict) > 0:
                    _dict.pop(_cont)
                _max = _x
                _dict[self._cDictionary[key]] = _x
                _cont = self._cDictionary[key]
        for item in _dict.items():
            return(item[0], item[1])
    #Function to sort all countries by Population Density
    def filterCountriesByPopDensity(self, lower = 0, upper = inf):
        _dict = dict()
        _list = []
        for i in range(len(self._countryCat)):
            if lower <= self._countryCat[i].getPopDensity() <= upper:
                _dict[self._countryCat[i].getPopDensity()] = self._countryCat[i].getName()

        for item in sorted(_dict.items()):
            _temp = item[1] + ":" + str(item[0])
            _list.append(_temp)

        if len(_list) > 0:
            _list.reverse()
        return _list
    #Function to write data.txt to a specified file
    def saveCountryCatalogue(self, filename):
        _count = 0
        _write = ""
        _outfile = open(filename, "w")
        for key in sorted(self._cDictionary):
            for i in range(len(self._countryCat)):
                if key == self._countryCat[i].getName():
                    _object = self._countryCat[i]
                    _write = key + "|" + self._cDictionary[key] + "|" + str(_object.getPopulation()) + "|" + str(_object.getArea()) \
                        + "|" + str(_object.getPopDensity()) + "\n"
                    _outfile.write(_write)
                    _count += 1
        _outfile.close()
        if _count == 0:
            return(-1)
        return _count



