import streamlit as st
import pandas as pd
import sqlite3
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import OpenAI
import io

# Function to create database and table
def create_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS uploaded_data (id INTEGER PRIMARY KEY, data TEXT)''')
    conn.commit()
    conn.close()

# Function to insert CSV data into the database
def insert_data_into_database(data):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO uploaded_data (data) VALUES (?)''', (data,))
    conn.commit()
    conn.close()

# Function to retrieve CSV data from the database
def retrieve_data_from_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''SELECT data FROM uploaded_data ORDER BY id DESC LIMIT 1''')
    data = c.fetchone()[0]
    conn.close()
    return io.StringIO(data)

def run():
    st.set_page_config(
        page_title="SDM Me Bro",
        page_icon="🦸🏻‍♂️",
    )

    # Create or connect to the database
    create_database()

    # Visible on load
    st.write("# 👨🏻‍💼 SDM Me Bro 🦸🏻‍♂️")
    uploaded_file = st.file_uploader("Dump yo data", type=["csv"])
    if uploaded_file is not None:
        st.write("File uploaded magically.")

        # Read CSV and store it in the database
        df = pd.read_csv(uploaded_file)
        insert_data_into_database(df.to_csv(index=False))

        # Show preview of uploaded data
        st.write("Preview of uploaded data:")
        st.write(df)

    query = st.text_area("What would you like to know?")
    button = st.button("Run Magic")
    if button:
        # Retrieve data from the database
        data = retrieve_data_from_database()
        df = pd.read_csv(data)

        # Run the agent on the retrieved data
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0, openai_api_key="YOUR_OPENAI_API_KEY"), df, verbose=False)
        answer = agent.run(query)
        st.write(answer)

if __name__ == "__main__":
    run()
