"""
MCQ to ICON Format Converter - Flask version

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000
"""

import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB upload limit


# =========================================================
# CONVERSION LOGIC
# =========================================================

ANSWER_PATTERN = re.compile(
    r"\b(?:answer|answe|correct\s+answer|correct\s+option|correct)"
    r"\s*(?::|=|-)\s*[\(\[]?\s*([A-Da-d])\s*[\)\]]?",
    re.IGNORECASE,
)

QUESTION_NUMBER_PATTERN = re.compile(
    r"^(?:Q(?:uestion)?\s*)?\d+\s*(?:\\?\)\.?|\\?\.|\))\s*",
    re.IGNORECASE,
)

OPTION_PATTERN = re.compile(r"(?:^|\s)([A-Da-d])\s*(?:\)|\.)\s*")


def clean_text(text):
    """Convert multiple spaces/newlines/tabs into a single space."""
    text = text.replace("\r", " ").replace("\n", " ").replace("\t", " ")
    return re.sub(r"\s+", " ", text).strip()


def remove_question_number(text):
    """1. Q / 2) Q / 3). Q / Q1. Q  ->  Q"""
    return QUESTION_NUMBER_PATTERN.sub("", text.strip()).strip()


def find_answer(text):
    """Detect an answer marker anywhere in the text."""
    return ANSWER_PATTERN.search(text)


def get_option_matches(text):
    """Find A/B/C/D option markers anywhere in a block."""
    return list(OPTION_PATTERN.finditer(text))


def parse_mcq_block(block, answer):
    block = clean_text(block)
    if not block:
        return None

    matches = get_option_matches(block)
    if len(matches) < 4:
        return None

    # First valid A-B-C-D sequence
    selected = None
    for i in range(len(matches) - 3):
        letters = [matches[i + k].group(1).upper() for k in range(4)]
        if letters == ["A", "B", "C", "D"]:
            selected = matches[i:i + 4]
            break
    if selected is None:
        return None

    question = remove_question_number(block[:selected[0].start()].strip())

    options = {}
    for i in range(4):
        start = selected[i].end()
        end = selected[i + 1].start() if i < 3 else len(block)
        options[selected[i].group(1).upper()] = block[start:end].strip()

    if not question:
        return None
    for letter in "ABCD":
        if not options.get(letter):
            return None
    if answer not in ("A", "B", "C", "D"):
        return None

    return {
        "question": question,
        "A": options["A"],
        "B": options["B"],
        "C": options["C"],
        "D": options["D"],
        "answer": answer,
    }


def convert_to_icon(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    mcqs, skipped = [], []
    previous_end = 0

    for m in ANSWER_PATTERN.finditer(text):
        block = text[previous_end:m.start()]
        answer = m.group(1).upper()

        mcq = parse_mcq_block(block, answer)
        if mcq is not None:
            mcqs.append(mcq)
        else:
            cleaned = clean_text(block)
            if cleaned:
                skipped.append({"block": cleaned, "answer": answer})

        previous_end = m.end()

    remaining = clean_text(text[previous_end:])
    if remaining:
        skipped.append({"block": remaining, "answer": None})

    lines = []
    for q in mcqs:
        lines += [
            q["question"],
            f"A) {q['A']}",
            f"B) {q['B']}",
            f"C) {q['C']}",
            f"D) {q['D']}",
            f"ANSWER: {q['answer']}",
        ]

    return "\n".join(lines), mcqs, skipped


# =========================================================
# ROUTES
# =========================================================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    file = request.files.get("file")
    if file is None or not file.filename:
        return jsonify(error="No file was uploaded."), 400
    if not file.filename.lower().endswith(".txt"):
        return jsonify(error="Only .txt files are supported."), 400

    try:
        text = file.read().decode("utf-8")
    except UnicodeDecodeError:
        return jsonify(
            error="The file could not be read as UTF-8. "
                  "Save the TXT file as UTF-8 and try again."
        ), 400

    try:
        converted, mcqs, skipped = convert_to_icon(text)
    except Exception as exc:  # pragma: no cover
        return jsonify(error=f"An error occurred while processing the file: {exc}"), 500

    base = file.filename.rsplit(".", 1)[0]
    return jsonify(
        converted=converted,
        questions=len(mcqs),
        options=len(mcqs) * 4,
        lines=len(mcqs) * 6,
        skipped=skipped,
        download_name=f"{base}_ICON.txt",
    )


@app.errorhandler(413)
def too_large(_):
    return jsonify(error="File is too large (limit 5 MB)."), 413


if __name__ == "__main__":
    app.run(debug=False)
