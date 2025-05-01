from typing import Literal, cast
import httpx


def get_client():
    return httpx.Client(base_url="https://hacker-news.firebaseio.com/v0")


def fetch_top_stories(client: httpx.Client):
    r = client.get("/topstories.json")
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
    stories = fetch_top_stories(client=client)
    hn_stories: dict[Literal["default", "ask_hn", "show_hn"], list[dict]] = {
        "default": [],
        "ask_hn": [],
        "show_hn": [],
    }
    for item_id in stories:
        item = get_item(client=client, item_id=item_id)
        item_type = get_item_type(item)
        if item_type == "ask_hn" or item_type == "show_hn" or item_type == "default":
            hn_stories[item_type].append(
                {
                    "by": item["by"],
                    "descendants": item["descendants"],
                    "id": item["id"],
                    "score": item["score"],
                    "time": item["time"],
                    "title": item["title"],
                    "type": item["type"],
                    "url": item["url"],
                }
            )
    return hn_stories


def save_to_file(file_path: str, file_data: str):
    with open(file_path, "w") as f:
        f.write(file_data)
