#!/usr/bin/env python3
import subprocess
import time
import sys
import colors


def main():
    # Initial startup messages.
    print(colors.cyan("=" * 39))
    print(colors.cyan("<<Booting realtime monitoring servies>>"))
    print(colors.cyan("=" * 39))
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

##########################  Menu for various choice output    #########################################
    time.sleep(1)
    while True:
        menu_controller = input("\n[Q]-quit\n[I]-information\n[C]-continue\n\n//:")
        if menu_controller.lower() == "q":
            print(colors.cyan("Closing program..."))
            sys.exit()
            break
        elif menu_controller.lower() == "i":
            print("=" * 29)
            print("Information about the program")
            print("=" * 29)
        elif menu_controller.lower() == "c":
            print(colors.blue("=" * 32))
            print(colors.blue("<<Monitoring service initiated>>"))
            print(colors.blue("=" * 32))
            break
    




if __name__ == "__main__":
    main()