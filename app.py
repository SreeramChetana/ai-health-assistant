import streamlit as st
from modules.medication import MedicationTracker
from modules.database import create_tables
from modules.health_chatbot import HealthChatbot

# ---------------- Page Config ----------------
st.set_page_config(page_title="AI Personal Health Assistant", page_icon="🏥")

# ---------------- Initialize DB ----------------
create_tables()
tracker = MedicationTracker()
chatbot = HealthChatbot()

# ---------------- Title ----------------
st.title("🏥 AI Personal Health Assistant")
# ================= DASHBOARD METRICS =================
st.subheader("📊 Health Dashboard")

meds = tracker.get_medications()
med_count = len(meds)

col1, col2 = st.columns(2)

with col1:
    st.metric("💊 Total Medications", med_count)

with col2:
    st.metric("🕒 Active Reminders", med_count)

st.caption(
    "⚠️ This assistant provides general health information only and is not medical advice."
)

# ================= MEDICATION SECTION =================
st.header("💊 Add Medication")

name = st.text_input("Medication Name")
time = st.time_input("Reminder Time")

if st.button("Add Medication"):
    if name.strip():
        tracker.add_medication(name, str(time))
        st.success("Medication added successfully!")
    else:
        st.error("Please enter medication name")

# ---------------- Show Medications ----------------
st.header("📋 Your Medications")



if meds:
    for med in meds:
        st.write(f"💊 {med[0]} at {med[1]}")
else:
    st.info("No medications added yet.")

# ================= AI HEALTH CHAT =================
st.header("🤖 Ask Health Assistant")

user_question = st.text_input("Ask a health question")

if st.button("Get Answer"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            try:
                answer = chatbot.ask(user_question)
                st.write(answer)
            except Exception as e:
                st.error("Error getting response. Check your API key.")
                st.exception(e)
    else:
        st.error("Please enter a question")