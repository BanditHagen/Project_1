## Linux Security Monitor

A real-time security monitoring tool for Linux systems. Monitors system logs using journalctl and alerts potential security compromising events.

### Functionality:

This program watches your Linux system in real-time and alerts you when:

- Failed login attempts occur
- Root SSH logins happen
- Dangerous commands are executed (rm -rf, dd, shutdown, etc.)
- SUDO commands are used
- SUDO attempts fail
- User accounts are modified

The program parses system logs and highlights security events with colors, making it easy to spot potential security issues quickly.

### Requirements:

- Linux system with systemd (Ubuntu, Debian, Fedora, Arch, etc.)
- Python3
- Root/sudo privileges

### Installation:

1. Clone the repository:
```bash
git clone https://github.com/BanditHagen/Project_1.git
cd Project_1
```

2. Run the program:
```bash
sudo python3 main.py
```

### How to Use:
Start the program with:
```bash
sudo python3 main.py
```

Menu display with three options:
- Q - Quit the program
- I - Show information about the program
- C - Start monitoring

Press C to begin monitoring. The program will display alerts as security events occur.

Press Ctrl+C to stop monitoring.

### Example Output:
```
1 [Failed Login]
Event Info: Jan 07 14:23:15 hostname sshd[12345]: Failed password for invalid user admin from 192.168.1.100
-------------------------------------------------------------------------------------------------------------------------------

2 [SUDO Command Executed] COMMAND: apt update
Event Info: Jan 07 14:24:30 hostname sudo: user : TTY=pts/0 ; PWD=/home/user ; USER=root ; COMMAND=/usr/bin/apt update
-------------------------------------------------------------------------------------------------------------------------------

3 [Dangerous Command]
Event Info: Jan 07 14:25:10 hostname sudo: user : TTY=pts/0 ; PWD=/home/user ; USER=root ; COMMAND=/bin/rm -rf /tmp/old_files
-------------------------------------------------------------------------------------------------------------------------------
```

### Project Structure:
```
Project_1/
├── main.py                       # Main program file
├── modules/
│   ├── colors.py                 # Color formatting for terminal output
│   ├── startup_menu.py           # Startup checks and menu system
│   └── journalctl_function.py    # Core monitoring logic
├── .gitignore
└── README.md
```

### Alert Types:

** Dangerous Command** - Detects risky commands like rm -rf, dd, shutdown (Red highlight)

** ROOT SSH Login** - Alerts on successful root SSH authentication (Magenta highlight)

** Failed Login** - Tracks failed password and SSH key attempts (Yellow highlight)

** SUDO Attempt Failed** - Monitors unsuccessful privilege escalation (Yellow highlight)

** SUDO Command Executed** - Logs all commands run with SUDO privileges (Blue highlight)

** User Change Event** - Detects user account modifications (Cyan highlight)

### Customization

You can customize what the program monitors by editing `modules/journalctl_function.py`.

Add new keywords to monitor:
```python
keywords = {
    "Your Alert Label": ["pattern1", "pattern2", "pattern3"],
}
```

Add keywords to ignore:
```python
ignore_keywords = ["routine_process", "non_critical_event"]
```

Change alert colors:
```python
keyword_colors = {
    "Your Alert Label": colors.hlgreen // colors.green
}
```

### Learnings:
- Python subprocess management
- Real-time data processing and parsing
- Pattern matching for security events
- Linux system administration with systemd and journalctl
- Security monitoring concepts
- Modular code design

### Security Notes:

This tool monitors system logs but does not prevent attacks. It should be used as one part of a complete security strategy alongside other tools like firewalls, fail2ban, and intrusion detection systems.

The program requires sudo privileges to read system logs. Only run this on systems you own or have permission to monitor.

### Troubleshooting

** Permission denied error **

Run with sudo: `sudo python3 main.py`
Or change permissions 'chmod +x main.py' and rund from terminal 'sudo ./main.py' 

** journalctl command not found **

Your system does not use systemd. This tool only works on systemd-based Linux distributions.

** No alerts appearing **

The system may have no activity matching the keywords, or the keywords may need adjustment. Check if journalctl works: `sudo journalctl -f`
Or run 'sudo su' in new terminal leaving system monitoring open.

** Module import errors **

Make sure you run the program from the Project_1 directory.

### Future Improvements:

- Log alerts to file for later analysis
- Email or SMS notifications for critical events
- Web dashboard for remote monitoring
- Integration with SIEM systems
- Custom alert rules via configuration file
- Statistics and reporting features
- Auditd function along with rules to find specific end more detailed events

### Contributing

Contributions are welcome. Fork the repository, make your changes, and submit a pull request.

### Author:

BanditHagen - Currently studying IT and Cybersecurity

GitHub: https://github.com/BanditHagen

### License:

This project is open source and available under the MIT License.

### Disclaimer:

This tool is for authorized system monitoring only. Always ensure you have permission to monitor any system. Use responsibly and ethically.

Last Updated: January 2026

