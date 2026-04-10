import streamlit as st
import datetime

# --- PAGE SETUP ---
st.set_page_config(page_title="Hospital AI Assistant", page_icon="🏥")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 Hospital AI Assistant")
st.write("Welcome! Main aapki appointments aur queries mein madad kar sakta hoon.")


# --- LOGIC FUNCTIONS ---
def get_faq_response(user_input):
    user_input = user_input.lower()
    responses = {
        "timing": "Hamara hospital 24/7 khula hai.",
        "location": "Hum Main Road, Block 5, Karachi mein waqay hain.",
        "fee": "Consultation fee 1000 PKR hai."
    }
    for key, val in responses.items():
        if key in user_input:
            return val
    return None


# --- SIDEBAR: APPOINTMENT BOOKING ---
st.sidebar.header("📅 Book Appointment")
with st.sidebar.form("appointment_form"):
    patient_name = st.text_input("Apna poora naam likhein")
    doctor_dept = st.selectbox("Department", ["Heart", "Skin", "General"])
    submit_btn = st.form_submit_button("Book Karein")

    if submit_btn:
        if patient_name:
            today = datetime.date.today()
            appointment_date = today + datetime.timedelta(days=1)
            st.success(
                f"Shukriya {patient_name}! Aapki appointment {doctor_dept} ke liye {appointment_date} ko fix ho gayi hai.")
        else:
            st.error("Baraye meharbani apna naam likhein.")

# --- MAIN CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Poochiye: Timing, Fee ya Location?"):
    # User message display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot response logic
    response = get_faq_response(prompt)
    if not response:
        response = "Maazrat, mujhay samajh nahi aaya. Kya aap 'timing', 'fee' ya 'location' ke bare mein poochna chahte hain?"

    # Bot message display
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
