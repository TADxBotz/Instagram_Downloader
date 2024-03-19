import instaloader
import requests
import uuid

def download_media(media_url):
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()

        # Get the media URL type (reel, reels, or post)
        if "/reel/" in media_url or "/reels/" in media_url:
            # Reel URL format
            shortcode = media_url.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            if post.is_video:
                # If the reel is a video, get the video URL
                media_url = post.video_url
                ext = ".mp4"
            else:
                # If the reel is an image, get the image URL
                media_url = post.url
                ext = ".jpg"
        elif "/p/" in media_url:
            # Post URL format
            shortcode = media_url.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            if post.is_video:
                # If the post is a video, get the video URL
                media_url = post.video_url
                ext = ".mp4"
            else:
                # If the post is an image, get the image URL
                media_url = post.url
                ext = ".jpg"
        else:
            return None, None

        # Download the media using requests
        response = requests.get(media_url)

        if response.status_code == 200:
            # Generate a unique filename using uuid
            filename = str(uuid.uuid4()) + ext

            # Save the media file
            with open(filename, "wb") as f:
                f.write(response.content)

            return filename, ext
        else:
            return None, None
    except instaloader.exceptions.InstaloaderException as e:
        # Handle Instaloader exceptions
        return None, None
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions
        return None, None
