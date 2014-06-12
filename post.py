import soundcloud
import sys
import datetime
import subprocess

client = soundcloud.Client(client_id='',
                           client_secret='',
                           username='',
                           password='')
                           
date = str(datetime.date.today())

track = client.post('/tracks', track={
    'title': '____ - Live From Prison - ' + date,
    'sharing': 'public',
    'asset_data': open(sys.argv[1], 'rb')
})

subprocess.call(["php5", "tweet.php", track.permalink_url])
