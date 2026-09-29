```markdown
# MCQ to ICON Format Converter

A free, lightweight web application that converts multiple-choice questions (MCQs) from a plain text file into the **ICON output format** — cleaned, structured, and ready to use.

Built with **Flask** and deployed on **Render**.

---

## ✨ Features

- 📤 Upload a `.txt` file containing MCQ questions
- 🧹 Automatically cleans up messy formatting (extra spaces, newlines, tabs)
- 🔍 Detects options `A)`, `B)`, `C)`, `D)` and their corresponding answer markers
- 🎯 Strips question numbers (`1.`, `Q2)`, `Question 3.` etc.)
- 📊 Shows a live summary — questions converted, options, output lines, skipped blocks
- ⚠️ Reports skipped blocks with details so you can fix them
- 📥 Download the converted file as `<original_name>_ICON.txt`
- 📋 One-click copy to clipboard
- 🎨 Clean, centered, animated ocean-themed UI

---

## 🖼️ How It Works

```
MCQ TXT file  →  [ Flask app ]  →  ICON formatted output
```

The app parses your file using regex patterns and produces output in this exact format:

```
Question text here?
A) Option 1
B) Option 2
C) Option 3
D) Option 4
ANSWER: A
```

---

## 📁 Project Structure

```
mcq-to-icon-converter/
├── app.py                 # Flask application + conversion logic
├── requirements.txt       # Python dependencies
├── Procfile               # Production start command (for Render)
├── README.md              # This file
└── templates/
    └── index.html         # Frontend UI
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/mcq-to-icon-converter.git
cd mcq-to-icon-converter
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**

---

## ☁️ Deploy on Render (Free)

1. Push your code to a GitHub repository.
2. Go to **https://render.com** and sign up with GitHub.
3. Click **New +** → **Web Service**.
4. Connect your repository.
5. Use these settings:

   | Setting | Value |
   |---|---|
   | Environment | `Python 3` |
   | Build Command | `pip install -r requirements.txt` |
   | Start Command | `gunicorn app:app` |
   | Instance Type | **Free** |

6. Click **Create Web Service**.

Your app will be live at:

```
https://your-app-name.onrender.com
```

> ⚠️ **Free tier note:** The app sleeps after 15 minutes of inactivity. The next visit takes ~50 seconds to wake up. Use [UptimeRobot](https://uptimerobot.com) (free) to ping the URL every 5 minutes and keep it awake.

---

## 📝 Input File Requirements

- Format: **`.txt`** only
- Encoding: **UTF-8**
- Max size: **5 MB**
- Each question block must contain:
  - A question text
  - Four options labelled `A)`, `B)`, `C)`, `D)` (or `A.`, `B.`, `C.`, `D.`)
  - An answer marker like `Answer: A`, `Correct: B`, `Ans - C`

### Example input

```
1. What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome
Answer: C

2. What is 2 + 2?
A) 3
B) 4
C) 5
D) 6
Correct: B
```

### Example output

```
What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome
ANSWER: C
What is 2 + 2?
A) 3
B) 4
C) 5
D) 6
ANSWER: B
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Production Server | Gunicorn |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Fonts | Sora, Source Serif 4, JetBrains Mono |
| Hosting | Render (free tier) |

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'app'` | Ensure `app.py` is at the **root** of the repo, not inside a subfolder. |
| `Procfile` treated as `Procfile.txt` | On Windows, use VS Code or Notepad++ to create it without a `.txt` extension. |
| `UnicodeDecodeError` on upload | Save your `.txt` file in **UTF-8** encoding. |
| Nothing converts | Check that each question has `A) B) C) D)` options and an `Answer:` marker. |
| App takes 50s to load | Free-tier cold start. Use UptimeRobot to keep it awake. |

---

## 📜 License

This project is free to use, modify, and distribute for personal or educational purposes.

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 👤 Author

**Your Name**
- GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)

---

⭐ If you found this useful, consider giving the repository a star!
```

---

### 📝 What to Customize Before Committing

Before you push the README, replace these placeholders with your real details:

| Placeholder | Replace with |
|---|---|
| `YOUR-USERNAME` | Your GitHub username (appears 2 times) |
| `your-app-name` | Your actual Render app name |
| `Your Name` | Your actual name |
| Author GitHub link | Your profile URL |

---

### 📁 Updated Folder Structure

```
your-project/
├── app.py
├── requirements.txt
├── Procfile
├── README.md              ← NEW (safe to add)
└── templates/
    └── index.html
```

### ✅ Why a README is Safe

- **Flask** ignores it — it only looks for Python files and `templates/`.
- **Gunicorn** ignores it — it only imports `app:app`.
- **Render's build** ignores it — it only runs `pip install -r requirements.txt`.
- **GitHub** displays it on your repo homepage — making your project look professional.

So go ahead — add it, push it, and your project will look polished and well-documented. 🚀
