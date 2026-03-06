import streamlit as st
from openai import OpenAI
from animals import animals
import os


client = OpenAI (
    base_url="https://api.groq.com/openai/v1",
    api_key=st.secrets["GROQ_API_KEY"]
)

BASE_DIR = os.path.dirname(__file__)
logo_path = os.path.join(BASE_DIR, "beastgpt_logo.png")

# BEASTGPT HEADER
col1, col2 = st.columns([1, 4])

with col1:
    st.image(logo_path, width=100)

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
    animal1 = st.selectbox("Select Animal 1:", animals)
    st.markdown(
        '<img src="https://cdn1.parksmedia.wdprapps.disney.com/resize/mwImage/1/1600/900/75/dam/wdpro-assets/parks-and-tickets/attractions/animal-kingdom/disney-animals/disney-animals-asian-sumatran-tigers/disney-animals-asian-sumatran-tigers-00.jpg?1658996208764" style="width: 100%; height: 250px; object-fit: cover; border: 3px solid #ff4b4b; border-radius: 8px;"/>',
        unsafe_allow_html=True
    )
with col2:
    animal2 = st.selectbox("Select Animal 2:", animals)
    st.markdown(
        '<img src="https://i.natgeofe.com/k/3373927f-fa15-4c55-bf49-73f44073b768/burmese-python-tree_4x3.jpg" style="width: 100%; height: 250px; object-fit: cover; border: 3px solid #ff4b4b; border-radius: 8px;"/>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)


# ari lang modify ang prompt if ganahan mo naay usbon   

system_prompt = """
You are BeastGPT, an educational animal battle simulator for kids (ages 6–12).

Rules:
- Use simple words.
- Keep explanations short.
- Use ⭐ from 1 to 5 to rate traits.
- Output must be a MARKDOWN TABLE.

Output format:

WHO WINS?

<WINNER NAME IN ALL CAPS>

<One short sentence explaining why.>

BATTLE STATS

| Trait | Animal 1 | Animal 2 |
|------|------|------|
| Size | ⭐⭐⭐ | ⭐⭐⭐ |
| Strength | ⭐⭐⭐ | ⭐⭐⭐ |
| Speed | ⭐⭐⭐ | ⭐⭐⭐ |
| Bite Force | ⭐⭐⭐ | ⭐⭐⭐ |
| Habitat | short word | short word |

IMPORTANT:
Each trait MUST be on a new row in the table.
Do NOT place everything on one line.
"""
if st.button("⚔️ FIGHT!", use_container_width=True):

    with st.spinner("Simulating battle..."):

        user_prompt = f"""
        Simulate a battle between {animal1} and {animal2}.

        Compare them using:
        - sizze
        - strength
        - speed
        - bite force
        - habitat
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7
        )

        result = response.choices[0].message.content

        st.subheader("Battle Result")
        st.markdown(result)

st.button(
    "🎲 RANDOM", 
    help="Select animal fighters randomly",
    use_container_width=True, 
    type="secondary"
)
