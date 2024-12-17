import instaloader
import os

# Initialize Instaloader
L = instaloader.Instaloader()

# Load the profile
profile = instaloader.Profile.from_username(L.context, 'park_pappa')

# Create a folder for sorted images
sorted_folder = './sorted_parks/'
os.makedirs(sorted_folder, exist_ok=True)

# Function to ensure unique filenames
def get_unique_filename(path, base_filename, ext):
    counter = 1
    new_filename = f"{base_filename}{ext}"
    while os.path.exists(os.path.join(path, new_filename)):
        new_filename = f"{base_filename}_{counter}{ext}"
        counter += 1
    return new_filename

PostNumber = 1
# Loop through the profile's posts
for post in profile.get_posts():
    # Define base filename using the post's unique timestamp
    base_filename = f"post_{post.date_utc.strftime('%Y%m%d_%H%M%S')}"
    # Download the image directly to the sorted folder with a unique name
    L.download_pic(os.path.join(sorted_folder, str(PostNumber)), post.url, post.date_utc)
    PostNumber += 1 

print("Done downloading all images!")
