import asyncio
import edge_tts

async def make_voice():
    # Read the script we just wrote
    with open("current_script.txt", "r") as f:
        story_text = f.read()
    
    communicate = edge_tts.Communicate(story_text, "en-US-ChristopherNeural")
    await communicate.save("story_voice.mp3")
    print("Audio 'story_voice.mp3' is ready!")

if __name__ == "__main__":
    asyncio.run(make_voice())