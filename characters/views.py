import requests
from django.shortcuts import render

API_URL = "https://rickandmortyapi.com/api/character"


def index(request):
    """Загружает персонажей из Rick and Morty API и передаёт их в шаблон."""
    characters = []
    info = {}
    error = None

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        characters = data.get("results", [])
        info = data.get("info", {})
    except requests.RequestException:
        error = "Не удалось получить данные от Rick and Morty API. Попробуйте обновить страницу позже."

    context = {
        "characters": characters,
        "info": info,
        "error": error,
        "api_url": API_URL,
    }
    return render(request, "characters/index.html", context)
