# python-project-school-1
This is a Question and Answer program that allows
a user to ask questions and receive answers. If the 
answer is not found in the locally stored data set,
it will query the DuckDuckGo Instant Answer API to
retrieve an answer. The answer is then added to the
data set for future use. The program also displays
fun facts randomly generated from the facts module.
The answers are displayed with a typing animation 
and color-coded based on whether the answer came 
from the data set (green) or from the DuckDuckGo 
API (yellow). The program continues to prompt the 
user for questions until "exit" is entered.

This script uses the following libraries:

requests for making HTTP requests
re for regular expression operations
datetime for working with dates and times
ast for string literal evaluation
time for time-related functions
random for generating random numbers
loading for a custom loading animation
facts for a custom fun facts generator
fuzzywuzzy for fuzzy string matching
termcolor for adding color to text output.
