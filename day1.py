import requests
from dotenv import load_dotenv
import os
import re

load_dotenv()

URL = "https://adventofcode.com/2023/day/1/input"

cookies = {
    "session": os.getenv("aoc_session"),
}

response = requests.get(URL, cookies=cookies)

vals = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
valid_nos = {v:i+1 for i, v in enumerate(vals)}
print(valid_nos)
if __name__ == "__main__":
    with open(r"C:\Users\n529634\OneDrive - British Airways Plc\personal\code\adventOfCode23\out.txt", "w") as f:
        f.write(response.text)



    with open("out.txt", "r") as f:
        data = f.readlines()


    sum = 0
    for line in data:
        numbs_in_line = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)
        first_no = numbs_in_line[0]
        last_no = numbs_in_line[-1]

        if first_no in valid_nos.keys():
            first_no_int = valid_nos[first_no]
            first_no = first_no_int

        if last_no in valid_nos.keys():
            last_no_int = valid_nos[last_no]
            last_no = last_no_int

        # print(line)
        # print(numbs_in_line)
        # print(first_no,last_no)


        number_as_str = f"{str(first_no)}{str(last_no)}"

        final_no = int(number_as_str)

        sum += final_no

    print(sum)
    
