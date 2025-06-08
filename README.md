# **TalentScout Hiring Assistant**

## 📝 **Project Overview**

TalentScout Hiring Assistant is an AI-powered chatbot built with Streamlit.
It guides candidates step-by-step to enter their personal and professional details, collects their tech stack, and automatically generates tailored technical interview questions using a local Hugging Face language model.
This ensures a smoother, more personalized candidate screening experience—while maintaining data privacy.

🛠️ Installation Instructions

Requirements:

Python 3.8 or above

4GB+ RAM (recommended 8GB+ for smoother model loading)

#Steps:

1)Clone or download the project folder.

2)Install dependencies:

pip install -r requirements.txt

3)Run the application: 

streamlit run app.py

4)Open your browser to:
 
 http://localhost:8501

🚀 Usage Guide

Stepwise Data Entry:
Enter candidate information field by field (name, email, etc.).

Tech Stack:
Input one or more technologies (comma-separated, e.g., Python, SQL, Django).

Generate Questions:
Click the button to get 3–5 custom interview questions for each technology.

Restart:
Use the “Restart” button to clear data and start with a new candidate.

Privacy:
No data is stored or shared. All entries are session-based and cleared on restart.

⚙️ Technical Details
Frontend:
Streamlit for rapid UI prototyping and deployment.

AI Model:
MBZUAI/LaMini-Flan-T5-783M (Hugging Face Transformers),
a compact, instruction-tuned text2text LLM suitable for interview question generation.

Libraries:

streamlit

transformers

torch

re (for regex-based formatting)

Architecture:

Stepwise candidate info collection (Streamlit session state).

Prompt design for LLM to generate relevant technical questions.

No database/storage: All data handled in-memory for privacy.

🧠 Prompt Design

Information Gathering:
Each candidate detail is collected individually, with prompts like
“Enter your Full Name:” ensuring clear, sequential data entry.

Technical Question Generation:
For each entered technology, the prompt is:
“Generate 3 to 5 technical interview questions for a candidate skilled in [tech]. The questions should test core knowledge and real-world problem-solving.”
This ensures the LLM returns relevant, scenario-based questions, rather than generic definitions.


🏔️ Challenges & Solutions

Model Size vs. Hardware Constraints:

Challenge: Large models (7B+) require high RAM/VRAM; not practical for all users.

Solution: Switched to LaMini-Flan-T5-783M, which is instruction-tuned and CPU-friendly.

Duplicate Numbering in Questions:

Challenge: LLM sometimes returns numbered questions, which could overlap with UI numbering.

Solution: Regex-based parsing to split questions, removing extra numbers for a clean display.

Data Privacy Compliance:

Challenge: Ensuring candidate data isn’t inadvertently stored or shared.

Solution: All data is handled in Streamlit’s session state (RAM only), with a privacy info banner shown to the user.

User Experience (UX):

Challenge: Preventing users from skipping required info or being confused by too many fields at once.

Solution: Stepwise field entry and clear status messages after each phase.



