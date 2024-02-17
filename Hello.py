import streamlit as st
import pandas as pd
#import os
import langchain
import openai
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent, create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI, OpenAI

def run():
    st.set_page_config(
        page_title="Finance Bro",
        page_icon="🦸🏻‍♂️",
    )

    st.write("# 👨🏻‍💼 Finance Bro 🦸🏻‍♂️")

    # File upload
    uploaded_file = st.file_uploader("Dump yo data", type=["csv"])

    if uploaded_file is not None:
        st.write("File uploaded magically.")

# Read CSV
        df = pd.read_csv(uploaded_file)
        # Show DataFrame
        st.write("Preview of uploaded data:")
        st.write(df)

    if uploaded_file is not None:
      query = st.text_area("Ask any question related to the document")
      button = st.button("Submit")
      if button: 
        #st.write(get_answer_csv(uploaded_file, query))
        #agent = create_pandas_dataframe_agent(OpenAI(temperature=0,openai_api_key="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"), df, verbose=False)
        agent = create_csv_agent(OpenAI(temperature=0, openai_api_key="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"),uploaded_file,verbose=True,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,)
        answer = agent.run(query)
        st.write(answer)

if __name__ == "__main__":
    run()
