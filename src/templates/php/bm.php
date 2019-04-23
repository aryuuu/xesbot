<!DOCTYPE html>
<html>
<head>
	<title> subscribetoPewdiepie | KMP </title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- <link rel="stylesheet" href="../css/style.css"> -->
	<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
	<header>
		<div class = "container">
			<div id = title>
				<h1>XesBot</h1>
			</div>
			<nav>
				<ul class="options">
					<li><a href = "index">About</a></li>
					<li><a>Let's Match Patterns</a>
						<ul>
							<li><a href = "kmp">KMP</a></li>
							<li class="current"><a href = "bm.php">BM</a></li>
							<li><a href = "regex">Regex</a></li>
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
					<h3 class="headerText">Hello there, I'm XesBot with BM Algorithm !	</h3>
				</div>
				<div class="chatMessages">
					<li class='cm'> <b> XesBot : </b>How may I help you ? </li>
					<li class='cm'> <b> Question :  </b> {{quest}} </li>
					{% if answer %}
						<li class='cm'> <b> XesBot : </b> {{answer}} </li>
					{% endif %}
						
					
					
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