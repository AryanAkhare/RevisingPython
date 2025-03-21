from flask import Flask, render_template, request
from weather import get_curr_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city', 'Nagpur').strip()

    # Fetch weather data
    weather_data = get_curr_weather(city)  # ✅ Fix: Define `weather_data` before using it

    # Check if API returned a valid city
    if weather_data.get('cod') != 200:  # ✅ Fix: Use `.get()` instead of `weather_data('cod')`
        return render_template('citynotfound.html')

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
