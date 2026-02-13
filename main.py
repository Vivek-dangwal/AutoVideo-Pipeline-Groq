import subprocess
import os
import time

def run_pipeline():
    topic = input("🎬 What is the topic for your video? ").strip()
    
    if not topic:
        print("Please enter a valid topic!")
        return

    # --- CLEANUP: Kill old files so they don't 'ghost' into the new video ---
    old_files = ["background_video.mp4", "final_movie.mp4", "story_voice.mp3", "current_script.txt"]
    for f in old_files:
        if os.path.exists(f):
            try: os.remove(f)
            except: pass

    print(f"\n🚀 Starting AI Video Pipeline for: {topic}...")
    
    # Passing 'topic' as a direct argument to each script
    subprocess.run(["python", "script_writer.py", topic])
    subprocess.run(["python", "2_voice.py"])
    
    print(f"--- FETCHING VISUALS FOR: {topic} ---")
    subprocess.run(["python", "3_video_finder.py", topic])
    
    subprocess.run(["python", "4_final_video.py"])
    
    print("\n✅ MISSION ACCOMPLISHED!")
    time.sleep(2)
    
    if os.path.exists("final_movie.mp4"):
        os.startfile("final_movie.mp4")

if __name__ == "__main__":
    run_pipeline()