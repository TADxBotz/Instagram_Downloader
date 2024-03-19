<!DOCTYPE html>
<html>
<head>
  <title>Instagram Downloader Bot</title>
</head>
<body>

<h1>Instagram Downloader Bot</h1>

<p>Welcome to the Instagram Downloader bot repository. This README provides instructions on how to set up, run, and deploy the bot.</p>

<h2>Features</h2>
<ul>
  <li>Download Instagram posts and reels.</li>
  <li>Supports both images (.jpg) and videos (.mp4).</li>
  <li>Handles Instagram URLs for posts and reels.</li>
  <li>Runs as a Telegram bot for easy access and usage.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.9 or higher</li>
  <li>Docker (optional, for containerization)</li>
  <li>Heroku CLI (optional, for deploying to Heroku)</li>
</ul>

<h2>Installation</h2>

<h3>Step 1: Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/instagram-downloader-bot.git
cd instagram-downloader-bot</code></pre>

<h3>Step 2: Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>Configuration</h3>
<p>Create a <code>config.py</code> file in the root directory and add your Telegram bot token:</p>
<pre><code>TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"</code></pre>

<h2>Usage</h2>

<h3>Running Locally</h3>
<p>To run the bot locally, use the following command:</p>
<pre><code>python main.py</code></pre>

<h3>Deployment</h3>

<h4>Docker</h4>
<p>To run the bot using Docker:</p>
<pre><code>docker build -t instagram_downloader_bot .
docker run -d --name instagram_downloader_container instagram_downloader_bot</code></pre>

<h4>Heroku</h4>
<p>To deploy the bot to Heroku:</p>
<ol>
  <li>Log in to Heroku:</li>
  <pre><code>heroku login</code></pre>
  <li>Create a new Heroku app:</li>
  <pre><code>heroku create</code></pre>
  <li>Deploy the bot:</li>
  <pre><code>git push heroku main</code></pre>
  <li>Scale the bot:</li>
  <pre><code>heroku ps:scale worker=1</code></pre>
</ol>

<h2>Contributing</h2>
<p>Feel free to contribute to this project by submitting pull requests or reporting issues.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
