import streamlit as st
import yt_dlp
import os
from time import sleep

st.set_page_config(page_title="💀 GOD 2025", page_icon="🔥", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Rajdhani:wght@700&display=swap');
    .main {background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); background-attachment: fixed;}
    .title {font-family: 'Orbitron', sans-serif; text-align: center; font-size: 5rem; background: linear-gradient(45deg, #ff00ff, #00ffff, #ffff00, #ff0000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 50px rgba(255,0,255,1); animation: neon 1.5s infinite;}
    @keyframes neon {0%,100%{transform: scale(1);} 50%{transform: scale(1.15);}}
    .glow-btn {background: linear-gradient(45deg, #ff0080, #ff8c00, #ffff00)!important; border: none!important; padding: 25px 60px!important; border-radius: 60px!important; font-size: 2rem!important; box-shadow: 0 0 60px rgba(255,0,255,1)!important;}
    .glow-btn:hover {transform: translateY(-15px) scale(1.3); box-shadow: 0 0 100px rgba(255,0,255,1)!important;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">💀 GOD DOWNLOADER 2025</h1>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#00ffff; text-shadow: 0 0 30px #00ffff;'>🔥 Pornhub ⋅ xHamster ⋅ OnlyFans ⋅ YouTube ⋅ Insta ⋅ XVideos ⋅ SAB 8K Mein!</h2>", unsafe_allow_html=True)

url = st.text_input("🔗 Link daal bhai:", placeholder="https://pornhub.com/...", label_visibility="collapsed")
if url:
    try:
        with st.spinner("🚀 Scan kar raha..."):
            sleep(2)
            ydl = yt_dlp.YoutubeDL({'quiet': True})
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Video')[:100]
        st.success(f"**🔥 Mil gaya!** {title}")
        
        quality = st.selectbox("💎 Quality:", ["8K", "4K", "1080p", "720p", "480p", "Audio", "Photo"])
        
        if st.button("🚀 DOWNLOAD →", type="primary"):
            with st.spinner("🔥 Ho raha hai..."):
                fmt = 'best[height<=4320]' if '8K' in quality else 'best[height<=2160]' if '4K' in quality else 'best[height<=1080]' if '1080p' in quality else 'best'
                opts = {'format': fmt, 'outtmpl': '%(title)s.%(ext)s', 'merge_output_format': 'mp4'}
                yt_dlp.YoutubeDL(opts).download([url])
            st.balloons()
            st.success("**HO GAYA! FILE READY!**")
    except:
        st.error("Link galat!")

st.markdown("<p style='text-align:center; color:#ff00ff; font-size:2.5rem;'>Cyber Bhai 💀 | Free Forever</p>", unsafe_allow_html=True)
