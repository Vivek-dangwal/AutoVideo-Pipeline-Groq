import sys
import requests
import os

PEXELS_API_KEY = "YOUR_REAL_KEY_HERE"

def download_video(query):
    # CLEANUP: Remove old video so we don't accidentally use the wrong one
    if os.path.exists("background_video.mp4"):
        try: os.remove("background_video.mp4")
        except: pass

    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"
    
    print(f"DEBUG: Searching Pexels for --> {query}")
    response = requests.get(url, headers=headers).json()
    
    # Check if a video was actually found
    if response.get('videos') and len(response['videos']) > 0:
        video_url = response['videos'][0]['video_files'][0]['link']
        print(f"✅ Found video for '{query}'. Downloading...")
    else:
        # FALLBACK: This prevents the 'FileNotFoundError' crash
        print(f"⚠️ No video found for '{query}'. Fetching fallback 'nature' video...")
        url = "https://api.pexels.com/videos/search?query=nature&per_page=1"
        response = requests.get(url, headers=headers).json()
        video_url = response['videos'][0]['video_files'][0]['link']

    # Final Download
    video_data = requests.get(video_url).content
    with open("background_video.mp4", 'wb') as f:
        f.write(video_data)
    print("✅ background_video.mp4 is ready.")

if __name__ == "__main__":
    user_topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "nature"
    download_video(user_topic)