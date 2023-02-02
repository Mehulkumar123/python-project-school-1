# python-project-school-1
This code implements a simple question and answer program. The program first
checks if the user's question is already in the data set, which is loaded from 
a text file "data_set.txt". If the question is in the data set, the answer is returned.
If the answer is not in the data set, the program checks if the user is asking a math
question. If the user is asking a math question, the program evaluates the expression
using the ast.literal_eval function.
If the answer is still not found, the program searches 
for an answer using the DuckDuckGo Instant Answer API and if 
that fails, it uses Wikipedia's API. If the answer is still 
not found, the program asks the user if they would like to 
manually add the answer to the data set.
Finally, the program outputs the answer with a typing animation
and a yellow color if the answer was not found in the data set 
and a green color if it was. The user can ask as many questions
as they want by repeating this process until they type "exit".

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
