# Fritz!Box / OpenSense / PfSense automatic reboot
Script for rebooting Fritz!Box / OpenSense / PfSense routers using TR-064 protocol.

You must create a new user who has permission to change the setting of your Fritz!Box for the script to work.
Username and password are stored in the .env file by default. However, it is also possible to hardcode them in the script.

In order to run this script automatically from a Raspberry Pi or a Linux server, you have to add this script to your crontab file (crontab -e).
For example:
`30 4 * * * /usr/bin/python /opt/router_reboot.py`
This will run the script from the opt folder every morning at 4:30.

On Windows you can create a scheduled task, in order to run the script automatically.
Don't forget to install Python and the necessary modules to make the script work.

Module installation with pip:
`pip install python-decouple`
`pip install requests`
