import requests
import json

api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjNmNDNjMzE4NWQyMWEwYTMwOTY2NWU3NmM2YjQ3MCIsInN1YiI6IjYyMDJhMWE0NDM5YmUx" \
          "N2IzMmExNjcxYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FhWZUxZRh_oUiHgsCZXUu98iQjogIYbtdGyXgP1xgRI"


def get_api(url):
    response = requests.get("https://api.themoviedb.org/3" + url, headers={
        "Authorization": f"Bearer {api_key}", "Content-Type": "application/json;charset=utf-8"})
    if response.status_code != 200:
        raise Exception(f"Incorrect status code of {response.status_code}")
    else:
        return json.loads(response.content.decode())


def get_popular_media():
    popular_media = set()
    popular_media.update(get_api("/trending/movie/day")["results"] + get_api("/trending/movie/week")["results"])
    popular_media.update(get_api("/trending/tv/day")["results"] + get_api("/trending/tv/week")["results"])
    return [*popular_media]

