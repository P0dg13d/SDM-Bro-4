import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Chat with Finance Data",
        page_icon="👋",
    )

    st.sidebar.success("Select a demo above.")

    st.write("# Chat with Finance Data 👋")

    st.markdown(
        """
        Streamlit eshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
