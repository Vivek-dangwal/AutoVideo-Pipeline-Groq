from moviepy import VideoFileClip, AudioFileClip

def make_final_movie():
    print("Sticking the voice and video together...")
    
    # Load files
    video = VideoFileClip("background_video.mp4")
    audio = AudioFileClip("story_voice.mp3")
    
    # Join them (MoviePy v2.0+ syntax)
    final_video = video.with_audio(audio).with_duration(audio.duration)
    
    # Save (fps=24 is standard for YouTube)
    final_video.write_videofile("final_movie.mp4", fps=24)
    print("Video ready!")

if __name__ == "__main__":
    make_final_movie()