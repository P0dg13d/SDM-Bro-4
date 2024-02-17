# type: ignore
import os
from typing import TextIO

import pandas as pd
import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI

openai.api_key = "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"


def get_answer_csv(file: TextIO, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """
 
    # Create an agent using OpenAI and the Pandas dataframe
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)
    #agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)

    # Run the agent on the given query and return the answer
    #query = "whats the square root of the average age?"
    answer = agent.run(query)
    return answer