import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from animals import animals, animal_images
from ai import simulate_battle
import time
import re
import random
 
BASE_DIR = Path(__file__).resolve().parent
logo_path = BASE_DIR / "beastgpt_logo.png"
 
st.set_page_config(
    page_title="BeastGPT – Animal Battle Simulator",
    page_icon="⚔️",
    layout="wide",
)

def load_css(filename: str = "styles.css") -> None:
    css_path = Path(__file__).resolve().parent / filename
    if not css_path.exists():
        st.error(f"Missing CSS file: {css_path}")
        st.stop()
    css = css_path.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
 
load_css("styles.css")
 
 # BEASTGPT HEADER
col_logo, col_title = st.columns([1, 8])
with col_logo:
    if BASE_DIR.joinpath("beastgpt_logo.png").exists():
        st.image(str(logo_path), width=90)
with col_title:
    st.markdown("""
        <h1 style='color:#cd4055;margin:0;padding:0;font-size:3.5rem;letter-spacing:2px;'>BeastGPT</h1>
        <p style='color:#e8e8e8;margin:0;padding:0;letter-spacing:2px;font-size:1rem;'>AI-POWERED ANIMAL BATTLE SIMULATOR</p>
    """, unsafe_allow_html=True)
 
# CHOOSE YOUR FIGHTERS
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("""
<h2 style='color:#ffd700;text-align:center;font-size:2rem;letter-spacing:5px;text-shadow:0 0 30px rgba(255,215,0,.5);margin-bottom:.3rem;'>
    CHOOSE YOUR FIGHTERS!
</h2>
""", unsafe_allow_html=True)
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
 
# DROPDOWN MENUS
if "sel1" not in st.session_state:
    st.session_state.sel1 = animals[0]
if "sel2" not in st.session_state:
    st.session_state.sel2 = animals[1]

def pick_random_animals() -> None:
    a1, a2 = random.sample(animals, 2)
    st.session_state.sel1 = a1
    st.session_state.sel2 = a2

col1, vs_col, col2 = st.columns([4, 2, 4])

with col1:
    animal1 = st.selectbox("🐾 Select Animal 1:", animals, key="sel1")
    img1 = animal_images.get(animal1)
    if img1:
        st.markdown(f"""
        <div style='display:flex;justify-content:center;'>
            <div class='beast-frame' style='max-width:450px;width:100%;'>
                <img src="{img1}" style="width:100%;height:250px;object-fit:cover;display:block;"/>
            </div>
        </div>
        <div class='fighter-name'>{animal1.upper()}</div>
        """, unsafe_allow_html=True)

with vs_col:
    st.markdown("<div style='height:120px'></div>", unsafe_allow_html=True)
    st.markdown("<div class='vs-badge'>VS</div>", unsafe_allow_html=True)

