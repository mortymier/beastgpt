# 🐾 BeastGPT

**AI-Powered Animal Battle Simulator**

BeastGPT is an educational AI chatbot that compares two animals and simulates a **friendly battle outcome** based on their real-life characteristics.

The chatbot analyzes animal traits such as **size, strength, speed, and behavior**, then determines which animal would most likely win in a hypothetical scenario.

This project is designed for **young learners (ages 6–12)** to make learning about wildlife fun and interactive.

---

# 🌐 Live App

**🔗 [Open BeastGPT on Streamlit Cloud] https://beastgpt.streamlit.app/**

---

# 🎯 Project Goal

The goal of BeastGPT is to help students learn about animals through a **comparative battle simulation**.

⚠️ The battles are **fictional and educational**.
The system **does NOT promote animal cruelty or violence**.

---

# ⚙️ Features

* Select **two animals** to simulate a battle
* Compare animal **traits and abilities**
* AI determines the **most likely winner**
* Kid-friendly explanations
* Optional **random animal selection**

---

# 🧰 Technologies Used

* **Python**
* **Streamlit**
* **Groq API**
* **Llama 3.1 8B Instant Model**
* **Llama 3.3 70b Versatile**

---

# 📦 Installation Guide

##  Clone the Repository

```bash
cd beastgpt
```

---

##  Install Required Libraries

Install the dependencies:

```bash
pip install streamlit
pip install groq
```

or

```bash
pip install -r requirements.txt
```

---

# 🔐 Setting Up API Key

BeastGPT uses the **Groq AI API**, which follows the OpenAI API format.

Create a folder named:

```
.streamlit
```

Inside it, create a file called:

```
secrets.toml
```

project structure:

```
beastgpt/
│
├── app.py
├── animals.py
├── beastgpt_logo.png
│
└── .streamlit/
    └── secrets.toml
```

---

## secrets.toml Example

Inside `secrets.toml`, add your **Groq API key**:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

**Important:**
Never upload this file to GitHub.
Add it to `.gitignore`.

Example `.gitignore`:

```
.streamlit/secrets.toml
```

---

# AI Model Configuration

BeastGPT connects to Groq using this configuration:

```python
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
```

Models used:

```
llama-3.1-8b-instant
llama-3.3-70b-versatile
```

---

# Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Streamlit will open in your browser:

```
http://localhost:8501
```

---

# 📚 Educational Purpose

This chatbot is built for **learning and entertainment**.

The battle results are **simplified comparisons based on known animal traits** and are not intended to represent real-world animal fights.

---

# 👨‍💻 Contributors

* Flores, E.J Boy Gabriel
* Gabiana, Nicolo Francis
* Oswa, Yusuf Bin Mohammad Ali
* Perales, Clint
* Saniel, Mitchel Gabrielle

---

# 📜 License

This project is for **educational use** as part of the CSIT349 course.
