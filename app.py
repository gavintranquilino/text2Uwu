from TextToOwO.owo import text_to_owo
from flask import Flask, render_template, request

app = Flask(__name__)

results = []


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("base.html", result="")
    else:
        content = request.form["content"]

        if content != "":
            results.append(text_to_owo(content).strip())
            return render_template("base.html", results=results)

        else:
            return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
