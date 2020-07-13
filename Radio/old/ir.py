#read csv file into dict
import os
stations = []

def read_stations():
	with open('c:\py\ir\stations.csv', mode='r') as f:
		for line in f.readlines():
			station = line.strip().split(',')
			stations.append((station))
	return stations

def list_stations():
	read_stations()
	print "Welcome to Internet Radio"
	print "Stations are:\n"+"="*87
	for station in stations:
		print ("{: <5} {: <10}".format( stations.index(station)+1, station[0]))

def station_selector():
	list_stations()
	print "="*87
	selected = raw_input("Please enter the number of the station you want.\n or <ENTER> to 'quit' \n>> ")
	if selected :
		global station_index
		station_index = int(selected)
		play_station()
	else:
		exit
	
def play_station():
	os.system("C:\mplayer\mplayer -playlist "+stations[station_index-1][1])
	os.system("cls")
	

station_selector()