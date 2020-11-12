#!python
import os, re
import subprocess
stations = {
"Arpeggio Radio": "http://146.185.18.251:7067/",
"Cinemix":"http://listen.shoutcast.com/CINEMIX-1",
"Mozart": "http://listen.shoutcast.com/radio-mozart",
"ClassicFM":"http://media-ice.musicradio.com/ClassicFMMP3",
"Italy":"http://176.31.107.8:8204/",
"Beethoven Radio":"http://listen.radionomy.com/beethoven-radio",
"Radio Mozart":"http://listen.radionomy.com/radio-mozart",
"CALM RADIO - BACH":"http://streams.calmradio.com/api/299/128/stream/",
"CALM RADIO - BEETHOVEN":"http://streams.calmradio.com/api/283/128/stream/",
"CALM RADIO - BAROQUE":"http://streams.calmradio.com/api/173/128/stream/",
"CALM RADIO - VIVALDI":"http://streams.calmradio.com/api/131/128/stream/",
"CALM RADIO - MOZART":"http://streams.calmradio.com/api/303/128/stream",
"CALM RADIO - SOLO PIANO":"http://streams.calmradio.com/api/29/128/stream/",
"CALM RADIO - CLASSICAL PIANO":"http://streams.calmradio.com/api/51/128/stream/",
"CALM RADIO - CLASSICAL GUITAR":"http://streams.calmradio.com/api/147/128/stream/",
"CALM RADIO - LIGHT CLASSICAL":"http://streams.calmradio.com:21128/stream/"
}
def list_stations():
    print("Welcome to Internet Radio")
    print("Stations are:\n"+"="*70)
    for index, station in enumerate(stations, 1):
        print("{:<5}{: <10}".format(index, station))

def play_station():
    url = stations[list(stations.keys())[station_index-1]]
    p= subprocess.Popen(["c:/mplayer/mplayer.exe",url], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    for line in p.stdout:
        if line.startswith(b'ICY Info:'):
            os.system("cls")
            info = line.split(b':', 1)[1].strip()
            st = info.decode(encoding= "ISO-8859-1" ) #"ISO-8859-1"
            st = re.sub("StreamTitle='", "", st)
            st = re.sub("';StreamNext='';", "", st)
            title = " ".join(st.split(' '))
            selection = list(stations.keys())[station_index-1]
            print(selection,"\n"+"="*70, "\n")
            print(title[:8]+title[8:], '\n')
            print("="*70)
def station_selector():
    list_stations()
    print("="*70)
    selected = input("Please enter the number of the station you want.\n or <ENTER> to 'quit' \n ")
    if selected :
        global station_index
        station_index = int(selected)
        play_station()
    else:
        exit

station_selector()

