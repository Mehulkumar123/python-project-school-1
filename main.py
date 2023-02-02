import requests
import re
from datetime import datetime
import ast
import time
import random
import loading as load
import facts as Fact
from fuzzywuzzy import process
from termcolor import colored

load.loading_animation(1)

def answer_question(query, data_set):
    # Check if the answer is already in the data set
    if query in data_set:
        return (data_set[query], True)

    # Check if the user is asking a math question
    match = re.search(r"^\s*(\d+\s*[+\-*/%^]\s*\d+)\s*$", query)
    if match:
        try:
            # Evaluate the mathematical expression and return the result
            expression = match.group(1)
            result = str(eval(expression))
            return (result, False)
        except:
            return ("Sorry, I couldn't understand your question.", False)

    # If the answer is not in the data set or a math question, search the DuckDuckGo Instant Answer API
    response = requests.get(f"http://api.duckduckgo.com/?q={query}&format=json")
    data = response.json()

    # Extract the answer from the API response
    answer = data.get("AbstractText")

    # If there is no answer, return a default message
    if not answer:
        # Suggest a query based on the closest match in the data set
        closest_match = process.extractOne(query, data_set.keys(), scorer=fuzzywuzzy.fuzz.token_sort_ratio)
        if closest_match[1] >= 60:
            return (f"Did you mean '{closest_match[0]}'?\n{data_set[closest_match[0]]}", False)
        return ("Sorry, I couldn't find an answer to your question.", False)

    # Add the answer to the data set for future use
    data_set[query] = answer
    with open("data_set.txt", "a") as f:
        f.write(f"{query}:{answer}\n")

    return (answer, False)

# Load the data set from the text file
data_set = {}
try:
    with open("data_set.txt", "r") as f:
        for line in f:
            query, answer = line.strip().split(":")
            data_set[query] = answer
except FileNotFoundError:
    open("data_set.txt", "w").close()


def print_with_typing_animation(summary):
    delay = 0.005
    for char in summary:
        print(char, end="", flush=True)
        time.sleep(delay)


print_with_typing_animation(colored(f"Welcome to the Question and Answer Program! ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})", "magenta"))
print_with_typing_animation(Fact.generate_fun_fact())

# Example usage
while True:
    question = input("\nWhat's your question? (type 'exit' to quit) ")

    # Allow the user to exit the program
    if question.lower() == "exit":
        break

    answer, is_data_set = answer_question(question, data_set)

    # Display the answer with a typing animation
    for char in answer:
        print(colored(char, "yellow") if not is_data_set else colored(char, "green"), end="", flush=True)
        time.sleep(random.uniform(0.001, 0.01))
    print("\n")
