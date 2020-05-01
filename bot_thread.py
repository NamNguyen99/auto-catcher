import discord
from discord.ext.commands import Bot
import asyncio
import json
import requests
import time
from discord.ext import commands
import sys, os
import random
import hashlib
from pathlib import Path
import threading
# import Image
import functools
import math, operator
from PIL import ImageChops, Image
path= str(Path().absolute()) 

# Start client
client = discord.Client()
client2 = commands.Bot(command_prefix = '.')
#Intent to fix windows problem, define a function to LOCK a file before trying to write to it.
im2_path = "C:\\Users\\admin\\Desktop\\Python\\pokedex"
im2_label = os.listdir(im2_path)
print(len(im2_label))

spam=True

lock = threading.Lock()
def write_lock_jsonDump(fileObject, fileContent):
    try:
        for line in fileContent:
            print("Contents: "+str(line))
        lock.acquire()
        print(fileObject.name)
        json.dump(fileContent, fileObject)
        fileObject.flush()
        lock.release()
    except Exception as e:
        print(e)
        print(e.__class__.__name__)
legendaries = ['arceus', 'articuno', 'azelf', 'celebi', 'cobalion', 'cosmoem', 'cosmog', 'cresselia',
            'darkrai', 'deoxys', 'dialga', 'diancie', 'Entei', 'genesect', 'giratina', 'groudon',
            'heatran', 'ho-Oh', 'hoopa', 'jirachi', 'Keldeo', 'kyogre', 'kyurem', 'landorus',
            'latias', 'latios', 'lugia', 'lunala', 'Magearna', 'manaphy', 'marshadow', 'meloetta',
            'mesprit', 'mew', 'mewtwo', 'moltres', 'Necrozma', 'palkia', 'phione', 'raikou',
            'rayquaza', 'regice', 'regigigas', 'regirock', 'registeel', 'reshiram', 'shaymin', 'silvally',
            'solgaleo', 'suicune', 'tapu bulu', 'tapu fini', 'tapu koko', 'tapu lele', 'terrakion', 'thundurus',
            'tornadus', 'type: null', 'uxie', 'victini', 'virizion', 'volcanion', 'xerneas', 'yveltal', 'naganadel']

#Define write to json
def file_read(folder, fname):
    caught = open(str(os.path.join(path,folder,fname)), 'r')
    lines = caught.readlines()
    caught.close()
    return lines
def clear_file(folder, fname):
    open(str(os.path.join(path,folder,fname)), 'w').close()
def file_append(folder, fname, append):
    p = (str(os.path.join(path,folder,fname)))
    f = open(p, "a")
    f.write(append + " ")
    f.close()
def add_pokemon(name):
    try:
        with open(str(os.path.join(path,'User','customs.json'))) as cs:
            jsdecoded = json.load(cs)
            jsdecoded[str(name)] = ""
            cs.close()
        with open(str(os.path.join(path,'User','customs.json')), 'w') as jfil:
            json.dump(jsdecoded, jfil)
            jfil.close()
    except Exception as e: print(e)
def write_json(wrtline, wrt):
    try:
        with open(str(os.path.join(path,'preferences.json'))) as pr:
            jsdecoded = json.load(pr)
            jsdecoded[str(wrtline)] = str(wrt)
            pr.close()
        with open(str(os.path.join(path,'preferences.json')), 'w') as jfil:
            write_lock_jsonDump(jfil,jsdecoded)
            jfil.close()
    except Exception as e: print(e)
def rmsdiff(im1, im2):
       h = ImageChops.difference(im1, im2).histogram()

       # calculate rms
       return math.sqrt(functools.reduce(operator.add,
           map(lambda h, i: h*(i**2), h, range(256))
       ) / (float(im1.size[0]) * im1.size[1]))
#Presets
with open (str(os.path.join(path,'preferences.json'))) as p:
    prefs = json.load(p)
    p.close()
with open (str(os.path.join(path,'User','guilds.json'))) as g:
    guild_list = json.load(g)
    g.close()
with open (str(os.path.join(path,'User','channels.json'))) as ch:
    channel_list = json.load(ch)
    ch.close()
with open (str(os.path.join(path,'User','customs.json'))) as cs:
            custom_list = json.load(cs)
            cs.close()
#Start
#Pref
#Startup process. Check files, and proceed.
def startUp():
    print("\n\nChecking file size...")
    #Check if file size is less than 5 bytes, in that case it must be empty (ergo only contains the empty array)
    if (os.path.getsize(str(os.path.join(path,'User','channels.json')).replace("\\","/")) < 5):
        
        print("\n\nChannel list appears to be empty. Please refresh it by going to the webpage>settings>refresh channels \n\n")
    else:    
        print("""--------------------------------------------
Everything is alright. JokerCord will start. Please start the spam function from the settings menu in the webpage.
-------------------------------------------- \n\n""")
        #sys.exit(0)
        

startUp()




