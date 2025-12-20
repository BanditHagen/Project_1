#!/usr/bin/env python3
import subprocess
import time
import sys
import colors


def main():
    # Initial startup messages.
    print("\033c")  # Clears terminal output.
    print(colors.cyan("=" * 39))
    print(colors.cyan("<<Booting realtime monitoring servies>>"))
    print(colors.cyan("=" * 39))
    time.sleep(2)
    print("\033c")  #   flushes the output in terminal
    time.sleep(1)
    ###############################     Small system Checkup    ######################################

    #   System information + check if on right OS.
    print(colors.magenta(f"\nCurrent OS: |{sys.platform}|\n"))    # Print the current operating system(in blue).
    if sys.platform != "linux": # Check if OS is Linux, if not print message and exit.
        print("<<Script is compatible with Linux systems only>>")
        print("=" * 60)
        print(colors.cyan("Realtime monitoring service has been stopped."))
        print("=" * 60)
        sys.exit()  # Exit the script.

    time.sleep(1)
    print(colors.blue("=" * 26))
    print(colors.blue("<<System check completed>>"))
    print(colors.blue("=" * 26))
    time.sleep(2)
##########################  Menu for various choice output    #########################################
    while True:
        print("\033c")  # For each lap terminal output is cleared.
        menu_controller = input(colors.white("\n[Q]-quit\n[I]-information\n[C]-continue\n\n//:"))
        if menu_controller.lower() == "q":
            print("\033c")  # Clears terminal output
            print(colors.cyan("Closing program..."))
            sys.exit()
            break
        elif menu_controller.lower() == "i":
            print("\033c")  # Clears terminal output
            print("=" * 29)
            print("Information about the program")
            print("=" * 29)
            input("Press Enter to continue")
        elif menu_controller.lower() == "c":
            print("\033c")  # Clears terminal output.
            print(colors.blue("=" * 32))
            print(colors.blue("<<Monitoring service initiated>>"))
            print(colors.blue("=" * 32))
            break
        else:   # Wrong input displays error message. 
            print(colors.red("<<Input failure>> \nplease chose from menu."))
            time.sleep(1)


#   Makes module runnable by itself for testing.
if __name__ == "__main__":
    main()