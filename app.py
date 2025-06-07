from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

# Load questions from file
with open("ques.txt", "r", encoding="utf-8") as f:
    questions = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/questions")
def get_questions():
    return jsonify(questions)

@app.route("/api/check", methods=["POST"])
def check_answer():
    data = request.get_json()
    question_text = data.get("question")
    user_answer = data.get("answer")

    for q in questions:
        if q["question"] == question_text:
            correct = (q["correct_answer"].lower() == user_answer.lower())
            return jsonify({"correct": correct})

    return jsonify({"error": "Question not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
