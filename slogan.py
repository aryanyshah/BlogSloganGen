import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from LLaMA 2 model
def get_llama_response(input_text, no_words):
    try:
        # Load the LLaMA 2 model
        llm = CTransformers(
            model="C:/Users/aryan/Desktop/ECI blogslogan/Blog-Generation-using-LLMs/model/llama-2-7b-chat.ggmlv3.q2_K (1).bin",
            model_type="llama",
            config={"max_new_tokens": 256, "temperature": 0.01},
        )
        
        # Prompt Template
        template = """
            Write a slogan for the Election Commission Of India in a formal way 
            on the topic "{input_text}" within {no_words} words.
        """
        # Fill the template with actual inputs
        formatted_prompt = template.format(input_text=input_text, no_words=no_words)
        
        # Generate the response from the LLaMA 2 model
        response = llm(formatted_prompt)
        return response
    except Exception as e:
        return f"Error: {e}"

# Streamlit App Configuration
st.set_page_config(
    page_title="Generate Slogans",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Generate Slogans 🤖")

# User Inputs
input_text = st.text_input("Enter the Slogan Topic")
no_words = st.text_input("Enter the Number of Slogans")

# Submit Button
submit = st.button("Generate")

# Final Response
if submit:
    if input_text.strip() == "" or no_words.strip() == "":
        st.error("Please fill in both the Blog Topic and the Number of Words.")
    else:
        try:
            # Convert no_words to integer
            no_words = int(no_words)
            response = get_llama_response(input_text, no_words)
            st.write(response)
        except ValueError:
            st.error("Number of Words must be a valid integer.")
