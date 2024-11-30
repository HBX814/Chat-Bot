# Enhanced API Code Generator with Groq

Welcome to the **Enhanced API Code Generator**! This Streamlit app leverages the Groq API to generate, explain, and improve API code based on user-provided prompts. It also visualizes workflows using Mermaid syntax.

---

## 🚀 Features

- **Code Generation**  
  Generate API code for various environments (e.g., local, production) based on user prompts.

- **Workflow Diagram**  
  Automatically create workflow diagrams in Mermaid syntax by analyzing generated API code.

- **Code Explanation**  
  Get detailed explanations for the generated code.

- **Code Improvements**  
  Receive suggestions to enhance the quality and structure of your generated code.

- **Download Option**  
  Save the generated code as a `.js` or `.py` file.

- **Prompt History**  
  View and revisit previously generated code and prompts.

---

## 🛠️ Getting Started

### Prerequisites
- **Python 3.9+**
- A `.env` file containing a valid `GROQ_API_KEY`.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Add your Groq API key to a .env file:
   ```bash
   GROQ_API_KEY=your_api_key_here
6. Run the application:
   ```bash
   streamlit run app.py

### Usage
1. Enter a prompt describing the API you want to generate (e.g., "Create a WebSocket chat application with Redis, Kafka, and PostgreSQL in Node.js").
2. Select the environment (local or production).
3. Click Generate to:
4. View the generated code.
   - *Download the code.*
   - *Visualize the workflow as a Mermaid diagram.*
   - *Get a detailed explanation.*
   - *View improvement suggestions.*
   - *Access previous prompts and code from the Prompt History section.*

