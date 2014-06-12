jail2net
=========
Allows creation of a PBX to accept calls from prisoners and post their recorded messages on SoundCloud and Twitter.

###Requirements:

Asterisk, lame, Python, PHP, Bash, soundcloud-python, twitteroauth, a DID and SIP account

###Instructions:

1. Set up Asterisk and configure your sip.conf and SIP provider
2. `apt-get install lame` and `pip install soundcloud`
3. Move *.gsm files to /usr/share/asterisk/sounds
4. Make the directory /var/asterisk and chown it to asterisk:asterisk
5. Move process.sh, post.py and tweet.php to /var/asterisk and make them executable
6. Also move twitteroauth.php and OAuth.php to /var/asterisk
7. Edit post.py and insert your SoundCloud API details for client_id, client_secret, username, password
8. Change the track title as desired
9. Edit tweet.php and insert your Twitter API details for $consumerKey, $consumerSecret, $oAuthToken and $oAuthSecret
10. Change the status message as desired
11. Edit extensions.conf, move it to /etc/asterisk and insert your DID, set up access control and DTMF tone if needed
12. Restart Asterisk and have fun!
