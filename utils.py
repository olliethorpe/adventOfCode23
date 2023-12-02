import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_input(day):
    print("Obtaining input via https")

    URL = "https://adventofcode.com/2023/day/{}/input".format(day)

    cookies = {
        "session": os.getenv("aoc_session"),
    }

    response = requests.get(URL, cookies=cookies)
    return response


def write_input_to_file(day, path):
    response = get_input(day)

    with open(path, "x") as f:
        f.writelines(response.text)


def cache_and_read_input(day) -> list[str]:
    out_file_path = f"./outputs/day{day}.txt"
    is_cached = os.path.isfile(out_file_path)

    if not is_cached:
        write_input_to_file(day, out_file_path)

    with open(out_file_path, "r") as f:
        read_input = f.read()

    return read_input


if __name__ =="__main__":
    cache_and_read_input(2)