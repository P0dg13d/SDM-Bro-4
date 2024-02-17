import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Chat with Finance Data",
        page_icon="👋",
    )

    st.write("# Chat with Finance Data 👋")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        st.write("File uploaded successfully.")


# Read CSV
        df = pd.read_csv(uploaded_file)

        # Show DataFrame
        st.write("Preview of uploaded data:")
        st.write(df)

        # Allow user to ask a question
        question = st.text_input("Ask a question about the data:")
        if st.button("Get Answer"):
            if not question:
                st.error("Please enter a question.")
            else:
                try:
                    # Extract answer using LangChain
                    answer = langchain_qa(question=question, context=df.to_string())
                    st.success("Answer: {}".format(answer['answer']))
                except Exception as e:
                    st.error("Error: {}".format(e))


if __name__ == "__main__":
    run()
