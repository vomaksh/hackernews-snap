from typing import cast
import httpx


def get_client():
    return httpx.Client(base_url="https://hacker-news.firebaseio.com/v0")


def fetch_top_stories(client: httpx.Client):
    r = client.get("/topstories.json")
    return r.json()


def fetch_best_stories(client: httpx.Client):
    r = client.get("/beststories.json")
    return r.json()


def fetch_ask_stories(client: httpx.Client):
    r = client.get("/askstories.json")
    return r.json()


def fetch_show_stories(client: httpx.Client):
    r = client.get("/showstories.json")
    return r.json()


def get_item(client: httpx.Client, item_id: int):
    r = client.get(f"/item/{item_id}.json")
    return r.json()


def get_item_type(item: dict):
    item_title = cast(str, item["title"])
    item_type = cast(str, item["type"])
    if item_type == "story":
        if item_title.startswith("Ask HN:"):
            return "ask_hn"
        elif item_title.startswith("Show HN:"):
            return "show_hn"
        else:
            return "default"
    return item_type


def get_top_stories():
    client = get_client()
    top_stories = fetch_top_stories(client=client)
    items = []
    for item_id in top_stories:
        item = get_item(client=client, item_id=item_id)
        if item.get("kids"):
            del item["kids"]
        items.append(item)
    return items


def get_best_stories():
    client = get_client()
    top_stories = fetch_best_stories(client=client)
    items = []
    for item_id in top_stories:
        item = get_item(client=client, item_id=item_id)
        if item.get("kids"):
            del item["kids"]
        items.append(item)
    return items


def get_ask_stories():
    client = get_client()
    ask_stories = fetch_ask_stories(client=client)
    items = []
    for item_id in ask_stories:
        item = get_item(client=client, item_id=item_id)
        if item.get("kids"):
            del item["kids"]
        items.append(item)
    return items


def get_show_stories():
    client = get_client()
    show_stories = fetch_show_stories(client=client)
    items = []
    for item_id in show_stories:
        item = get_item(client=client, item_id=item_id)
        if item.get("kids"):
            del item["kids"]
        items.append(item)
    return items


def save_to_file(file_path: str, file_data: str):
    with open(file_path, "w") as f:
        f.write(file_data)
