# python.exe C:\\Users\\pobrzut\\Desktop\\Coding_is_fun\\program3\\geo_sort.py
# -*- coding: utf-8 -*-
import urllib
import json
import unicodedata

KEY = 'paste here your google API key'
URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='
index = 0
folderList = dict()

# Tuples for assigning pin color to a person
colors = {'Agnieszka Kluczewska':'ffff8000',
'Aleksandra Bu\xf1kowska':'ffff8000', # jasno-niebieski
'Aleksandra Regulska':'ffff4db8',
'Aneta B\xb3achuci\xf1ska':'ffc65353', #jasno-fioletowy
'Anna Brzozowska':'ffff4db8', #jasny-purpurowy
'Anna Fr\xb9tczak':'ff40bf40', #jasny-zielony
'Barbara Jasi\xf1ska':'ffc3ff4d', # jasny-morski
'Daniel Elwart':'ffffcc66', # ciemny-morski
'El\xbfbieta Boro\xf1':'ffffffff', # bialy
'Ewa Gierasimiuk':'ff4080bf', # brazowy
'Jacek Gliwi\xf1ski':'ff8533ff', # madzenta
'Jan Marsza\xb3kowski':'ff66ffb3', #blady-zielony
'Jaros\xb3aw \xa3ukaszewicz':'ff003366', # ciemny-brazowy
'Karolina Sobolewska':'ffcc99ff', # rozowy
'Krzysztof Cichocki':'ff333399', # cimeny-czerwony
'Lilianna Wieczorek':'ff0040ff', # czerwony
'Marcin Bobrowski':'ff009999', # brudny zolty
'Marcin Piekarski':'ffb3cccc', # szary
 'Marek Pawluk':'ff99ff99', # seledynowy
'Mariusz Osetek':'ff402060', # sliwka
'Marta Hernik': 'ff00ffff', # zolty
'Pawe\xb3 Chobot':'ffcc6600', # niebieski
'Rados\xb3aw Ciach':'ff000000', # czarny
'Rafa\xb3 Grzeszczuk':'ff669999', # jakis bez
'Sylwia Licha\xf1ska':'ff0066ff', # pomaranczowy
'Wojciech Stanek':'ff001f4d', # braz
'Wojciech Wyszomierski':'ff00ff00'} # zielony

# open external file and put read data in an array
def readFile(openedFile):
	openedFile = open(openedFile, 'r')
	content = []
	for line in openedFile:
		line = line.strip()
		if line.find('&') != -1:
			line = line.replace('&', ' and ')
		content.append(line)
	openedFile.close()
	return content

# Build body of the KML file
def buildKml(salesPerson,countPersonOccur):
	if salesPerson not in countPersonOccur.keys():
		myKML.write('<Folder><name>'+salesPerson+'</name>\n')
		myKML.write('<Placemark>\n')
		myKML.write('<name>' + companyNamesList[index] + '</name>\n')
		myKML.write('<description>' + salesPerson + '\n' + zipcodesList[index] + '\n' + citiesList[index] + '</description>\n')
		myKML.write('<Point><coordinates>' + lng + ',' + lat + ',0</coordinates></Point>\n')
		myKML.write('<Style><IconStyle><colorMode>normal</colorMode>\n')
		myKML.write('<color>'+ colors[salesPerson] +'</color>\n')
		myKML.write('</IconStyle></Style>\n')
		myKML.write('</Placemark>\n')
		countPersonOccur[salesPerson] = countPersonOccur.get(salesPerson,0) + 1
	elif salesPerson in countPersonOccur.keys() and countPersonOccur[salesPerson]!=salesPersonList.count(salesPerson):
		myKML.write('<Placemark>\n')
		myKML.write('<name>' + companyNamesList[index] + '</name>\n')
		myKML.write('<description>' + salesPerson + '\n' + zipcodesList[index] + '\n' + citiesList[index] + '</description>\n')
		myKML.write('<Point><coordinates>' + lng + ',' + lat + ',0</coordinates></Point>\n')
		myKML.write('<Style><IconStyle><colorMode>normal</colorMode>\n')
		myKML.write('<color>'+ colors[salesPerson] +'</color>\n')
		myKML.write('</IconStyle></Style>\n')
		myKML.write('</Placemark>\n')
		countPersonOccur[salesPerson] = countPersonOccur.get(salesPerson,0) + 1
	if salesPerson in countPersonOccur.keys() and countPersonOccur[salesPerson]==salesPersonList.count(salesPerson):
		myKML.write('</Folder>\n')

# For proper Folder structure in KML data needs to be deleted when Error occurs
def deleteItems():
	del salesPersonList[index]
	del citiesList[index]
	del zipcodesList[index]
	del companyNamesList[index]

citiesList = readFile('C:\\Users\\pobrzut\\Desktop\\Coding_is_fun\\program3\\cities.txt')
zipcodesList = readFile('C:\\Users\\pobrzut\\Desktop\\Coding_is_fun\\program3\\zipcodes.txt')
companyNamesList = readFile('C:\\Users\\pobrzut\\Desktop\\Coding_is_fun\\program3\\companies.txt')
salesPersonList = readFile('C:\\Users\\pobrzut\\Desktop\\Coding_is_fun\\program3\\sprzedawca.txt')

