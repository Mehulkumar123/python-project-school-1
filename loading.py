import random
import time
import itertools
from tqdm import tqdm
from termcolor import colored

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

def loading_animation(total):
    if not isinstance(total, int) or total <= 0:
        raise ValueError("Total number of steps must be a positive integer")
    text = "Loading the AI Time Machine..."
    stages = [stage_1, stage_2, stage_3, stage_4, stage_5, stage_6, stage_7, stage_8, stage_9, stage_10]
    spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
    with tqdm(total=total, desc=text, bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]", leave=False) as pbar:
        for i in range(total):
            stage = random.choice(stages)
            stage()
            postfix_str = f"Step {i+1} - Stage: {stage.__name__} {next(spinner)}"
            pbar.set_postfix_str(colored(postfix_str, "cyan"))
            pbar.update(1)

