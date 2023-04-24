#Mazen Baioumy
#Assignment 3: developing a code for processing and analyzing tweets with a touch of graphics
listOfkeywords= []
listOftweetsvalues = []
#create lists for tweets
centraltweets = []
easterntweets = []
pacifictweets = []
mountaintweets = []
count = 0
#create a list for the keywords depending on their sentiment value
lowSentiment = set()
midSentiment = set()
highsentiment = set()
veryhighsentiment= set()
#set the score value for the timezones
easternValue = 0
centralValue = 0
mountainValue = 0
pacificValue = 0
#create function to ask user for input
def validateFile():
        validFile = True
        while validFile:
            try:
                fileName = input("Please Enter The File Name:")
                inFile = open(fileName,"r")
                validFile= False
            except IOError:
                print("File Not Found Check For Any Spelling Errors")
                fileName = input("Try again by entering another name:")
        return inFile


#Funtion to determine timezone of the tweet
def location (latitude, longitude):
    if 24.660845 <= latitude <= 49.189787 and -87.518395 <= longitude <= -67.444574:
        region = 'Eastern'
    elif 24.660845 <= latitude <= 49.189787 and -125.242264 <= longitude <= -115.236428:
        region = 'Pacific'
    elif 24.660845 <= latitude <= 49.189787 and -115.236428 <= longitude <= -101.998892:
        region = 'Mountain'
    elif 24.660845 <= latitude <= 49.189787 and -101.998892 <= longitude <= -87.518395:
        region = 'Central'
    else:
        region = "no available region"
    return region

#create function to add keywords to list based on value
def assignmentKeyValues(file):
    global lowSentiment, midSentiment, highsentiment, veryhighsentiment
    for line in file:
        word, sentiment = line.split(",")
        sentiment=int(sentiment)
        if sentiment == 1:
            lowSentiment.add(word)
        elif sentiment == 5:
            midSentiment.add(word)
        elif highsentiment == 7:
            highsentiment.add(word)
        elif sentiment == 10:
            veryhighsentiment.add(word)

#create a function to calucate sentiment value
def sentimentValue (regionOfTweets):
    numOfWords = 0
    value = 0
    for i in range (len(listOfkeywords)):
        for j in range (len(regionOfTweets)):
            if listOfkeywords[i] in regionOfTweets[j]:
                value = value + listOftweetsvalues[i]
                numOfWords = numOfWords + 1
    sentiment = (value/numOfWords)
    sentiment = round(sentiment,6)
    return sentiment

#sort the tweets depending on the timezone
def sortingtweet (timezone, text):
    if timezone == 'Central':
        easterntweets.append(text)
    elif timezone == 'Eastern':
        centraltweets.append(text)
    elif timezone == 'Pacific':
        mountaintweets.append(text)
    elif timezone == 'Mountain':
        pacifictweets.append(text)

#validate the keyword file name entered
print("Enter The Keyword File Name")
keywords = validateFile()

for line in keywords:
    words = line.strip().split(",")
    listOfkeywords.append(words[0])
    listOftweetsvalues.append(int(words[1]))

#validate the tweet file name entered with a helping message
print("Enter The Tweet File Name")
tweets = validateFile()

#a for loop for tweets to be included in specific timezone and coordinates
for line in tweets:
    tweet = line.strip().split(" ",5)
    text = tweet[5].lower().strip("()',")
    cord1 = float(tweet[0].strip('[,'))
    cord2 = float(tweet[1].strip('],'))
    timezone = location(cord1,cord2)
    sortingtweet(timezone, text)

#create function to clean lines
def cleantheLines(line):
    line=list(line)
    for i in line:
        if i !=" " and not i.isdigit():
            line.remove(i)
        if i != " " and i.isdigit():
            line.remove(i)
    line ="".join(line)
    return line

#print lines with number of tweets and sentiment value of each tweet
print("Their are",len(centraltweets),"Eastern tweets, with a sentiment value of",sentimentValue(centraltweets))
print("Their are",len(easterntweets),"Mountain tweets, with a sentiment value of",sentimentValue(easterntweets))
print("Their are",len(pacifictweets),"Centraltweets, with a sentiment value of",sentimentValue(pacifictweets))
print("Their are",len(mountaintweets),"Pacific tweets, with a sentiment value of",sentimentValue(mountaintweets))
tweets.close()
keywords.close()
#close the files
#create a histogram based on sentiment values
def graphicsFun():
    import happy_histogram as hp
    hp.drawSimpleHistogram(sentimentValue(easterntweets),sentimentValue(mountaintweets),sentimentValue(centraltweets),sentimentValue(pacifictweets))

graphicsFun()
