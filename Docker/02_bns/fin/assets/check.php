<?php
	$username = filter_var(trim($_POST['username']), FILTER_SANITIZE_STRING);	
	$email = filter_var(trim($_POST['email']), FILTER_SANITIZE_STRING);
	$pass = filter_var(trim($_POST['pass']), FILTER_SANITIZE_STRING);

	if (mb_strlen($username) < 3 || mb_strlen($username) > 50) {
		echo "Too short or too long";
		exit();
	} else if (mb_strlen($email) < 3 || mb_strlen($email) > 50) {
		echo "Too short or too long";
		exit();	
	} else if (mb_strlen($pass) < 3) {
		echo "Too short";
		exit();
	}

	$pass = md5($pass."site1");

	$mysql = new mysqli('localhost', 'root', '8Pfvtxnjq+12', 'registrybd');
	$mysql->query("INSERT INTO `users` (`username`, `email`, `password`) VALUES('$username', '$email', '$pass')");

	$mysql->close();

	header('Location: /');
?>
