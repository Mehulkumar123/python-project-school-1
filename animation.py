import time

# The print_with_typing_animation function will display a string with a typing animation effect
def print_with_typing_animation(summary):
    # delay is the time in seconds between each character being printed
    delay = 0.005
    # loop through each character in the string
    for char in summary:
        # print the character and flush the output to make it appear immediately
        print(char, end="", flush=True)
        # sleep for the specified delay time
        time.sleep(delay)
