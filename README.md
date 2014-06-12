jail2net
=========
Allows creation of a PBX to accept calls from prisoners and post their recorded messages on SoundCloud and Twitter.

###Requirements:

Asterisk, lame, Python, PHP, Bash, soundcloud-python, twitteroauth, a DID and SIP account

###Instructions:

Set up Asterisk and configure your sip.conf and SIP provider
`apt-get install lame` and `pip install soundcloud`
Move *.gsm files to /usr/share/asterisk/sounds
Make the directory /var/asterisk and chown it to asterisk:asterisk
Move process.sh, post.py and tweet.php to /var/asterisk and make them executable
Also move twitteroauth.php and OAuth.php to /var/asterisk
Edit post.py and insert your SoundCloud API details for client_id, client_secret, username, password
Change the track title as desired
Edit tweet.php and insert your Twitter API details for $consumerKey, $consumerSecret, $oAuthToken and $oAuthSecret
Change the status message as desired
Edit extensions.conf, move it to /etc/asterisk and insert your DID, set up access control and DTMF tone if needed
Restart Asterisk and have fun!
