import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import re

st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- INFO BOX (for demo/data privacy compliance) ---
st.info(
    "🚨 **Privacy Notice:** This demo does not store or share your information. "
    "All data is simulated and used only for this session."
)

# --- CANDIDATE DETAILS COLLECTION ---
info_fields = [
    ("full_name", "Full Name"),
    ("email", "Email Address"),
    ("phone", "Phone Number"),
    ("experience", "Years of Experience"),
    ("position", "Position(s) Applying For"),
    ("location", "Current Location"),
]

if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}
if "question_idx" not in st.session_state:
    st.session_state.question_idx = 0
if "completed_info" not in st.session_state:
    st.session_state.completed_info = False

st.title("TalentScout Hiring Assistant")

if not st.session_state.completed_info:
    idx = st.session_state.question_idx
    field, prompt = info_fields[idx]
    st.markdown(f"#### Step {idx+1} of {len(info_fields)}")
    user_input = st.text_input(f"**Enter your {prompt}:**", key=field)
    if user_input:
        st.session_state.candidate_info[field] = user_input
        st.session_state.question_idx += 1
        if st.session_state.question_idx == len(info_fields):
            st.session_state.completed_info = True
        st.rerun()
    st.stop()

st.success("Thank you for submitting your details! Here is what you've entered:")
st.json(st.session_state.candidate_info)

st.markdown("---")

# --- TECH STACK INPUT ---
st.markdown("### Enter one or more technologies (comma-separated):")
tech_input = st.text_input("Tech stack (e.g., Python, SQL, Django):")

# --- MODEL LOADING ---
@st.cache_resource
def load_model():
    model_id = "MBZUAI/LaMini-Flan-T5-783M"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    generator = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=128,
        do_sample=True,
        temperature=0.7
    )
    return generator

generator = load_model()

# --- TECHNICAL QUESTION GENERATION ---
if st.button("Generate Questions") and tech_input:
    tech_list = [tech.strip() for tech in tech_input.split(",") if tech.strip()]
    for tech in tech_list:
        prompt = (
            f"Generate 3 to 5 technical interview questions for a candidate skilled in {tech}. "
            "The questions should test core knowledge and real-world problem-solving."
        )
        with st.spinner(f"Generating questions for {tech}..."):
            output = generator(prompt)[0]['generated_text']

        st.subheader(f"🧑‍💻 {tech.capitalize()}")
        # Split into separate questions, remove empty results
        questions = re.split(r"\d+\.\s*", output)
        questions = [q.strip() for q in questions if q.strip()]
        for i, question in enumerate(questions, 1):
            st.markdown(f"**{i}.** {question}")

st.markdown("---")
# --- RESTART BUTTON ---
if st.button("🔄 Restart"):
    for key in ["candidate_info", "question_idx", "completed_info"]:
        if key in st.session_state:
            del st.session_state[key]
    st.experimental_rerun()
