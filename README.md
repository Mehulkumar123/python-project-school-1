# python-project-school-1
This code implements a Question and Answer Program. It first
checks if the user's question is already in the data set, which
is a dictionary stored in a text file. If it is, it returns
the answer immediately. If not, it checks if the user is asking 
a math question and calculates the result using the eval function
if the question is a valid expression. If the answer is not in
the data set or a math question, the code makes a request to the 
DuckDuckGo Instant Answer API, which returns a JSON object containing
information about the user's query. The code then extracts the 
abstract text, which is the answer to the user's question. If
there is no answer, the code checks if there is a similar question
in the data set and suggests the closest match, or returns a
default message if there is no similar question. Finally, the
code displays the answer with a typing animation. The user can
exit the program by typing "exit".

This script uses the following libraries:

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
