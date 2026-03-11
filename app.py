import streamlit as st
from animals import animals, animal_images
from ai import simulate_battle
import os

BASE_DIR = os.path.dirname(__file__)
logo_path = os.path.join(BASE_DIR, "beastgpt_logo.png")

# BEASTGPT HEADER
col1, col2 = st.columns([1, 6])

with col1:
    st.image(logo_path, width=75)
with col2:
    st.markdown("<h1 style='color: #cd4055; margin: 0; padding: 0'>BeastGPT</h1>", unsafe_allow_html=True)
    st.markdown("<div style='margin: 0; padding: 0'>AI-Powered Animal Battle Simulator</div>", unsafe_allow_html=True)

st.markdown("<hr style='margin: 0; padding: 0; margin-top: 1em; margin-bottom: 2em'/>", unsafe_allow_html=True)

# DROPDOWN MENUS
st.markdown(
    "<h3 style='color: #cd4055; text-align: center; margin-bottom: 1em;'>CHOOSE YOUR FIGHTERS!</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:
    animal1 = st.selectbox("Select Animal 1:", animals)
    img1 = animal_images.get(animal1)
    if img1:
        st.markdown(
            f'<img src="{img1}" style="width: 100%; height: 250px; object-fit: cover; border: 3px solid #ff4b4b; border-radius: 8px;"/>',
            unsafe_allow_html=True
        )
with col2:
    animal2 = st.selectbox("Select Animal 2:", animals)
    img2 = animal_images.get(animal2)
    if img2:
        st.markdown(
            f'<img src="{img2}" style="width: 100%; height: 250px; object-fit: cover; border: 3px solid #ff4b4b; border-radius: 8px;"/>',
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

if st.button("⚔️ FIGHT!", help="Start battle!", use_container_width=True, type="primary"):
    with st.spinner("Simulating battle..."):
       result = simulate_battle(animal1, animal2)
       st.subheader("Battle Result")
       st.markdown(result)

st.button(
    "🎲 RANDOM", 
    help="Select animal fighters randomly",
    use_container_width=True, 
    type="secondary"
)
