import streamlit as st
import os
import time
import subprocess
import sys

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cinematiq AI | Vivek Dangwal", page_icon="🪄", layout="wide")

# --- MAGICAL STYLING & PARTICLES ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
    }
    .app-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 55px !important;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #00f2fe, #4facfe, #706fd3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        filter: drop-shadow(0 0 15px rgba(0, 242, 254, 0.4));
    }
    .dev-name {
        text-align: center;
        color: #706fd3;
        font-size: 18px;
        letter-spacing: 4px;
        margin-top: -10px;
        margin-bottom: 40px;
    }
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px) !important;
        border: 2px solid rgba(0, 242, 254, 0.3) !important;
        border-radius: 50px !important;
        color: white !important;
        padding: 20px !important;
        text-align: center !important;
    }
    .stButton>button {
        display: block;
        margin: 0 auto;
        width: 350px;
        background: linear-gradient(45deg, #706fd3, #4facfe) !important;
        border: none !important;
        border-radius: 50px !important;
        color: white !important;
        font-weight: bold !important;
        box-shadow: 0 10px 30px rgba(112, 111, 211, 0.4);
    }
    .metadata-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #4facfe;
        color: #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="app-title">CINEMATIQ AI</p>', unsafe_allow_html=True)
st.markdown('<p class="dev-name">DEVELOPED BY VIVEK DANGWAL</p>', unsafe_allow_html=True)

# --- MAIN INPUT ---
left, mid, right = st.columns([1, 2, 1])
with mid:
    topic = st.text_input("", placeholder="Enter your topic (e.g., Space Exploration)...", label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button("🪄 EXECUTE ONE-TRIGGER PIPELINE")

# --- EXECUTION LOGIC ---
if generate_btn:
    if topic:
        # CLEANUP OLD ASSETS
        files_to_kill = ["background_video.mp4", "final_movie.mp4", "story_voice.mp3", "seo_metadata.txt"]
        for f in files_to_kill:
            if os.path.exists(f): os.remove(f)

        with st.status("🔮 Orchestrating Pipeline...", expanded=True) as status:
            st.write("📝 Step 1: Generating Script (Groq Llama 3.3)...")
            subprocess.run(["python", "script_writer.py", topic])
            
            st.write("🎙️ Step 2: Synthesizing Voice (Edge-TTS)...")
            subprocess.run(["python", "2_voice.py"])
            
            st.write("🎬 Step 3: Fetching Visuals (Pexels API)...")
            subprocess.run(["python", "3_video_finder.py", topic])
            
            st.write("🎞️ Step 4: Assembling Video (MoviePy)...")
            subprocess.run(["python", "4_final_video.py"])

            st.write("📊 Bonus: Generating SEO Metadata...")
            # We add a small local SEO generation here
            title = f"The Incredible Journey of {topic.title()}"
            description = f"Discover the story of {topic}. Automated by Cinematiq AI.\n#AI #{topic.replace(' ','')}"
            tags = f"{topic}, AI Video, Automation, Vivek Dangwal"
            with open("seo_metadata.txt", "w") as f:
                f.write(f"TITLE: {title}\n\nDESC: {description}\n\nTAGS: {tags}")
            
            status.update(label="✨ MISSION ACCOMPLISHED!", state="complete")

        # --- RESULTS DISPLAY ---
        if os.path.exists("final_movie.mp4"):
            st.snow()
            st.markdown("### 🍿 Final AI Masterpiece")
            st.video("final_movie.mp4")
            
            # SHOW SEO METADATA
            st.markdown("### 📊 YouTube SEO Metadata (Bonus)")
            with st.container():
                st.markdown(f"""
                <div class="metadata-box">
                    <b>Title:</b> {title}<br><br>
                    <b>Description:</b><br>{description}<br><br>
                    <b>Tags:</b> {tags}
                </div>
                """, unsafe_allow_html=True)
            
            # DOWNLOAD BUTTONS
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Video", open("final_movie.mp4", "rb"), "video.mp4")
            with c2:
                st.download_button("📥 Download SEO Tags", open("seo_metadata.txt", "r"), "seo.txt")
        else:
            st.error("Error in assembly. Check terminal for logs.")
    else:
        st.warning("The pipeline requires a topic to begin.")

# --- FOOTER ---
st.markdown("<br><hr><center>B.Tech CSE Capstone | Submission for ASTRONOVA SYNERGIES</center>", unsafe_allow_html=True)