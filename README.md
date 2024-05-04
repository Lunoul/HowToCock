# OSINT Telegram Bot 🕵️

This Telegram bot provides sources to find people in open source intelligence (OSINT).
The bot returns links to sources where you can find information about the search object 🌍. (Sources should be added by self).

## 📜 Disclaimer
This project is made for educational and ethical testing purposes only. Use of this tool to find information about the target without prior consent is illegal. Developers assume no liability and are not responsible for any misuse or damage caused by this tool.

## Features
```This version without countries, if you want to use version with countries, you can use this``` [HowToFuck](https://github.com/Lunoul/HowToFuck)
#### At this point, you can add the following methods:
    Phone number (phone_number.txt) 📱
    Full name (fullname.txt) 👤
    Car number (car_number.txt) 🚗
    Nickname in social networks and games (nickname.txt) 👾
    Face recognition (face_scan.txt) 🧑



## 🛠️ Installation
**Requirements:** [Python 3.8 or 3.9](https://www.python.org/downloads/release/python-3913/)<br>

+ ### On Windows/Mac OS and Linux

```bash
git clone https://github.com/Lunoul/HowToCock.git
cd HowToCock/
pip3 install -r requirements.txt

python3 main.py
```

## Configuration

In the config.py file you need to specify your bot token:
```bash
BOT_TOKEN = "YOUR_TOKEN"
```
You need to add channel id and url:
```bash
CHANNEL_ID = (YOUR ID) # Example: -1001234567899
CHANNEL_LINK= "(Your channel link)" # Example: https://t.me/Durov/
```

## Project Structure
```
+ main.py - bot launch
+ config.py - configuration
+     db.py - database operations
+     keyboards.py - keyboard creation
+     dispatcher.py - dispatcher
+     states.py - aiogram state machine
+     handlers.py - handlers for commands and requests
+     utils.py - utility functions
+ data/ - search data
+     Car_Number.txt - car number search data
+     Face_Scan.txt - face recognition search data
+     FullName.txt - full name search data
+     NickName.txt - nickname search data
+     Phone_Number.txt - phone number search data

```

The `data/` folder contains text files with search data for each country and method.

## How to add a new search source?
In the `data` folder you need to create the name of the method in txt format
Example: `/data/car_number.txt`


## Todo

### Profile
+ Add donate

### Main
+ admin panel
+ the ability to add your own sources/categories at admin panel
+ Anti-spam system
+ arrows to information
+ multilanguage

## 🙏 Support
If you like the project, you can support it by giving a star ⭐, this will help the project to develop and grow.

## 📝 License
**(MIT) Massachusetts Institute of Technology license**


