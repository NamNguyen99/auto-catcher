from flask import Flask, render_template, request, url_for, redirect, flash
import os
import time
import logging
import threading
import sys
import json
import platform
from pathlib import Path
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
pth = str(Path().absolute())
pth_r = pth
sys.path.append(pth_r)
import bot_thread
import asyncio
from threading import Thread
with open (os.path.join(pth_r,'preferences.json'),'r') as pr:
        pr_l = json.load(pr)
        pr.close()
app = Flask(__name__)
legendaries = ['arceus', 'articuno', 'azelf', 'celebi', 'cobalion', 'cosmoem', 'cosmog', 'cresselia',
            'darkrai', 'deoxys', 'dialga', 'diancie', 'Entei', 'genesect', 'giratina', 'groudon',
            'heatran', 'ho-oh', 'hoopa', 'jirachi', 'Keldeo', 'kyogre', 'kyurem', 'landorus',
            'latias', 'latios', 'lugia', 'lunala', 'Magearna', 'manaphy', 'marshadow', 'meloetta',
            'mesprit', 'mew', 'mewtwo', 'moltres', 'Necrozma', 'palkia', 'phione', 'raikou',
            'rayquaza', 'regice', 'regigigas', 'regirock', 'registeel', 'reshiram', 'shaymin', 'silvally',
            'solgaleo', 'suicune', 'tapu bulu', 'tapu fini', 'tapu koko', 'tapu lele', 'terrakion', 'thundurus',
            'tornadus', 'type: null', 'uxie', 'victini', 'virizion', 'volcanion', 'xerneas', 'yveltal', 'naganadel']
async def startClient():
    print("Starting client:")
    try:
        await bot_thread.client.start(pr_l["token"],bot=False)
    except Exception as e:
        if(e.__class__.__name__ == "LoginFailure"):
                print("Something went wrong with the token. If this is the first time you use this bot, please go to http://localhost:5555 and edit your preferences.")
        else:
            print(e)
def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startClient())
app.secret_key = "mysecretkey"
def add_pokemon(name):
    try:
        with open(os.path.join(pth_r,'User','customs.json')) as cs:
            jsdecoded = json.load(cs)
            jsdecoded[str(name)] = ""
            cs.close()
        with open(os.path.join(pth_r,'User','customs.json'), 'w') as jfil:
            json.dump(jsdecoded, jfil)
            jfil.close()
    except Exception as e: print(e)

def file_del(dfile, item):
    with open(os.path.join(pth_r,dfile)) as f:
        list_del = json.load(f)
        f.close()
    if item in list_del:
        del list_del[item]
    with open(os.path.join(pth_r,dfile), "w") as n:
        json.dump(list_del, n)
        n.close()
def restart():

        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        
        print("Restarting")
        os.execv(sys.executable, ['python3'] + sys.argv)

@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        restart()
        return redirect(url_for("home"))
    else:
        with open (os.path.join(pth_r,'User','caught.txt')) as p:
            pl = p.read().split(" ")
            p.close()
        return render_template("home.html", pokemons=(len(pl) - 2))
@app.route("/delay/<string:g_id>/<string:dly>")
def delay(g_id, dly):
    with open (os.path.join(pth_r,'User','guilds.json'), "r") as glds:
        d = json.load(glds)
        glds.close()
    d[g_id][3] = dly
    with open (os.path.join(pth_r,'User','guilds.json'), "w") as glds:
        json.dump(d, glds)
        glds.close()
    return redirect(url_for("custom_guilds"))
@app.route("/start_spamming")
def start_spamming():
    bot_thread.createTasks()
    return redirect(url_for("settings"))
@app.route("/stop_spamming")
def stop_spamming():
    bot_thread.stopSpam()
    return redirect(url_for("settings"))
@app.route("/refresh_channels")
def refresh_channels():
    bot_thread.refreshChannels()
    return redirect(url_for("home"))
@app.route("/update", methods=["POST"])
def update():
    if request.method == "POST":
        return render_template("update.html")
@app.route("/disable_guild/<string:id>")
def disable_guild(id):
    with open (os.path.join(pth_r,'User','guilds.json'), "r") as glds:
        disable = json.load(glds)
        glds.close()
    disable[id][0] = "False"
    with open (os.path.join(pth_r,'User','guilds.json'), "w") as glds:
        json.dump(disable, glds)
        glds.close()
    return redirect(url_for("custom_guilds"))
@app.route("/enable_guild/<string:id>")
def enable_guild(id):
    with open (os.path.join(pth_r,'User','guilds.json'), "r") as glds:
        enable = json.load(glds)
        glds.close()
    enable[id][0] = "True"
    with open (os.path.join(pth_r,'User','guilds.json'), "w") as glds:
        json.dump(enable, glds)
        glds.close()
    return redirect(url_for("custom_guilds"))
