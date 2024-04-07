import dramatiq
import requests

@dramatiq.actor
def fetch_cat_fact():
    try:
        response = requests.get("https://cat-fact.herokuapp.com/facts")
        response.raise_for_status()
        cat_fact = response.json()[0]["text"]
        return cat_fact
    except Exception as e:
        raise e
