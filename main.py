import sys
import argparse

import termcolor

from modules.utils import cool_print


parser = argparse.ArgumentParser(
    description="Simple CLI tool to print in a cool way"
)

parser.add_argument(
    "-c",
    "--color",
    type=str,
    dest="color",
    nargs='?',
    default="white",
    help="color in which you want to print"
)

parser.add_argument(
    "-w",
    "--wait-time",
    type=float,
    dest="wait_time",
    nargs='?',
    default=0.01,
    help="time betwen to random guesses (the lower it is, the faster your text will be printed)"
)

parser.add_argument(
    "-t",
    "--text",
    type=str,
    dest="text",
    nargs='*',
    default="",
    help="text you want to print"
)

args = parser.parse_args()
args.text = ' '.join(args.text)


cool_print(
    text=args.text,
    wait_time=args.wait_time,
    color=args.color
)

