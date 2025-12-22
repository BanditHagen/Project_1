#!/usr/bin/env python3
import subprocess
from . import colors

# Dictonary, each keyword is an alert label and each label is a list of patterns to look for to generate warnings.
keywords = {
    "Dangerous Command" : ["rm -rf", "rm -r /", "dd if=", "shutdown", "reboot"],
    "ROOT SSH Login" : ["Accepted password for root", "Accepted publickey for root"],
    "Failed Login" : ["failed password for", "sshd.*authentication failure", "failed publickey", "invalid user", "authentication failure"],
    "SUDO Attempt Failed" : ["incorrect password attempt", "not in sudoers", "user not in sudoers"],
    "User Change Event" : ["useradd", "userdel", "usermod", "password changed for"],
    "SUDO Command Executed" : ["pam_unix(sudo:session): session opened for user root"]
    } 

#   List of words to ignore(reduce noise).
ignore_keywords = ["systemd", "cron", "session closed", "session opened for user root by"]

#   Dictionary that maps each label to a highlight color.
keyword_colors = {
                "SUDO Attempt Failed": colors.hlyellow,
                "Failed Login": colors.hlyellow,
                "SUDO Command Executed": colors.hlblue,
                "User Change Event": colors.hlcyan,
                "ROOT SSH Login": colors.hlmagenta,
                "Dangerous Command": colors.hlred 
                }

def journalctl_function(keywords, ignore_keywords, keyword_colors):
    try:
        process = subprocess.Popen(["journalctl", "-f", "-n", "0"], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
            # stdout stores the output from "journalctl -f".
            # stderr stores any error messages.
            # "-f" means follow, -> adds new log entries in real-time.
            # "-n 0" means show 0 old lines -> only show NEW log entries from start of program.
            # text = True makes output to string format instead of binaries.
        
        count = 0   # Count variable initiated.

        # Main loop to process each entry piped out to stdout by journalclt.
        for line in process.stdout:
            line = line.strip() # Removes whitespace before and after.

            ########################  Ignore Keywords part  ########################
            # Check for matches in ignore keywords list.
            should_ignore = False
            for ignore_word in ignore_keywords: # Loop through each ignore keyword.
                if ignore_word.lower() in line.lower(): # if the ignore keyword is found in the line <- stdout.
                    should_ignore = True    
                    break  # if True match is found, exit loop early.
        
            if should_ignore: 
                continue  # Skip to next line if ignore keyword was found.

            ########################  Find Keywords part  ########################
            
            should_alert = False
            for alert_label, patterns in keywords.items(): # Loop through each category in the keywords dictionary.
                if should_alert:    # If matched stop going through the alert labels.
                    break

                for pattern in patterns:
                    if pattern.lower() in line.lower(): # If pattern is in line <- stdout do this:
                        count += 1

                        alert_color = keyword_colors.get(alert_label, colors.hlcyan)    #   Match alert_label to a color label.
                        if "command=" in line.lower():  # To extract commands if any executed. 
                            command_start = line.lower().find("command=")    # Find "command=" in line <- stdout.
                            command = line[command_start + 8:].split(";")[0].strip()   # Command = 8 characters, find the word after "command=" until ";"
                            print(alert_color(f"{count} [{alert_label}] COMMAND: {command}")) # Prints which command executed.
                        else:
                            print(alert_color(f"{count} [{alert_label}]"))   # If no command executed print
                        
                        print(f"Event Info: {line}")    # Finally print this:
                        print("-" * 100)
                        should_alert = True 
                        break   # Stop looking for patterns
              
    except KeyboardInterrupt:
        print(colors.cyan("Realtime monitoring service has been stopped."))
        process.terminate()
    finally:
        process.terminate()

#   To make separate testing of module possible.
#   If tesing locally: "from . import colors" has to be changed to "import colors".
if __name__ == "__main__":
    journalctl_function(keywords, ignore_keywords, keyword_colors)