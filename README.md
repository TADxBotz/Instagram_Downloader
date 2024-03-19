<!DOCTYPE html>
<html>
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

<h3>Installation</h3>
<p>To get started, follow these steps:</p>
<ol>
  <li>Clone the repository:</li>
  <code>git clone https://github.com/yourusername/instagram-downloader-bot.git<br>cd instagram-downloader-bot</code>
  <li>Install dependencies:</li>
  <code>pip install -r requirements.txt</code>
</ol>

<h3>Configuration</h3>
<p>Create a <code>config.py</code> file in the root directory and add your Telegram bot token:</p>
<code>TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"</code>

<h2>Usage</h2>

<h3>Running Locally</h3>
<p>To run the bot locally, use the following command:</p>
<code>python main.py</code>

<h3>Deployment</h3>

<h4>Docker</h4>
<p>To run the bot using Docker:</p>
<code>docker build -t instagram_downloader_bot .<br>docker run -d --name instagram_downloader_container instagram_downloader_bot</code>

<h4>Heroku</h4>
<p>To deploy the bot to Heroku:</p>
<ol>
  <li>Log in to Heroku:</li>
  <code>heroku login</code>
  <li>Create a new Heroku app:</li>
  <code>heroku create</code>
  <li>Deploy the bot:</li>
  <code>git push heroku main</code>
  <li>Scale the bot:</li>
  <code>heroku ps:scale worker=1</code>
</ol>

<h2>Contributing</h2>
<p>Feel free to contribute to this project by submitting pull requests or reporting issues.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
