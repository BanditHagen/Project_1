#!/usr/bin/env python3
import time
import sys
from . import colors

def startup():
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
def display_menu():
    while True:
        print("\033c")  # For each lap terminal output is cleared.
        menu_controller = input(colors.white("\n[Q]-quit\n[I]-information\n[C]-continue\n\n//:"))
        if menu_controller.lower() == "q":  # Option "q" will exit with message.
            print("\033c")  # Clears terminal output
            print(colors.cyan("Closing program..."))
            sys.exit()
            break
        elif menu_controller.lower() == "i":    # Option "i" will display a description/info about program.
            print("\033c")  # Clears terminal output
            print("=" * 80)
            print("""
                  INFO:

            Program is built for Linux OS as a command-line utility tool.
                  
            "journalctl"  is run with a follow flag ("-f") if conditions are met.
            requirements:
                        Linux OS
                        sudo privilege
                        Linux distribution uses "systemd"
                  
            This program translates the default binary formatted logs from
            journald(logging service for systemd)to human readable form.

            Main function is iterating through the logs and return information 
            of chosen events as security alerts in real-time. Service will run
            if teminal window is left open until abrupted by [CTRL+C].

            Alerts are built on keywords to find, and keywords to ignore for 
            simplicity.

            WARNING. This program is limited to activety found in systemd,
            monitoring all services or activety on your system may require
            more advanced tools.

            -------------------------------------------------------------------------
            For bugs and reports feel free to reach out.

                Thank you,
                Team Bandithagen.
                ----------------- 
            """)    
            print("=" * 80)
            input("Press Enter to continue")
        elif menu_controller.lower() == "c":    # Option "c" will return True = used to later lauch journalctl function.
            print("\033c")  # Clears terminal output.
            print(colors.cyan("Leave terminal window open.\n[CTRL + C] to quit."))
            print(colors.blue("=" * 32))
            print(colors.blue("<<Monitoring service initiated>>"))
            print(colors.blue("=" * 32))
            return True
        else:   # Wrong input displays error message but keeps the loop. 
            print(colors.red("<<Input failure>> \nplease chose from menu."))
            time.sleep(2)

#   Makes module runnable by itself for testing.
#   If tesing locally: "from . import colors" has to be changed to "import colors".
if __name__ == "__main__":
    startup()
    display_menu()