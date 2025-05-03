import json
from hn import (
    get_ask_stories,
    get_best_stories,
    get_show_stories,
    get_top_stories,
    save_to_file,
)


def main():
    # top stories
    print("Fetching top stories")
    top_stories = get_top_stories()
    save_to_file("out/topstories.json", json.dumps(top_stories))
    print("Saved top stories successfully")

    # best stories
    print("Fetching best stories")
    best_stories = get_best_stories()
    save_to_file("out/beststories.json", json.dumps(best_stories))
    print("Saved best stories successfully")

    # ask stories
    print("Fetching ask stories")
    ask_stories = get_ask_stories()
    save_to_file("out/askstories.json", json.dumps(ask_stories))
    print(f"Saved ask stories successfully")

    # show stories
    print("Fetching show stories")
    show_stories = get_show_stories()
    save_to_file("out/showstories.json", json.dumps(show_stories))
    print(f"Saved show stories successfully")


if __name__ == "__main__":
    main()
