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

load.loading_animation(10)
# Add a dictionary to store the subject categories and the questions and answers under each category
subject_categories = {}

def categorize_question(question):
    # Function to determine the subject category of a question
    for subject in subject_categories:
        if subject in question:
            return subject
    return None

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
        # Check if the question belongs to any of the subject categories
        subject = categorize_question(query)
        if subject:
            # If the subject category exists, return a message to ask the user to add their own answer
            return (f"No answer found for '{query}' in the {subject} category.\nWould you like to add your own answer? (y/n)", False)
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
            subject = categorize_question(query)
            if subject:
                if subject not in subject_categories:
                    subject_categories[subject] = {}
                subject_categories[subject][query] = answer
            else:
                data_set[query] = answer
except FileNotFoundError:
    print("data_set.txt file not found.")
except Exception as e:
    print("An error occurred while reading the file:", str(e))

def categorize_question(query):
    """
    Function to categorize the question based on its subject matter
    """
    # Add logic to categorize the question based on its subject matter
    subject = None
    # Example implementation: categorize based on keywords in the question
    if "math" in query.lower():
        subject = "math"
    elif "history" in query.lower():
        subject = "history"
    # Add more conditions as required
    return subject   

def save_data_set(data_set, subject_categories):
    """
    Function to save the data set to the text file
    """
    with open("data_set.txt", "w") as f:
        for query, answer in data_set.items():
            f.write("{}:{}\n".format(query, answer))
        for subject, questions in subject_categories.items():
            for question, answer in questions.items():
                f.write("{}:{}:{}\n".format(subject, question, answer))

# Save the data set to the text file
save_data_set(data_set, subject_categories)

print(colored(f"Welcome to the Question and Answer Program! ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})", "magenta"))
print(Fact.generate_fun_fact())

# Example usage
while True:
    question = input("\nWhat's your question? (type 'exit' to quit) ")

    # Allow the user to exit the program
    if question.lower() == "exit":
        break

    # Check if the user wants to add an answer in manual mode
    if question.lower() == "add":
        question = input("Enter a question: ")
        answer = input("Enter an answer: ")
        subject = input("Enter a subject: ")
        add_answer(question, answer, data_set, subject_categories)
        continue

    answer, is_data_set, subject = answer_question(question, data_set, subject_categories)

    # Display the answer with a typing animation
    for char in answer:
        print(colored(char, "yellow") if not is_data_set else colored(char, "green"), end="", flush=True)
        time.sleep(random.uniform(0.1, 0.3))
    print("\n")
    if subject:
        print(f"Subject: {subject}")
