from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    qr_code = None

    if request.method == "POST":

        data = request.form["data"]

        qr = qrcode.make(data)
        qr.save("static/qr_code.png")

        qr_code = "qr_code.png"

    return render_template("index.html", qr_code=qr_code)


if __name__ == "__main__":
    app.run()