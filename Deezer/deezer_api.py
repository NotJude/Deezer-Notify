
from deezer import Client
import requests

FIRST_RUN = True

ARTIST_KEY = 13612387 # this one is for Maneskin
c = Client()
now_tracks = c.get_artist(ARTIST_KEY).get_top()

if FIRST_RUN:
    file = open("tracks.txt", "x")

    for t in now_tracks:
        file.write(str(t.id)+'\n')

    print("REMEMBER TO SET 'FIRST_RUN' TO 'False'")


else:
    filer = open("tracks.txt", "r")
    pv_tracks = [pvt.replace('\n', '') for pvt in filer.readlines()]
    filer.close()

    secur = 0
    if len(pv_tracks) != len(now_tracks):
        filew = open("tracks.txt", "w")
        if filew.writable():
            for t in now_tracks:
                id = str(t.id)
                if id not in pv_tracks and secur < 3:
                    requests.post('https://api.mynotifier.app', {
                        "apiKey": '****-****-****-****',
                        "message": "New Maneskin song out!",
                        "description": str(c.get_track(t.id))[8:-1],
                        "type": "info", 
                        })
                    secur += 1
                filew.write(id+'\n')

        filew.close()