@app.route("/custom_guilds")
def custom_guilds():
    with open (os.path.join(pth_r,'User','guilds.json')) as glds:
        guilds = json.load(glds)
        glds.close()
    return render_template("custom_guilds.html", guilds=guilds)#, icons=icons, ids=ids)
@app.route("/spam")
def spam():
    with open (os.path.join(pth_r,'User','channels.json')) as chnl:
        channels = json.load(chnl)
        chnl.close()
    return render_template("spam.html",channels=channels);
@app.route("/spam_delay/<string:id>",methods=['POST'])
def spam_delay(id):
    with open (os.path.join(pth_r,'User','channels.json'),'r') as delay:
        change_delay=json.load(delay)
        delay.close()
    change_delay[id][2]=request.form.get(str(id))
    with open (os.path.join(pth_r,'User','channels.json'),'w') as delay:
        json.dump(change_delay,delay)
        delay.close()

    return redirect(url_for("spam"))

@app.route("/custom_list", methods=['GET', 'POST'])
def custom_list():
    error = False
    if request.method == "POST":
        if(request.form.get("new_pokemon")):
            n_p = request.form.get("new_pokemon")
            with open (os.path.join(pth_r,'Lists','hashes.json')) as check:
                check_read = json.load(check)
                check.close()
            if (n_p in check_read):
                add_pokemon(n_p)
                return redirect(url_for("custom_list"))
            else:
                error = n_p 
        elif(request.form.get("custom_list_state")):
            if(request.form.get("custom_list_state") == "custom_list_true"):
                bot_thread.write_json("custom_list", "True")
            elif(request.form.get("custom_list_state") == "custom_list_false"):
                bot_thread.write_json("custom_list", "False")
    with open (os.path.join(pth_r,'User','customs.json')) as c:
        cl = json.load(c)
        c.close()
    return render_template("custom_list.html", cl=cl, err=error)
@app.route("/custom_prefix", methods=['GET', 'POST'])
def custom_prefix():
    with open (os.path.join(pth_r,'preferences.json')) as pcp:
        pref = json.load(pcp)
        pcp.close()
        custom_prefix = pref["custom_prefix"]
    return render_template("custom_prefix.html", custom_prefix=custom_prefix)
@app.route("/change_channel/<string:id>/<string:status>")
def change_channel(id,status):
    with open (os.path.join(pth_r,'User','channels.json'), 'r') as channels_list:
        channels=json.load(channels_list)
        channels_list.close()
    with open (os.path.join(pth_r,'User','channels.json'), 'w') as channels_write:
        channels[str(id)][1]=status
        json.dump(channels,channels_write)
        channels_write.close()
    return redirect(url_for("spam"))

@app.route("/del_custom/<string:id>")
def del_custom(id):
    try:
        file_del(os.path.join('User','customs.json'), id)
    except:
        pass
    return redirect(url_for("custom_list"))
@app.route("/setup")
def setup():
    with open (os.path.join(pth_r,'preferences.json')) as p:
        pref = json.load(p)
        p.close()
    if(pref["token"] != ""):
        token = pref["token"]
    else:
        token = "Insert your token here:"
    return render_template("setup.html", token=token)
@app.route("/settings")
def settings():
    return render_template("settings.html")
@app.route("/list", methods=['POST', 'GET'])
def caught_list():
    l = []
    with open (os.path.join(pth_r,'User','caught.txt')) as caught:
        lines = caught.read().split(" ")
        caught.close()
    if request.method == "POST":
        open (os.path.join(pth_r,'User','caught.txt'),'w').close()
        return redirect(url_for("caught_list"))
    else:
        
        return render_template("list.html", l=lines, legs=legendaries)
    
@app.route("/setup_finished", methods=['POST'])
def setup_finished():
        if request.method == 'POST':
            error = None
            token = request.form.get('token')
            if(token == ""): 
                 error = "Please fill out all the required fields"
                 return render_template("setup.html", error=error)
            else:
                bot_thread.write_json("token", token)
                return redirect(url_for("home"))
            
@app.route("/prefix_finished", methods=['POST'])
def prefix_finished():
        if request.method == 'POST':
            error = None
            custom_prefix = request.form.get('custom_prefix')
            if(custom_prefix == ""): 
                 error = "Please fill out all the required fields"
                 return render_template("custom_prefix.html", error=error)
            else:
                bot_thread.write_json("custom_prefix", custom_prefix)
                return redirect(url_for("home"))

@app.route("/preferences")
def pref_page():
    return "<h1>Preferences Page</h1>"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop_in_thread, args=(loop,))
    t.start()
    app.run(port="5555", debug = False)
