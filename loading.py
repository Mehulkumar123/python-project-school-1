import sys
import time
import random
import itertools
import termgraph
import prettytable
import matplotlib.pyplot as plt
from tqdm import tqdm
from time import sleep
from termcolor import colored
from prettytable import PrettyTable

def stage_1():
    time.sleep(random.uniform(0.1, 0.5))

def stage_2():
    time.sleep(random.uniform(0.5, 1))

def stage_3():
    time.sleep(random.uniform(0.2, 0.8))

def stage_4():
    time.sleep(random.uniform(0.5, 2))

def stage_5():
    time.sleep(random.uniform(0.1, 0.3))

def stage_6():
    time.sleep(random.uniform(0.1, 0.5))

def stage_7():
    time.sleep(random.uniform(0.5, 1))

def stage_8():
    time.sleep(random.uniform(0.2, 0.8))

def stage_9():
    time.sleep(random.uniform(0.5, 2))

def stage_10():
    time.sleep(random.uniform(0.1, 0.3))

def stage_11():
    time.sleep(random.uniform(0.1, 0.5))

def stage_12():
    time.sleep(random.uniform(0.5, 1))

def stage_13():
    time.sleep(random.uniform(0.2, 0.8))

def stage_14():
    time.sleep(random.uniform(0.5, 2))

def stage_15():
    time.sleep(random.uniform(0.1, 0.3))

def loading_animation(total, stage_list=None, spinner_list=None, desc=None, bar_format=None, leave=False):
    if not isinstance(total, int) or total <= 0:
        raise ValueError("Total number of steps must be a positive integer")
    
    stages = stage_list if stage_list else [stage_1, stage_2, stage_3, stage_4, stage_5, stage_6, stage_7, stage_8, stage_9, stage_10, stage_11, stage_12, stage_13, stage_14, stage_15]
    spinner = itertools.cycle(spinner_list if spinner_list else ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
    desc = desc if desc else "Loading the AI Time Machine..."
    bar_format = bar_format if bar_format else "{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"
    
    with tqdm(total=total, desc=desc, bar_format=bar_format, leave=leave) as pbar:
        for i in range(0, total, 15):
            random_stages = random.choices(stages, k=15)
            for stage in random_stages:
                stage()
                postfix_str = f"Step {i+1} - Stage: {stage.__name__} {next(spinner)}"
                pbar.set_postfix_str(colored(postfix_str, "cyan"))
                i += 1
                if i >= total:
                    break
                pbar.update(1)

def loading_animation2():
    spinner = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for char in spinner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")

def loading_animation3():
    progress_bar = "█▓▒░"
    for char in progress_bar:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b")

def loading_animation6(duration):
    circle = "◜◝◞◟"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in circle:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")

def loading_animation7(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining = int(end_time - time.time())
        sys.stdout.write("\rLoading... %d seconds remaining" % remaining)
        sys.stdout.flush()
        time.sleep(1)

def loading_animation9(duration):
    flag = ["🎌    ",
            " 🎌   ",
            "  🎌  ",
            "   🎌 ",
            "    🎌"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(5):
            sys.stdout.write("\r" + flag[i % 5])
            sys.stdout.flush()
            time.sleep(0.2)
