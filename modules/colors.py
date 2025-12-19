#!/usr/bin/env python3

def red(text):
    return f"\033[91m{text}\033[0m"

def green(text):
    return f"\033[92m{text}\033[0m"

def yellow(text):
    return f"\033[93m{text}\033[0m"

def blue(text):
    return f"\033[94m{text}\033[0m"

def magenta(text):
    return f"\033[95m{text}\033[0m"

def cyan(text):
    return f"\033[96m{text}\033[0m"


if __name__ == "__main__":  # makes script runnable standalone for testing.
    print(red("testing red"))
    print(yellow("testing yellow"))
    print(cyan("testing cyan"))
    print(magenta("testing magenta"))
    print(blue("testing blue"))