"""Internet Radio :
It displays a list of stations from stations.csv file.User select a number of station to play, which starts in 
a cleared screen with display of piece now playing.
It needs stations.csv and music player like mplayer.
"""

import os,re
import subprocess
#========================================================================
class Radio():
	def __init__(self, file=None, player=None, selected =None, names=None):
		self.file = 'stations.csv'
		self.player = "c:/mplayer/mplayer.exe"
		# "c:/ffmpeg/bin/ffplay -vn -nostats -loglevel 0 {}"
		self.stations = {}
		self.names = names
		self.selected = selected

	def read_stations(self):
		with open(self.file, mode='r') as f:
			for line in f.readlines():
				station = line.strip().split(',')
				self.stations[station[0]] = station[1]
		return self.stations

	def list_stations(self):
		self.read_stations()
		print("Welcome to Internet Radio")
		print(("Stations are:\n"+"="*110))
		self.names = list(self.stations.keys())
		rows = [(0,5), (5,12), (12,18), (18,23), (23,27),(27,31), (31,34), (35,38), (38,42)]
		for row in rows:
			for count in range(row[0],row[1]): print("|", count, self.names[count], end=" ")
			print("|\n", "-"*110)

	def station_selector(self):
		self.list_stations()
		print("="*70)
		try:
			self.n_selected = input("Please enter the number of the station to play, spacebar to pause, ESC yo quit\n : >> ")
		except:
			print( "Quiting ...")
		return self.names[int(self.n_selected)]

	def play_station(self):
		selection = self.station_selector()
		if selection:
			print("="*80)
			url = self.stations[selection]
			p= subprocess.Popen(["c:/mplayer/mplayer.exe",  url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			for line in p.stdout:
				if line.startswith(b'ICY Info:'):
					os.system("cls")
					info = line.split(b':', 1)[1].strip()
					st = info.decode(encoding= "ISO-8859-1" ) #"ISO-8859-1"
					st = re.sub("StreamTitle='", "", st)
					st = re.sub("';StreamNext='';", "", st)
					title = " ".join(st.split(' '))
					print(selection,"\n"+"="*115, "\n")
					print(title[:8]+title[8:], '\n')
					print("="*115)
#==========================================================================
if __name__ == "__main__":
	station = Radio()
	station.play_station()