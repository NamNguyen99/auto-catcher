If you like my work and want to support it, you can donate here :)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/jokerware)

# DISCLAIMER
The bot has been broken as of the recent update of pokecord. New bot (a.k.a Nearix) is working 100%, but it is still not finished.
You can check out latest updates and info at the discord server. Thanks for your patience.

# Discontinued version (As of 18/02/2020)
(Keep track of the new bot at https://github.com/joker-ware/nearix-beta
This version will soon be discontinued. I will rewrite the bot 100% from scratch in another language (Go) with improved stability,
usability, reduced bugs , cleaner and with a massively easier setup process. Please be patient until I release it. For any updates
you can join the discord server. https://discord.gg/UHVY23g

# NEW UPDATE FOR WINDOWS USERS
This version fixes the known error of no servers or channels showing on the webpage and KeyErrors on the console. Please let me know if any other error happens.
# NEW UPDATE MULTI-1.0.0 3/2/2020
This update brings a1new awesome feature: Multi spam!
Enable and disable spam in specific channels and set a delay for each of them! 
-The setup of the bot has been simplified

The bot is being updated and rewritten. Please add any suggestions in issues. Old suggestions will be considered too.
Current objectives:
Items marked with ~~this line~~ have already been completed.
Items marked with *italic* are being discussed.
1. Add custom prefix support.
2. ~~Simplify setup of the bot~~
3. ~~Add the option to spam on multiple channels~~
4. *Discard pokemons by IV*
5. Make a video tutorial for Windows and ~~Linux~~

# NEW: Video tutorials

This video covers the bot setup, not the Python installation.

(OLD) Tutorial for MacOS [here](https://youtu.be/4Lqbk2k2fwk)
(NEW) Tutorial for Linux [here](https://youtu.be/Zuy4nqE3DEE)

## Old version - 08/Oct/2019

**To manage the bot, go to your browser of preference after running joker.py and type http://localhost:5555**

## Please, if this is the first time you use this bot, select the guilds (or servers) where you want this bot to work, all of them come disabled by default. Go to the webpage and navigate to settings to enable them.


Please if you come from version 0.0.3 (without GUI) make sure to install the **flask** module.


**FIXED POKEMON DETECTION ON 0.0.4b**
Dhash, imagehash, and python-resize-image are no longer needed. You can delete them by doing:
```bash
pip3 uninstall dhash imagehash python-resize-image
```
In your OS's terminal.

**Added support to enable/disable guilds on which to catch pokemons.**
To enable or disable a guild, go to the bot management page and select Settings>Enable/Disable Guilds

**Added support to set custom catching delay for each server**

Can access it on settings.

# JokerCord
If you like my work and want to support it, the best way is by adding a star to this project (top of the page) you don't know how happy that makes me. It also tells me to continue working on this project. Thank you!

Check future plans here! https://github.com/joker-ware/JokerCord/wiki

Welcome to JokerCord Pokécord SelfBot. This bot has been made by JokerWare and it is aimed for cheating the PokéCord Discord bot. Please be aware I am not responsible for any bans or problems caused by the usage of this bot. Use at your own risk.


This bot is under heavy development. I am aware some bugs can occur and there are things left to do (many of them are already being worked on), so let me thank you for stopping by and giving my project a shot. Remember that contributions are always appreciated. <3

---------------------------
What is JokerCord? JokerCord is a project made by joker-ware (a.k.a SteeW) to help people automatize and get advantage on the discord Pokecord bot. It comes with an useful built in Web Interface, which helps the user manage the bot. Currently, this is maintained only by one person, so any issue, idea or suggestion you make is more than welcome here. 

Functionalities:
- Auto catch
- Set custom list to catch only some Pokemon's
- Modern Web Interface for easy management
- Auto spam
- Multi spam
- Enable/Disable auto catching on certain servers
- Set custom catch delay for each server

More things are going to be added as the development progresses. Remember, if you have any idea don't hesitate to post it on Issues!

You can see some captures in the bottom of this Readme.

---------------------


## Installation

Just make sure to have installed the last Python version. You can download it here: 

[Download the latest Python version](https://www.python.org/downloads/)

A brief list of the required libraries can be seen below.


## Beginner Guide
If you wanna use this bot, just click on the green button that says "Clone or Download" and select Download to Zip. Extract the folder anywhere you like.


If you have never used Python, this will guide you through each step in order to make this bot work.

First of all, identify your Operating System (Windows, GNU/Linux, MacOS...)

## For Linux
Open a terminal session and run apt update:
```bash
sudo apt-get update
```
Install Python3 and Pip:
```bash
sudo apt-get install python3 && sudo apt-get install python3-pip
```
To install the required libraries, simply run pip as follows:
```bash
pip3 install discord.py requests flask
```
Lastly, to run JokerCord navigate to the downloaded folder:
```bash
cd /path/to/the/folder
```
Please make sure the path is the same as joker.py or else the bot will probably not work.
Then run it with python3:
```bash
python3 joker.py
```
## For Windows
Firstly make sure to download Python from the link provided above. When installing check the box that says *add Python to Path*.
After it finishes installing, you can open the Windows console by pressing <kbd>⌘R</kbd> and typing
```bash
cmd
```
In the search box. After the console opens, you can install each library by typing:
```bash
pip3 install discord.py requests flask
```
**NOTE**
This will not work if you didn't add Python to the PATH as referenced before.
After installing all the dependencies, just close the terminal and open your File Manager. Go to the Downloaded folder and double click joker.py. You're done!

## Usage

After you start joker.py, navigate to http://localhost:5555 to manage the bot, and go to Preferences to add your token. 

**Getting your token**

**This token is not a BOT token, but an USER token. Please follow this tutorial or else the token you might have gotten may not be valid**

To get your discord token: [Tutorial](https://discordhelp.net/discord-token)


## Contributing
Any bugs you find please consider sending them. Do notice this bot is in a very early beta stage so not all names will be correct.


## Required libraries
- [Discord.py](https://pypi.org/project/discord.py/)
- [Flask](https://pypi.org/project/Flask/)
- [Requests](https://pypi.org/project/requests/)

## Some captures!
![Homepage](https://cdn1.imggmi.com/uploads/2019/10/8/fcef494ae5630ecdb4030fd909583cbc-full.png)
![Caught pokemons list](https://cdn1.imggmi.com/uploads/2019/10/8/3d0d55b3715c804ca6b8936d1fd8fc5e-full.png)
![Caught pokemon](https://cdn1.imggmi.com/uploads/2019/10/8/fe7647e7e60dff40317d735cdf3366da-full.png)
![Preferences](https://cdn1.imggmi.com/uploads/2019/10/8/6358168da65f3d0427d483a7efeb3702-full.png)
![Custom guilds](https://cdn1.imggmi.com/uploads/2019/10/12/60984f6df03f49ef2f385fa0e2b931c8-full.png)
![Custom List](https://cdn1.imggmi.com/uploads/2019/10/8/47621012cf4b164f3a6cc3a5cfd97034-full.png)

