from flask import Flask, render_template, request
import cv2
import os
import tempfile

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        file = request.files.get("file")

        if not file or file.filename == "":
            result = "Please select an image."
            return render_template("index.html", result=result)

        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        filepath = temp_file.name
        temp_file.close()

        try:
            file.save(filepath)

            image = cv2.imread(filepath)

            if image is None:
                result = "Could not read the image."
            else:
                detector = cv2.QRCodeDetector()

                data, points, _ = detector.detectAndDecode(image)

                if data:
                    result = data
                else:
                    result = "No QR code detected."

        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()