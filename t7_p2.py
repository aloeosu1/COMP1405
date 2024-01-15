condition=""
f = open("weather_data.html", 'r')
text = f.read()
findOne = text.find("media-body") +15
findTwo = text.find("s=\"header3m\"") -27
condition=(text[findOne:findTwo])
print(condition)
findThree = text.find("metricData text-center vertical-center\"")+40
findFour = text.find("td headers=\"header3i\" class=\" imperialData hidden text-center vertical-center\"")-107
temp = (text[findThree:findFour])
print(temp)

