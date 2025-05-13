# weather-condition-app

A simple Python console application that fetches and displays current weather data for a given city using the [OpenWeatherMap API](https://openweathermap.org/api).  
The application also keeps track of previously queried cities.

---

## Setup

1. Sign up to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your free API key.
2. Open the code and enter your own API key:
   ```python
   apikey = "ENTER_YOUR_API_KEY"
   ```
3. Run the code using Python.

---

## Features

- Get current weather conditions by city name.
- View a list of previously queried cities.
- Outputs are displayed in Turkish (`lang=tr`) and use metric units (`units=metric`).
- Gracefully handles incorrect city names or network errors.

---

## API Info

This app uses the `/data/2.5/weather` endpoint from OpenWeatherMap.  
Example query:

```plaintext
https://api.openweathermap.org/data/2.5/weather?q=istanbul&appid=YOUR_API_KEY&units=metric&lang=tr
```

- `q`: City name (e.g., `vienna`, `wien`, `viyana` — all supported)
- `appid`: Your API key
- `units=metric`: Uses Celsius and metric system
- `lang=tr`: Returns weather descriptions in Turkish

Useful resources:  
[API Parameters and Fields](https://openweathermap.org/weather-data)  
[API FAQ](https://openweathermap.org/faq#:~:text=with%20your%20system%3F-,APIs,-What%20are%20the)

---

## Example API JSON Response

```json
{
  "coord": {"lon": 30.52, "lat": 50.45},
  "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
  "main": {
    "temp": 283.35,
    "feels_like": 280.9,
    "temp_min": 283.35,
    "temp_max": 283.35,
    "pressure": 1023,
    "humidity": 60
  },
  "wind": {"speed": 3, "deg": 240},
  "clouds": {"all": 0},
  "sys": {"country": "UA", "sunrise": 1611562067, "sunset": 1611595751},
  "name": "Kiev",
  "cod": 200
}
```

This response is parsed in the code to extract:
- `"weather"[0]["description"]`
- `"main"]["temp"]`
- `"main"]["humidity"]`

---

## Example Output using my own API key

![havadurumu_output](https://github.com/user-attachments/assets/05a5d589-fe08-42c0-be22-8255e8e03d5f)


## Notes
- This project was originally created in May and June 2024 as part of my "Algorithms and Programming II" course. Before uploading it to GitHub, the code was revised.
- Assistance from various educational and programming-related sources was used during the development of this project, as part of the learning process.
- This code was developed for educational purposes as part of a course project.
- All prompts and messages are in Turkish.
- Thanks to OpenWeatherMap for providing free API.

## Libraries Used

- `requests` (Apache License 2.0)

