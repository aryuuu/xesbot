<!DOCTYPE html>
<html>
<head>
	<title> subscribetoPewdiepie | KMP </title>
	<link rel="stylesheet" href="../css/style.css">

</head>
<body>
	<header>
		<div class = "container">
			<div id = title>
				<h1>XesBot</h1>
			</div>
			<nav>
				<ul class="options">
					<li><a href = "index.php">About</a></li>
					<li><a>Let's Match Patterns</a>
						<ul>
							<li class="current"><a href = "kmp.php">KMP</a></li>
							<li><a href = "bm.php">BM</a></li>
							<li><a href = "regex.php">Regex</a></li>
						</ul>
					</li>
				</ul>
			</nav>
		</div>
	</header>

	<section>
		<div class = "container">
			<img src="../img/bot.png" atl ="bot image" width = 340px style="float: left">			
			<div class="chatContainer">
				<div class="chatHeader">
					<h3 class="headerText">Hello there, I'm XesBot with KMP Algorithm !	</h3>
				</div>
				<div class="chatMessages">
					<li class='cm'> <b> XesBot : </b>How may I help you ? </li>
					<!-- Algoritma KMP disini -->
					<!-- Misal var answer = hasilAlgoKMP -->
					<?php
						if (isset($_POST['submit'])){
							$text = strip_tags(stripslashes($_POST['text']));
							echo "<li class='cm'> <b> Question : </b>" .$text. "</li>";
							/*Algoritma KMP disini*/
							/*Misal var answer = hasilAlgoKMP*/
							$answer = "hasilAlgoKMP";
							echo "<li class='cm'> <b> XesBot : </b>" .$answer. "</li>";
						}
					?>
				</div>
				<div class="questionForm">
					<form id="chatForm" action = "" method = "POST">
						<input type="text" name="text" id="text" placeholder="Ask a Question..">
						<input type="submit" name="submit" value="Ask !">
						
					</form>
				</div>
			</div>
		</div>
	</section>

	<footer>
		<p>XesBot by subscribetoPewdiepie</p>
	</footer>
</body>
</html>