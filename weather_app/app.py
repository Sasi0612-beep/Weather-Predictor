import os
import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

app = Flask(__name__)
app.secret_key = "replace-with-a-random-secret"  # needed for flash messages
API_KEY = os.getenv("OPENWEATHER_API_KEY", "6a9a6c17f63336ef20e34bac34cc7903")  # fallback

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str, units: str = "metric", lang: str = "en"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,  # "metric"=°C, "imperial"=°F
        "lang": lang
    }
    r = requests.get(BASE_URL, params=params, timeout=10)
    data = r.json()

    # Handle errors from API
    if r.status_code != 200 or str(data.get("cod")) != "200":
        # Try to extract message from API
        msg = data.get("message", "Unable to fetch weather.")
        raise ValueError(msg)

    # Extract useful fields
    main = data.get("main", {})
    wind = data.get("wind", {})
    sys = data.get("sys", {})
    weather_list = data.get("weather", [])
    weather_desc = weather_list[0]["description"] if weather_list else "N/A"

    result = {
        "city": f'{data.get("name", city)}, {sys.get("country", "")}',
        "temp": main.get("temp"),
        "feels_like": main.get("feels_like"),
        "humidity": main.get("humidity"),
        "pressure": main.get("pressure"),
        "wind_speed": wind.get("speed"),
        "condition": weather_desc.capitalize(),
        "icon": weather_list[0].get("icon") if weather_list else None,
        "units_label": "°C" if units == "metric" else "°F"
    }
    return result

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        units = request.form.get("units", "metric")
        lang = request.form.get("lang", "en")

        if not city:
            flash("Please enter a city name.")
            return redirect(url_for("home"))

        try:
            weather = fetch_weather(city, units=units, lang=lang)
            return render_template("result.html", weather=weather, units=units, lang=lang)
        except ValueError as e:
            flash(f"Error: {e}")
            return redirect(url_for("home"))
        except requests.RequestException:
            flash("Network error. Please try again.")
            return redirect(url_for("home"))

    return render_template("index.html")

if __name__ == "__main__":
    # Run: python app.py
    app.run(debug=True)