# OSINT Telegram Bot 🕵️

This Telegram bot provides sources to find people in open source intelligence (OSINT).
The bot returns links to sources where you can find information about the search object 🌍. (Sources should be added by self).


## Features
```This version without countries, if you want to use version with countries, you can use this [HowToFuck](https://github.com/Lunoul/HowToFuck)```
#### At this point, you can add the following methods:
    Phone number (PhoneNumber.txt) 📱
    Full name (FullName.txt) 👤
    Car number (CarNumber.txt) 🚗
    Nickname in social networks and games (NickName.txt) 👾
    Face recognition (FaceScan.txt) 🧑



## 🛠️ Installation
**Requirements:** [Python 3.8 or 3.9](https://www.python.org/downloads/release/python-3913/)<br>

+ ### On Windows/Mac OS and Linux

```bash
git clone https://github.com/Lunoul/HowToFuck.git
cd HowToFuck/
pip3 install -r requirements.txt

python3 main.py
```

## Configuration

In the config.py file you need to specify your bot token:
```bash
TOKEN = "YOUR_TOKEN"
```
You can also specify the bot admin ID:
```bash
admin_id = YOUR_ID
```
Set logging mode:
```bash
MODE = "MODE" # prod or dev
```

## Project Structure
```
+ main.py - bot launch
+ config.py - configuration
+ modules/ - all modules
+     database/
+         db.py - database operations
+     handlers/
+         admin.py - admin panel
+     keyboards/
+         keyboards.py - keyboard creation
+         profile.py - user profile
+         startbuttons.py - start menu buttons
+         startchannels.py - check channels at start
+     middlewares/
+         antiflood.py - spam protection
+         dispatcher.py - dispatcher
+         states.py - aiogram state machine
+     utils/
+         handlers.py - handlers for commands and requests

```

The `data/` folder contains text files with search data for each country and method.

## How to add a new search method
In the `data` folder you need to create the name of the desired country, the name of the method in txt format
Example: `/data/USA/Carnumber.txt`


### Todo

#### Profile
+ Add donate

#### Main
+ add arrows to information
+ database of users (aiosqlite)

## 📝 License

**(MIT) Massachusetts Institute of Technology license**


