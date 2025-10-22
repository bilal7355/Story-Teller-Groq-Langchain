import streamlit as st
# from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage
from langchain.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
import os

def get_message_history(session_id: str) -> BaseChatMessageHistory:
        return ChatMessageHistory()
# Load environment variables
# load_dotenv()

# Replace this in production with env vars
groq_api_key = os.getenv("GROQ_API_KEY")

def main():
    st.title("Story Generator Chatbot")
    st.markdown("**Disclaimer:** This chatbot provides creative stories based on given prompts, and may produce similar stories to movies/series/novels.")

    # Sidebar controls
    st.sidebar.title('Chatbot Settings')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['llama-3.3-70b-versatile']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)

    # Prompt template
    prompt_template = PromptTemplate.from_template("""
    You are an enthusiastic and creative story generator chatbot. Your role is to:
    - Understand the story setup given by the user.
    - Provide creatively thought-out stories with good plots.
    - Take inspiration from novels, manga, movies and series.
    - Stories you provide must be complete from beginning to end.
    - Be mindful of the story length.

    Current conversation:
    {chat_history}
    
    User: {input}
    Chatbot:
    """)

    # Initialize model
    chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)

    # Initialize memory store per session
    



    # Use RunnableLambda to convert input/output with memory
    chain = (
        prompt_template
        | chat
    )

    # Add message history support
    conversational_chain = RunnableWithMessageHistory(
    chain,
    get_message_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)


    # Set user input
    user_input = st.text_area("Set up the story:")

    # Initialize session_id
    session_id = "session"  # Could be per-user for multi-user apps

    # Handle response
    if user_input:
        # Convert current session history to messages
        inputs = {"input": user_input}
        response = conversational_chain.invoke(inputs, config={"configurable": {"session_id": session_id}})
        st.write("**Chatbot:**", response.content)

if __name__ == "__main__":
    main()
