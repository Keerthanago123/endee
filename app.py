
from flask import Flask,render_template,request,jsonify
import json
from backend.resume_parser import extract_text
from backend.vector_search import recommend_jobs
from backend.chatbot import reply

app=Flask(__name__)

with open("jobs.json") as f:
    jobs=json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload",methods=["POST"])
def upload():
    file=request.files["resume"]
    path="resume.pdf"
    file.save(path)

    text=extract_text(path)
    results=recommend_jobs(text,jobs)

    return jsonify(results)

@app.route("/chat",methods=["POST"])
def chat():
    msg=request.json["message"]
    return jsonify({"reply":reply(msg)})

if __name__=="__main__":
    app.run(debug=True)
