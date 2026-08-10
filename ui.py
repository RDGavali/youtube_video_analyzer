import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="Youtube video Analyzer",
    layout="centered"
)

st.title("🎥 AI youtube Video Analyzer ")

@st.cache_resource  #decorator for cache
def get_agent():
    return build_youtube_agent()

agent=get_agent() 

#input box 
video_url=st.text_input("Enter YouTube Video Link")
button=st.button("Analyze Video") #True/false
if video_url and button:
    with st.spinner("Analyzing video..."):
        response=agent.run(
            f"Analyze this video:{video_url}"
        )
        st.markdown("Analyze Report of Video:")
        st.markdown(response.content)