with col2:
    animal2 = st.selectbox("🐾 Select Animal 2:", animals, key="sel2")
    img2 = animal_images.get(animal2)
    if img2:
        st.markdown(f"""
        <div style='display:flex;justify-content:center;'>
            <div class='beast-frame' style='max-width:450px;width:100%;'>
                <img src="{img2}" style="width:100%;height:250px;object-fit:cover;display:block;"/>
            </div>
        </div>
        <div class='fighter-name'>{animal2.upper()}</div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

_, btn_col, _ = st.columns([2, 3, 2])
with btn_col:
    fight_btn = st.button("⚔️ BEGIN BATTLE!", use_container_width=True, type="primary")

_, rand_col, _ = st.columns([2, 3, 2])
with rand_col:
    st.button("🎲 SELECT RANDOM", use_container_width=True, type="secondary", on_click=pick_random_animals)
 
st.markdown("<br>", unsafe_allow_html=True)
 
if fight_btn:
    if animal1 == animal2:
        st.warning("⚠️ Pick two DIFFERENT animals for an epic battle!")
        st.stop()

    # Anchor near arena
    st.markdown("<div id='arena-anchor'></div>", unsafe_allow_html=True)

    arena = st.empty()
    has_scrolled = False

    for num in ["3", "2", "1", "FIGHT! ⚔️"]:
        with arena.container():
            st.markdown(f"<div class='countdown-digit'>{num}</div>", unsafe_allow_html=True)

        # Scroll down automatically when countdown starts
        if not has_scrolled and num == "3":
            components.html(
                """
                <script>
                  const el = window.parent.document.getElementById("arena-anchor");
                  if (el) {
                    el.scrollIntoView({ behavior: "smooth", block: "start" });
                  }
                </script>
                """,
                height=0,
            )
            has_scrolled = True

        time.sleep(1)

    arena.empty()
 
    with arena.container():
        st.markdown("""
        <div style='text-align:center;animation:fadeSlideUp .5s ease-out;'>
            <h2 style='font-family:Bebas Neue,cursive;font-size:2.5rem;color:#cd4055;letter-spacing:4px;'>
                🌪️ THE ARENA AWAKENS... 🌪️
            </h2>
        </div>""", unsafe_allow_html=True)
        a1col, mid_col, a2col = st.columns([4, 2, 4])
        with a1col:
            img1 = animal_images.get(animal1, "")
            st.markdown(f"""
            <div style='text-align:center;animation:fadeSlideUp .5s .1s ease-out both;'>
                <img src='{img1}' style='width:100%;max-width:300px;border-radius:10px;border:3px solid #cd4055;box-shadow:0 0 40px rgba(205,64,85,.7);'/>
                <div style='font-family:Bebas Neue,cursive;font-size:1.8rem;color:#ffd700;margin-top:.5rem;letter-spacing:3px;'>{animal1.upper()}</div>
            </div>""", unsafe_allow_html=True)
        with mid_col:
            st.markdown("""
            <div style='height:80px'></div>
            <div class='vs-badge' style='font-size:3.5rem;'>⚔️</div>""",
            unsafe_allow_html=True)
        with a2col:
            img2 = animal_images.get(animal2, "")
            st.markdown(f"""
            <div style='text-align:center;animation:fadeSlideUp .5s .2s ease-out both;'>
                <img src='{img2}' style='width:100%;max-width:300px;border-radius:10px;border:3px solid #cd4055;box-shadow:0 0 40px rgba(205,64,85,.7);'/>
                <div style='font-family:Bebas Neue,cursive;font-size:1.8rem;color:#ffd700;margin-top:.5rem;letter-spacing:3px;'>{animal2.upper()}</div>
            </div>""", unsafe_allow_html=True)
    time.sleep(2)
    arena.empty()
 
    battle_cries = [
        f"😤 {animal1} SHARPENS ITS CLAWS...",
        f"💨 {animal2} CHARGES FORWARD!",
        "⚡ THE GROUND TREMBLES...",
        "🔥 CALCULATING WHO SURVIVES...",
        "🧠 AI ANALYZING BEAST STATS...",
        "💥 EPIC COLLISION INCOMING!",
    ]
    for cry in battle_cries:
        with arena.container():
            st.markdown(f"""
            <div style='text-align:center;padding:2rem;font-family:Bebas Neue,cursive;font-size:2rem;color:#ff6b35;letter-spacing:3px;animation:fadeSlideUp .3s ease-out;'>
                {cry}
            </div>""", unsafe_allow_html=True)
        time.sleep(1)
    arena.empty()
 
    with st.spinner("⚡ THE AI ORACLE DECIDES THE VICTOR..."):
        result = simulate_battle(animal1, animal2)
 
    st.markdown("<div class='flash-overlay'></div>", unsafe_allow_html=True)
    time.sleep(0.1)
 
    winner_match = re.search(r'WHO WINS\?\s*\n\s*([A-Z][A-Z\s&]+)\n', result)
    winner = winner_match.group(1).strip() if winner_match else None
 
    sections = result.split('\n\n')
    story_paragraphs = []
    table_block = None
    in_stats = False
 
    for section in sections:
        stripped = section.strip()
        if '|Trait' in stripped or '|---' in stripped or (stripped.startswith('|') and '|' in stripped[1:]):
            table_block = stripped
            in_stats = True
        elif 'WHO WINS' in stripped or (winner and winner in stripped and len(stripped) < 60):
            continue
        elif 'BATTLE STATS' in stripped:
            in_stats = True
        elif not in_stats and stripped and stripped not in ['BATTLE STATS']:
            story_paragraphs.append(stripped)
 
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
 
    if winner:
        st.markdown(f"""
        <div style='text-align:center;padding:1.5rem 0;'>
            <div style='font-family:Bebas Neue,cursive;font-size:1.2rem;color:#e8e8e8;letter-spacing:5px;margin-bottom:.5rem;'>
                🏆 &nbsp; AND THE WINNER IS... &nbsp; 🏆
            </div>
            <div class='winner-banner'>
                <span class='crown'>👑</span> &nbsp; {winner} &nbsp; <span class='crown'>👑</span>
            </div>
        </div>""", unsafe_allow_html=True)

        # Auto-scroll to winner section
        components.html(
            """
            <script>
            const el = window.parent.document.getElementById("winner-section");
            if (el) {
                el.scrollIntoView({ behavior: "smooth", block: "start" });
            }
            </script>
            """,
            height=0,
        )

        time.sleep(0.4)
        st.balloons()
    else:
        st.markdown("""
        <div style='text-align:center;padding:1rem 0;'>
            <div class='winner-banner'>⚔️ EPIC BATTLE CONCLUDED! ⚔️</div>
        </div>""", unsafe_allow_html=True)
 
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
 
    story_html = "".join(
        f"<p style='margin-bottom:1.2rem;animation:fadeSlideUp .5s {i*0.15:.2f}s ease-out both;'>{p}</p>"
        for i, p in enumerate(story_paragraphs[:4]) if p
    )
    if story_html:
        st.markdown(f"""
        <div style='margin-bottom:2rem;'>
            <div class='section-head' style='color:#cd4055;border-color:#cd4055;'>
                📖 &nbsp; THE TALE OF BATTLE
            </div>
            <div class='story-card'>{story_html}</div>
        </div>""", unsafe_allow_html=True)
        time.sleep(0.3)
 
    if table_block:
        rows = [r for r in table_block.strip().split('\n') if r.strip().startswith('|')]
        header_row = rows[0] if rows else ""
        data_rows = [r for r in rows[2:] if r.strip() and '---' not in r]
 
        def parse_row(row):
            return [cell.strip() for cell in row.strip().strip('|').split('|')]
 
        headers = parse_row(header_row)
        th_html = "".join(f"<th>{h}</th>" for h in headers)
        td_rows_html = ""
        for dr in data_rows:
            cells = parse_row(dr)
            while len(cells) < len(headers):
                cells.append("")
            td_html = "".join(f"<td>{c}</td>" for c in cells[:len(headers)])
            td_rows_html += f"<tr>{td_html}</tr>"
 
        table_html = f"<table class='battle-table'><thead><tr>{th_html}</tr></thead><tbody>{td_rows_html}</tbody></table>"
 
        st.markdown(f"""
        <div style='margin-bottom:2rem;'>
            <div class='section-head' style='color:#4ecdc4;border-color:#4ecdc4;'>
                ⚔️ &nbsp; BATTLE STATS
            </div>
            {table_html}
        </div>""", unsafe_allow_html=True)
    else:
        stats_start = result.find('BATTLE STATS')
        if stats_start != -1:
            st.markdown(f"""
            <div class='section-head' style='color:#4ecdc4;border-color:#4ecdc4;'>
                ⚔️ &nbsp; BATTLE STATS
            </div>""", unsafe_allow_html=True)
            st.markdown(result[stats_start + len('BATTLE STATS'):])
 
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
 
    _, replay_col, _ = st.columns([2, 3, 2])
    with replay_col:
        if st.button("🔄 BATTLE AGAIN!", use_container_width=True, type="secondary"):
            st.rerun()
 
st.markdown("<br><br>", unsafe_allow_html=True)