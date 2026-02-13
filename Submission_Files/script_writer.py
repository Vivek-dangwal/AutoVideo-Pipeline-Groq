import sys
from groq import Groq

# PASTE YOUR KEY HERE
client = Groq(api_key="PASTE_YOUR_GROQ_API_KEY_HERE")

def get_script(topic):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Write a 3-sentence fun story for a video. No emojis."},
            {"role": "user", "content": topic}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    # Check if a topic was passed from main.py
    if len(sys.argv) > 1:
        user_topic = " ".join(sys.argv[1:])
        script = get_script(user_topic)
        # We save the script to a text file so Step 2 can read it
        with open("current_script.txt", "w") as f:
            f.write(script)
        print(f"Script saved: {script}")
    else:
        print("Error: No topic provided.")