from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    amount = None
    from_currency = None
    to_currency = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()

        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url)
        data = response.json()

        rate = data["rates"][to_currency]
        result = amount * rate

    return render_template(
        "index.html",
        result=result,
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency
    )


if __name__ == "__main__":
    app.run()