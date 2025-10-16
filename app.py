import streamlit as st
from time import sleep

def show_loading_overlay():
    overlay = st.empty()
    overlay.markdown(
        """
        <style>
          .chempop-loader { position: fixed; inset: 0; z-index: 9999;
            display: grid; place-items: center;
            background: linear-gradient(180deg, #FFF1F5 0%, #FFFFFF 60%); }
          .flask-wrap { position: relative; width: 240px; height: 260px; }
          .flask { width: 240px; filter: drop-shadow(0 8px 20px rgba(236,72,153,0.25)); }
          .liquid { fill: url(#liquidGradient); }
          .bubble { animation: rise 3s infinite ease-in; opacity: 0.9; }
          .bubble:nth-child(1){ animation-delay: 0.0s }
          .bubble:nth-child(2){ animation-delay: 0.6s }
          .bubble:nth-child(3){ animation-delay: 1.2s }
          .bubble:nth-child(4){ animation-delay: 1.8s }
          .bubble:nth-child(5){ animation-delay: 2.4s }
          @keyframes rise {
            0%{ transform: translateY(0) scale(1); opacity: 0; }
            10%{ opacity: 1; }
            70%{ transform: translateY(-80px) scale(1.05); opacity: 0.9; }
            100%{ transform: translateY(-110px) scale(0.9); opacity: 0; }
          }
          .caption { margin-top: 16px; font: 600 14px/1.4 ui-sans-serif, system-ui;
            color: #334155; text-align: center; }
        </style>
        <div class="chempop-loader">
          <div class="flask-wrap">
            <svg class="flask" viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <linearGradient id="liquidGradient" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%"  stop-color="#EC4899"/>
                  <stop offset="50%" stop-color="#D4AF37"/>
                  <stop offset="100%" stop-color="#14B8A6"/>
                </linearGradient>
              </defs>
              <rect x="88" y="10" width="24" height="40" rx="6" fill="#0F172A"/>
              <path d="M70 60 L130 60 L120 90 L80 90 Z" fill="#0F172A"/>
              <path d="M50 90 C40 120, 40 160, 100 190 C160 160, 160 120, 150 90 Z"
                    fill="none" stroke="#0F172A" stroke-width="5" />
              <path class="liquid"
                    d="M55 140 C60 155, 85 170, 100 175 C115 170, 140 155, 145 140
                       C145 150, 145 160, 100 180 C55 160, 55 150, 55 140 Z" opacity="0.92"/>
              <circle class="bubble" cx="95" cy="150" r="6" fill="#ffffff" />
              <circle class="bubble" cx="115" cy="155" r="5" fill="#ffffff" />
              <circle class="bubble" cx="105" cy="160" r="4" fill="#ffffff" />
              <circle class="bubble" cx="90"  cy="165" r="3" fill="#ffffff" />
              <circle class="bubble" cx="120" cy="162" r="4" fill="#ffffff" />
            </svg>
            <div class="caption">Your CHEMPOP lab is baking…</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return overlay

_loading_overlay = show_loading_overlay()
# keep the loader on screen briefly, then hide it
sleep(2)                 # you can change 2 → 3 or 1 if you like
_loading_overlay.empty()
import streamlit as st
from time import sleep

def show_loading_overlay():
    overlay = st.empty()
    overlay.markdown(
        """
        <style>
          .chempop-loader { position: fixed; inset: 0; z-index: 9999;
            display: grid; place-items: center;
            background: linear-gradient(180deg, #FFF1F5 0%, #FFFFFF 60%); }
          .flask-wrap { position: relative; width: 240px; height: 260px; }
          .flask { width: 240px; filter: drop-shadow(0 8px 20px rgba(236,72,153,0.25)); }
          .liquid { fill: url(#liquidGradient); }
          .bubble { animation: rise 3s infinite ease-in; opacity: 0.9; }
          .bubble:nth-child(1){ animation-delay: 0.0s }
          .bubble:nth-child(2){ animation-delay: 0.6s }
          .bubble:nth-child(3){ animation-delay: 1.2s }
          .bubble:nth-child(4){ animation-delay: 1.8s }
          .bubble:nth-child(5){ animation-delay: 2.4s }
          @keyframes rise {
            0%{ transform: translateY(0) scale(1); opacity: 0; }
            10%{ opacity: 1; }
            70%{ transform: translateY(-80px) scale(1.05); opacity: 0.9; }
            100%{ transform: translateY(-110px) scale(0.9); opacity: 0; }
          }
          .caption { margin-top: 16px; font: 600 14px/1.4 ui-sans-serif, system-ui;
            color: #334155; text-align: center; }
        </style>
        <div class="chempop-loader">
          <div class="flask-wrap">
            <svg class="flask" viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <linearGradient id="liquidGradient" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%"  stop-color="#EC4899"/>
                  <stop offset="50%" stop-color="#D4AF37"/>
                  <stop offset="100%" stop-color="#14B8A6"/>
                </linearGradient>
              </defs>
              <rect x="88" y="10" width="24" height="40" rx="6" fill="#0F172A"/>
              <path d="M70 60 L130 60 L120 90 L80 90 Z" fill="#0F172A"/>
              <path d="M50 90 C40 120, 40 160, 100 190 C160 160, 160 120, 150 90 Z"
                    fill="none" stroke="#0F172A" stroke-width="5" />
              <path class="liquid"
                    d="M55 140 C60 155, 85 170, 100 175 C115 170, 140 155, 145 140
                       C145 150, 145 160, 100 180 C55 160, 55 150, 55 140 Z" opacity="0.92"/>
              <circle class="bubble" cx="95" cy="150" r="6" fill="#ffffff" />
              <circle class="bubble" cx="115" cy="155" r="5" fill="#ffffff" />
              <circle class="bubble" cx="105" cy="160" r="4" fill="#ffffff" />
              <circle class="bubble" cx="90"  cy="165" r="3" fill="#ffffff" />
              <circle class="bubble" cx="120" cy="162" r="4" fill="#ffffff" />
            </svg>
            <div class="caption">Your CHEMPOP lab is baking…</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return overlay

# show overlay immediately
_loading_overlay = show_loading_overlay()
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json, time
from pathlib import Path

st.set_page_config(page_title="CHEMPOP Virtual Lab", page_icon="🧪", layout="wide")

# ---------- Styles ----------
st.markdown("""
<style>
.big-title{font-size:28px;font-weight:800;margin-bottom:4px}
.subtitle{color:#476;margin-top:-6px;margin-bottom:14px}
.steel{background:linear-gradient(180deg,#f2f4f7 0%,#d9dee3 100%);border-radius:16px;padding:14px 16px;box-shadow:0 4px 20px rgba(0,0,0,.08)}
.pill{display:inline-block;padding:6px 12px;border-radius:999px;background:#eef7ff;border:1px solid #cfe6ff;font-size:12px;margin-right:8px}
.smallnote{color:#667}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">CHEMPOP Virtual Lab</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Premium interactive chemistry simulations & dynamic quizzes</div>', unsafe_allow_html=True)

tabs = st.tabs(["Distillation","Single-Tube","6-Tube Reactivity","Heating Curve","Electrolysis","Periodic Table","Quizzes"])

# ---------- Session state helpers ----------
if "distillate_ml" not in st.session_state: st.session_state.distillate_ml = 0.0
if "last_tick" not in st.session_state: st.session_state.last_tick = time.time()
if "tube_level" not in st.session_state: st.session_state.tube_level = 0.0  # 0..1

# ---------- Distillation ----------
with tabs[0]:
    colL, colR = st.columns([1.2,1])
    with colL:
        st.image(str(Path("assets/distillation.svg")), use_column_width=True, caption="Slightly tilted condenser, three‑way adaptor, Erlenmeyer receiver")
        st.markdown('<div class="steel"><span class="pill">Cooling water</span><span class="pill">Thermometer</span><span class="pill">Three‑way adaptor</span></div>', unsafe_allow_html=True)
    with colR:
        st.markdown("#### Controls & Readouts")
        coolant = st.radio("Condenser water", ["Cold","Warm"], horizontal=True)
        heat = st.slider("Heating mantle power (%)", 0, 100, 40)
        running = st.toggle("Start / Stop distillation", value=False)
        # compute drop rate (drops/min) and accumulation (assume 0.05 mL per drop)
        drop_rate = 0
        if running and heat>10:
            base = np.interp(heat,[10,100],[0.5,12])
            if coolant=="Cold": base *= 1.0
            else: base *= 0.8
            drop_rate = int(base)
            # accumulate volume since last tick
            now = time.time()
            dt_min = (now - st.session_state.last_tick)/60.0
            st.session_state.last_tick = now
            st.session_state.distillate_ml += drop_rate * dt_min * 0.05
        st.metric("Drop rate (drops/min)", drop_rate)
        st.progress(min(1.0, st.session_state.distillate_ml/50.0), text=f"Distillate collected: {st.session_state.distillate_ml:.1f} mL (approx)")
        if st.button("Reset receiver"):
            st.session_state.distillate_ml = 0.0
        st.caption("Note: visualization approximates droplet formation & collection volume.")

# ---------- Single-Tube Reactions ----------
with tabs[1]:
    left, right = st.columns([1.05,1])
    with left:
        st.markdown("#### Curved Test Tube on Metallic Bench")
        element = st.selectbox("Element (powder / small ribbon)", ["Magnesium (sanded)","Aluminum (sanded)","Zinc","Iron","Copper"])
        temp_sel = st.radio("Water temperature", ["Cold water","Warm water"], horizontal=True)
        indicator = st.radio("Indicator", ["None","Universal indicator","Phenolphthalein"], horizontal=True)
        c1,c2,c3 = st.columns(3)
        with c1:
            drop = st.button("Drop solid")
        with c2:
            add_water = st.button("Add water")
        with c3:
            clear = st.button("Clear tube")
        if clear:
            st.session_state.tube_level = 0.0
        # Waterline animation
        if add_water:
            st.session_state.tube_level = min(1.0, st.session_state.tube_level + 0.25)
        st.image(str(Path("assets/distillation.svg")), caption="Bench aesthetic (left shows tube & burner)", use_column_width=True)
        st.progress(st.session_state.tube_level, text=f"Water level: {int(st.session_state.tube_level*100)}%")
    with right:
        st.markdown("#### Visuals & Explanation")
        warm = (temp_sel=="Warm water")
        bubbles = 0  # 0 none, 1 slow, 2 moderate, 3 vigorous
        eqn = "-"
        if drop and add_water:
            if element=="Magnesium (sanded)":
                bubbles = 2 if warm else 1
                eqn = "Mg(s) + 2 H₂O(l) → Mg(OH)₂(aq) + H₂(g)"
            elif element=="Aluminum (sanded)":
                bubbles = 1 if warm else 0
                eqn = "2 Al(s) + 6 H₂O(l) → 2 Al(OH)₃(aq) + 3 H₂(g)"
            elif element=="Zinc":
                bubbles = 1 if warm else 0
                eqn = "Zn(s) + 2 H₂O(l) → Zn(OH)₂(aq) + H₂(g)"
            elif element=="Iron":
                bubbles = 0
                eqn = "No reaction with pure water at room temperature."
            else:
                bubbles = 0
                eqn = "No reaction."
        # indicator color
        color = "clear"
        if indicator=="Universal indicator" and bubbles>0: color="green→blue (alkaline)"
        if indicator=="Phenolphthalein" and bubbles>0: color="pink near metal surface"
        # flame test (loop)
        flame = st.toggle("Move loop to flame")
        flame_note = ""
        if flame:
            flame_colors = {
                "Magnesium (sanded)": "Intense white light",
                "Aluminum (sanded)": "Silvery sparks (no persistent color)",
                "Zinc": "Weak bluish edge (impurities)",
                "Iron": "Orange/gold sparks",
                "Copper": "Blue‑green flame"
            }
            flame_note = flame_colors.get(element,"")
        hydrogen_test = st.toggle("Hydrogen pop test (if bubbles present)")
        if hydrogen_test and bubbles>0:
            st.success("✅ Small 'pop' would be heard: hydrogen present.")
        vigor_text = ["none","slow","moderate","vigorous"][bubbles]
        st.write(f"**Effervescence:** {vigor_text}")
        st.write(f"**Indicator color:** {color}")
        st.write(f"**Balanced equation:** {eqn}")
        st.write(f"**Flame test:** {flame_note}")

# ---------- 6-Tube Reactivity ----------
with tabs[2]:
    st.markdown("#### Displacement of Copper (visual color change & solid formation)")
    sol = st.radio("Solution", ["CuSO₄(aq) — blue","Dil. HCl(aq)"], horizontal=True)
    metals = ["Mg","Al (sanded)","Zn","Fe","Sn","Cu"]
    chosen = st.multiselect("Add metals (one per tube)", metals, default=metals)
    cols = st.columns(6)
    vigor_map = {"Mg":3,"Al (sanded)":1,"Zn":2,"Fe":2,"Sn":1,"Cu":0}
    for i, m in enumerate(chosen[:6]):
        with cols[i]:
            vigor = ["none","slow","moderate","vigorous"][vigor_map[m]]
            if sol.startswith("CuSO"):
                after = "colorless" if m!="Cu" else "blue"
                solid = "brown Cu(s) coat" if m!="Cu" else "—"
                st.markdown(f"**Tube {i+1}: {m}**")
                st.caption(f"Blue → {after}; {solid}. Effervescence: {vigor}.")
            else:
                st.markdown(f"**Tube {i+1}: {m}**")
                st.caption(f"In HCl: H₂ release depends on reactivity — {vigor}.")

# ---------- Heating Curve ----------
with tabs[3]:
    st.markdown("#### Heating Curve with Start/Stop (5‑min sampling)")
    st.image(str(Path("assets/heating_curve.svg")), use_column_width=True)
    cA, cB = st.columns([1,1])
    with cA:
        running = st.toggle("Start/Stop", value=False)
        base_T = st.slider("Initial temperature (°C)", -20, 60, 0)
        minutes = st.number_input("Duration (minutes)", min_value=5, max_value=180, step=5, value=60)
    with cB:
        times = np.arange(0, minutes+1, 5)
        T = base_T
        temps = []
        for t in times:
            if T < 0:
                T = min(0, base_T + t*1.3)
            elif T < 100:
                T = min(100, 0 + (t - max(0,(0-base_T)/1.3))*1.05)
            else:
                T = min(130, 100 + (t-100)*0.35)
            temps.append(T)
        fig, ax = plt.subplots()
        ax.plot(times, temps, marker="o")
        ax.set_xlabel("Time (min)"); ax.set_ylabel("Temperature (°C)")
        ax.set_title("Heating Curve (sampled every 5 min)")
        if running:
            st.pyplot(fig)
        else:
            st.info("Press Start to plot the curve.")
            st.pyplot(fig)  # still show one pass so you can preview

# ---------- Electrolysis ----------
with tabs[4]:
    st.markdown("#### Electrolysis Cell — Graphite Rods, External Battery + Bulb + Switch")
    st.image(str(Path("assets/electrolysis.svg")), caption="Green gas at the anode; sodium plating at the cathode (molten NaCl demo)", use_column_width=True)
    on = st.toggle("Switch ON/OFF", value=False)
    if on:
        st.success("Current ON → bulb glows; green gas at anode; golden sodium coating at cathode.")
    else:
        st.info("Switch open: no current.")

# ---------- Periodic Table (118) ----------
with tabs[5]:
    st.markdown("#### Pastel Periodic Table (scrollable; noble gases visible)")
    data = json.loads(Path("periodic_118.json").read_text())
    df = pd.DataFrame(data, columns=["Z","Symbol","Name","Group","Shells"])
    # Shift noble gases visually by sorting Group so '18' comes earlier
    df = df.sort_values(by=["Group","Z"], ascending=[False,True])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.caption("Hover to read 'Shells' (compressed Bohr shells). Full Bohr diagrams can be added later.")

# ---------- Quizzes (expanded pools; no brand label) ----------
with tabs[6]:
    st.markdown("#### Quiz Bank")
    quiz = st.selectbox("Choose a quiz", [
        "Ions & Charges","Isotopes & Neutrons","Balance Equations",
        "Periodic Trends","Electron Configs","Reactivity Ordering",
        "Atomic Structure (mixed)"
    ])

    rng = np.random.default_rng()

    def ions_quiz():
        Z = int(rng.choice([3,11,12,17,19,20,26,29,30,35]))
        charge = int(rng.choice([-2,-1,1,2,3]))
        electrons = Z - charge
        st.write(f"**Q:** An ion has atomic number {Z} and charge {charge:+}. How many electrons does it have?")
        ans = st.number_input("Electrons", 0, 200, 0, 1, key='ion_e')
        if st.button("Check", key="ion_chk"):
            st.write("**A:**", electrons)
            st.success("Correct!" if ans==electrons else "Not quite — try again.")

    def isotope_quiz():
        pairs = [(23,11),(24,12),(25,12),(35,17),(37,17),(40,20),(56,26)]
        A,Z = pairs[rng.integers(0,len(pairs))]
        N = A - Z
        st.write(f"**Q:** For nuclide with mass number **A={A}** and atomic number **Z={Z}**, find neutrons **N**.")
        ans = st.number_input("Neutrons N", 0, 200, 0, 1, key="isoN")
        if st.button("Check", key="iso_chk"):
            st.write("**A:**", N)
            st.success("Correct!" if ans==N else "Not quite.")

    def balance_quiz():
        # bank of simple single-replacement and combustion
        bank = [
            ("__ Fe + __ CuSO₄ → __ FeSO₄ + __ Cu",[1,1,1,1]),
            ("__ Zn + __ HCl → __ ZnCl₂ + __ H₂",[1,2,1,1]),
            ("__ Al + __ O₂ → __ Al₂O₃",[4,3,2]),
            ("__ C₃H₈ + __ O₂ → __ CO₂ + __ H₂O",[1,5,3,4]),
            ("__ Na + __ Cl₂ → __ NaCl",[2,1,2])
        ]
        eq, sol = bank[rng.integers(0,len(bank))]
        st.write(f"**Q:** Balance: {eq}")
        fields = [st.number_input(f"Coeff {i+1}",1,12,1,key=f"b{i}") for i in range(len(sol))]
        if st.button("Check", key="bal_chk"):
            st.write("**A:**", ", ".join(map(str,sol)))
            st.success("Perfect!" if fields==sol else "Not balanced yet — try again.")

    def trends_quiz():
        q = rng.choice(["Which increases down a group more?","Which increases left→right across a period more?"])
        pick = st.radio(q, ["Atomic radius","Ionization energy","Electronegativity"], horizontal=True, key="trend_pick")
        if st.button("Check", key="trend_chk"):
            correct = "Atomic radius" if "down a group" in q else "Ionization energy"
            st.write("**A:**", correct)
            st.success("Correct." if pick==correct else "Close — review periodic trends.")

    def configs_quiz():
        el = rng.choice([(21,"Sc"),(29,"Cu"),(26,"Fe"),(12,"Mg"),(17,"Cl")])
        Z,sym = el
        st.write(f"**Q:** Provide a *shell* configuration for **{sym} (Z={Z})**.")
        ans = st.text_input("Enter shells e.g. 2,8,9,2", key="cfg_in")
        # quick validator from JSON shells
        data = json.loads(Path("periodic_118.json").read_text())
        correct = [x["Shells"] for x in data if x["Z"]==Z][0]
        if st.button("Check", key="cfg_chk"):
            st.write("**A:**", correct, "  (subshell aufbau e.g. 3d¹4s² for Sc)")
            st.success("Nice!" if ans.replace(" ","")==correct else "Compare your result.")

    def reactivity_quiz():
        left = ["Mg","Zn","Fe","Cu","Na","Al"]
        pick = rng.choice([["Mg","Fe","Cu","Zn"],["Na","Al","Zn","Cu"],["Fe","Zn","Cu","Mg"]])
        st.write("**Q:** Order by decreasing reactivity (most→least): " + ", ".join(pick))
        ans = st.text_input("Your order (comma-separated)", key="react_in")
        correct_map = {"Mg":3,"Zn":2,"Fe":1,"Cu":0,"Na":5,"Al":2.5}
        correct = sorted(pick, key=lambda m: -correct_map[m])
        if st.button("Check", key="react_chk"):
            st.write("**A:**", ", ".join(correct))
            user = [s.strip().title() for s in ans.split(",")]
            st.success("Correct!" if user==correct else "Not quite — try again.")

    def atomic_mixed_quiz():
        which = rng.integers(0,5)
        if which==0: ions_quiz()
        elif which==1: isotope_quiz()
        elif which==2: balance_quiz()
        elif which==3: trends_quiz()
        else: configs_quiz()

    if quiz=="Ions & Charges": ions_quiz()
    elif quiz=="Isotopes & Neutrons": isotope_quiz()
    elif quiz=="Balance Equations": balance_quiz()
    elif quiz=="Periodic Trends": trends_quiz()
    elif quiz=="Electron Configs": configs_quiz()
    elif quiz=="Reactivity Ordering": reactivity_quiz()
    else: atomic_mixed_quiz()

st.markdown("---")
st.caption("© CHEMPOP — premium, polished, classroom‑ready.")
