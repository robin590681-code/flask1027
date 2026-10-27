
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 儲存學生資料
students = []

# 首頁：顯示學生資料
@app.route("/")
def index():
    return render_template("index.html", students=students)

# 新增學生資料
@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    student_id = request.form.get("student_id", "").strip()
    department = request.form.get("department", "").strip()

    # 確認三個欄位都有填寫
    if name and student_id and department:
        student = {
            "name": name,
            "student_id": student_id,
            "department": department
        }

        students.append(student)

    return redirect(url_for("index"))

# 啟動 Flask
if __name__ == "__main__":
    app.run(debug=True)
