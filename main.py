import json
from hn import get_top_stories, save_to_file


def main():
    # get stories
    print(f"Fetching top stories")
    top_stories = get_top_stories()
    print(f"Fetched top stories successfully")
    # destructure by category
    ask_hn_stories, show_hn_stories, default_stories = (
        top_stories["ask_hn"],
        top_stories["show_hn"],
        top_stories["default"],
    )
    # save extracted stories as json
    save_to_file("out/ask_hn.json", json.dumps(ask_hn_stories))
    print(f"Saved Ask HN stories successfully")
    save_to_file("out/show_hn.json", json.dumps(show_hn_stories))
    print(f"Saved Show HN stories successfully")
    save_to_file("out/default.json", json.dumps(default_stories))
    print(f"Saved default stories successfully")


if __name__ == "__main__":
    main()
