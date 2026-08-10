# 🎥 AI YouTube Video Analyzer

An AI-powered YouTube Video Analyzer that analyzes a YouTube video using only its URL. It generates a video overview, meaningful timestamps, segment summaries, and key insights.

## ✨ Features

* 🔗 Analyze a YouTube video by simply pasting its link
* 📝 Generate an AI-powered video summary
* ⏱️ Generate meaningful timestamps
* 📚 Identify major topics and themes
* 💡 Highlight important learning points
* 🎯 Analyze different sections of the video
* 🖥️ Simple and interactive Streamlit interface

## 📸 Screenshots

### Streamlit Application
<img width="1350" height="622" alt="image" src="https://github.com/user-attachments/assets/3cbf1220-4c88-4ca9-af7c-a8854e9e0f0b" />
<img width="1303" height="595" alt="image" src="https://github.com/user-attachments/assets/1e057dc1-f9ec-4dc8-a609-51f6205ce9c3" />
<img width="1238" height="598" alt="image" src="https://github.com/user-attachments/assets/ab39ea09-c261-4825-bd1d-4bc2b17eeac1" />
<img width="1208" height="628" alt="image" src="https://github.com/user-attachments/assets/7f7bc152-9abf-4c4b-9fba-afcae978edc7" />




## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Agno**
* **Groq LLM**
* **YouTubeTools**
* **python-dotenv**

## 📂 Project Structure

```text
youtube-video-analyzer/
│
├── youtube_analyzer.py
├── ui.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    └── youtube_analyzer.png
```

> 🔐 The `.env` file is not included in the repository because it contains the API key.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd youtube-video-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Setup

Create a `.env` file in the root directory of the project.

Add your own Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

⚠️ **Never share or upload your `.env` file or API key to GitHub.**

The `.gitignore` file contains:

```text
.env
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run ui.py
```

The application will open in your browser.

## 🚀 How It Works

```text
YouTube Video Link
        ↓
   Streamlit UI
        ↓
   Agno AI Agent
        ↓
    YouTubeTools
        ↓
     Groq LLM
        ↓
  Video Analysis
        ↓
Summary + Timestamps + Key Insights
```

## 📊 Output

The analyzer provides:

* 🎥 Video Overview
* ⏱️ Timestamp-based analysis
* 📝 Segment summaries
* 📚 Main topics
* 💡 Key learning points
* 🔍 Important content markers

## 🌟 Future Improvements

* 💬 Chat with the YouTube video
* 📄 Export analysis as PDF
* 🌍 Multi-language support
* 🎯 Automatic chapter generation
* 📊 Advanced video analytics

## 👩‍💻 Author

**Rohini Gavali**

Built with Python, Agno, Groq, and Streamlit.
