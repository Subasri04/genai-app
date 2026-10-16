# GenAI Application

A generative AI web application built with Python and Streamlit.

---

## 🛠️ Prerequisites

- **Python 3.10+** (Tested on Python 3.14)
- **Git**
- A Gemini API Key from Google AI Studio

---

## 🚀 Setup Instructions in VS Code

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd genai-app
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```
If python defaults to an older version or doesn't work, use:
```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment
1. On Windows (Command Prompt):
```bash
DOS
venv\Scripts\activate.bat
```
2. On Windows (PowerShell):
```bash
PowerShell
.\venv\Scripts\Activate.ps1
```

3. On macOS / Linux:
```bash
Bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit google-genai python-dotenv
```
### 4. Configure API Key
Create a .env file in the root folder and add your key:

```bash
GEMINI_API_KEY="your-api-key-here"
```

### 5. Running the Application
Launch the Streamlit app:
```bash
streamlit run web-app-sidebar.py
```