#Defines
async def spamThread(channelInstance,delay):
    while(spam):
        await channelInstance.send(str(random.randint(0,9999999)))
        await asyncio.sleep(int(delay))
def gethash(img):
    with open (img, "rb") as h:
        md = hashlib.md5(h.read()).hexdigest()
        h.close()
    return md
async def setSpam(value):
    spam = value
def stopSpam():
    setSpam(False)
##########

#Lists
with open (str(os.path.join(path,'Lists','hashes.json'))) as h:
    hashdata = json.load(h)
    h.close()

#End
def refreshChannels():
    print("""Starting channel refresh... This may take a long time.
------------------------------------------------------
Relax and get a drink.
----------------------""")
    user_guilds = client.guilds
    for guild in user_guilds:
        try:
            if(guild_list[str(guild.id)] and guild_list[str(guild.id)][3]):
                guild_list[str(guild.id)] = [guild_list[str(guild.id)][0], guild.name, guild.icon, guild_list[str(guild.id)][3]]
            else:
                guild_list[str(guild.id)] = ["False", guild.name, guild.icon, "2"]
        except:
            guild_list[str(guild.id)] = ["False", guild.name, guild.icon, "2"]
        finally:
            for channel in guild.text_channels:
                try:
                    if(channel_list[str(channel.id)][1] == "True" or channel_list[str(channel.id)][1] == "False"):
                        pass
                    else:
                        channel_list[channel.id] = [channel.name+"@"+guild.name, "False", "5"]

                except:
                    channel_list[channel.id] = [channel.name+"@"+guild.name, "False", "5"]
            with open (str(os.path.join(path,'User','channels.json')), 'w') as clr_channels:
                clr_channels.write("{}")
                clr_channels.close()

            with open(str(os.path.join(path,'User','channels.json')), 'w') as jfil:
                write_lock_jsonDump(jfil,channel_list)
                jfil.close()
    try:
        with open (str(os.path.join(path,'User','guilds.json')), 'w') as clr_guilds:
            clr_guilds.write("{}")
            clr_guilds.close()
        with open(str(os.path.join(path,'User','guilds.json')), 'w') as jfil:
            write_lock_jsonDump(jfil,guild_list)
            jfil.close()
    except Exception as e: print(e)
    print("""-----------------------------------
Channels have been successfully updated. You may need to reboot.""")
    
#Ready
def createTasks():
    taskNumber=1
    print("Starting spam threads:")
    for channel in channel_list:
        if channel_list[channel][1] == "True":
            print(str(channel)+" is enabled, starting task #"+str(taskNumber))
            taskNumber = taskNumber + 1
            spchannel = client.get_channel(int(channel))
            client.loop.create_task(spamThread(spchannel,channel_list[channel][2]))
        else:
            pass
    

@client.event
async def on_message(message):
    try:
        ev = 1
        #Get the embed message
        try:
            embed = message.embeds[0]
        except IndexError:
            ev = 0
        #Check if message is from Pokecord Spawn
        if (message.author.id != client.user.id and ev == 1 and (guild_list[str(message.guild.id)][0] == "True")): #and "A wild" in message.content):
            stopSpam()
            try:
                url = embed.image.url
                try:
                        if 'discordapp' not in url:
                            return
                except TypeError:
                        return
                print(url)
                #Open image and save it to JPG
                openimg = open(str(os.path.join(path,'Assets','pokemon.jpg')),'wb')
                openimg.write(requests.get(url).content)
                openimg.close()
            
            

                #Get hashes

                mdhash = gethash(str(os.path.join(path,'Assets','pokemon.jpg')))
                im1 = os.path.join(path,'Assets','pokemon.jpg')
                print(mdhash)
                #Compare hashes with the lists
                save_line = None
            
                # for i in hashdata:
                #     if (hashdata[i] == mdhash):
                #         save_line = i
                #         break
                for i in im2_label:
                    im2 = os.path.join(im2_path, i) 
                    if rmsdiff(Image.open(im1), Image.open(im2)) == 0.0:
                        save_line = i.split('.')[0]
                        print(save_line)
                        break
                
                if(save_line in legendaries):
                    print("You have catch legendary pokemon")
                    await asyncio.sleep(3)
                else:
                    await asyncio.sleep(int(guild_list[str(message.guild.id)][3]))
                if(prefs["custom_list"] == "True"):
                    if(save_line in custom_list):
                        await message.channel.send(prefs["custom_prefix"] + "catch " + save_line.lower())
                    if (save_line not in file_read("User", "caught.txt")):
                        file_append("User","caught.txt",save_line)
                        
                else:
                    await message.channel.send(prefs["custom_prefix"] + "catch " + save_line.lower())
                    # await message.channel.send(prefs["custom_prefix"] + "catch " + save_line.lower())
                    if (save_line not in file_read("User", "caught.txt")):
                        file_append("User","caught.txt",save_line)
                    
                    else:
                        return
            except AttributeError:
                return
    except Exception as e:
        if(e.__class__.__name__ == "KeyError"):
            pass
        else:
            print (e)