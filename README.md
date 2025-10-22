
# Story Generator Chatbot

The **Story Generator Chatbot** is an AI-powered storytelling application built with **Streamlit** and **LangChain**, integrated with **Groq’s LLaMA-3.3-70B model**.
It generates creative and coherent stories from user prompts, maintaining short-term conversational memory to enhance narrative consistency.

---

## Overview

This chatbot acts as a creative writing assistant capable of producing complete, original stories based on short prompts.
It leverages Groq’s LLM through LangChain to deliver structured and imaginative narratives inspired by novels, anime, and films.

The project demonstrates how to:

* Integrate **LangChain** components for prompt creation and memory management
* Use **Groq’s LLaMA models** via LangChain wrappers
* Implement **conversational context and message history**
* Build a **Streamlit UI** for interactive real-time chat experiences

---

## Features

* Generates full, creative stories from brief prompts
* Adjustable conversational memory window (1–10)
* Model selection via Streamlit sidebar
* Maintains short-term conversation history for better coherence
* Simple and responsive Streamlit-based web interface

---

## Architecture

| Component               | Purpose                                                     |
| ----------------------- | ----------------------------------------------------------- |
| **Streamlit**           | Provides the web-based user interface.                      |
| **LangChain**           | Handles prompt templates, chaining, and message history.    |
| **ChatGroq**            | Connects to Groq’s LLaMA-3.3-70B model for text generation. |
| **Conversation Memory** | Stores short-term chat history for contextual responses.    |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Story-Teller-Groq-Langchain.git
cd Story-Teller-Groq-Langchain
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

Alternatively, set it in your terminal session:

```bash
export GROQ_API_KEY=your_groq_api_key_here   # macOS/Linux
setx GROQ_API_KEY "your_groq_api_key_here"   # Windows
```

---

## Requirements

`requirements.txt`

```
streamlit
python-dotenv
langchain
langchain-core
langchain-groq
```

---

## Running the Application

Run the Streamlit app with:

```bash
streamlit run app.py
```

Once the server starts, open your browser and navigate to the displayed local URL (usually `http://localhost:8501`).

---

## Usage

1. Enter a story setup or scenario in the text box.
2. Adjust the conversational memory length and model in the sidebar.
3. Submit the input. The chatbot will return a complete, creative story.

Example input:

```
A young astronaut stranded on Mars discovers an ancient alien ruin.
```

---

## Disclaimer

This chatbot is intended for creative and educational purposes only.
The generated stories are fictional and may coincidentally resemble existing works due to shared narrative patterns.

---

## Future Enhancements

* Support for multiple Groq models and runtime switching
* Genre and tone customization options
* Export functionality for stories (text or PDF)
* Multi-user session tracking with persistent chat history

---