# Remove ASCII characters in order to build proper url / I did not find a method that would encode string to IRI format i.e. %20 for space, replace polish characters etc
i=0
for i in range(len(citiesList)):
	citiesList[i] = citiesList[i].lower()
	citiesList[i] = citiesList[i].replace('\xb9','a')
	citiesList[i] = citiesList[i].replace('\x8c','s')
	citiesList[i] = citiesList[i].replace('\xea','e')
	citiesList[i] = citiesList[i].replace('\xf3','o')
	citiesList[i] = citiesList[i].replace('\xf3','o')
	citiesList[i] = citiesList[i].replace('\xa3','l')
	citiesList[i] = citiesList[i].replace('\x9f','z')
	citiesList[i] = citiesList[i].replace('\xf1','n')
	citiesList[i] = citiesList[i].replace('\x9c','s')
	citiesList[i] = citiesList[i].replace('\xbf','z')
	citiesList[i] = citiesList[i].replace('\xaf','z')
	citiesList[i] = citiesList[i].replace('\xb3','l')
	citiesList[i] = citiesList[i].replace('\xe9','e')
	i += 1

# Create and build the head of KML file
myKML = open('C:\\Users\\pobrzut\\Desktop\\Coding_is_fun\\program3\\map.kml','w')
myKML.write('<?xml version="1.0" encoding="UTF-8"?>\n')
myKML.write('<kml xmlns="http://www.opengis.net/kml/2.2"\n')
myKML.write(' xmlns:gx="http://www.google.com/kml/ext/2.2">\n')
myKML.write('<Document>\n')

# Complex loop: furter preparation of url, using google api for getting latitude and longitude
while index < len(citiesList):
	try:
		city = citiesList[index].decode('cp1252').strip()
	except:
		city = citiesList[index]
	zipcode = zipcodesList[index]
	prepUrl = URL + zipcode + ',' + city + KEY
	prepUrl = prepUrl.replace(" ","+")
	try:
		content = urllib.urlopen(prepUrl)
	except:
		print "Invalid URL: ", prepUrl
		print "Placemark for " + companyNamesList[index] + "is not included in your kml"
		deleteItems()
		continue
	data = content.read()
	js = json.loads(data)
	if js['status'] == "OVER_QUERY_LIMIT":
		print "ERROR ERROR ERROR = OVER_QUERY_LIMIT"
		break
	elif js['status'] == "OK":
		print "OK " + companyNamesList[index]
		lat = js['results'][0]['geometry']['location']['lat']
		lng = js['results'][0]['geometry']['location']['lng']
		lat = str(lat)
		lng = str(lng)
		# Many if statements to organise Folders with customer's placemarks by sales person
		if salesPersonList[index] == 'Agnieszka Kluczewska':	
			buildKml(salesPersonList[index],folderList)
		
		elif salesPersonList[index] == 'Aleksandra Bu\xf1kowska':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Aleksandra Regulska':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Aneta B\xb3achuci\xf1ska':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Anna Brzozowska':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] =='Anna Fr\xb9tczak':
			buildKml(salesPersonList[index],folderList)
		
		elif salesPersonList[index] == 'Barbara Jasi\xf1ska':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Daniel Elwart':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'El\xbfbieta Boro\xf1':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Ewa Gierasimiuk':	
			buildKml(salesPersonList[index],folderList)
	
		elif salesPersonList[index] == 'Jacek Gliwi\xf1ski':	
			buildKml(salesPersonList[index],folderList)
		
		elif salesPersonList[index] == 'Jan Marsza\xb3kowski':	
			buildKml(salesPersonList[index],folderList)
	
		elif salesPersonList[index] == 'Jaros\xb3aw \xa3ukaszewicz':	
			buildKml(salesPersonList[index],folderList)
		
		elif salesPersonList[index] == 'Karolina Sobolewska':	
			buildKml(salesPersonList[index],folderList)
	
		elif salesPersonList[index] == 'Krzysztof Cichocki':	
			buildKml(salesPersonList[index],folderList)
		
		elif salesPersonList[index] == 'Lilianna Wieczorek':	
			buildKml(salesPersonList[index],folderList)
	
		elif salesPersonList[index] == 'Marcin Bobrowski':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Marcin Piekarski':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Mariusz Osetek':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] =='Marta Hernik':
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Marek Pawluk':	
			buildKml(salesPersonList[index],folderList)
		
		elif salesPersonList[index] == 'Pawe\xb3 Chobot':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Rados\xb3aw Ciach':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Rafa\xb3 Grzeszczuk':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Sylwia Licha\xf1ska':	
			buildKml(salesPersonList[index],folderList)
		
		elif salesPersonList[index] == 'Wojciech Stanek':	
			buildKml(salesPersonList[index],folderList)
			
		elif salesPersonList[index] == 'Wojciech Wyszomierski':	
			buildKml(salesPersonList[index],folderList)
			
		else:
			print 'There is a gap in your code or input data for: ' + companyNamesList[index]
			print 'Assign sales Person is: ' + salesPersonList[index]
			deleteItems()
			continue
	else:
		print 'Something went wrong for: ' + companyNamesList[index]
		print 'Status is ', js['status']
		print prepUrl
		print '\n'
		deleteItems()
		continue
		
	index += 1

# ending and closing KML file
myKML.write('</Document>\n')
myKML.write('</kml>\n')
myKML.close()

print 'KML File is ready. Thank you.'