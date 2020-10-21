<?php
	$email = filter_var(trim($_POST['email']), FILTER_SANITIZE_STRING);	
	$pass = filter_var(trim($_POST['pass']), FILTER_SANITIZE_STRING);
	
	$pass = md5($pass."site1");

	$mysql = new mysqli('localhost', 'root', '8Pfvtxnjq+12', 'registrybd');

	$result = $mysql->query("SELECT * FROM `users` WHERE `email` = '$email' AND `password` = '$pass'");
	$user = $result->fetch_assoc();

	if (count($user) == 0) {
		echo "User's not found";
		exit();
	}

	setcookie('user', $user['username'], time() + 3600, "/");

	$mysql->close();

	header('Location: /');
?>
