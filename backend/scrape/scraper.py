"""
    Script used as a tool to extract images from the park_pappa account (not
    used in favor of embeds).

    Author: David Lockley
"""
import instaloader
import os
import json
import requests
from requests.exceptions import RequestException

# Constants
USERNAME = 'park_pappa'
OUTPUT_FOLDER = './scraped_data'
IMAGES_FOLDER = os.path.join(OUTPUT_FOLDER, 'images')
JSON_FILE = os.path.join(OUTPUT_FOLDER, 'posts.json')
TIMEOUT = 10  # seconds for requests

# Create directories
os.makedirs(IMAGES_FOLDER, exist_ok=True)

# Initialize Instaloader
L = instaloader.Instaloader(download_pictures=False, download_videos=False, compress_json=False)
profile = instaloader.Profile.from_username(L.context, USERNAME)

posts_data = []

for post in profile.get_posts():
    post_details = {
        "id": post.shortcode,
        "caption": post.caption or "",
        "hashtags": post.caption_hashtags,
        "timestamp": post.date_utc.isoformat(),
        "image_filenames": []
    }

    try:
        # Fetch image URLs
        image_urls = []
        if post.typename == "GraphSidecar":
            sidecar_nodes = list(post.get_sidecar_nodes())  # Convert generator to list
            for node in sidecar_nodes:
                image_urls.append(node['display_url'])  # Ensure 'display_url' is valid
        else:
            image_urls = [post.url]

        # Download images
        for idx, image_url in enumerate(image_urls):
            image_filename = f"{post.shortcode}_{idx + 1}.jpg"
            image_path = os.path.join(IMAGES_FOLDER, image_filename)

            try:
                response = requests.get(image_url, stream=True, timeout=TIMEOUT)
                response.raise_for_status()  # Raise HTTP errors
                with open(image_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)

                post_details["image_filenames"].append(image_filename)

            except RequestException as e:
                print(f"Failed to download {image_url}: {e}")

        # Save post details
        posts_data.append(post_details)

    except Exception as e:
        print(f"Error processing post {post.shortcode}: {e}")

# Save all posts to JSON
with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(posts_data, f, ensure_ascii=False, indent=4)

print(f"Scraping completed! Data saved to {OUTPUT_FOLDER}")
