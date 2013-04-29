<?php
	// $_GET['user'] is the Jabber ID (email) of the user who sent the message
	// $_GET['message'] is the text content of their message they sent
	header('Content-Type: text/plain');
	die($_GET['user'] . ' said "' . $_GET['message'] . '" which is "' . strrev($_GET['message']) . '" backwards.');
