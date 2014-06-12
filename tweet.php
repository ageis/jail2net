<?php
require_once('twitteroauth.php');
$consumerKey    = '';
$consumerSecret = '';
$oAuthToken     = '';
$oAuthSecret    = '';

$msg = 'New audio message from ____ in jail: ' . $argv[1];
$update['status'] = $msg;
$tweet = new TwitterOAuth($consumerKey, $consumerSecret, $oAuthToken, $oAuthSecret);
$tweet->post('statuses/update', $update);

?>
