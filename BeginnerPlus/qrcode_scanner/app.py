from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        file = request.files["file"]

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        image = cv2.imread(filepath)

        detector = cv2.QRCodeDetector()

        data, points, _ = detector.detectAndDecode(image)

        if data:
            result = data
        else:
            result = "No QR code detected."

        os.remove(filepath)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()