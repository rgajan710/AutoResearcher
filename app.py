import streamlit as st
from crew_setup import crew

st.title("AutoResearcher: Multi-Agent Paper Generator")

if st.button("Start Agent Crew"):
    result = crew.kickoff()
    st.success("Crew Finished! View Result Below")
    st.text_area("Paper Draft", result, height=600)
