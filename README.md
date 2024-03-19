<!DOCTYPE html>
<html>

<h1>Instagram Downloader Bot</h1>

<p>Welcome to the Instagram Downloader bot repository. This README provides instructions on how to set up, run, and deploy the bot.</p>

<h2>Features</h2>
<ul>
  <li>Download Instagram posts and reels.</li>
  <li>Supports both images (.jpg) and videos (.mp4).</li>
  <li>Handles Instagram URLs for posts and reels.</li>
  <li>Runs as a Telegram bot for easy access and usage.</li>
</ul>

<h2>Installation</h2>

<h3>Docker Installation</h3>
<p>If you prefer to run the bot using Docker:</p>
<ol>
  <li>Clone the repository:</li>
  <pre><code>git clone https://github.com/yourusername/instagram-downloader-bot.git
cd instagram-downloader-bot</code></pre>
  <li>Build the Docker image:</li>
  <pre><code>docker build -t instagram_downloader_bot .</code></pre>
  <li>Run the Docker container:</li>
  <pre><code>docker run -d --name instagram_downloader_container instagram_downloader_bot</code></pre>
</ol>

<h3>Heroku Deployment</h3>
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

<h3>Local Installation</h3>
<p>If you prefer to run the bot locally:</p>
<ol>
  <li>Clone the repository:</li>
  <pre><code>git clone https://github.com/yourusername/instagram-downloader-bot.git
cd instagram-downloader-bot</code></pre>
  <li>Install dependencies:</li>
  <pre><code>pip install -r requirements.txt</code></pre>
  <li>Create a <code>config.py</code> file in the root directory and add your Telegram bot token:</li>
  <pre><code>TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"</code></pre>
  <li>Run the bot:</li>
  <pre><code>python main.py</code></pre>
</ol>

<h2>Contributing</h2>
<p>Feel free to contribute to this project by submitting pull requests or reporting issues.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
