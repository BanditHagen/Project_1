#!/usr/bin/env python3
# On call return a colored string. 
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

def white(text):
    return f"\033[97m{text}\033[0m"

def black(text):
    return f"\033[90m{text}\033[0m"

# On call return highligt on a string
def hlred(text):
    return f"\033[41m{text}\033[0m"

def hlyellow(text):
    return f"\033[43m{text}\033[0m"

def hlcyan(text):
    return f"\033[46m{text}\033[0m"

def hlmagenta(text):
    return f"\033[45m{text}\033[0m"

def hlblue(text):
    return f"\033[44m{text}\033[0m"

def hlwhite(text):
    return f"\033[47m{text}\033[0m"

def hlblack(text):
    return f"\033[40m{text}\033[0m"

def hlgreen(text):
    return f"\033[42m{text}\033[0m"

if __name__ == "__main__":  # makes script runnable standalone for testing.
    # Colored string test/display
    print(red("testing red"))
    print(yellow("testing yellow"))
    print(cyan("testing cyan"))
    print(magenta("testing magenta"))
    print(blue("testing blue"))
    print(green("testing green"))
    print(white("testing white"))
    print(black("testing black"))
    # Highlight test/display
    print(hlred("testing red highlight"))
    print(hlyellow("testing yellow highlight"))
    print(hlcyan("testing cyan highlight"))
    print(hlmagenta("testing magenta highlight"))
    print(hlblue("testing blue highlight"))
    print(hlgreen("testing green highlight"))
    print(hlwhite("testing white highlight"))
    print(hlblack("testing black highlight"))