import streamlit as st
from animals import animals

# BEASTGPT HEADER
col1, col2 = st.columns([1, 4])

with col1:
    st.image("beastgpt_logo.png", width=100)
with col2:
    st.title("BeastGPT")
    st.markdown("<div style='color: gray;'>AI-Powered Animal Battle Simulator</div>", unsafe_allow_html=True)

st.divider()

# DROPDOWN MENUS
st.markdown(
    "<h3 style='text-align: center; margin-bottom: 1em;'>CHOOSE YOUR FIGHTERS!</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.selectbox("Select Animal 1:", animals)
    st.markdown(
        '<img src="https://cdn1.parksmedia.wdprapps.disney.com/resize/mwImage/1/1600/900/75/dam/wdpro-assets/parks-and-tickets/attractions/animal-kingdom/disney-animals/disney-animals-asian-sumatran-tigers/disney-animals-asian-sumatran-tigers-00.jpg?1658996208764" style="width: 100%; height: 250px; object-fit: cover; border: 3px solid #ff4b4b; border-radius: 8px;"/>',
        unsafe_allow_html=True
    )
with col2:
    st.selectbox("Select Animal 2:", animals)
    st.markdown(
        '<img src="https://i.natgeofe.com/k/3373927f-fa15-4c55-bf49-73f44073b768/burmese-python-tree_4x3.jpg" style="width: 100%; height: 250px; object-fit: cover; border: 3px solid #ff4b4b; border-radius: 8px;"/>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

st.button(
    "⚔️ FIGHT!", 
    help="Click to start battle!",
    use_container_width=True, 
    type="primary"
)

st.button(
    "🎲 RANDOM", 
    help="Select animal fighters randomly",
    use_container_width=True, 
    type="secondary"
)
