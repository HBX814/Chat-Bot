# Required imports
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
import re

# Load environment variables from .env file
load_dotenv()

# Access the API key securely from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


# Function to generate API code using Groq with error handling
def generate_api(prompt, environment="local"):
    try:
        if not GROQ_API_KEY:
            return "API key is missing. Please provide a valid Groq API key."

        # Customize prompt based on environment
        env_prompt = f"{prompt} for {environment} environment"

        # Groq API call for code generation
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": env_prompt}],
            temperature=1,
            max_tokens=1500,
            top_p=1
        )

        # Access the message content directly from the choices list
        generated_code = completion.choices[0].message.content
        return generated_code.strip()

    except Exception as e:
        return f"Error generating API: {str(e)}, completion response: {completion}"


# Function to generate a workflow diagram using Mermaid syntax
def generate_workflow_diagram(api_code):
    services = re.findall(r"app\.use|app\.get|app\.post|app\.put|app\.delete|Kafka|Redis|PostgreSQL", api_code)

    # Create a basic Mermaid flowchart based on detected services and endpoints
    mermaid_code = "graph TD;\n    Start[API Start]"
    for service in services:
        service_name = service.split('.')[1] if '.' in service else service
        mermaid_code += f"\n    Start --> {service_name}[{service_name} Endpoint]"

    return mermaid_code


# Function to generate code explanations with Groq
def generate_code_explanation(generated_code):
    try:
        explanation_prompt = f"Explain the following code in detail: {generated_code}"
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": explanation_prompt}],
            temperature=1,
            max_tokens=700,
            top_p=1
        )

        # Access the explanation from the message content
        explanation = completion.choices[0].message.content
        return explanation.strip()
    except Exception as e:
        return f"Error generating explanation: {str(e)}"


# Function to suggest improvements with Groq
def suggest_improvements(generated_code):
    try:
        improvement_prompt = f"Suggest improvements for the following code: {generated_code}"
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": improvement_prompt}],
            temperature=1,
            max_tokens=700,
            top_p=1
        )

        # Access suggestions from the message content
        suggestions = completion.choices[0].message.content
        return suggestions.strip()
    except Exception as e:
        return f"Error generating suggestions: {str(e)}"


# Streamlit App Interface
st.title("Enhanced API Code Generator")

# Store prompt history in session state
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []

# Prompt input from user
prompt = st.text_input("Enter a prompt to generate API code",
                       "Create a WebSocket chat application with Redis, Kafka, and PostgreSQL in Node.js")

environment = st.radio("Select the environment", ("local", "production"))

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating code..."):
            generated_code = generate_api(prompt, environment=environment)
            if "Error" in generated_code:
                st.error(generated_code)
            else:
                st.success("Code generated successfully!")
                st.code(generated_code, language="javascript" if "Node.js" in prompt else "python")
                st.session_state.prompt_history.append((prompt, generated_code, environment))

                # Option to download the generated code as a .js or .py file
                filename = "generated_api.js" if "Node.js" in prompt else "generated_api.py"
                st.download_button(
                    label="Download Code as File",
                    data=generated_code,
                    file_name=filename,
                    mime="text/x-javascript" if "Node.js" in prompt else "text/x-python"
                )

                # Generate workflow diagram
                st.subheader("Workflow Diagram")
                workflow_diagram = generate_workflow_diagram(generated_code)
                st.markdown(f"```mermaid\n{workflow_diagram}\n```")

                # Generate code explanation
                st.subheader("Code Explanation")
                explanation = generate_code_explanation(generated_code)
                st.text(explanation)

                # Suggest improvements
                st.subheader("Improvement Suggestions")
                suggestions = suggest_improvements(generated_code)
                st.text(suggestions)

    else:
        st.error("Please provide a prompt!")

# Show prompt history
if st.session_state.prompt_history:
    st.subheader("Prompt History")
    for i, (past_prompt, past_code, past_env) in enumerate(st.session_state.prompt_history):
        st.text(f"Prompt {i + 1} ({past_env}): {past_prompt}")
        with st.expander(f"View Generated Code for Prompt {i + 1}"):
            st.code(past_code, language="javascript" if "Node.js" in past_prompt else "python")

# Footer
st.write("Powered by Groq and Streamlit")
