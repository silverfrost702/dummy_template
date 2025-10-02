import requests

def fetch_data(url="https://jsonplaceholder.typicode.com/todos/1"):
    """Dummy API fetch"""
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
