import streamlit as st
import requests

# Constants
base_url = "https://api.aimlapi.com/v1"
api_key = "741ce4f93b1343d2906dd9f3c7a0637a"
system_prompt = "You are a data science assistant. Provide insightful and clear explanations about data science topics."

# Streamlit UI Styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }

    .stApp {
        background-color: black;
        color: white;
    }

    input {
        color: white !important;
        background-color: #333 !important;
    }

    button {
        background-color: black !important;
        border-color: #333 !important;
        color: white !important;
        width: 80px !important;
    }

    .stCaption {
        color: white !important;
    }

    hr {
        border-color: #333 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App Logic
st.title("AskMe (Powered by AIML API)")
st.divider()

prompt = st.text_input("What do you want to learn?")
gptbutton = st.button("GO")
st.caption("Press the Go button to know your answer.")
st.divider()

if gptbutton:
    if prompt.strip():
        with st.spinner("I am preparing..."):
            try:
                response = requests.post(
                    f"{base_url}/chat/completions",
                    json={
                        "model": "mistralai/Mistral-7B-Instruct-v0.2",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt},
                        ],
                        "temperature": 0.7,
                        "max_tokens": 256,
                    },
                    headers={"Authorization": f"Bearer {api_key}"},
                )

                if response.status_code in [200, 201]:  
                    data = response.json()
                    ai_response = data["choices"][0]["message"]["content"]
                    st.success("Here is the information:")
                    st.write(ai_response)
                else:
                    st.error(f"Unexpected status code {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before clicking GO.")
