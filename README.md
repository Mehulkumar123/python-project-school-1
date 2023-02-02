# python-project-school-1
This code is a question-answering chatbot that retrieves
information based on the user's input. If the answer to 
the user's question is found in the stored data set, the
bot returns the answer. If not, it searches the DuckDuckGo
Instant Answer API for an answer. If no answer is found 
there, the bot either suggests a closest match to the user's 
question or asks the user if they would like to add an answer.
The data set is stored in a file, and the bot saves any new 
answers to the data set after each search.

The chatbot is also able to categorize questions
based on their subject matter and store the question and 
answer under the relevant subject category. The data set is 
saved to a text file and loaded from it each time the program runs.
This script uses the following libraries:

Library used in this project.
Requests: to make HTTP requests to the DuckDuckGo Instant Answer API.
re (regular expressions): to match the mathematical expressions.
datetime: to display the current date and time.
ast (abstract syntax trees): to evaluate the mathematical expressions.
time: to display the loading animation.
random: to generate random fun facts.
loading: a custom library for the loading animation.
facts: a custom library to generate fun facts.
fuzzywuzzy: to find the closest match between the input question and the questions in the data set.
termcolor: to color the text in the terminal.
