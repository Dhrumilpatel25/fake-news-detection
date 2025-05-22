import streamlit as st
from clearml import Task
import time
import uuid
# from utils import visualize

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

#Title
st.markdown('<div class="title">Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Fact-check news headlines with ML-powered models</div>', unsafe_allow_html=True)

#Custom CSS Styling
st.markdown("""
    <style>
    .main-container {
        background-color: #f7fbff;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }
    .title {
        text-align: center;
        font-size: 36px;
        color: #2c3e50;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #6c757d;
        margin-bottom: 20px;
    }
    .result-box {
        margin-top: 30px;
        padding: 1.5rem;
        border-radius: 12px;
        background-color: #e8f9f1;
        border: 2px solid #a3e4d7;
        text-align: center;
        font-size: 20px;
        color: #117a65;
    }
    .fake-result {
        background-color: #fdecea;
        border: 2px solid #f5b7b1;
        color: #c0392b;
    }
    .stTextArea>label {
        font-weight: 600;
    }
    .stSelectbox>label {
        font-weight: 600;
    }
    .stButton>button {
        background-color: #2980b9;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

#text input
news_text = st.text_area("Paste the news headline below", height=150)

#model choice
model_choices = ['Passive Aggressive','SVM','XGBoost']
model_choice = st.selectbox("🤖 Select Model", model_choices)

if st.button("Check if it's Fake or Real",use_container_width=True):
    if not news_text.strip():
        st.error("Please enter some text.")
    else:
            with st.spinner("Sending to ClearML..."):
                    
                    #Choose base task IDs (get real id from ClearML backend)
                    base_task_id = {
                          
                          ##TODO: ADD ID FROM BACKEND

                        "SVM": "SVM_model.pkl",
                        "XGBoost": "XGBoost_model.pkl",
                        "Passive Aggressive": "PassiveAggressive_model.pkl",
                    }[model_choice]

                    #Create a clearml task clone
                    task = Task.clone(source_task=base_task_id, name=f"{model_choice}_fact_ceck_{uuid.uuid4().hex[:6]}")

                    task.set_parameter("General/news_text", news_text)
                    task.enqueue("default")

                    st.info(f"Model running via ClearML: Task ID `{task.id}`")

                    #completion
                    while task.status not in ("completed","failed", "stopped"):
                          time.sleep(4)
                          task.reload()
                        
                    if(task.status == 'completed'):
                          label = task.get_parameters().get("Results/predicted_label")
                          #CALCULATE PROBABILITY / TRUE OR FALSE
                    
                    else:
                          st.error("Task failed or was stopped.")

                    