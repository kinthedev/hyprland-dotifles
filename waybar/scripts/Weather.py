#!/usr/bin/env python3

import requests
import json
import os

weather_icons = {
    "Sunny": "",
    "Clear": "",
    "Partly cloudy": "",
    "Cloudy": "",
    "Overcast": "",
    "Mist": "",
    "Fog": "",
    "Patchy rain nearby": "",
    "Light rain": "",
    "Moderate rain": "",
    "Heavy rain": "",
    "Light rain shower": "",
    "Moderate or heavy rain shower": "",
    "Thundery outbreaks nearby": "",
    "Patchy snow nearby": "",
    "Light snow": "",
    "Heavy snow": "",
}

try:
    response = requests.get(
        "https://wttr.in/?format=j1",
        headers={"User-Agent": "curl/8.0"},
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    current = data["current_condition"][0]

    temp = current["temp_C"] + "°C"
    feels_like = current["FeelsLikeC"] + "°C"
    humidity = current["humidity"] + "%"
    wind = current["windspeedKmph"] + " km/h"
    visibility = current["visibility"] + " km"
    status = current["weatherDesc"][0]["value"]

    icon = weather_icons.get(status, "")

    tooltip = (
        f"<span size='xx-large'>{temp}</span>\n"
        f"<big>{icon}</big>\n"
        f"<b>{status}</b>\n\n"
        f"🌡 Feels like: {feels_like}\n"
        f"💨 Wind: {wind}\n"
        f"💧 Humidity: {humidity}\n"
        f"👁 Visibility: {visibility}"
    )

    output = {
        "text": f"{icon} {temp}",
        "alt": status,
        "tooltip": tooltip,
        "class": status.lower().replace(" ", "-")
    }

    print(json.dumps(output, ensure_ascii=False))

    cache = (
        f"{icon} {status}\n"
        f"🌡 {temp} (Feels like {feels_like})\n"
        f"💨 {wind}\n"
        f"💧 {humidity}\n"
        f"👁 {visibility}\n"
    )

    cache_file = os.path.expanduser("~/.cache/.weather_cache")

    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(cache)

except Exception as e:
    print(json.dumps({
        "text": "󰖐 N/A",
        "alt": "Error",
        "tooltip": str(e),
        "class": "error"
    }))
