import time
import datetime
import requests
import re
import ast
import random
import wikipedia
import animation as ani
import loading as load
from datetime import datetime
import facts as Fact
from fuzzywuzzy import process, fuzz
from termcolor import colored

# Function to answer questions, it takes the query and a data_set as input
def answer_question(query, data_set):
    
    # Check if the query is already present in the data_set
    if query in data_set:
        return (data_set[query], True)
    
    # Check if the query is a mathematical expression
    match = re.search(r"^\s*(\d+\s*[+\-*/%^]\s*\d+)\s*$", query)
    if match:
        try:
            expression = match.group(1)
            result = str(ast.literal_eval(expression))
            return (result, False)
        except:
            raise ValueError("Couldn't evaluate the expression.")
    
    # Call the DuckDuckGo API to get the answer to the query
    try:
        response = requests.get(f"http://api.duckduckgo.com/?q={query}&format=json")
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise ValueError("Error making the API request.") from e
    
    # Get the abstract text from the API response
    answer = data.get("AbstractText")
    
    # If the abstract text is not present, use Wikipedia to get the answer
    if not answer:
        try:
            answer = wikipedia.summary(query)
        except wikipedia.exceptions.DisambiguationError as e:
            raise ValueError("Multiple Wikipedia pages found.") from e
        except wikipedia.exceptions.PageError as e:
            raise ValueError("Wikipedia page not found.") from e
    
    # If the answer is still not present, check if there's a query that's similar in the data_set
    if not answer:
        closest_match = process.extractOne(query, data_set.keys(), scorer=fuzz.token_sort_ratio)
        if closest_match[1] >= 60:
            return (f"Did you mean '{closest_match[0]}'?\n{data_set[closest_match[0]]}", False)
        raise ValueError("Couldn't find an answer to the question.")
    
    # Update the data_set with the new query and answer
    data_set[query] = answer
    with open("data_set.txt", "a") as f:
        f.write(f"{query}:{answer}\n")
    return (answer, False)

# Initialize the data_set
data_set = {}

# Try to open the data_set.txt file for reading
try:
    with open("data_set.txt", "r") as f:
        # For each line in the file, split the line by the colon separator and add the query and answer to the data_set dictionary
        for line in f:
            query, answer = line.strip().split(":")
            data_set[query] = answer
# If the file is not found, create an empty file
except FileNotFoundError as e:
    open("data_set.txt", "w").close()

# Call the loading_animation function from the loading module to show a loading animation
load.loading_animation(15)

# Print a welcome message and a fun fact using the print_with_typing_animation function from the animation module
ani.print_with_typing_animation(colored(f"Welcome to the Question and Answer Program! ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})", "magenta"))
ani.print_with_typing_animation(Fact.generate_fun_fact())

# Infinite loop to ask the user for questions
while True:
    # Try block to catch any exceptions that may occur
    try:
        # Ask the user for their question
        question = input("\nWhat's your question? (type 'exit' to quit): ")
        # If the user types 'exit', break out of the loop
        if question.lower() == "exit":
            break
        # Get the answer to the question and a flag indicating whether the answer is from the data_set or not
        answer, is_data_set = answer_question(question, data_set)
        # Loop through each character in the answer
        for char in answer:
            # Print the character, color-coded based on whether it's from the data_set or not
            print(colored(char, "yellow") if not is_data_set else colored(char, "green"), end="", flush=True)
            # Add a random delay to simulate typing
            time.sleep(random.uniform(0, 0.0001))
        # Print a newline character
        print("\n")
    # If an exception occurs, print an error message
    except Exception as e:
        print(f"An error occurred: {str(e)}")
