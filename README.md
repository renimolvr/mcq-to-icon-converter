# MCQ to ICON Format Converter

A free, lightweight web application that converts multiple-choice questions (MCQs) from a plain text file into the **ICON output format** — cleaned, structured, and ready to use.

Built with **Flask** and deployed on **Render**.

---

## ✨ Features

* 📤 Upload a `.txt` file containing MCQ questions
* 🧹 Automatically cleans up messy formatting (extra spaces, newlines, tabs)
* 🔍 Detects options `A)`, `B)`, `C)`, `D)` and their corresponding answer markers
* 🎯 Strips question numbers (`1.`, `Q2)`, `Question 3.` etc.)
* 📊 Shows a live summary — questions converted, options, output lines, skipped blocks
* ⚠️ Reports skipped blocks with details so you can fix them
* 📥 Download the converted file as `<original_name>_ICON.txt`
* 📋 One-click copy to clipboard
* 🎨 Clean, centered, animated ocean-themed UI

---

## 🖼️ How It Works

```text
MCQ TXT file  →  [ Flask app ]  →  ICON formatted output
```

The app parses the input file and produces output in this format:

```text
Question text here?
A) Option 1
B) Option 2
C) Option 3
D) Option 4
ANSWER: A
```

---

## 📁 Project Structure

```text
mcq-to-icon-converter/
├── app.py                 # Flask application + conversion logic
├── requirements.txt       # Python dependencies
├── Procfile               # Production start command (for Render)
├── README.md              # Project documentation
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

### 2. Create a virtual environment

This step is optional but recommended.

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open your browser at:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deploy on Render

1. Push your project to a GitHub repository.
2. Go to [Render](https://render.com/) and sign in with GitHub.
3. Click **New + → Web Service**.
4. Connect your GitHub repository.
5. Use the following settings:

| Setting       | Value                             |
| ------------- | --------------------------------- |
| Environment   | `Python 3`                        |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app`                |
| Instance Type | Free                              |

6. Click **Create Web Service**.

Your application will be available at:

```text
https://your-app-name.onrender.com
```

### ⚠️ Free Tier Note

The Render free tier may put inactive services to sleep. When someone visits after inactivity, the service may require some time to wake up.

---

## 📝 Input File Requirements

* **Format:** `.txt`
* **Encoding:** UTF-8
* **Maximum file size:** 5 MB
* Each question block should contain:

  * A question
  * Four options labelled `A)`, `B)`, `C)`, `D)` or `A.`, `B.`, `C.`, `D.`
  * An answer marker such as `Answer: A`, `Correct: B`, or `Ans - C`

### Example Input

```text
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

### Example Output

```text
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

| Layer             | Technology                           |
| ----------------- | ------------------------------------ |
| Backend           | Python 3, Flask                      |
| Production Server | Gunicorn                             |
| Frontend          | HTML, CSS, Vanilla JavaScript        |
| Fonts             | Sora, Source Serif 4, JetBrains Mono |
| Hosting           | Render                               |

---

## 🐛 Troubleshooting

| Problem                                      | Fix                                                                                    |
| -------------------------------------------- | -------------------------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'app'` | Ensure `app.py` is at the root of the repository, not inside a subfolder.              |
| `Procfile` treated as `Procfile.txt`         | Create the file as `Procfile` without a `.txt` extension.                              |
| `UnicodeDecodeError` on upload               | Save the `.txt` file using UTF-8 encoding.                                             |
| Nothing converts                             | Check that each question contains `A)`, `B)`, `C)`, `D)` options and an answer marker. |
| App takes time to load                       | The Render free tier may experience cold starts after inactivity.                      |

---

## 📜 License

This project is free to use, modify, and distribute for personal and educational purposes.

---

## 🙌 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

## 👤 Author

**Your Name**

* GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)

---

⭐ If you found this useful, consider giving the repository a star!
