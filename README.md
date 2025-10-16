# CHEMPOP Virtual Lab (Premium)

This Streamlit app delivers professional interactive chemistry simulations and quizzes inspired by regional syllabi and past paper patterns — **without using any exam board branding**.

## Features
- Simple distillation with a tilted condenser, three-way adaptor, Erlenmeyer receiver, and **droplet accumulation**.
- Curved test-tube single-tube reactions: choose element, water temp (cold/warm), indicators, **bubble intensity**, flame test, hydrogen "pop" test, and auto-balanced reaction prompts.
- Six-tube reactivity series: visible **blue→colorless fade** and **brown copper deposition**, with vigor hints.
- Heating curve experiment with **Start/Stop** and sampling every 5 minutes; clean beaker + thermometer art.
- Electrolysis with **graphite rods**, external **battery + bulb + switch**, green gas at anode and sodium plating at cathode.
- Periodic table (full **118 elements**) with compressed Bohr **shells** on hover.
- Expanded quiz bank (ions, isotopes, balancing, periodic trends, electron configs, reactivity, mixed).

## Quickstart
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud
1. Create a **GitHub** repository and push this folder.
2. Go to https://share.streamlit.io → New app → choose your repo/branch → `app.py`.
3. After the build, you’ll get a **public URL** (shareable preview link).

## One‑shot Git push script
If you have `git` and a fresh repo ready on GitHub (replace placeholders):
```bash
# set once
git init
git branch -M main
git add .
git commit -m "CHEMPOP Virtual Lab — initial release"
git remote add origin https://github.com/YOUR-USER/chempop-virtual-lab.git
git push -u origin main
```

> **Note:** The quizzes are generated from general chemistry principles and patterns **without** using protected “CSEC” branding.
