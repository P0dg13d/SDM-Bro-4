import streamlit as st
import pandas as pd
from utils import get_answer_csv

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

        # Allow user to ask a question
        question = st.text_input("Ask a question about the data:")

    if uploaded_file is not None:
      query = st.text_area("Ask any question related to the document")
      button = st.button("Submit")
      if button:
        st.write(get_answer_csv(uploaded_file, query))


if __name__ == "__main__":
    run()
