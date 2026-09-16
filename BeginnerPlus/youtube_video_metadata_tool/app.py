from flask import Flask, render_template, request
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import requests
import os
import re

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("YOUTUBE_API_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    video = None
    duration = None

    if request.method == "POST":
        video_url = request.form["video_url"]

        parsed_url = urlparse(video_url)
        video_id = parse_qs(parsed_url.query).get("v", [None])[0]

        url = "https://www.googleapis.com/youtube/v3/videos"

        params = {
            "part": "snippet,contentDetails,statistics",
            "id": video_id,
            "key": API_KEY
        }

        response = requests.get(url, params=params)

        data = response.json()

        video = data["items"][0]

        content_details = video["contentDetails"]

        duration = content_details["duration"]

        match = re.match(
            r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?",
            duration
        )

        hours = int(match.group(1) or 0)
        minutes = int(match.group(2) or 0)
        seconds = int(match.group(3) or 0)

        if hours:
            duration = f"{hours}:{minutes:02d}:{seconds:02d}"
        else:
            duration = f"{minutes}:{seconds:02d}"

    return render_template(
        "index.html",
        video=video,
        duration=duration
    )


if __name__ == "__main__":
    app.run()