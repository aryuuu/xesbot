<!DOCTYPE html>
<html>
<head>
	<title> subscribetoPewdiepie | About </title>
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
					<li class = "current"><a href = "index">About</a></li>
					<li><a>Let's Pattern Match</a>
						<ul>
							<li><a href = "kmp">KMP</a></li>
							<li><a href = "bm">BM</a></li>
							<li><a href = "regex">Regex</a></li>
						</ul>
					</li>
				</ul>
			</nav>
		</div>
	</header>	
	<section>
		<div class = "container">
			<div class = "about">
				<!-- <img src="../img/about.jpg" alt= "chatbot image" width = 300px>	 -->
				<img src="{{ url_for('static', filename='img/about.jpg') }}" alt= "chatbot image" width = 300px>	
				<aside id ="sidebar">
					<h2> What is this ? </h2>
					<p>
						Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
						tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
						quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
						consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
						cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
						proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
					</p>
				</aside>
			</div>
		</div>
	</section>

	<footer>
		<p>XesBot by subscribetoPewdiepie</p>
	</footer>

</body>
</html>	