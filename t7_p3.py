def makeHomepage(name, hobby):
    
    #weather
    f = open("weather_data.html", 'r')
    text = f.read()
    findOne = text.find("media-body") +15
    findTwo = text.find("s=\"header3m\"") -27
    condition=(text[findOne:findTwo])
    findThree = text.find("metricData text-center vertical-center\"")+40
    findFour = text.find("td headers=\"header3i\" class=\" imperialData hidden text-center vertical-center\"")-107
    temp = (text[findThree:findFour])
    
    f.close()
    #name, hobby
    f = open("my_homepage.html", 'w')
    f.write(f"Name: {name}"+'\n')
    f.write(f"Hobby: {hobby}"+'\n\n\n')
    f.write(f"Weather:   Condition: {condition}, Temperature: {temp}")

    
    
    
    f.close()

makeHomepage("Michael", "Basketball")