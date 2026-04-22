import streamlit as st
import time

st.set_page_config(page_title="Calories Quest", page_icon="🍎", layout="centered")

# ---------------- SESSION STATE ----------------
if "calories" not in st.session_state:
    st.session_state.calories = 0

if "food_log" not in st.session_state:
    st.session_state.food_log = []

if "xp" not in st.session_state:
    st.session_state.xp = 0

# ---------------- FUNCTIONS ----------------
def add_food(food, cal):
    st.session_state.food_log.append((food, cal))
    st.session_state.calories += cal
    st.session_state.xp += int(cal / 10)

def reset_day():
    st.session_state.calories = 0
    st.session_state.food_log = []
    st.session_state.xp = 0

def get_level(xp):
    return xp // 100 + 1

# ---------------- UI ----------------
st.title("🍏 Calories Quest")
st.subheader("Turn your diet into a game!")

st.write("### 🎯 Your Stats")
level = get_level(st.session_state.xp)

col1, col2, col3 = st.columns(3)
col1.metric("Calories", st.session_state.calories)
col2.metric("XP", st.session_state.xp)
col3.metric("Level", level)

# Progress bar (daily target 2000 kcal default)
target = 2000
progress = min(st.session_state.calories / target, 1.0)
st.progress(progress)

if progress >= 1:
    st.warning("⚠️ You exceeded your daily calorie target!")
else:
    st.success("Keep going, Quest Hero 💪")

st.divider()

# ---------------- INPUT ----------------
st.write("### ➕ Add Food Item")

food = st.text_input("Food name")
calories = st.number_input("Calories", min_value=0, step=10)

if st.button("Add to Quest"):
    if food:
        add_food(food, calories)
        st.success(f"{food} added!")
        st.balloons()
        time.sleep(0.5)
        st.rerun()

st.divider()

# ---------------- FOOD LOG ----------------
st.write("### 📜 Food Log")

if st.session_state.food_log:
    for item, cal in reversed(st.session_state.food_log):
        st.write(f"🍽️ {item} — {cal} kcal")
else:
    st.info("No food logged yet. Start your quest!")

st.divider()

# ---------------- RESET ----------------
if st.button("🔄 Reset Day"):
    reset_day()
    st.rerun()
