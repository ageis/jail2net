jail2net
=========
Allows creation of a PBX to accept calls from prisoners and post their recorded messages on SoundCloud and Twitter.

###Requirements:

Asterisk, lame, Python, PHP, Bash, soundcloud-python, twitteroauth, a DID and SIP account

###Instructions:

1. Purchase a DID (telephone number) from a SIP provider. I recommend (VoIP.ms)[https://voip.ms])
2. Install Asterisk and (configure your sip.conf)[http://wiki.voip.ms/article/PBXs#Asterisk_.28SIP.29]. Set context= to default.
3. Clone this repository to /opt/jail2net
4. `apt-get install lame` and `pip install soundcloud`
5. Move *.gsm files to /usr/share/asterisk/sounds
6. Move process.sh, post.py and tweet.php to /opt/jail2net and make them executable
7. Also move twitteroauth.php and OAuth.php to /opt/jail2net
8. `chown -R asterisk:asterisk /opt/jail2net`
9. Edit post.py and insert your SoundCloud API details for client_id, client_secret, username, password
10. Change the track title as desired
11. Edit tweet.php and insert your Twitter API details for $consumerKey, $consumerSecret, $oAuthToken and $oAuthSecret
12. Change the status message as desired
13. Move extensions.conf to /etc/asterisk, edit and insert your DID, set up access control and DTMF tone if needed
14. Restart Asterisk and give the phone number to your prisoner. Have fun trolling the BOP!

It helps to know what number they'll be calling from and the number you have press to accept their call.

This concept has been (covered by Mashable)[http://mashable.com/2013/04/15/weev-soundcloud-message/]. Mad props to Jaime Cochran for the idea and Python script. Prisoners should be informed of the risks; weev lost his phone privileges and was thrown in solitary for using this.
