import streamlit as st
from animals import animals, animal_images
from ai import simulate_battle
import os
import time
import re
import random
 
BASE_DIR = os.path.dirname(__file__)
logo_path = os.path.join(BASE_DIR, "beastgpt_logo.png")
 
st.set_page_config(
    page_title="BeastGPT – Animal Battle Simulator",
    page_icon="⚔️",
    layout="wide",
)
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Bangers&family=Nunito:wght@400;700;900&display=swap%27);
 
:root {
    --blood:  #cd4055;
    --gold:   #ffd700;
    --ember:  #ff6b35;
    --dark:   #0d0d0d;
    --mid:    #1a1a2e;
    --light:  #e8e8e8;
    --teal:   #4ecdc4;
}
 
.stApp {
    background: radial-gradient(ellipse at top, #1a0a0a 0%, #0d0d0d 60%);
    background-attachment: fixed;
}
 
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        radial-gradient(1px 1px at 10% 20%, rgba(255,215,0,.35) 0%, transparent 100%),
        radial-gradient(1px 1px at 80% 10%, rgba(205,64,85,.3) 0%, transparent 100%),
        radial-gradient(1px 1px at 50% 70%, rgba(78,205,196,.25) 0%, transparent 100%),
        radial-gradient(1px 1px at 30% 90%, rgba(255,107,53,.2) 0%, transparent 100%);
    background-size: 200px 200px, 300px 300px, 250px 250px, 180px 180px;
    animation: drift 20s linear infinite;
    pointer-events: none;
    z-index: 0;
}
 
@keyframes drift {
    0%{ background-position: 0 0, 0 0, 0 0, 0 0; }
    100%{ background-position: 200px 200px, -300px 300px, 250px -250px, -180px 180px; }
}
 
h1,h2,h3{font-family:'Bebas Neue',sans-serif !important;letter-spacing:2px;}
body,p,span,div{font-family:'Nunito',sans-serif;}
 
