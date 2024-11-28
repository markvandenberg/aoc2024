import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def get_full_input(day, session_token):
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookies = {"session": session_token}
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        with open(f"advent_of_code/day{day:02d}/input.txt", "w") as file:
            file.write(response.text)
        print(f"Input for day {day} downloaded successfully.")
    else:
        with open(f"advent_of_code/day{day:02d}/input.txt", "w") as file:
            file.write('')
        print(f"Failed to download input for day {day}. Status code: {response.status_code}")

def get_test_input(day, session_token):
    url = f"https://adventofcode.com/2024/day/{day}"
    cookies = {"session": session_token}
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
 
        samples = soup.find_all('pre')
        for i, sample in enumerate(samples):
            sample_input = sample.get_text()
            with open(f"advent_of_code/day{day:02d}/test_input_{i+1}.txt", "w") as file:
                file.write(sample_input)
        print(f"Test inputs for day {day} downloaded successfully.")
 
        em_items = [em.get_text() for code in soup.find_all('code') for em in code.find_all('em')]
        for i, sample_answer in enumerate(em_items):
            with open(f"advent_of_code/day{day:02d}/assert_answer_{i+1}.txt", "w") as file:
                file.write(sample_answer)
        print(f"Test answers for day {day} downloaded successfully.")
    else:
        for i in range(2):
            with open(f"advent_of_code/day{day:02d}/test_input_{i+1}.txt", "w") as file:
                file.write('')
            with open(f"advent_of_code/day{day:02d}/assert_answer_{i+1}.txt", "w") as file:
                file.write('0')
        print(f"Failed to download sample input for day {day}. Status code: {response.status_code}")

if __name__ == "__main__":
    session_token = ''
    session_token_file_path = os.path.join(os.path.dirname(__file__), "session_token.txt")
    with open(session_token_file_path) as f:
        session_token = f.read()

    today = datetime.now()
    day = today.day if today.month == 12 else int(input("Enter the Advent day: "))
    get_full_input(day, session_token)
    get_test_input(day, session_token)
