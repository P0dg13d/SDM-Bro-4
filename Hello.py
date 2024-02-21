import streamlit as st
import pandas as pd
import langchain
import openai
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent, create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI, OpenAI
from gtts import gTTS
from io import BytesIO

def run():
    st.set_page_config(
        page_title="SDM Me Bro",
        page_icon="🦸🏻‍♂️",
    )

# Visible on load
    st.write("# 👨🏻‍💼 SDM Me Bro 🦸🏻‍♂️")
    uploaded_file = st.file_uploader("Dump yo data", type=["csv"])
    if uploaded_file is not None:
        st.write("File uploaded magically.")

# Read csv and show
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.write(df)

    if uploaded_file is not None:
      query = st.text_area("What would you like to know?")
      button = st.button("Run Magic")
      if button: 
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0,openai_api_key="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"), df, verbose=False)
        #agent = create_csv_agent(OpenAI(temperature=0, openai_api_key="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"),uploaded_file,verbose=True,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,)
        answer = agent.run(query)
        st.write(answer)
        sound_file = BytesIO()
        tts = gTTS(answer, lang='en')
        tts.write_to_fp(sound_file)
        st.audio(sound_file)
        
if __name__ == "__main__":
    run()