.fighter-name{font-family:'Bebas Neue',cursive;font-size:2rem;color:var(--gold);text-align:center;letter-spacing:3px;margin-top:.5rem;text-shadow:0 0 20px rgba(255,215,0,.6);}
.vs-badge{font-family:'Bangers',cursive;font-size:5rem;color:var(--blood);text-align:center;line-height:1;text-shadow:4px 4px 0 #000,0 0 40px rgba(205,64,85,.8);animation:pulse-vs 1.5s ease-in-out infinite;}
@keyframes pulse-vs{0%,100%{transform:scale(1);text-shadow:4px 4px 0 #000,0 0 40px rgba(205,64,85,.8);}50%{transform:scale(1.12);text-shadow:4px 4px 0 #000,0 0 70px rgba(205,64,85,1);}}
 
.beast-frame{position:relative;border-radius:12px;overflow:hidden;border:3px solid var(--blood);box-shadow:0 0 30px rgba(205,64,85,.5),inset 0 0 30px rgba(0,0,0,.4);transition:transform .3s,box-shadow .3s;}
.beast-frame:hover{transform:scale(1.03) rotate(-1deg);box-shadow:0 0 60px rgba(205,64,85,.9);}
 
.stButton>button[kind="primary"]{background:linear-gradient(135deg,#cd4055,#8b0000) !important;color:white !important;font-family:'Bebas Neue',sans-serif !important;font-size:1.8rem !important;letter-spacing:4px !important;border:2px solid var(--gold) !important;border-radius:8px !important;padding:.6rem 2rem !important;box-shadow:0 0 30px rgba(205,64,85,.6) !important;transition:all .25s !important;animation:shimmer-btn 3s ease-in-out infinite;}
.stButton>button[kind="primary"]:hover{transform:scale(1.07) !important;box-shadow:0 0 60px rgba(255,215,0,.7) !important;}
@keyframes shimmer-btn{0%,100%{box-shadow:0 0 30px rgba(205,64,85,.6);}50%{box-shadow:0 0 50px rgba(255,215,0,.5);}}
 
.divider{height:2px;background:linear-gradient(to right,transparent,var(--blood),var(--gold),var(--blood),transparent);margin:1.5rem 0;border:none;}
.section-head{font-family:'Bebas Neue',cursive;font-size:2rem;letter-spacing:3px;padding-bottom:.3rem;border-bottom:2px solid;margin-bottom:1rem;}
.story-card{background:linear-gradient(135deg,rgba(26,10,10,.95),rgba(13,13,13,.95));border:1px solid rgba(205,64,85,.5);border-radius:12px;padding:1.8rem 2rem;line-height:1.9;font-size:1.08rem;color:var(--light);box-shadow:0 0 40px rgba(205,64,85,.15);animation:fadeSlideUp .6s ease-out both;}
 
.winner-banner{font-family:'Bangers',cursive;font-size:3.5rem;text-align:center;color:var(--gold);text-shadow:3px 3px 0 #000,0 0 60px rgba(255,215,0,.9);animation:winnerPop .7s cubic-bezier(.175,.885,.32,1.275) both;letter-spacing:4px;}
@keyframes winnerPop{0%{transform:scale(0) rotate(-10deg);opacity:0;}100%{transform:scale(1) rotate(0deg);opacity:1;}}
.crown{display:inline-block;animation:crownSpin 2s ease-in-out infinite;}
@keyframes crownSpin{0%,100%{transform:rotate(-8deg) scale(1);}50%{transform:rotate(8deg) scale(1.2);}}
@keyframes fadeSlideUp{from{opacity:0;transform:translateY(30px);}to{opacity:1;transform:translateY(0);}}
 
.battle-table{width:100%;border-collapse:collapse;animation:fadeSlideUp .8s ease-out both;font-size:.95rem;}
.battle-table th{font-family:'Bebas Neue',cursive;font-size:1.1rem;letter-spacing:2px;background:rgba(205,64,85,.3);color:var(--gold);padding:.7rem 1rem;text-align:left;border-bottom:2px solid var(--blood);}
.battle-table td{padding:.65rem 1rem;border-bottom:1px solid rgba(255,255,255,.08);color:var(--light);vertical-align:top;}
.battle-table tr:nth-child(even) td{background:rgba(255,255,255,.03);}
.battle-table tr:hover td{background:rgba(205,64,85,.1);transition:background .2s;}
.battle-table td:first-child{font-weight:700;color:var(--teal);white-space:nowrap;}
 
.countdown-digit{font-family:'Bebas Neue',cursive;font-size:8rem;color:var(--blood);text-align:center;text-shadow:0 0 60px rgba(205,64,85,1);animation:countPop .4s cubic-bezier(.175,.885,.32,1.275) both;}
@keyframes countPop{from{transform:scale(2);opacity:0;}to{transform:scale(1);opacity:1;}}
 
.flash-overlay{position:fixed;inset:0;background:#fff;opacity:0;pointer-events:none;animation:flashOnce .3s ease-out;z-index:9999;}
@keyframes flashOnce{0%{opacity:.8;}100%{opacity:0;}}
 
.stButton>button[kind="secondary"]{background:transparent !important;border:2px solid var(--gold) !important;color:var(--gold) !important;font-family:'Bebas Neue',sans-serif !important;font-size:1.2rem !important;letter-spacing:3px !important;border-radius:8px !important;transition:all .25s !important;}
.stButton>button[kind="secondary"]:hover{background:rgba(255,215,0,.1) !important;box-shadow:0 0 30px rgba(255,215,0,.4) !important;}
 
.stSelectbox label{color:var(--gold) !important;font-family:'Bebas Neue',cursive !important;font-size:1.1rem !important;letter-spacing:2px !important;}
.stSpinner>div{border-color:var(--blood) transparent transparent transparent !important;}
 
#MainMenu,footer{visibility:hidden;}
header{background:transparent !important;}
</style>
""", unsafe_allow_html=True)
 
col_logo, col_title = st.columns([1, 8])
with col_logo:
    if os.path.exists(logo_path):
        st.image(logo_path, width=80)
with col_title:
    st.markdown("""
        <h1 style='color:#cd4055;margin:0;padding:0;font-size:3.5rem;letter-spacing:4px;'>BeastGPT</h1>
        <p style='color:#e8e8e8;margin:0;padding:0;letter-spacing:2px;font-size:1rem;'>
            ⚔️ &nbsp; AI-POWERED ANIMAL BATTLE SIMULATOR &nbsp; ⚔️
        </p>
    """, unsafe_allow_html=True)
 
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
 
st.markdown("""
<h2 style='color:#ffd700;text-align:center;font-size:2.8rem;letter-spacing:5px;text-shadow:0 0 30px rgba(255,215,0,.5);margin-bottom:.3rem;'>
    CHOOSE YOUR FIGHTERS!
</h2>
""", unsafe_allow_html=True)
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
 
if "random_trigger" not in st.session_state:
    st.session_state.random_trigger = False
if "random_a1" not in st.session_state:
    st.session_state.random_a1 = animals[0]
if "random_a2" not in st.session_state:
    st.session_state.random_a2 = animals[1]
 
col1, vs_col, col2 = st.columns([5, 1, 5])
 
with col1:
    idx1 = animals.index(st.session_state.random_a1) if st.session_state.random_trigger else 0
    animal1 = st.selectbox("🐾 Select Animal 1:", animals, index=idx1, key="sel1")
    img1 = animal_images.get(animal1)
    if img1:
        st.markdown(f"""
        <div style='display:flex;justify-content:center;'>
            <div class='beast-frame' style='max-width:280px;width:100%;'>
                <img src="{img1}" style="width:100%;height:200px;object-fit:cover;display:block;"/>
            </div>
        </div>
        <div class='fighter-name'>{animal1.upper()}</div>
        """, unsafe_allow_html=True)
 
with vs_col:
    st.markdown("<div style='height:120px'></div>", unsafe_allow_html=True)
    st.markdown("<div class='vs-badge'>VS</div>", unsafe_allow_html=True)
 
with col2:
    idx2 = animals.index(st.session_state.random_a2) if st.session_state.random_trigger else 1
    animal2 = st.selectbox("🐾 Select Animal 2:", animals, index=idx2, key="sel2")
    img2 = animal_images.get(animal2)
    if img2:
        st.markdown(f"""
        <div style='display:flex;justify-content:center;'>
            <div class='beast-frame' style='max-width:280px;width:100%;'>
                <img src="{img2}" style="width:100%;height:200px;object-fit:cover;display:block;"/>
            </div>
        </div>
        <div class='fighter-name'>{animal2.upper()}</div>
        """, unsafe_allow_html=True)
 
st.session_state.random_trigger = False
 
st.markdown("<br>", unsafe_allow_html=True)
 
_, btn_col, _ = st.columns([2, 3, 2])
with btn_col:
    fight_btn = st.button("⚔️  L E T ' S  F I G H T !", use_container_width=True, type="primary")
 
st.markdown("<br>", unsafe_allow_html=True)
 
_, rand_col, _ = st.columns([2, 3, 2])
with rand_col:
    if st.button("🎲  RANDOM BATTLE", use_container_width=True, type="secondary"):
        pool = animals.copy()
        a1 = random.choice(pool)
        pool.remove(a1)
        a2 = random.choice(pool)
        st.session_state.random_a1 = a1
        st.session_state.random_a2 = a2
        st.session_state.random_trigger = True
        st.rerun()
 
st.markdown("<br>", unsafe_allow_html=True)
 
if fight_btn:
    if animal1 == animal2:
        st.warning("⚠️ Pick two DIFFERENT animals for an epic battle!")
        st.stop()
 
    arena = st.empty()
    for num in ["3", "2", "1", "FIGHT! ⚔️"]:
        with arena.container():
            st.markdown(f"<div class='countdown-digit'>{num}</div>", unsafe_allow_html=True)
        time.sleep(0.7)
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
                <img src='{img1}' style='width:100%;max-width:220px;border-radius:10px;border:3px solid #cd4055;box-shadow:0 0 40px rgba(205,64,85,.7);'/>
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
                <img src='{img2}' style='width:100%;max-width:220px;border-radius:10px;border:3px solid #cd4055;box-shadow:0 0 40px rgba(205,64,85,.7);'/>
                <div style='font-family:Bebas Neue,cursive;font-size:1.8rem;color:#ffd700;margin-top:.5rem;letter-spacing:3px;'>{animal2.upper()}</div>
            </div>""", unsafe_allow_html=True)
    time.sleep(1.8)
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
        time.sleep(0.6)
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
        if st.button("🔄  BATTLE AGAIN!", use_container_width=True, type="secondary"):
            st.rerun()
 
st.markdown("<br><br>", unsafe_allow_html=True)
 
 
# sdadsa