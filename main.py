#!/usr/bin/env python3
from modules.startup_menu import startup, display_menu
from modules.journalctl_function import journalctl_function, keywords, ignore_keywords, keyword_colors
from modules import colors
import sys
import os
import time
#   Main entry point for Project_1
#   Realtime system monitor using "journalctl" on Linux.
def main():
    
        try:
            #Launch startup checks.
            startup()
            #   Check for sudo privileges.
            if os.getuid() != 0:
                print(colors.red("WARNING, sudo privilege required. Rerun with correct credentials."))
                time.sleep(2)
                sys.exit()
            else:
                pass  # User has sudo privileges, continue.
                
            #   Launch menu.
            if display_menu():  # If returning True(user input "c") start journalctl_function.
                journalctl_function(keywords, ignore_keywords, keyword_colors)
        except KeyboardInterrupt:   # "Ctl + C" interrupts program and displays message and exits.
            print(colors.cyan("Realtime monitoring service has been stopped."))
            sys.exit()
    

if __name__ == "__main__":
   main()
