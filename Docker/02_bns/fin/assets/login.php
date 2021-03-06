<!DOCTYPE html>
<html lang="eng">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<link rel="stylesheet" href="css/reg.css">
		<link href="https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Montserrat:wght@400;800&display=swap" rel="stylesheet">
		<title>Helen</title>
	</head>
	<body>
<?php
if (!isset($_COOKIE['user'])):
?>
		<section class="section">
			<div class="container">
				<div class="container__header">
					<h2 class="container__title">Create a free account</h2>
				</div>
				<div class="container__form">
					<form action="check.php" method="POST">
						<div class="form__title">
							<span>Username</span><br />
							<input type="text" class="form__input" name="username" id="username">
						</div>
						<div class="form__title">
							<span>Email</span><br />
							<input type="text" class="form__input" name="email" id="email">
						</div>
						<div class="form__title">
							<span>Password</span><br />
							<input type="password" class="form__input" name="pass" id="pass">
						</div>
						<div class="form__button">
							<button class="btn btn-sucess" type="submit">sign up</button>
						</div>
					</form>
				</div>
			</div>
			<div class="container">
				<div class="container__header">
					<h2 class="container__title">Log in</h2>
				</div>
				<div class="container__form">
					<form action="auth.php" method="POST">
						<div class="form__title">
							<span>Email</span><br />
							<input type="text" class="form__input" name="email" id="email">
						</div>
						<div class="form__title">
							<span>Password</span><br />
							<input type="password" class="form__input" name="pass" id="pass">
						</div>
						<div class="form__button">
							<button class="btn btn-sucess" type="submit">log in</button>
						</div>
					</form>
				</div>
			</div>
		</section>
		<?php else: ?>
		<section class="section">
			<div class="auth">
			It's <?=$_COOKIE['username']?>! Welcome, delicious friend! If you want to leave click <a href="/exit.php">here</a>.
			</div>
		</section>
	<?php endif;?>
	</body>
</html>
