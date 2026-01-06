# 🎮 GameRx | Your Digital Dose
# App-ready UI aligned to: 17_games_hybrid_app_ready.csv
# Uses locked outputs only (Relief Pathway + Therapeutic Fit %)

import pandas as pd
import streamlit as st
from pathlib import Path
st.write("✅ Running GitHub app.py")

# ------------------------------------------------
# 1. Page Config
# ------------------------------------------------
st.set_page_config(
    page_title="GameRx | Your Digital Dose",
    page_icon="🎮",
    layout="wide",
)

# ------------------------------------------------
# 2. File Paths & Column Names (LOCKED)
# ------------------------------------------------
DATA_PATH = Path("..") / "02 Data" / "cleaned" / "app_data" / "17_games_hybrid_app_ready.csv"

GAME_NAME_COL = "Name"
RELIEF_COL = "Relief Pathway"
FIT_COL = "Therapeutic Fit %"

BLOCK_COL = "is_blocked"
COLOR_COL = "fit_color"

# ------------------------------------------------
# 3. Load Data (SAFE)
# ------------------------------------------------
@st.cache_data
def load_app_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    if BLOCK_COL in df.columns:
        df = df[df[BLOCK_COL] == False].copy()

    required = {GAME_NAME_COL, RELIEF_COL, FIT_COL}
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"Missing required columns: {missing}")

    df[FIT_COL] = pd.to_numeric(df[FIT_COL], errors="coerce")
    df = df.dropna(subset=[FIT_COL]).copy()

    df[RELIEF_COL] = df[RELIEF_COL].astype(str).str.lower().str.strip()

    if COLOR_COL in df.columns:
        df[COLOR_COL] = df[COLOR_COL].astype(str).str.lower().str.strip()
    else:
        df[COLOR_COL] = "yellow"

    df = df.drop_duplicates(subset=[GAME_NAME_COL]).copy()
    return df

# ------------------------------------------------
# 4. Mood → Relief Mapping (LOCKED)
# ------------------------------------------------
MOOD_TO_RELIEF = {
    "Sad": ["comfort"],
    "Lonely": ["validation"],
    "Low-energy": ["comfort"],
    "Angry": ["catharsis"],
    "Frustrated": ["comfort", "distraction"],
    "Anxious": ["distraction"],
    "Stressed": ["distraction"],
    "Overwhelmed": ["comfort"],
    "Numb": ["validation"],
}

MOOD_ORDER = list(MOOD_TO_RELIEF.keys())

# ------------------------------------------------
# 5. Filter & Rank
# ------------------------------------------------
def filter_and_rank(df: pd.DataFrame, reliefs: list[str]) -> pd.DataFrame:
    results = []

    for relief in reliefs:
        subset = df[df[RELIEF_COL] == relief].copy()
        if subset.empty:
            continue

        subset["relief_priority"] = reliefs.index(relief)
        results.append(subset)

    if not results:
        return pd.DataFrame()

    combined = pd.concat(results, ignore_index=True)

    return combined.sort_values(
        by=["relief_priority", FIT_COL],
        ascending=[True, False],
    )

# ------------------------------------------------
# 6. Display Helpers
# ------------------------------------------------
def confidence_label(color: str) -> str:
    if color == "green":
        return "🟢 Strong match"
    if color == "yellow":
        return "🟡 Worth exploring"
    return "🔴 Gentle option"

def build_recommendation_table(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "Name": df[GAME_NAME_COL],
        "Relief Pathway": df[RELIEF_COL].str.title(),
        "Therapeutic Fit %": df[FIT_COL].round(1),
        "Confidence": df[COLOR_COL].apply(confidence_label),
    })

# ------------------------------------------------
# 6.5 Relief Pathway Explanations (UI ONLY)
# ------------------------------------------------
RELIEF_EXPLANATIONS = {
    "comfort": "Calm, gentle experiences that help you feel safe and grounded.",
    "catharsis": "High-energy play that helps release built-up emotion.",
    "distraction": "Engaging focus that pulls attention away from stress or rumination.",
    "validation": "Story-driven experiences that help you feel seen and understood.",
}

# ------------------------------------------------
# 7. Main App
# ------------------------------------------------
def main():
    st.title("🎮 GameRx | Your Digital Dose")
    st.write("Find games that match how you feel today.")

    df = load_app_data(DATA_PATH)

    # Sidebar
    st.sidebar.header("How are you feeling today?")
    selected_mood = st.sidebar.radio(
        "Select your mood:",
        MOOD_ORDER,
        index=None,
        key="selected_mood",
    )

    # ------------------------------------------------
    # HOME VIEW (no mood selected)
    # ------------------------------------------------
    if selected_mood is None:
        st.markdown("### How GameRx Works")

        st.write(
            "GameRx helps you find games based on **how you feel**, not just what’s popular."
        )
        st.write(
            "Instead of genres alone, it uses **relief pathways**, different ways games can "
            "support emotional regulation."
        )

        st.markdown("#### Relief Pathways")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Comfort**")
            st.write(RELIEF_EXPLANATIONS["comfort"])

            st.markdown("**Catharsis**")
            st.write(RELIEF_EXPLANATIONS["catharsis"])

        with col2:
            st.markdown("**Distraction**")
            st.write(RELIEF_EXPLANATIONS["distraction"])

            st.markdown("**Validation**")
            st.write(RELIEF_EXPLANATIONS["validation"])

        st.info("Select a mood from the left sidebar to begin.")
        return

    # ------------------------------------------------
    # RESULT VIEW (mood selected)
    # ------------------------------------------------
    reliefs = MOOD_TO_RELIEF[selected_mood]

    if selected_mood == "Frustrated":
        reliefs = [r for r in reliefs if r != "catharsis"]

    display_relief = "comfort" if selected_mood == "Frustrated" else reliefs[0]

    st.markdown(
        f"### You selected: **{selected_mood}** → Relief Pathway: **{display_relief.title()}**"
    )
    st.write(RELIEF_EXPLANATIONS.get(display_relief, ""))
    st.divider()

    ranked = filter_and_rank(df, reliefs)

    if ranked.empty:
        st.write("No recommendations available.")
        return

    st.markdown("### Top Recommendations")

    strong_df = ranked[ranked[COLOR_COL] == "green"].head(10)
    moderate_df = ranked[ranked[COLOR_COL] == "yellow"].head(7)
    gentle_df = ranked[ranked[COLOR_COL] == "red"].head(5)

    tab_strong, tab_moderate, tab_gentle = st.tabs(
        ["🟢 Strong matches", "🟡 Worth exploring", "🔴 Gentle options"]
    )

    with tab_strong:
        st.dataframe(build_recommendation_table(strong_df), use_container_width=True)

    with tab_moderate:
        st.dataframe(build_recommendation_table(moderate_df), use_container_width=True)

    with tab_gentle:
        st.dataframe(build_recommendation_table(gentle_df), use_container_width=True)

# ------------------------------------------------
if __name__ == "__main__":
    main()







