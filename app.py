from flask import Flask, render_template, request

app = Flask(__name__)

def ultra_encode(text):
    return ''.join(str(ord(char) + 1000) + '#' for char in text)

def ultra_decode(code):
    return ''.join(chr(int(c) - 1000) for c in code.strip().split('#') if c)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encode():
    msg = request.form.get("message", "")
    result = ultra_encode(msg)
    return render_template("result.html", result=result)

@app.route("/decode", methods=["POST"])
def decode():
    code = request.form.get("code", "")
    result = ultra_decode(code)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
