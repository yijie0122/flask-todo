import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 示範任務資料
tasks = [
    {
        "task_name": "繳交 Web 作業二",
        "priority": "高 (High)",
        "due_and_notes": "本週五前上傳到數位學習平台"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_name = request.form.get("task_name")
        priority = request.form.get("priority")
        due_and_notes = request.form.get("due_and_notes")
        
        if task_name and priority and due_and_notes:
            tasks.append({
                "task_name": task_name,
                "priority": priority,
                "due_and_notes": due_and_notes
            })
        return redirect(url_for("index"))
        
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)