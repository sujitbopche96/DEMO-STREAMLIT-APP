from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Creating prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You're a helpful assistant. Please respond correctly."),
        ("user", "Question: {question}")
    ]
)

st.title("LangChain Demo Chat App with Gemma 2B")

# Input box
question = st.text_input("Enter your question")

# Load Ollama model
llm = Ollama(model="gemma2:2b")

# Output parser
output_parser = StrOutputParser()

# Create chain
chain = prompt | llm | output_parser

# When user enters question
if question:
    response = chain.invoke({"question": question})
    st.write(response)
