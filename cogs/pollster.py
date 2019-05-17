#from .dataIO import dataIO
from copy import deepcopy
from difflib import SequenceMatcher
from statistics import mode,mean
import discord
from unidecode import unidecode
from discord.ext import commands
from discord.ext.commands import Bot
from .utils.chat_formatting import escape_mass_mentions, italics, pagify
from random import randint
from random import choice
from enum import Enum
from urllib.parse import quote_plus
from datetime import tzinfo, timedelta, datetime
import time
import random
from time import mktime
import aiohttp
import textwrap
import asyncio
import re
import io
import math
import cv2 as cv
import shutil
from PIL import Image
import pytesseract
import pytesseract as tes
import cv2
import subprocess
import tempfile
import imutils
import pandas as pd
import numpy as np
from cogs.utils import checks
import os
import traceback
from crontab import CronTab
import argparse
from math import sin, cos, sqrt, atan2, radians
from cogs.utils.dataIO import dataIO
import gspread
from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from oauth2client.service_account import ServiceAccountCredentials
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


#server = discord.Server()
settings = {"POLL_DURATION" : 60}
client = discord.Client(max_messages=100000)
my_bot = Bot(command_prefix="%")
#timez=-4  #Change this 
#bot=
default_path = "configuration/settings.json"
 
@my_bot.event
async def on_ready():
    print("Bot is ready")
    bot.loop.create_task(ballzy.checkraidbuffer())
    
class RPS(Enum):
    rock     = "\N{MOYAI}"
    paper    = "\N{PAGE FACING UP}"
    scissors = "\N{BLACK SCISSORS}"

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(hours=offset)
        self.__dst = timedelta(hours=offset-1)
        self.__name = ''

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return self.__dst

class RPSParser:
    def __init__(self, argument):
        argument = argument.lower()
        if argument == "rock":
            self.choice = RPS.rock
        elif argument == "paper":
            self.choice = RPS.paper
        elif argument == "scissors":
            self.choice = RPS.scissors
        else:
            raise


#This is a helper class that is called throughout the bot.              
class subf():
    def __init__(self,message):
        a=1
    
    #If you want someone to react to rules before using the discord, you'll need to setup this function
    async def gethell(self,member):
        success=0
        while success==0:
            channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
            server=channre.server              
            rulesch = self.bot.get_channel("351617228157878272")
            #print(rulesch.id)
            msgid1 = await self.bot.get_message(rulesch,"387389760068386821")
            msgid2 = await self.bot.get_message(rulesch,"387389972094648341")
            #count the number of reactions on the rules messages
            rmsg1=0
            for xi in range(0,len(msgid1.reactions)):
                useri = await self.bot.get_reaction_users([x for x in msgid1.reactions][xi])
                for yi in range(0,len(useri)):
                    rmsg1+=1
            rmsg2=0
            for xi in range(0,len(msgid2.reactions)):
                useri = await self.bot.get_reaction_users([x for x in msgid2.reactions][xi])
                for yi in range(0,len(useri)):
                    rmsg2+=1
            ormsg1=rmsg1
            ormsg2=rmsg2
            print(rmsg1)
            print(rmsg2)
            
            ARPr=await self.bot.send_message(rulesch,member.mention + ", review the rules here. Once completed, react to __**each**__ of the rules messages with any emoji (by clicking any of the reactions to __**ALL THREE**__ rules messages), __**then**__ react to this message.  You will not allowed to complete registration until this step is completed.  If you reacted as I've asked, and this message doesn't get removed, it means you've waited too long, and you need to restart the process by typing `%approval` via DM to me.")
            
            
            #tmess1 = await self.bot.wait_for_reaction(emoji=None, user=member, timeout=None, message=msgid1, check=None)
            tm=await self.bot.wait_for_reaction(timeout=3000,message=ARPr)
            rmsg1=0
            for xi in range(0,len(msgid1.reactions)):
                useri = await self.bot.get_reaction_users([x for x in msgid1.reactions][xi])
                for yi in range(0,len(useri)):
                    rmsg1+=1
            rmsg2=0
            for xi in range(0,len(msgid2.reactions)):
                useri = await self.bot.get_reaction_users([x for x in msgid2.reactions][xi])
                for yi in range(0,len(useri)):
                    rmsg2+=1
            if rmsg2>ormsg2 and rmsg1>ormsg1:
                success=1
            await self.bot.delete_message(ARPr)
            print(tm)
    
    #This function creates the raid 
    async def raidbypass(self,message,msgtxt):
        """Create a new raid announcement!"""
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server

        mutelist=[]
        a11=1
        if a11==1:
        #try:
            
            alltimeout=30
            if message.channel.is_private==True:
                donada=1
            else:
                if not (message.channel.id==self.raidsightings or message.channel.id==self.programid):# or message.channel.id==self.raidsightings or      message.channel.id==self.RaidNotifier):
                    chh=self.bot.get_channel(self.raidsightings)
                    await self.bot.send_message(message.channel,"Sorry, trainer. Please go to "+chh.mention+"  to enter this command.")
                    return
            #await self.bot.send_message(message.channel,"A system update is being performed.  Data entry will be enabled in 5 minutes.")
            #return
            ara=self.mutemap
            if ara==1:
                try:
                    if (message.author.id=="341977078213902336"):
                        await self.bot.send_message(message.channel,"To continue, please post a screen capture of the raid boss.")
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        if len(msgrt.attachments)==0:
                            await self.bot.send_message(message.channel,"This is not a gym screen capture.  Please start over.")
                            return
                        if "%raid" in msgrt.content:
                            await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                            return
                except:
                    arrr=1
                    await self.bot.send_message(message.channel,"I need a screen capture of the gym to continue.  Please start over.") 
                    return
            member = discord.utils.get(server.members, name=message.author.name)
            b=discord.Server.get_member(server,message.author.id)
            f=b.roles
            isRO=0
            for findl in range(1,len(f)):
                if f[findl].id==self.RaidObserver:
                    isRO=0
                    break
            if any(xpp == message.author.display_name for xpp in self.threeleaders):
                isRO=0

            #See if this message just needs to be parsed
            oneline=0
            maxatt=3
            arff=msgtxt.split(" ")
            print (arff)
            #arff=message.content.split(" ")
            if len(arff)>=5:
                oneline=1
                maxatt=1
                location=""
                for y in arff[4:]:
                    location+=y + " "
                status=arff[1]  #1=egg 2=hatched
                #phystime=
                #try:
                #    phystime
                #phystime=
                if status=="1":
                    if not "LEVEL" in arff[2].upper():  
                        await self.bot.send_message(message.channel,"To input a raid egg, you must say `LevelX`!")
                        return
                    type=arff[2]    #ensure the bossname starts with level
                    timeleft=int(arff[3])
                    if (timeleft)>60 or (timeleft)<0:
                        await self.bot.send_message(message.channel,"The number of minutes on an egg must be between 0 and 60")
                        return
                if status=="2":
                    type=arff[2]    #if 
                    timeleft=int(arff[3])
                    if (timeleft)>self.bossactivetime or (timeleft)<0:
                        await self.bot.send_message(message.channel,"The number of minutes on a boss must be between 0 and 45")
                        return
                print("%raid " + status + " " + type + " " + str(timeleft) + " " + str(location))
                #See if an ex-raid gym
            
            if int(timeleft)<15 and status=="2":
                xtra="Doesn't seem fair to not give people sufficient time to get to a raid.  I can't let you enter that in good conscience (15 mins required)."
                await self.bot.send_message(message.channel, xtra)
                #attempt+=1
                return
            
            #return            
            
            sill=1
            if sill==1:
            #try:
                await asyncio.sleep(0.5)
                attempt=0
                #maxatt=3
                success=0
                extra="Looks like you're trying to tell everyone about a raid. If you need to quit at any time, press `q`.\n"
                while attempt<maxatt and success==0:
                    
                    if oneline==0:
                        await self.bot.send_message(message.channel,extra+"__**What is the Pokemon Go gym name?**__ \nYou may enter *a keyword* or the first 8 letters without spaces or special characters (i.e. A+ Storage Mural = astorage)")
                        extra=""
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        location=msgrt.content
                    else:
                        success=1
                        print (location)
                        #location=msgrt.content
                    loc=location
                    newloca=location
                    if oneline==0:
                        if "%raid" in location:
                            await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                            return
                        if msgrt.content.upper()=="Q": 
                            await self.bot.send_message(message.channel,"Feeling sad now... :frowning:")
                            return
                    #print(location)
                    cntt=0
                    uniq=0
                    grid=0
                    dontcont=0
                    if len(location)<8:
                        for x in range(0,8-len(location)):
                            location=location + " "
                    loc=location[0:8]
                    
                    for x in self.angroup:
                        if loc.upper()==x.upper():
                            uniq=uniq+1
                            Nameval=self.cngroup[cntt]
                            #print(Nameval+"WTF")
                            #linkn=self.lngroup[cntt]
                            gymlat=self.latgroup[cntt]
                            gymlon=self.longroup[cntt]
                            linkn= "" + gymlat + "," + gymlon +""+ ""
                            olink=linkn
                            #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                        cntt=cntt+1
                    cntt=0
                    
                    if uniq>1:
                        optnum=1
                        cntt=0
                        ncha=0
                        LVal=[]
                        Nameval=''
                        newloca=''
                        for x in self.sngroup:
                            if loc.upper()==x.upper():
                                Nameval=Nameval + str(optnum) + ")" + self.cngroup[cntt] + "\n"#: Use '" + self.angroup[cntt] + "'\n"
                                LVal.append(self.angroup[cntt])
                                optnum=optnum+1
                                ncha=ncha+1
                            cntt=cntt+1
                    
                        if ncha==0:  #Channel name isn't in alt or shortname
                            await self.bot.say("`The gym name you entered is not available in the system`")
                            dontcont=1
                            attempt+=1
                            #return
                        elif ncha>1: #Unique Channel name doesn't exist
                            await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.say("`{}`".format(Nameval))
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                            try:
                                loc=LVal[int(msgrt.content)-1]
                                #Nameval=loc
                                newloca=loc
                                print(loc+"Hello")
                            except:
                                attempt+=1
                                dontcont=1
                                #return
                    elif uniq==0: #see if keyword
                        scrubmess=await subf.filtNameval(self,location.upper())          
                        locn=""
                        #Try finding the names of the gyms
                        loclist=[]
                        for x in self.WL:
                            if x.upper() in location.upper(): 
                                loclist.append(x)
                        #Xref the list with the gym names
                        possn=[]
                        maxcom=0
                        gyml=""
                        cntt=0
                        gymlist=[]
                        suggch=[]
                        
                        for y in self.cngroup:
                            comwords=0
                            tpp=await subf.filtNameval(self,y)
                            for x in loclist:
                                if x.upper() in tpp.upper():
                                    comwords+=1
                                    gymlist.append(y)
                            if comwords>maxcom:
                                suggch.append(y)
                                #gyml=self.lngroup[cntt]
                                gymlat=self.latgroup[cntt]
                                gymlon=self.longroup[cntt]
                                gyml= "" + gymlat + "," + gymlon +""+ ""
                                
                                maxcom=comwords
                            cntt+=1
                        #get unique gyms names only
                        ugym=[]
                        for x in gymlist:
                            if x not in ugym:
                                ugym.append(x) 
                        print (ugym)
                        print (gymlist)
                        
                        txt="`"
                        cntr=1
                        for x in ugym:
                            txt+=str(cntr)+ ") " +x +" \n"
                            cntr+=1
                        txt+="`"
                        #User selects which gym if confused
                        alltimeout=30
                        bypassq=0
                        if len(ugym)>1:
                            await self.bot.send_message(message.channel,"I got confused. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.send_message(message.channel,txt)
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                            try:
                                loclist=ugym[int(msgrt.content)-1]
                                Nameval=loclist
                                newloca=loclist
                                #bypassq=1
                                #newloca=loc
                                print(loclist)
                            except:
                                attempt+=1
                                dontcont=1
                                bypassq=1
                        elif len(ugym)==0:
                            #no keyword found
                            attempt+=1
                            dontcont=1
                            bypassq=1
                        else:                            
                            loclist=ugym[0]
                            newloca=loclist
                            Nameval=loclist
                        
                        #print(bypassq)
                        if bypassq==0:
                            cntt=0

                            #print(loclist+"GOOD")
                            for y in self.cngroup:
                                if loclist==y:
                                    #gyml=self.lngroup[cntt]
                                    gymlat=self.latgroup[cntt]
                                    gymlon=self.longroup[cntt]
                                    gyml= "" + gymlat + "," + gymlon +""+ ""
                                    newloca=self.angroup[cntt]
                                    Nameval=self.cngroup[cntt]
                                    print(newloca)
                                    #gyml=self.lngroup[cntt]
                                cntt+=1
                            
                            #now find the gym in the lists
                            cntt=0
                            uniq=0
                            grid=0
                            
                            for x in self.group1an:
                                if newloca.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=1
                                    Nameval=self.group1cn[cntt]
                                    #linkn=self.group1ln[cntt]
                                    #newloca=self.group1an[cntt]
                                    mutelist=await subf.getmemlist2(self,message,self.muteg1)
                                    gymlat=self.group1lat[cntt]
                                    gymlon=self.group1lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ ""
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group2an:
                                if newloca.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=2
                                    Nameval=self.group2cn[cntt]
                                    #linkn=self.group2ln[cntt]
                                    #newloca=self.group2an[cntt]
                                    mutelist=await subf.getmemlist2(self,message,self.muteg2)
                                    gymlat=self.group2lat[cntt]
                                    gymlon=self.group2lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ ""
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group3an:
                                if newloca.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=3
                                    Nameval=self.group3cn[cntt]
                                    #linkn=self.group3ln[cntt]
                                    #newloca=self.group3an[cntt]
                                    mutelist=await subf.getmemlist2(self,message,self.muteg3)
                                    gymlat=self.group3lat[cntt]
                                    gymlon=self.group3lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ ""
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            print(uniq)
                        #uniq=0
                    #print(loc)
                    if dontcont==0:
                        cntt=0
                        uniq=0
                        grid=0
                        
                        for x in self.group1an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=1
                                Nameval=self.group1cn[cntt]
                                #linkn=self.group1ln[cntt]
                                mutelist=await subf.getmemlist2(self,message,self.muteg1)
                                gymlat=self.group1lat[cntt]
                                gymlon=self.group1lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ ""
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group2an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=2
                                Nameval=self.group2cn[cntt]
                                #linkn=self.group2ln[cntt]
                                mutelist=await subf.getmemlist2(self,message,self.muteg2)
                                gymlat=self.group2lat[cntt]
                                gymlon=self.group2lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ ""
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group3an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=3
                                Nameval=self.group3cn[cntt]
                                #linkn=self.group3ln[cntt]
                                mutelist=await subf.getmemlist2(self,message,self.muteg3)
                                gymlat=self.group3lat[cntt]
                                gymlon=self.group3lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ ""
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                    
                        #if uniq==0:
                            
                            
                                
                                #linkn="Directions to " + loclist + " can be found here:\n " + "https://goo.gl/" + gyml + ""
                                #await self.bot.send_message(message.channel, linkn) 
                                #print(loclist) 
                            
                    if uniq==0:
                        await self.bot.say("`The gym name you entered is not available in the system`")
                        attempt+=1
                            #else:
                            #    success=1
                            #return
                
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                #print("Made to return")
                #print(Nameval)
                RaidBossfound=0
                isLoc=0
                if any(xpp == Nameval for xpp in self.Locbypass): #We need to allow this boss to be entered anyway
                    RaidBossfound=1    
                    isLoc=1
                

                #Raid already entered - here
                #if chch1==None and chch2==None: #The channels haven't been created yet, and continue
                #    rpp=1
                #else:
                #    await self.bot.send_message(message.channel,message.author.display_name+", looks like that raid was already created!")
                #    return
                tempNameval=await subf.filtNameval(self,Nameval)
                
                for x in self.allbutmtch:
                    rdd=self.bot.get_channel(x)
                    try:
                        xrd=rdd.name.split('---')
                        if xrd[0]==tempNameval or xrd[1]==tempNameval:
                    #if tempNameval in rdd.name:
                            await self.bot.send_message(message.channel,message.author.display_name+", looks like that raid was already created!")
                            return
                    except:
                        allowcont=1
                
                attempt=0
                
                success=0
                #time=0
                
                extra="So there's a raid about to start at "+Nameval
                #if Nameval=="John Purdue Fountain":
                #    if not message.author=="330830919604633604":
                #        await self.bot.send_message(message.channel, "CRITICAL ERROR.")
                #        return
                while success==0 and attempt<maxatt:
                    if oneline==0:
                        status=0
                        await self.bot.send_message(message.channel, extra+ ". Has the egg hatched yet (Y/N)?")
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        
                    else:
                        success=1
                    if oneline==0:
                        if "%raid" in msgrt.content:
                            await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                            return
                        if msgrt.content.upper()=="Q": 
                            await self.bot.send_message(message.channel,"Feeling sad now... :frowning:")
                            return
                        if msgrt.content.upper()=="N": 
                            await self.bot.send_message(message.channel,"So, it's still an egg! How many minutes until the egg hatches (round down)?")
                            #time=45
                            status="1"
                            success=1
                        elif msgrt.content.upper()=="Y": 
                            await self.bot.send_message(message.channel,"So, it's a boss ready to get taken down! How many minutes until the raid boss leaves (round down)?")
                            #time=0
                            status="2"
                            success=1
                        else: 
                            extra="I didn't quite get that."
                            attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                    
                 
                
                if status=="1":  #If an egg
                    attempt=0
                    success=0
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            timeleft=0
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        else: 
                            success=1
                        if oneline==0:                        
                            try:
                                if "%raid" in msgrt.content:
                                    await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                    return
                                if msgrt.content.upper()=="Q": 
                                    await self.bot.send_message(message.channel,"Feeling sad now... :frowning:")
                                    return
                                if int(msgrt.content)<60 and int(msgrt.content)>0: 
                                    timeleft=int(msgrt.content)
                                    if timeleft>30 and isRO==1:
                                        areaf=1
                                        await self.bot.send_message(message.channel, "Top 3 on the leaderboard cannot enter data yet for this raid (wait 30 minutes).  Please wait for 15 minutes to elapse.  HINT, HINT, WINK, WINK for those who want to try %raid!")
                                        #return
                                    success=1
                                else:
                                    attempt+=1
                                    #extra="Something doesn't look right there. The time should be between 0 and 60 minutes."
                                    #await self.bot.send_message(message.channel, extra+ " \nHow many minutes until the egg hatches (round down)?")
                                    #attempt+=1
                            except:
                                extra="Something doesn't look right there. The time should be between 0 and 60 minutes."
                                await self.bot.send_message(message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                attempt+=1
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return
                    #print(message.author.id)
                    if oneline==1: #Make sure someone isn't entering low level eggs at non-ex gyms
                        if isLoc==0 and status=="1":
                            if type.upper()=="LEVEL1" or type.upper()=="LEVEL2":
                                await self.bot.send_message(message.channel, "I can only notify everyone about Level 3,4,and 5 eggs unless it's at an ex-raid gym.  Sorry.")
                                return
                    #if message.author.id=="345200594421547018":
                    #    print(str(isLoc) + "CMK_debug")
                    #    return
                    attempt=0
                    success=0
                    if oneline==0:
                        await self.bot.send_message(message.channel,"Last question! What tier level is the egg?")
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        else:
                            success=1
                        
                        if oneline==0:
                            try:
                                if "%raid" in msgrt.content:
                                    await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                    return
                                if msgrt.content.upper()=="Q": 
                                    await self.bot.send_message(message.channel,"Feeling sad now... :frowning:")
                                    return
                                if int(msgrt.content)<6 and int(msgrt.content)>0: 
                                    if isLoc==1:
                                        type="Level"+msgrt.content
                                        success=1
                                    else:
                                        if int(msgrt.content)<6 and int(msgrt.content)>2:
                                            type="Level"+msgrt.content
                                            success=1
                                        else:
                                            await self.bot.send_message(message.channel, "I can only notify everyone about Level 3,4,and 5 eggs unless it's at an ex-raid gym.  Sorry.")
                                            return
                                else:
                                    extra="Something doesn't look right there. The tier should be between 1 and 5, inclusive."
                                    await self.bot.send_message(message.channel, extra+ " \nWhat tier level is the egg?")
                                    attempt+=1
                            except:
                                extra="Something doesn't look right there. What tier level is the egg?"
                                await self.bot.send_message(message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                attempt+=1
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return
                
                elif status=="2":  #If a boss
                    attempt=0
                    success=0
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            msgrt2 = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        else:
                            success=1
                        #print (int(msgrt2.content))
                        if oneline==0:
                            try:
                                if "%raid" in msgrt.content:
                                    await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                    return
                                if msgrt2.content.upper()=="Q": 
                                    await self.bot.send_message(message.channel,"Feeling sad now... :frowning:")
                                    return
                                #print (int(msgrt2.content))
                                if int(msgrt2.content)<self.bossactivetime and int(msgrt2.content)>=15: 
                                        timeleft=int(msgrt2.content)
                                        success=1
                                elif int(msgrt2.content)<15:
                                    xtra="Doesn't seem fair to not give people sufficient time to get to a raid.  I can't let you enter that in good conscience (15 mins required)."
                                    await self.bot.send_message(message.channel, xtra)
                                    attempt+=1
                                    return
                                else:
                                    extra="Something doesn't look right there. The time should be between 0 and 45 minutes."
                                    await self.bot.send_message(message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                    attempt+=1
                                    
                            except:
                                extra="Something doesn't look right there. The time should be between 0 and 45 minutes."
                                await self.bot.send_message(message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                attempt+=1
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return
                    #print("Before Raid Boss")
                    attempt=0
                    success=0
                    if oneline==0:
                        await self.bot.send_message(message.channel,"Last question! What is the name of the raid boss?")
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        else:
                            success=1
                        if oneline==0:
                            if "%raid" in msgrt.content:
                                await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                return
                            if msgrt.content.upper()=="Q": 
                                await self.bot.send_message(message.channel,"Feeling sad now... :frowning:")
                                return
                            type=msgrt.content
                        
                        raidn=0
                        for x in range(0,len(self.L4types)):
                            if type.upper()==self.L4types[x].upper():
                                RaidBossfound=1
                                raidn=4
                        for x in range(0,len(self.L5types)):
                            if type.upper()==self.L5types[x].upper():
                                RaidBossfound=1    
                                raidn=5                
                        for x in range(0,len(self.L3types)):
                            if type.upper()==self.L3types[x].upper():
                                RaidBossfound=1    
                                raidn=3 
                        for x in range(0,len(self.PStypes)):
                            if type.upper()==self.PStypes[x].upper():
                                RaidBossfound=1    
                                raidn=6                
                        for x in range(0,len(self.OItypes)):
                            if type.upper()==self.OItypes[x].upper():
                                RaidBossfound=1    
                                raidn=7
                        #Origname
                        
                        if RaidBossfound==0:
                            await self.bot.send_message(message.channel,"I couldn't find that raid boss. What's the name of the raid boss?")
                            attempt+=1
                        else:
                            success=1
                        
                        
                        
                        
                        
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return
                
                if oneline==0:
                    if status=="1":  #If an egg
                        await self.bot.send_message(message.channel,"Based on what you told me: \nA "+type+" egg will hatch in "+str(timeleft)+" minutes at "+Nameval+". \nDid I understand you correctly (Y/N)?")
                    elif status=="2":  #If an egg
                        await self.bot.send_message(message.channel,"Based on what you told me: \nA "+type+" will be at "+Nameval+" for the next "+str(timeleft)+" minutes. \nDid I understand you correctly (Y/N)?")
                    attempt=0
                    success=0
                    #if oneline==0:
                    while success==0 and attempt<maxatt:
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                        if msgrt.content.upper()=="N": 
                            await self.bot.send_message(message.channel,"Looks like you may have entered something wrong then.  How about you try again.")
                            success=1
                            return
                        elif msgrt.content.upper()=="Y": 
                            success=1
                        else: 
                            await self.bot.send_message(message.channel, "Please answer the question, did I get that right (Y/N)?")
                            attempt+=1
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return    
            else:
            #except:
                await self.bot.say("Purdue Pollster fell asleep while waiting for a reply, but you can always try again!")
                return
            
            #await self.bot.send_message(message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
            #await self.bot.send_message(message.channel,"The raid notification has been made! Thank you.")
            #return
            print(status)
            print(type.upper())
            print(str(timeleft))
            print(newloca[0:8])
            origmessv="%raid " + status + " " + type.upper() + " " + str(timeleft) + " " + newloca[0:8]
            #origmessv2=type.ljust(8) + " " + str(timeleft).ljust(5)+ " " +newloca[0:8].ljust(8)+ " "+ " " +message.author.display_name
            #print (origmessv2)
            #return
            #return
            #argg=timeleft.split(':')
            #if len(argg)>1:
            #    await self.bot.say("`Please do not include seconds within the time remaining!`")
                 
            if status == "1": 
                statmess=" Egg"
            elif status=="2":
                statmess="Boss"
            else:
                await self.bot.say("The status must be `1` or `2`")
                return
            str_time = datetime.utcnow()+timedelta(hours=self.timez)
            hatch_time= str_time
            if status=="1":
                str_time += timedelta(minutes=self.bossactivetime)
            else:
                hatch_time+= timedelta(minutes=-self.bossactivetime)
            argg=timeleft
            str_time += timedelta(minutes=int(argg))
            hatch_time+= timedelta(minutes=int(argg))
            str_time = str_time.strftime(self.timeform)
            hatch_time = hatch_time.strftime(self.timeform)
            #hatch_time = hatch_time.strftime('%H:%M:%S')
            #hatch_time2 = hatch_time.strftime('%I:%M:%S')
            endtime1=str_time
            oendtime=str_time
            linkn="__**RAID:**__ A " + type.upper() + " raid boss ends at "
            #linkn+= str_time +"\n(Hatch time of : "+ hatch_time +")\n" + "https://goo.gl/" + olink + "\n"
            linkn+=str_time +"\n(Hatch time of : "+ hatch_time +")\n" + "https://www.google.com/maps?q=" + olink
            
            #Get the appropriate ID here for location. Find the last channel in the list
            if grid==1:
                IDval_loc=await subf.getchid(self,self.g1locaid)
            elif grid==2:
                IDval_loc=await subf.getchid(self,self.g2locaid)
            elif grid==3:
                IDval_loc=await subf.getchid(self,self.g3locaid)
                
            Origname=Nameval
            Orignamo=Nameval
            Nameval=await subf.filtNameval(self,Nameval)       
            
            channloc=self.bot.get_channel(IDval_loc)
            #if not 'blank-0' in channloc.name:
            #    await self.bot.say("This raid cannot be entered because the maximum number of channels has been exceeded. Sorry.")
            #    return
                
            
            raidn=0
            for x in range(0,len(self.L4types)):
                if type.upper()==self.L4types[x].upper():
                    RaidBossfound=1
                    raidn=4
            for x in range(0,len(self.L5types)):
                if type.upper()==self.L5types[x].upper():
                    RaidBossfound=1    
                    raidn=5                
            for x in range(0,len(self.L3types)):
                if type.upper()==self.L3types[x].upper():
                    RaidBossfound=1    
                    raidn=3 
            for x in range(0,len(self.PStypes)):
                if type.upper()==self.PStypes[x].upper():
                    RaidBossfound=1    
                    raidn=6
            for x in range(0,len(self.OItypes)):
                if type.upper()==self.OItypes[x].upper():
                    RaidBossfound=1    
                    raidn=7
            #Get the boss channel ID here
            modv=0
            isPS=0
            
            if raidn==3:
                IDval_rb=await subf.getchid(self,self.L3groupid)
                modv=1
            elif raidn==4:
                IDval_rb=await subf.getchid(self,self.L4groupid)
                modv=1
            elif raidn==5:
                IDval_rb=await subf.getchid(self,self.L5groupid)
                modv=1
            elif raidn==6:  #It could be shiny
                isPS=1
                IDval_rb=await subf.getchid(self,self.PSgroupid)
                modv=1
            elif raidn==7:  #It could be shiny
                isPS=0
                IDval_rb=await subf.getchid(self,self.PSgroupid)
                modv=1
            if modv==0: #Then this is a forced raid boss entry
                channrb=channloc
            else:
                channrb=self.bot.get_channel(IDval_rb)    

            
             #If the channel is unique, find it to see if the data has been entered already
            counter = 0
            ####################################################################################
            #If either channel name exists and hasn't ended yet, prevent it from being added
            ####################################################################################
            rrx=0
            try:
                if raidn==3:
                    rrx=await subf.prevover2(self,self.L3groupid,Nameval,type,message)
                elif raidn==4:
                    rrx=await subf.prevover2(self,self.L4groupid,Nameval,type,message)
                elif raidn==5:
                    rrx=await subf.prevover2(self,self.L5groupid,Nameval,type,message)
                elif raidn==6:
                    rrx=await subf.prevover2(self,self.PSgroupid,Nameval,type,message)
                elif raidn==7:
                    rrx=await subf.prevover2(self,self.PSgroupid,Nameval,type,message)
            except:
                arerfe=1
            if rrx==1:
                return
                
            chch1=discord.utils.get(server.channels, name=Nameval+ "---" + type.lower())
            chch2=discord.utils.get(server.channels, name=type.lower() + "---" + Nameval)
            if chch1==None and chch2==None: #The channels haven't been created yet, and continue
                rpp=1
            else:
                await self.bot.send_message(message.channel,message.author.display_name+", looks like that raid was already created!")
                return
            try:
                for x in self.allbutmtch:
                    rdd=self.bot.get_channel(x)
                    if Nameval in rdd.name:
                        await self.bot.send_message(message.channel,message.author.display_name+", looks like that raid was already created!")
                        return
            except:
                afere=1
            
            member = discord.utils.get(server.members, name=message.author.name)
            b=discord.Server.get_member(server,message.author.id)
            f=b.roles
            
            isallowed=0
            bypassa=0
            role_RT=discord.utils.get(server.roles, id=self.RaidTrainer) 
            role_RO=discord.utils.get(server.roles, id=self.RaidObserver) 
            bypassa=1
            if any(xpp == role_RT for xpp in f):
                bypassa=1
            if any(xpp == role_RO for xpp in f):
                bypassa=1
            
            
            #for findl in range(1,len(f)):
                #try: #await self.bot.send_message(message.channel,f[findl].id + "&" + self.RaidObserver)
                #if f[findl].id==self.RaidObserver or f[findl].id==self.RaidTrainer:
            if bypassa==1:
                isallowed=1
                if not message.id=="532299638015918081":
                    await self.bot.send_message(message.channel,message.author.display_name+", your entry will be added momentarily. Thank you!")
                try:
                    await self.bot.move_channel(channrb, 0)
                    await self.bot.edit_channel(channrb, name=Nameval+ self.chanstrsp + type.upper() )
                except:
                    arefef=1
                await self.bot.move_channel(channloc, 0)
                await self.bot.edit_channel(channloc, name=type.upper() + self.chanstrsp + Nameval)
                #Need to set permissions for the channel now
                for idx in f: 
                    if idx.id==self.Approved:   
                        role_everyone = idx
                plopp=00
                if plopp==1:
                    role_pogomod=discord.utils.get(server.roles, id=self.POGOmod)  
                    overwrite = channloc.overwrites_for(role_everyone)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channloc, role_everyone, overwrite)
                    overwrite = channrb.overwrites_for(role_everyone)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channrb, role_everyone, overwrite)
                    overwrite = channloc.overwrites_for(role_pogomod)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channloc, role_pogomod, overwrite)
                    overwrite = channrb.overwrites_for(role_pogomod)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channrb, role_pogomod, overwrite)
                    role_RO=discord.utils.get(server.roles, id=self.RaidObserver)
                    overwrite = channloc.overwrites_for(role_RO)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channloc, role_RO, overwrite)
                    overwrite = channrb.overwrites_for(role_RO)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channrb, role_RO, overwrite)
                CPmax=0
                bossemo=[]
                for x in range(0,len(self.L4types)):
                    if type.upper()==self.L4types[x].upper():
                        CPmax=self.L4maxCP[x]
                        bossemo.append(self.L4emoji[x])
                for x in range(0,len(self.L5types)):
                    if type.upper()==self.L5types[x].upper():
                        CPmax=self.L5maxCP[x]
                        bossemo.append(self.L5emoji[x])
                for x in range(0,len(self.L3types)):
                    if type.upper()==self.L3types[x].upper():
                        CPmax=self.L3maxCP[x]
                        bossemo.append(self.L3emoji[x])
                for x in range(0,len(self.PStypes)):
                    if type.upper()==self.PStypes[x].upper():
                        CPmax=self.PSmaxCP[x]
                        bossemo.append(self.PSemoji[x])
                for x in range(0,len(self.OItypes)):
                    if type.upper()==self.OItypes[x].upper():
                        CPmax=self.OImaxCP[x]
                        bossemo.append(self.OIemoji[x])
                if len(bossemo)==0:
                    bossemo=["<:item_pokeball:284615009299070976>"]
                addlstr=""
                #print (CPmax)
                if CPmax>0:        
                    addlstr="\nThe CP for a 100IV " + type.upper() + " is " + str(CPmax)
                
                polltime = datetime.utcnow()+timedelta(hours=self.timez)
                if status=="1":
                    polltime += timedelta(minutes=self.bossactivetime)
                argg=timeleft
                polltime += timedelta(minutes=int(argg))
                tpolltime=polltime.strftime('%H:%M:%S')
                
                tdeltat = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime("0:0:0", '%H:%M:%S')
                hours, remainder = divmod(tdeltat.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                
                polltime += timedelta(seconds=int(60-seconds))
                polltime += timedelta(minutes=1)
                polltime += timedelta(minutes=-self.bossactivetime)
                #polltime += timedelta(minutes=15)
                trrta=polltime.strftime(self.timeform)
                             
                tdeltat3 = datetime.strptime(trrta, self.timeform)-datetime.strptime("0:0:0", '%H:%M:%S')
                hours1, remainder1 = divmod(tdeltat3.total_seconds(), 3600)
                minutes1, seconds1 = divmod(remainder1, 60)
                                
                                
                d3=timedelta(minutes=-(minutes1 % 5)+5)
                polltime=polltime + d3
                
                weathertime=0
                d3we=timedelta(minutes=-(minutes1 % 60)+60-5-4)
                weatherpoll=polltime + d3we
                
                
                tpollwe = weatherpoll.strftime('%H:%M:' + "00")
                if (minutes1 % 60)<45:
                    weathertime=1
                #print('@Start: ' + tpollwe)
                #tpoll = polltime.strftime('%H:%M:'+"00")
                #for x in range(0,self.maxtimeslots):
                #    print('@Start: ' + tpoll)
                #    #if not channrb==channloc:
                #    #    msggr2=await self.bot.send_message(channrb,'@Start: ' + tpoll)
                #    #await asyncio.sleep(0.25)
                #    polltime += timedelta(minutes=self.raidspacing)
                #    tpoll = polltime.strftime('%H:%M:%S')
                #return
                tpoll = polltime.strftime('%I:%M:'+"00"+"%p")
                #clear the channel first
                deleted=await self.bot.purge_from(channloc, limit=100)
                await self.bot.move_channel(channloc, 0)
                channrb=channloc #ADDED 01292018
                
                
                memlist=[]
                #Add logic here for the shiny notification
                shinynot=discord.utils.get(server.roles, id=self.PSNotify)
                shinyemo=""
                if isPS==0:
                    shinyn=""
                else:
                    shinyn=shinynot.mention
                    await subf.grantacc(self,channloc,channrb,shinynot)
                    shinyemo=self.PSemoji[0]
                    memlist+=await subf.getmemlist2(self,message,self.PSNotify)
                #Get the ID of the correct notify
                cntt=0
                Addlloc=0
                for xpp in self.Locbypass: #We need to allow this boss to be entered anyway
                    if xpp == Origname:
                        Addlloc=cntt
                        break
                    cntt+=1
                Locnot=discord.utils.get(server.roles, id=self.AddlNotiid[Addlloc])
                Locnot2=discord.utils.get(server.roles, id=self.SilentEX)
                locatemo=""
                if isLoc==0:
                    Locan=""
                else:
                    Locan=Locnot.mention
                    await subf.grantacc(self,channloc,channrb,Locnot)
                    await asyncio.sleep(0.05)
                    await subf.grantacc(self,channloc,channrb,Locnot2)
                    locatemo=self.emoji_exgym
                
                type=type.upper()
                xrs=channloc
                if not channrb==channloc:
                    xrs2=channrb
                else:
                    xrs2=xrs
                cntt=0
                mentioned=0
                msgchann = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.genchid)
                #msgchann=self.bot.get_channel(self.genchid)
                origname=Orignamo
                endtime=oendtime
                if not channrb==channloc:
                    chmention = xrs.mention + " or\n          " + xrs2.mention
                else:
                    chmention = xrs.mention
                linky="(Hatch time of : "+ hatch_time +")   https://www.google.com/maps?q="+olink + addlstr
                
                uniqemo=[]
                for x in bossemo:
                    if x not in uniqemo:
                        uniqemo.append(x) 
                emoji=uniqemo
                
                outp=""
                for x in emoji:
                    outp+=x
                
                emoji=outp+ shinyemo + locatemo
                
                allmention=""
                msgg6=None
                for x in self.L3types:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentL3)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.L3Notify)
                        memlist+=await subf.getmemlist2(self,message,self.L3Notify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        
                        nid=self.L3notid[cntt]
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist2(self,message,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention +" "+ rr5.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(, rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan+ ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        else:
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention  +" "+Locan+" "+shinyn + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                    cntt+=1
                cntt=0
                for x in self.L4types:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentL4)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.L4Notify)
                        memlist+=await subf.getmemlist2(self,message,self.L4Notify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        nid=self.L4notid[cntt]
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist2(self,message,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention +" "+ rr5.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        else:
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention  +" "+Locan+" "+shinyn + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                    cntt+=1
                cntt=0
                for x in self.L5types:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentL5)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.L5Notify)
                        memlist+=await subf.getmemlist2(self,message,self.L5Notify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        nid=self.L5notid[cntt]
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist2(self,message,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention +" "+ rr5.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        else:
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+shinyn + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                    cntt+=1
                if mentioned==0: #Maybe its a shiny
                    cntt=0
                    for x in self.PStypes:
                        if type==x.upper():
                            mentioned=1
                            #Show to Silent only
                            rr2=discord.utils.get(server.roles, id=self.SilentPS)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            #and hold on to the notify version
                            rr2=discord.utils.get(server.roles, id=self.PSNotify)
                            memlist+=await subf.getmemlist2(self,message,self.PSNotify)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            nid=self.PSnotid[cntt]
                            if not nid=="0":
                                rr5=discord.utils.get(server.roles, id=nid)
                                memlist+=await subf.getmemlist2(self,message,nid)
                                await subf.grantacc(self,channloc,channrb,rr5)
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention +" "+ rr5.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention  +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                            else:
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+Locan+ ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        cntt+=1
                if mentioned==0: #Maybe its a raid of interest
                    cntt=0
                    for x in self.OItypes:
                        if type==x.upper():
                            mentioned=1
                            #Show to Silent only
                            rr2=discord.utils.get(server.roles, id=self.SilentOI)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            #and hold on to the notify version
                            rr2=discord.utils.get(server.roles, id=self.OINotify)
                            memlist+=await subf.getmemlist2(self,message,self.OINotify)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            nid=self.OInotid[cntt]
                            if not nid=="0":
                                rr5=discord.utils.get(server.roles, id=nid)
                                memlist+=await subf.getmemlist2(self,message,nid)
                                await subf.grantacc(self,channloc,channrb,rr5)
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention +" "+ rr5.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention  +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                            else:
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+Locan+ ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        cntt+=1
                if mentioned==0: #If still not mentioned, its a special location raid.  Its not shiny or a system raid boss
                    cntt=0
                    for x in self.Locbypass:
                        if Origname==x:
                            mentioned=1
                            rr2=discord.utils.get(server.roles, id=self.AddlNotiid[cntt])
                            await subf.grantacc(self,channloc,channrb,rr2)
                            #nid=self.PSnotid[cntt]
                            nid="0"
                            if not nid=="0":
                                rr5=discord.utils.get(server.roles, id=nid)
                                await subf.grantacc(self,channloc,channrb,rr5)
                                if self.notifyon==1:
                                    allmention = rr2.mention +" "+ rr5.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention + rr5.mention + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                            else:
                                if self.notifyon==1:
                                    allmention = rr2.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        cntt+=1
                #Now to get the stuff to update the #active_raids channel
                #ch=self.bot.get_channel(self.genchid)
                print("Made it here")
                ch = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.genchid)
                print(ch)
                #First we have to find the message in the channel searching for o
                olocation=Origname
                #newlist=""
                #print(olocation)
                #print(ch)
                #await self.bot.send_message(message.channel, "Your update request has been processed!  Thank you.")
                
                #newlist=Milk.mention + " " + L3.mention +" "+Spec.mention
                #async for message in self.bot.logs_from(ch, limit=100): #Gets a list of the last 500 messages in the channel 
                    #print(message.content)
                #    if olocation in message.content: #This channel is the one needing updating
                        #print(message.content)
                if msgg6==None:
                    msgg6=await subf.sendnote(self,msgchann,"",chmention,origname,endtime,emoji,linky)
                message=msgg6
                argg=message.content.split("\n")
                #"__**Raid:**__"+allmention is on the first line
                arggn=argg[0].split("**__")
                oldmention=arggn[1]
            
                argg6=argg[1].split("ends at ")
                timeplusoldemo=argg6[1]
                
                argg7=timeplusoldemo.split(" ")
                oldemo=argg7[1]
                
                modmessp2=""
                for x in argg[2::]:
                    modmessp2+="\n" + x 
                
                #Now we need to reconstruct the message with the new mentions
                try:
                    #modmess=arggn[0] + "**__" + newlist + "\n" + argg6[0]+ "ends at " + argg7[0] + " " + emoji + modmessp2
                    meat=arggn[0] + "**__" + "\n" + argg6[0]+ "ends at " + argg7[0] + " " + emoji 
                    #We need unique members of the memlist
                    uniqmem=[]
                    for x in memlist:
                        if x not in uniqmem:
                            uniqmem.append(x) 
                    memlist=uniqmem
                    
                    mutelist=await subf.timemute2(self,message,mutelist)
                    
                    
                    #Supress notifies to members of the mutegroup
                    msg=""
                    for f in memlist:
                        if not f in mutelist:
                            msg+=f.mention
                            if len(msg)>1000:
                                tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg)
                                await asyncio.sleep(1.0)
                                #await self.bot.edit_message(tms,meat)
                                await self.bot.delete_message(tms)
                                msg=""#

                    if len(msg)>=0:
                        tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg+Locan)
                        await asyncio.sleep(1.0)
                        #await self.bot.edit_message(tms,meat)
                        await self.bot.delete_message(tms)
                    
                    #msggg=await self.bot.send_message(ch,newlist) 
                    #await asyncio.sleep(2.0)
                    #await self.bot.delete_message(msggg)
                    #await self.bot.edit_message(message,modmess) 
                except:
                    modmess=message.content
                    
                    
                if not channrb==channloc:
                    await self.bot.send_message(channloc,linkn + "\n"+ channrb.mention)
                else:
                    if "olores" in Nameval:
                        await self.bot.send_message(channloc,linkn + "__**NOTE: DO NOT RAID IN FRONT OF THE EMERGENCY ROOM ENTRANCE**__\n")
                    else:
                        await self.bot.send_message(channloc,linkn)
                msggr=await self.bot.send_message(channloc, "\n" + "\nReact to one of the following times with any emoji:")
                #delm=await self.bot.pin_message(msggr)
                #delm=await self.bot.delete_message(delm)
                
                if not channrb==channloc:
                    deleted=await self.bot.purge_from(channrb, limit=100)
                    await self.bot.move_channel(channrb, 0)
                    await self.bot.send_message(channrb,linkn+ "\n"+ channloc.mention)
                    msggr=await self.bot.send_message(channrb, "\n" + "\nReact to one of the following times with any emoji:")
                    #delm=await self.bot.pin_message(msggr)
                    #delm=await self.bot.delete_message(delm)
                await asyncio.sleep(0.25)
                msggr=await self.bot.send_message(channloc,'@Start: ' + hatch_time)
                if not channrb==channloc:
                    msggr2=await self.bot.send_message(channrb,'@Start: ' + hatch_time)
                await asyncio.sleep(0.25)
                for x in range(0,self.maxtimeslots):
                    
                    
                    msggr=await self.bot.send_message(channloc,'@Start: ' + tpoll)
                    if not channrb==channloc:
                        msggr2=await self.bot.send_message(channrb,'@Start: ' + tpoll)
                    await asyncio.sleep(0.25)
                    polltime += timedelta(minutes=self.raidspacing)
                    tpoll = polltime.strftime(self.timeform)
                try:
                    delm=await self.bot.pin_message(msggr)
                    delm=await self.bot.pin_message(msggr2)
                except:
                    uppo=1
                polltime += timedelta(minutes=-self.maxtimeslots* self.raidspacing)
                tpoll = polltime.strftime('%H:%M:%S')
                if weathertime==1:
                    arp=1
                    #msggr=await self.bot.send_message(channloc,"Pre-weather change raid time:\n")
                    #msggr=await self.bot.send_message(channloc,'@Start: ' + tpollwe)
                msggr=await self.bot.send_message(channloc,"_Use `%addtime` to create a new time_")
                msggr=await self.bot.send_message(channloc,"_^^^^^^^^^^^^^_")
                msggr=await self.bot.send_message(channloc,"RaidTrain: N/A")
                #return
                #delete the system pin messages, but keep the pin
                async for message in self.bot.logs_from(channrb, limit=500): #Gets a list of the last 500 
                    if message.type==discord.MessageType.pins_add:
                        await self.bot.delete_message(message)
                async for message in self.bot.logs_from(channloc, limit=500): #Gets a list of the last 500 
                    if message.type==discord.MessageType.pins_add:
                        await self.bot.delete_message(message)
                
                
                
                
                
                await subf.editnote(self,msgg6,allmention,chmention,origname,endtime,emoji,linky)
                polltimez = datetime.utcnow()+timedelta(hours=self.timez)
                tpolltimez=polltimez.strftime('%m/%d/%y %H:%M:%S')
                number = sum(1 for line in open('raids_ALL.txt'))+1
                onumber=str(number)
                number=str(number).zfill(4)              
                #await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
                #rr2=discord.utils.get(server.roles, id=self.RaidObserver)
                #await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
                
                line=(("RAID {}    {}     {}    {}    {}   {}   {}""".format(number.ljust(4),statmess,type.ljust(8),str(timeleft).ljust(5),newloca[0:8].ljust(8),tpolltimez,message.author.display_name)))
                with open("raids_ALL.txt","a") as f:
                    print(line,file=f)
                
                
                #break        
            else:
                isallowed=1
                #Reiterate the information
                number = sum(1 for line in open('raids.txt'))+1
                onumber=str(number)
                number=str(number).zfill(4)              
                await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
                rr2=discord.utils.get(server.roles, id=self.RaidObserver)
                await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
                
                line=(("{}    {}     {}    {}    {}   {}   {}""".format(number.ljust(4),statmess,type.ljust(8),str(timeleft).ljust(5),newloca[0:8].ljust(8),str_time,message.author.display_name)))
                with open("raids.txt","a") as f:
                    print(line,file=f)
                polltime = datetime.utcnow()+timedelta(hours=self.timez)
                if status=="1":
                    polltime += timedelta(minutes=45)
                argg=timeleft
                polltime += timedelta(minutes=int(argg))
                tpolltime=polltime.strftime('%H:%M:%S')
                
                tdeltat = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime("0:0:0", '%H:%M:%S')
                hours, remainder = divmod(tdeltat.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                
                polltime += timedelta(seconds=int(60-seconds))
                polltime += timedelta(minutes=1)
                polltime += timedelta(hours=-1)
                polltime += timedelta(minutes=15)
                tpoll = polltime.strftime('%H:%M:'+"00")
                for x in range(0,5):
                    polltime += timedelta(minutes=10)
                    tpoll = polltime.strftime('%H:%M:%S')
                polltime += timedelta(minutes=-50)
                tpoll = polltime.strftime('%H:%M:%S')
                polltimez = datetime.utcnow()+timedelta(hours=self.timez)
                tpolltimez=polltimez.strftime('%m/%d/%y %H:%M:%S')
                number = sum(1 for line in open('raids_ALL.txt'))+1
                onumber=str(number)
                number=str(number).zfill(4)              
                #await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
                #rr2=discord.utils.get(server.roles, id=self.RaidObserver)
                #await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
                
                line=(("RAID {}    {}     {}    {}    {}   {}   {}""".format(number.ljust(4),statmess,type.ljust(8),str(timeleft).ljust(5),newloca[0:8].ljust(8),tpolltimez,message.author.display_name)))
                with open("raids_ALL.txt","a") as f:
                    print(line,file=f)#break             
            #if isallowed==0:
            uname=message.author.display_name
            uname=uname+str(message.author.discriminator)
            userid=message.author.id
            uname=await subf.getusernick2(self,message,userid)
            #ap=10
            #if ap==10:
            try: #If the sheet exists, open it 
                df = pd.read_excel('RaidTrainer' + "\\" + uname + 'rt.xlsx')
                df.iloc[0,0]+=1    
                writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                #print('Here99',df.iat[0,0],df.iat[0,0])
                if df.iloc[0,0]>1 and df.iloc[0,1]>=1:
                    notta=1
                    rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                    if not rrL in b.roles:
                        fr=await subf.grantRT(self,b,rrL)
                elif df.iloc[0,0]==1 and df.iloc[0,1]==1:
                    rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                    fr=await subf.grantRT(self,b,rrL)
                    if fr==1:
                        apt=1
                        #await self.bot.send_message(message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                    else:
                        apt=1
                        #await self.bot.send_message(message.author,uname+", please pester an RO to give you access NOW!  We need your help!") 
                else:
                    apt=1
                    #await self.bot.send_message(message.author,"It looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer and won't get this annoying message. If you have already met this requirement, pester a RaidObserver to give you access.")
            #else:
            except: #The person hasn't established a level yet
                df = pd.read_excel('RaidTrainer' + "\\" + 'rt' + '.xlsx')
                df.iloc[0,0]+=1    
                writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                if df.iat[0,0]==1 and df.iat[0,1]==1:
                    rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                    fr=await subf.grantRT(self,b,rrL)
                    if fr==1:
                        apt=1
                        #await self.bot.send_message(message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                    else:
                        apt=1
                        #await self.bot.send_message(message.author,uname+", please pester an RO to give you access NOW!  We need your help!") 
                else:
                    #print('Here2')
                    apt=1
                    #await self.bot.send_message(message.author,"It looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer and won't get this annoying message. If you have already met this requirement, pester a RaidObserver to give you access.")   
            return
        else:
            arpr=1
        #except:
        #    arpr=10
    
    
    async def approvehelper(self,member,chan2):
        #if member.id=="237757849671827456":
        arss=1#update
        if arss==1:
            #await self.bot.send_message(member,"Hi, you have arrived.")
            server=self.bot.get_server(self.serverid)
            Ranger=discord.utils.get(server.members, id=member.id)
            chan = self.bot.get_channel("284729030983417859") #get approved channel
            chanr = self.bot.get_channel(self.programid) #get approved channel
            Ranger=discord.utils.get(server.roles, id=self.Ranger)
            Trainer=discord.utils.get(server.roles, id="284583203245916160")
            inschan = self.bot.get_channel("284555806320623618")
            myschan = self.bot.get_channel("284555776830472194")
            valchan = self.bot.get_channel("284555742395105280")
            #chan2 = ctx.message.channel #self.bot.get_channel(member.id)
            Valor=discord.utils.get(server.roles, id=self.valor)
            Mystic=discord.utils.get(server.roles, id=self.mystic)
            Instinct=discord.utils.get(server.roles, id=self.instinct)
            print(member.id)
            print(member.name)
            print(member.nick)
            #user=discord.utils.get(message.server.members, name=member.)
            success=0
            print(chan2)
            #return
            sto=3600*24
            await self.bot.send_message(member,"Welcome to the Purdue Pokemon Go Discord Server and welcome to the world of Pokémon! My name is Purdue Pollster! People call me the blind bird! This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Other use them for fights. Myself… I am one. \nAnyway, I am here to help your joining process, so without further ado, let's get started:\n__**What is your trainer name in Pokemon Go? Please enter it exactly as it is shown in the game!**__")
            while success==0:
                
                print(member)
                nmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                username=nmess.content
                success2=0
                await self.bot.send_message(member,"You told me your Pokemon Go Trainer name is " + username + ".  \nDid I get that correct? (Y/N) ")
                #success=1
                while success2==0:
                    mess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                    if mess.content.upper()=="Y":
                        success2=1#update
                        success=1
                    elif mess.content.upper()=="N":
                        success2=1
                        await self.bot.send_message(member,"__**What is your trainer name in Pokemon Go? Please enter it exactly as it is shown in the game!**__")
                    elif mess.content.upper()=="END":
                        return
                    else:
                        await self.bot.send_message(member,"Please answer Y or N.")
                        
            #Now change the nickname
            await self.bot.change_nickname(member, username)    
            
            success=0
            teamname=""
            await self.bot.send_message(member,"What is your team name?:\n1) Instinct (Yellow)\n2) Mystic   (Blue)\n3) Valor    (Red)")
            while success==0:
                
                nmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                if nmess.content.upper()=="1" or nmess.content.upper()=="INSTINCT" or nmess.content.upper()=="YELLOW":
                    #teamass=Instinct
                    teamname="Instinct"
                    role=Instinct
                    #success=1
                elif nmess.content.upper()=="2" or nmess.content.upper()=="MYSTIC" or nmess.content.upper()=="BLUE":
                    #teamass=self.mystic
                    teamname="Mystic"
                    role=Mystic
                    #success=1
                elif nmess.content.upper()=="3" or nmess.content.upper()=="VALOR" or nmess.content.upper()=="RED":
                    #teamass=self.valor
                    teamname="Valor"
                    role=Valor
                    #success=1
                elif nmess.content.upper()=="end":
                    return
                else:
                    await self.bot.send_message(member,"I didn't get that.\n__**What is your team name?:**__)\n1) Instinct (Yellow)\n2) Mystic   (Blue)\n3) Valor    (Red)")
                if not teamname=="":
                    success2=0
                    await self.bot.send_message(member,username + ", it looks like you are team " + teamname + ". Right? (Y/N)")
                    #success=1
                    while success2==0:
                        mess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                        if mess.content.upper()=="Y":
                            success2=1#update
                            success=1
                        elif mess.content.upper()=="N":
                            success2=1
                            await self.bot.send_message(member,"What is your team name?:\n1) Instinct (Yellow)\n2) Mystic   (Blue)\n3) Valor    (Red)")
                        elif mess.content.upper()=="END":
                            return
                        else:
                            await self.bot.send_message(member,"Please answer Y or N.")
            #add the team role to lock down the trainer name    
            await self.bot.add_roles(member,role) 
            await asyncio.sleep(0.75)
            await self.bot.remove_roles(member,Trainer) 
            await asyncio.sleep(0.75)            
            
            
            success=0
            #teamname=""
            #await self.bot.send_message(member,"Now, please follow me into the discord to review the rules.")
            #await subf.gethell(self,member)
            
            rulesch = self.bot.get_channel("351617228157878272")
            msgid1 = self.bot.get_message(rulesch,"387389760068386821")
            msgid2 = self.bot.get_message(rulesch,"387389972094648341")
            #ARPr=await self.bot.send_message(rulesch,member.mention + " review this and react to the rules with any emoji to continue!")
            
            
            #tmess1 = await self.bot.wait_for_reaction(emoji=None, user=member, timeout=None, message=msgid1, check=None)
            #tmess2 = await self.bot.wait_for_reaction(emoji=None, user=member, timeout=None, message=msgid2, check=None)
            #await self.bot.delete_message(ARPr)
            
            #Now for the approval side
            success=0
            #teamname=""
            await self.bot.send_message(member,"At this time, upload a screen capture of the screen with your trainer name and buddy to finalize the approval process.")
            while success==0:
                try:
                    tmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member) #print (tmess.attachments[0]['filename'])
                    if tmess.attachments[0]['size']:
                        success2=0
                        await self.bot.send_message(member,username + ", are you sure you want to upload this image? (Y/N)")
                        success=1
                        while success2==0:
                            mess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                            if mess.content.upper()=="Y":
                                success2=1#update
                                success=1
                            elif mess.content.upper()=="N":
                                success2=1
                                await self.bot.send_message(member,"At this time, upload a screen capture of the screen with your trainer name and buddy to finalize the approval process.")
                            elif mess.content.upper()=="END":
                                return
                            else:
                                await self.bot.send_message(member,"Please answer Y or N.")

                except:
                    await self.bot.send_message(member,"That didn't look like an image to me.  Try again.")
                #nmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
            
            if teamname=="Instinct":
                await self.bot.send_message(inschan,member.mention+" has joined Team Instinct! Welcome!")
            if teamname=="Mystic":
                await self.bot.send_message(myschan,member.mention+" has joined Team Mystic! Welcome!")
            if teamname=="Valor":
                await self.bot.send_message(valchan,member.mention+" has joined Team Valor! Welcome!")
                
            print("Passing image to Rangers.")
            await self.bot.send_message(chan,"Rangers" + ", a user named " + username + " has joined team " + teamname + ".\nPlease verify that their user name and team are correct and `!approve` " + member.mention + " to approve the user.")
            await self.bot.send_message(chan,tmess.attachments[0]['url'])
            await self.bot.send_message(member,"Once you have been approved, come back here and type `%guide` to get some the tools used on this server configured for you.  Welcome!")#chan
            #await self.bot.send_message(chan,"I am about to take over the world.  \nJust kidding!  Stinkpot is trying something here.")
    
    async def readbosses(self): 
        stuff = dataIO.load_json("configuration/crapola.json")
        usethis=1
        if usethis==1:
            self.L4types=stuff["L4types"]
            self.L4notid=stuff["L4notid"]
            self.L4maxCP=[ int(x) for x in stuff["L4maxCP"]]
            self.L4offset=[ int(x) for x in stuff["L4offset"]]
            self.L4slope=[ int(x) for x in stuff["L4slope"]]
            self.L4peeps=[ int(x) for x in stuff["L4peeps"]]
            self.L4emoji=stuff["L4emoji"]
            
            self.PStypes=stuff["PStypes"]
            self.PSnotid=stuff["PSnotid"]
            self.PSmaxCP=[ int(x) for x in stuff["PSmaxCP"]]
            self.PSoffset=[ int(x) for x in stuff["PSoffset"]]
            self.PSslope=[ int(x) for x in stuff["PSslope"]]
            self.PSpeeps=[ int(x) for x in stuff["PSpeeps"]]
            self.PSemoji=stuff["PSemoji"]
            
            self.L5types=stuff["L5types"]
            self.L5notid=stuff["L5notid"]
            self.L5maxCP=[ int(x) for x in stuff["L5maxCP"]]
            self.L5offset=[ int(x) for x in stuff["L5offset"]]
            self.L5slope=[ int(x) for x in stuff["L5slope"]]
            self.L5peeps=[ int(x) for x in stuff["L5peeps"]]
            self.L5emoji=stuff["L5emoji"]
            
            self.L3types=stuff["L3types"]
            self.L3notid=stuff["L3notid"]
            self.L3maxCP=[ int(x) for x in stuff["L3maxCP"]]
            self.L3offset=[ int(x) for x in stuff["L3offset"]]
            self.L3slope=[ int(x) for x in stuff["L3slope"]]
            self.L3peeps=[ int(x) for x in stuff["L3peeps"]]
            self.L3emoji=stuff["L3emoji"]
            
            print(self.L3emoji)
            print(self.L5offset)
        return self    
        #print([ int(x) for x in stuff["L4maxCP"]])
    
    async def addnewgym(self,name,region,latitude,longitude,exgym):
        #allow persistent changes to the gym file
        file = open("configuration/NewRaidLocas.json","w",encoding='utf-8') 
        #txt="Hello World!"
        txt='{\n    ';
        txt+='"group1an":['
        for x in self.group1an:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group1cn":['
        for x in self.group1cn:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group1sn":['
        for x in self.group1sn:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group1ex":['
        for x in self.group1ex:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group1lat":['
        for x in self.group1lat:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group1lon":['
        for x in self.group1lon:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        
        txt+='"group2an":['
        for x in self.group2an:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group2cn":['
        for x in self.group2cn:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group2sn":['
        for x in self.group2sn:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group2ex":['
        for x in self.group2ex:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group2lat":['
        for x in self.group2lat:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group2lon":['
        for x in self.group2lon:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        
        txt+='"group3an":['
        for x in self.group3an:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group3cn":['
        for x in self.group3cn:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group3sn":['
        for x in self.group3sn:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group3ex":['
        for x in self.group3ex:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group3lat":['
        for x in self.group3lat:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"group3lon":['
        for x in self.group3lon:
            txt+='"'+x+'",'
        txt=txt[:-1]+"]\n}"
        file.write(txt)          
        file.close()
    
    async def addnewstop(self,name,latitude,longitude):
        #allow persistent changes to the gym file
        file = open("configuration/Stopsfile.json","w",encoding='utf-8') 
        #txt="Hello World!"
        txt='{\n    ';
        txt+='"names":['
        for x in self.stopnam:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"Lat":['
        for x in self.stoplat:
            txt+='"'+x+'",'
        txt=txt[:-1]+"],\n"
        txt+='"Lon":['
        for x in self.stoplon:
            txt+='"'+x+'",'
        txt=txt[:-1]+"]\n}"
        file.write(txt)          
        file.close()
    
    async def writebossfile(self,ctx,fname):
        #Do this for L4types first
        txt='{\n'
        txt+='"L4types":["'
        cntt=0
        for f in self.L4types:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4notid":["'
        cntt=0
        for f in self.L4notid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4maxCP":["'
        cntt=0
        for f in self.L4maxCP:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4offset":["'
        cntt=0
        for f in self.L4offset:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4slope":["'
        cntt=0
        for f in self.L4slope:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4peeps":["'
        cntt=0
        for f in self.L4peeps:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4emoji":["'
        cntt=0
        for f in self.L4emoji:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        
        #Now level3 - append
        txt+='"L3types":["'
        cntt=0
        for f in self.L3types:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3notid":["'
        cntt=0
        for f in self.L3notid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3maxCP":["'
        cntt=0
        for f in self.L3maxCP:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3offset":["'
        cntt=0
        for f in self.L3offset:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3slope":["'
        cntt=0
        for f in self.L3slope:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3peeps":["'
        cntt=0
        for f in self.L3peeps:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3emoji":["'
        cntt=0
        for f in self.L3emoji:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        
        #Now PS - append
        txt+='"PStypes":["'
        cntt=0
        for f in self.PStypes:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSnotid":["'
        cntt=0
        for f in self.PSnotid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSmaxCP":["'
        cntt=0
        for f in self.PSmaxCP:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSoffset":["'
        cntt=0
        for f in self.PSoffset:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSslope":["'
        cntt=0
        for f in self.PSslope:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSpeeps":["'
        cntt=0
        for f in self.PSpeeps:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSemoji":["'
        cntt=0
        for f in self.PSemoji:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        
        #Now level5 - append
        txt+='"L5types":["'
        cntt=0
        for f in self.L5types:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5notid":["'
        cntt=0
        for f in self.L5notid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5maxCP":["'
        cntt=0
        for f in self.L5maxCP:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5offset":["'
        cntt=0
        for f in self.L5offset:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5slope":["'
        cntt=0
        for f in self.L5slope:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5peeps":["'
        cntt=0
        for f in self.L5peeps:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5emoji":["'
        cntt=0
        for f in self.L5emoji:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+=']\n}'
        print (txt)
        #txt.replace('\\', "\\\\")
        print("configuration/"+fname)
        file = open("configuration/"+fname,"w",encoding='utf-8') 
        file.write(txt)          
        file.close() 
    
    async def timemute(self,ctx,mutelist):
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        polltime = datetime.utcnow()+timedelta(hours=self.timez)
        tpolltime=polltime.strftime('%H:%M:%S')
        
        for filename in os.listdir('ExcludeTime\\'):
            Disname=filename[0:len(filename)-8]
            #print(filename)
            cntt=0
            t=[]
            with open('ExcludeTime\\'+filename) as fr:
                for line in fr:
                    t.append(line)
            #print(t[0]+" "+t[1])    
            tdeltat1 = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime(t[0], '%H:%M\n')
            tdeltat2 = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime(t[1], '%H:%M\n')
            print (str(tdeltat1.days) +" "+str(tdeltat2.days))
            if not (str(tdeltat1.days)=="0" and str(tdeltat2.days)=="-1"):
                b=discord.Server.get_member(server,Disname)
                mutelist.append(b)
        #print(mutelist)
        return mutelist
    
    async def timemute(self,message,mutelist):
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        polltime = datetime.utcnow()+timedelta(hours=self.timez)
        tpolltime=polltime.strftime('%H:%M:%S')
        
        for filename in os.listdir('ExcludeTime\\'):
            Disname=filename[0:len(filename)-8]
            #print(filename)
            cntt=0
            t=[]
            with open('ExcludeTime\\'+filename) as fr:
                for line in fr:
                    t.append(line)
            #print(t[0]+" "+t[1])    
            tdeltat1 = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime(t[0], '%H:%M\n')
            tdeltat2 = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime(t[1], '%H:%M\n')
            print (str(tdeltat1.days) +" "+str(tdeltat2.days))
            if not (str(tdeltat1.days)=="0" and str(tdeltat2.days)=="-1"):
                b=discord.Server.get_member(server,Disname)
                mutelist.append(b)
        #print(mutelist)
        return mutelist
        
    async def getmemlist(self,ctx,roleid): 
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        role = discord.utils.get(server.roles, id=roleid)
        memlist=[]
        for f in server.members:
            if not f==None:
                if any(xpp == role for xpp in f.roles): #Member is on mute list
                    memlist.append(f)
        return memlist
    
    async def getmemlist2(self,message,roleid): 
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        role = discord.utils.get(server.roles, id=roleid)
        memlist=[]
        for f in server.members:
            if not f==None:
                if any(xpp == role for xpp in f.roles): #Member is on mute list
                    memlist.append(f)
        return memlist
    
    async def getusernick(self,ctx,userid): 
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        member = discord.utils.get(server.members, id=userid)
        print (member.display_name + member.discriminator)
        return (member.display_name + member.discriminator)
    
    async def getusernick2(self,message,userid): 
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        member = discord.utils.get(server.members, id=userid)
        print (member.display_name + member.discriminator)
        return (member.display_name + member.discriminator)
    
    #@commands.command(pass_context=False)
    async def cll(self):
        await self.bot.send_message(self.bot.get_channel(self.programid),"Good")
    
    async def setlevel(self,ctx,level,user):
        uname=user.display_name
        uname=uname+str(user.discriminator)
        print("____")
        print(level)
        print(uname)
        print(ctx)
        print("____")
        try:
            newlev=float(level)
            newlev=int(newlev)
            posid=min(40,max(newlev,1))
            #open the sheet and see if the person exists
            try: #If the sheet exists, open it 
                df = pd.read_excel('ExcelFiles' + "\\" + uname + 'level.xlsx')
                currlev=df.iloc[0,0]
                df.loc[0]=posid    
                writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                await self.bot.send_message(user,user.display_name +", your level has been changed from " + str(currlev) + " to " + str(posid))
            except: #The person hasn't established a level yet
                df = pd.read_excel('ExcelFiles' + "\\" + 'level' + '.xlsx')
                df.loc[0]=posid    
                writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                await self.bot.send_message(user,user.display_name +", your new assigned level is " + str(posid))
        except:
            await self.bot.send_message(user,user.display_name +", please stop being an idiot and enter a number already!")

    async def shinywrite(self):
        txt='{\n'
        txt+='"shinylist":["'
        cntt=0
        for f in self.shinylist:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/shinies.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close() 
    
    async def L4bosswrite(self):
        txt='{\n'
        txt+='"L4types":["'
        cntt=0
        for f in self.L4types:
            #f2=
            if not cntt==0:
                txt+=',"'
                
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4notid":["'
        cntt=0
        for f in self.L4notid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L4maxCP":['
        cntt=0
        for f in self.L4maxCP:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L4offset":['
        cntt=0
        for f in self.L4offset:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L4slope":['
        cntt=0
        for f in self.L4slope:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L4peeps":['
        cntt=0
        for f in self.L4peeps:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L4emoji":["'
        cntt=0
        for f in self.L4emoji:
            if not cntt==0:
                txt+=',"'
            if cntt==0:
                f='NUMBER4'
            txt+=f + '"'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/L4bosses.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()
    
    async def L5bosswrite(self):
        txt='{\n'
        txt+='"L5types":["'
        cntt=0
        for f in self.L5types:
            #f2=
            if not cntt==0:
                txt+=',"'
                
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5notid":["'
        cntt=0
        for f in self.L5notid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L5maxCP":['
        cntt=0
        for f in self.L5maxCP:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L5offset":['
        cntt=0
        for f in self.L5offset:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L5slope":['
        cntt=0
        for f in self.L5slope:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L5peeps":['
        cntt=0
        for f in self.L5peeps:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L5emoji":["'
        cntt=0
        for f in self.L5emoji:
            if not cntt==0:
                txt+=',"'
            if cntt==0:
                f='NUMBER5'
            txt+=f + '"'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/L5bosses.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()
    
    async def L3bosswrite(self):
        txt='{\n'
        txt+='"L3types":["'
        cntt=0
        for f in self.L3types:
            #f2=
            if not cntt==0:
                txt+=',"'
                
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3notid":["'
        cntt=0
        for f in self.L3notid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3maxCP":['
        cntt=0
        for f in self.L3maxCP:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3offset":['
        cntt=0
        for f in self.L3offset:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3slope":['
        cntt=0
        for f in self.L3slope:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3peeps":['
        cntt=0
        for f in self.L3peeps:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3emoji":["'
        cntt=0
        for f in self.L3emoji:
            if not cntt==0:
                txt+=',"'
            if cntt==0:
                f='NUMBER3'
            txt+=f + '"'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/L3bosses.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()
    
    async def PSbosswrite(self):
        txt='{\n'
        txt+='"PStypes":["'
        cntt=0
        for f in self.PStypes:
            #f2=
            if not cntt==0:
                txt+=',"'
                
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSnotid":["'
        cntt=0
        for f in self.PSnotid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"PSmaxCP":['
        cntt=0
        for f in self.PSmaxCP:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"PSoffset":['
        cntt=0
        for f in self.PSoffset:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"PSslope":['
        cntt=0
        for f in self.PSslope:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"PSpeeps":['
        cntt=0
        for f in self.PSpeeps:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"PSemoji":["'
        cntt=0
        for f in self.PSemoji:
            if not cntt==0:
                txt+=',"'
            if cntt==0:
                f="<a:Shiny:407702531645505537>"
            txt+=f + '"'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/PSbosses.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()
    
    async def OIbosswrite(self):
        txt='{\n'
        txt+='"OItypes":["'
        cntt=0
        for f in self.OItypes:
            #f2=
            if not cntt==0:
                txt+=',"'
                
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"OInotid":["'
        cntt=0
        for f in self.OInotid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"OImaxCP":['
        cntt=0
        for f in self.OImaxCP:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"OIoffset":['
        cntt=0
        for f in self.OIoffset:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"OIslope":['
        cntt=0
        for f in self.OIslope:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"OIpeeps":['
        cntt=0
        for f in self.OIpeeps:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"OIemoji":["'
        cntt=0
        for f in self.OIemoji:
            if not cntt==0:
                txt+=',"'
            if cntt==0:
                f="<a:Shiny:407702531645505537>"
            txt+=f + '"'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/OIbosses.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()
    
    async def exraidwrite(self):
        txt='{\n'
        for f in range(0,12):
            txt+='"mtch' +  str(f+1) + 'id":['
            print(("self.mtch" + str(f+1) + "id"))
            exec("self.junk=self.mtch" + str(f+1) + "id")
            print(self.junk)
            if len(self.junk)>0:
                for g in self.junk:
                    txt+='"' + g + '",'
                txt=txt[:-1]
            else:
                txt+='""'
            txt+='],\n'
            #try:
                #print(a)
                #for g in a:
                        #txt+=g
            #except:
            #if a==None:
            #    txt+="none"
            #else:
                
            #txt+=self.exec("mtch" + str(f+1) + "id")
        txt=txt[:-2]
        txt+='\n}'
        file = open("configuration/exraid.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close() 
        
        return
        txt+='"L3types":["'
        cntt=0
        for f in self.L3types:
            #f2=
            if not cntt==0:
                txt+=',"'
                
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3notid":["'
        cntt=0
        for f in self.L3notid:
            if not cntt==0:
                txt+=',"'
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"L3maxCP":['
        cntt=0
        for f in self.L3maxCP:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3offset":['
        cntt=0
        for f in self.L3offset:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3slope":['
        cntt=0
        for f in self.L3slope:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3peeps":['
        cntt=0
        for f in self.L3peeps:
            if not cntt==0:
                txt+=','
            txt+=str(f) + ''
            cntt+=1
        txt+='],\n'
        txt+='"L3emoji":["'
        cntt=0
        for f in self.L3emoji:
            if not cntt==0:
                txt+=',"'
            if cntt==0:
                f='NUMBER3'
            txt+=f + '"'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/L3bosses.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()
    
    async def questwrite(self):
        txt='{\n'
        txt+='"tasklist":["'
        cntt=0
        for f in self.tasklist:
            #f2=
            if not cntt==0:
                txt+=',"'
                
            txt+=str(f) + '"'
            cntt+=1
        txt+='],\n'
        txt+='"rewardlist":[["'
        cntt=0
        for f in self.rewardlist:
            if not cntt==0:
                txt+=',["'
            txt+=str(f[0]) + '"]'
            cntt+=1
        txt+=']\n}'
        file = open("configuration/questlist.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()
    
    #This is the helper function for users to update their trainer level
    #Ready for publicattion
    async def levelhelper(self,message,level):
        chv=self.bot.get_channel(self.setupch) #Grab the setup channel
        try:
            allow=0
            newlev=float(level)
            newlev=int(newlev)
            if newlev==40:  #If the user's level is 40, let them show off a bit and allow in any channel
                allow=1
            if message.channel.id in self.allraidch: #Allow level changes in raid channels
                allow=1
            if message.channel.id==self.programid or message.channel.id==self.setupch:
                allow=1
            if allow==0:
                await self.bot.delete_message(message)
                await self.bot.send_message(chv,message.author.mention +", in the future, enter that command over here or in a raid channel!")
                #return
            uname=message.author.display_name
            uname=uname+str(message.author.discriminator)
            try:
                newlev=float(level)
                newlev=int(newlev)
                posid=min(40,max(newlev,1))
                if (message.author.display_name=="MrMasterMiltank"):  #I am a special case ;)
                    posid=min(1000,max(newlev,1))
                #open the sheet and see if the person exists
                try: #If the sheet exists, open it 
                    df = pd.read_excel('ExcelFiles' + "\\" + uname + 'level.xlsx')
                    currlev=df.iloc[0,0]
                    df.loc[0]=posid    
                    writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    if allow==1:
                        await self.bot.send_message(message.channel,message.author.display_name +", your level has been changed from " + str(currlev) + " to " + str(posid))
                    else:
                        await self.bot.send_message(message.author,message.author.display_name +", your level has been changed from " + str(currlev) + " to " + str(posid))
                except: #The person hasn't established a level yet
                    df = pd.read_excel('ExcelFiles' + "\\" + 'level' + '.xlsx')
                    df.loc[0]=posid    
                    writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    if allow==1:
                        await self.bot.send_message(message.channel,message.author.display_name +", your new assigned level is " + str(posid))
                    else: 
                        await self.bot.send_message(message.author,message.author.display_name +", your new assigned level is " + str(posid))
            except:
                await self.bot.send_message(message.channel,message.author.display_name +", please stop being an idiot and enter a number already!")
        except:
            arpr=10  #Do nothing
    
    async def checklevelhelper(self,message):
        chv=self.bot.get_channel('403939414977413122')
        try:
            if not (message.channel.id==self.programid or message.channel.id=='351944459115560991' or message.channel.id=='403939414977413122'):
                await self.bot.delete_message(message)
                await self.bot.send_message(chv,message.author.mention +", enter that command over here!")
                return
            uname=message.author.display_name
            uname=uname+str(message.author.discriminator)
            try:
                try: #If the sheet exists, open it 
                    df = pd.read_excel('ExcelFiles' + "\\" + uname + 'level.xlsx')
                    currlev=df.iloc[0,0]
                    await self.bot.send_message(message.channel,message.author.display_name +", your current level is " + str(currlev))
                except: #The person hasn't established a level yet
                    await self.bot.send_message(message.channel,message.author.display_name +", you don't have an assigned level.")
            except:
                junk=1
                #await self.bot.send_message(message.channel,message.author.display_name +", please stop being an idiot and enter a number already!")
        except:
            arpr=10
    async def leaderbhelper(self,ctx):
        #if not ctx.message.channel.id==self.RaidNotifier or ctx.message.channel.id=="403550523984183296":
        #    return
        
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        totraid=0
        totupda=0
        Milkmaid=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
        RO=discord.utils.get(ctx.message.server.roles, id=self.RaidObserver)
        if not (ctx.message.author.id=="345200594421547018" or ctx.message.author.id=="286714847989858305"):
        #if not Milkmaid in f:
            await self.bot.send_message(ctx.message.channel,"You're not the MilkMaid.  This command uses a lot of resources.")
            return
        Leaderlist=[]
        for filename in os.listdir('RaidTrainer\\'):
            if not filename=='rt.xlsx': #a blank file
                Disname=filename[0:len(filename)-11]
                #print(Disname)
                #if not filename=="thesperation2637rt.xlsx" or filename=="vtatebe5116rt.xlsx" or filename=="StinkpotMcGoo0265rt.xlsx":
                df = pd.read_excel('RaidTrainer' + "\\" + filename)
                #df.iloc[0,0] 
                Leaderlist.append((df.iloc[0,0]+df.iloc[0,1],Disname))
                totraid+=df.iloc[0,0]
                totupda+=df.iloc[0,1]
        Leaderlist.sort(reverse=True)
        Leaderlist2=[]
        for filename in os.listdir('Archive_RT\\RaidTrainer_04222018\\'):
            if not filename=='rt.xlsx': #a blank file
                Disname=filename[0:len(filename)-11]
                #print(Disname)
                #if not filename=="thesperation2637rt.xlsx" or filename=="vtatebe5116rt.xlsx" or filename=="StinkpotMcGoo0265rt.xlsx":
                df = pd.read_excel('Archive_RT' + "\\RaidTrainer_04222018\\" + filename)
                #df.iloc[0,0] 
                Leaderlist2.append((df.iloc[0,0]+df.iloc[0,1],Disname))  #Previous entry
        Leaderlist2.sort(reverse=True)
        Fleader=[]
        print(Leaderlist)
        print(Leaderlist2)
       
        for x in Leaderlist:
            namefound=0
            for y in Leaderlist2:
                if x[1]==y[1]: #Name is found
                    Fleader.append((x[0]-y[0],x[1]))
                    namefound=1
                    break
            if namefound==0: #new data enterer since last week
                Fleader.append((x[0],x[1]))
        Fleader.sort(reverse=True)
        print (Fleader)
        cntt=1
        
        self.threeleaders=[]    
        Leaderlist=Fleader
        for ldx in Leaderlist:
            if cntt<=3:
                #self.threeleaders.append(ldx[1])
                cntt+=1
        print(self.threeleaders)
        #return
        
        msgg="              __**WEEKLY RAID ENTRY LEADERBOARD**__\n"
        #msgg+="Previous maximum raid entry was ALOT by thesperation for week ending 04/01/2018\n"
        msgg+="       Discord Username             Raid/Update Entry Count\n`"
        for ldx in Leaderlist:
            #print (ldx)
            if ldx[0]>0:
                msgg+=str(ldx[1]).ljust(30) + str(ldx[0]).ljust(21) +  "\n"
                if len(msgg)>1500:
                    msgg+="`"
                    await self.bot.send_message(ctx.message.channel,msgg)
                    msgg="`"
            
        msgg+="`"
        await self.bot.send_message(ctx.message.channel,msgg)
        await self.bot.delete_message(ctx.message) 
        #print (Leaderlist)        
        #writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')  
    
    async def getemo(argument):
        switcher = {
            '0': '\U00000030\U000020e3',
            '1': '\U00000031\U000020e3',
            '2': '\U00000032\U000020e3',
            '3': '\U00000033\U000020e3',
            '4': '\U00000034\U000020e3',
            '5': '\U00000035\U000020e3',
            '6': '\U00000036\U000020e3',
            '7': '\U00000037\U000020e3',
            '8': '\U00000038\U000020e3',
            '9': '\U00000039\U000020e3',
            'A': '\U0001F1E6',
            'B': '\U0001F1E7',
            'C': '\U0001F1E8',
            'D': '\U0001F1E9',
            'E': '\U0001F1EA',
            'F': '\U0001F1EB',
            'G': '\U0001F1EC',
            'H': '\U0001F1ED',
            'I': '\U0001F1EE',
            'J': '\U0001F1EF',
            'K': '\U0001F1F0',
            'L': '\U0001F1F1',
            'M': '\U0001F1F2',
            'N': '\U0001F1F3',
            'O': '\U0001F1F4',
            'P': '\U0001F1F5',
            'Q': '\U0001F1F6',
            'R': '\U0001F1F7',
            'S': '\U0001F1F8',
            'T': '\U0001F1F9',
            'U': '\U0001F1FA',
            'V': '\U0001F1FB',
            'W': '\U0001F1FC',
            'X': '\U0001F1FD',
            'Y': '\U0001F1FE',
            'Z': '\U0001F1FF',
        }
        return switcher.get(argument, "nothing")
        
    
    async def leaderbover(self,ctx):
        #if not ctx.message.channel.id==self.RaidNotifier or ctx.message.channel.id=="403550523984183296":
        #    return
        
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        totraid=0
        totupda=0
        Milkmaid=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
        RO=discord.utils.get(ctx.message.server.roles, id=self.RaidObserver)
        if not (ctx.message.author.id=="345200594421547018" or ctx.message.author.id=="286714847989858305"):
        #if not Milkmaid in f:
            await self.bot.send_message(ctx.message.channel,"You're not the MilkMaid.  This command uses a lot of resources.")
            return
        Leaderlist=[]
        for filename in os.listdir('RaidTrainer\\'):
            if not filename=='rt.xlsx': #a blank file
                Disname=filename[0:len(filename)-11]
                #print(Disname)
                #if not filename=="thesperation2637rt.xlsx" or filename=="vtatebe5116rt.xlsx" or filename=="StinkpotMcGoo0265rt.xlsx":
                df = pd.read_excel('RaidTrainer' + "\\" + filename)
                #df.iloc[0,0] 
                Leaderlist.append((df.iloc[0,0]+df.iloc[0,1],Disname))
                totraid+=df.iloc[0,0]
                totupda+=df.iloc[0,1]
        msgg="A total of " + str(totraid) + " raids have been entered since adoption of the RM system.\n"
        msgg+="A total of " + str(totupda) + " updates have been entered since adoption of the RM system.\n"
        await self.bot.send_message(ctx.message.channel,msgg)
        return
        
        
        Leaderlist.sort(reverse=True)
        Leaderlist2=[]
        for filename in os.listdir('Archive_RT\\RaidTrainer_03232018\\'):
            if not filename=='rt.xlsx': #a blank file
                Disname=filename[0:len(filename)-11]
                #print(Disname)
                #if not filename=="thesperation2637rt.xlsx" or filename=="vtatebe5116rt.xlsx" or filename=="StinkpotMcGoo0265rt.xlsx":
                df = pd.read_excel('Archive_RT' + "\\RaidTrainer_03232018\\" + filename)
                #df.iloc[0,0] 
                Leaderlist2.append((df.iloc[0,0]+df.iloc[0,1],Disname))  #Previous entry
        Leaderlist2.sort(reverse=True)
        Fleader=[]
        print(Leaderlist)
        print(Leaderlist2)
       
        for x in Leaderlist:
            namefound=0
            for y in Leaderlist2:
                if x[1]==y[1]: #Name is found
                    Fleader.append((x[0]-y[0],x[1]))
                    namefound=1
                    break
            if namefound==0: #new data enterer since last week
                Fleader.append((x[0],x[1]))
        Fleader.sort(reverse=True)
        print (Fleader)
        cntt=1
        
        self.threeleaders=[]    
        Leaderlist=Fleader
        for ldx in Leaderlist:
            if cntt<=3:
                #self.threeleaders.append(ldx[1])
                cntt+=1
        print(self.threeleaders)
        #return
        
        msgg="              __**WEEKLY RAID ENTRY LEADERBOARD**__\n"
        msgg+="Previous maximum raid entry was 148 by thesperation for week ending 02/25/2018\n"
        msgg+="       Discord Username             Raid/Update Entry Count\n`"
        for ldx in Leaderlist:
            #print (ldx)
            if ldx[0]>0:
                msgg+=str(ldx[1]).ljust(30) + str(ldx[0]).ljust(21) +  "\n"
                if len(msgg)>1500:
                    msgg+="`"
                    await self.bot.send_message(ctx.message.channel,msgg)
                    msgg="`"
            
        msgg+="`"
        await self.bot.send_message(ctx.message.channel,msgg)
        await self.bot.delete_message(ctx.message) 
        #print (Leaderlist)        
        #writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter') 
        
    async def findboss(self,chnid):
        for x in range(0,len(self.L4groupid)):
            if self.L4groupid[x]==chnid:
                return 1
        for x in range(0,len(self.L5groupid)):
            if self.L5groupid[x]==chnid:
                return 1        
        for x in range(0,len(self.L3groupid)):
            if self.L3groupid[x]==chnid:
                return 1 
        return 0
    
    async def findchidloca(self,locaname):  #Optimized
        for x in self.alllocch:
            ch=self.bot.get_channel(x)
            if locaname in ch.name:
                return x
        return 0    
    
    async def findchidloca2(self,locaname):  #Optimized, #Get the location from a channel name
        for x in self.cngroup:
            if x.upper() == locaname.upper():
                return 1
        return 0  
    
    async def findchidboss(self,locaname):
        for x in self.L5groupid:
            ch=self.bot.get_channel(x)
            if locaname in ch.name:
                return x
        for x in self.L4groupid:
            ch=self.bot.get_channel(x)
            if locaname in ch.name:
                return x        
        for x in self.L3groupid:
            ch=self.bot.get_channel(x)
            if locaname in ch.name:
                return x 
        for x in self.PSgroupid:
            ch=self.bot.get_channel(x)
            if locaname in ch.name:
                return x
        return 0
    
    async def getcpmax(self,type):
        CPmax=0
        for x in range(0,len(self.L4types)):
            if type.upper()==self.L4types[x].upper():
                return self.L4maxCP[x]
        for x in range(0,len(self.L5types)):
            if type.upper()==self.L5types[x].upper():
                return self.L5maxCP[x]
        for x in range(0,len(self.L3types)):
            if type.upper()==self.L3types[x].upper():
                return self.L3maxCP[x]
        for x in range(0,len(self.PStypes)):
            if type.upper()==self.PStypes[x].upper():
                return self.PSmaxCP[x]   
        for x in range(0,len(self.OItypes)):
            if type.upper()==self.OItypes[x].upper():
                return self.OImaxCP[x]
        return 0
        
    async def filtNameval(self,Nameval):
        Nameval = Nameval.replace(' ', '-').lower()
        Nameval = Nameval.replace('+', '').lower()
        Nameval = Nameval.replace('/', '').lower()
        Nameval = Nameval.replace("'", '').lower()
        return Nameval.replace(".", '').lower()
    
    async def singlechan(self,channelid,role_everyone,ctx):
        ch=self.bot.get_channel(channelid)
        try:
            async for message in self.bot.logs_from(ch, limit=100): #Gets a list of the last 500 messages in the channel 
                #print(message.content)
                if message.content.startswith('__**RAID:**__'): #Then we need to get the ID of this message and see if it has the correct start time
                    a=message
                    arggn=a.content.split('\n')  #The second argument will be the minutes
                    argg=arggn[0].split(' ends at ')  #The second argument will be the minutes
                    #print(argg[1])
                    polltime = datetime.utcnow()+timedelta(hours=self.timez)
                    tpolltime=polltime.strftime(self.timeform)
                    tdeltat = datetime.strptime(tpolltime, self.timeform)-datetime.strptime(argg[1], self.timeform)
                    #self.bot.send_message(ctx.message.author,str(argg[1])+" "+str(tdelta))
                    #print(tdeltat.days)
                    return tdeltat.days      
        except:
            print(channelid + "failed")
            return 1
            
    async def clearset(self,setids,role_everyone):
        maxpos=0
        for x in setids:
            ch=self.bot.get_channel(x)
            overwrite = ch.overwrites_for(role_everyone)
            overwrite.read_messages = False
            #overwrite.read_message_history = False
            #overwrite.add_reactions = False
            await self.bot.edit_channel_permissions(ch, role_everyone, overwrite)
            async for message in self.bot.logs_from(ch, limit=500): #Gets a list of the last 500 messages in the channel 
                await self.bot.delete_message(message)
            await self.bot.edit_channel(ch, name='blank-' + str(maxpos))
            await self.bot.move_channel(ch, 10)
            maxpos=maxpos+1

    async def hideset(self,setids,role_everyone):
        maxpos=0
        for x in setids:
            ch=self.bot.get_channel(x)
            overwrite = ch.overwrites_for(role_everyone)
            overwrite.read_messages = False
            #overwrite.read_message_history = False
            #overwrite.add_reactions = False
            await self.bot.edit_channel_permissions(ch, role_everyone, overwrite)
            #wait self.bot.purge_from(ch, limit=100)
            #await self.bot.edit_channel(ch, name='blank-' + str(maxpos))
            maxpos=maxpos+1      
    
    async def showset(self,setids,role_everyone):
        maxpos=0
        for x in setids:
            ch=self.bot.get_channel(x)
            overwrite = ch.overwrites_for(role_everyone)
            overwrite.read_messages = True
            #overwrite.read_message_history = False
            #overwrite.add_reactions = False
            await self.bot.edit_channel_permissions(ch, role_everyone, overwrite)
            #wait self.bot.purge_from(ch, limit=100)
            #await self.bot.edit_channel(ch, name='blank-' + str(maxpos))
            maxpos=maxpos+1            
    
    async def genraidlist(self,tmess,user,reaction,bypasser):
        rxncnt=0
        for xi in range(0,len(tmess.reactions)):
            rxncnt+=1
        print(tmess.embeds[0])
        des=tmess.embeds[0]
        modtxt=des["description"]
        origtit=des["title"]
        #print(modtxt)
        arggs=modtxt.split("/")
        #reconstruct the message
        nm=""
        cnt=0
        newxs=0
        
        
        

        #try:
            
        raidrestr=discord.utils.get(tmess.server.roles, id=self.raidrestr)
        #print (user.roles)
        if bypasser==0:
            if raidrestr in user.roles:
                await self.bot.remove_reaction(reaction.message,reaction.emoji,user)
                return
        assiRM=0
        raidlevel=5 #Use this in the meantime
        #print("Here")
        

        chnid=tmess.channel.id
        #ctx=reaction
        chnam=tmess.channel.name
        #channel1=discord.utils.get(ctx.message.server.channels, id=channel_id)
        #chnam=channel1.name
        #chnid=channel1.id
        try:
            argg=chnam.split('_')
            found=await subf.findboss(self,chnid)
            
            #If the channel is a raid boss specific channel, the second channel will lead with the raid boss
            if found==1:
                raidboss=argg[1]
                location=argg[0]
                namel2=raidboss + "_" +  location
            else:
                raidboss=argg[0]
                location=argg[1]
                namel2=location + "_" +  raidboss
            
            #Get the two channels
            channel1=tmess.channel   
            channel2 = discord.utils.get(tmess.server.channels, name=namel2)
            
            if "xxxx" in  channel1.name:
                newargg=raidboss.split("xxxx")
                raidboss=newargg[1]
        except:
            raidboss="level5"
        cnttt=0
        BossmaxCP=30.0
        Bossoffset=30.0
        Bossslope=0.0
        Bosspeeps=0.0 
        for rp in self.Bosstypes:
            if rp.upper()==raidboss.upper():
                BossmaxCP=self.BossmaxCP[cnttt]
                Bossemoji=self.Bossemoji[cnttt]
                Bossoffset=self.Bossoffset[cnttt]
                Bossslope=self.Bossslope[cnttt]*0.0
                Bosspeeps=self.Bosspeeps[cnttt]*0.0    
                break
            cnttt+=1
        print(Bossoffset)
        

        #Now that we have both messages, we need to tally all of the reactions
        #await self.bot.send_message(self.bot.get_channel(self.programid),message.content+" "+message2.content)
        art=1
        if art==1:
            botmember = discord.utils.get(tmess.server.members, id=self.botid)
            RaidMan=discord.utils.get(tmess.server.roles, id=self.RaidManager)
            Ranger=discord.utils.get(tmess.server.roles, id=self.Ranger)
            Milk=discord.utils.get(tmess.server.roles, id=self.Milkmaid)
            Moder=discord.utils.get(tmess.server.roles, id=self.POGOmod)
            Valor=discord.utils.get(tmess.server.roles, id=self.valor)
            Mystic=discord.utils.get(tmess.server.roles, id=self.mystic)
            Instinct=discord.utils.get(tmess.server.roles, id=self.instinct)
        #try:
            a=tmess
            #argg=a.content.split('--> ')
            #a2=argg[0].split("(Delay for 2 minutes")
            #argg[0]=a2[0]
            #argg[0]=argg[0][0:16]
            #await self.bot.send_message(self.bot.get_channel(self.programid),"yt")
            #Get the list of users and their levels
            levelsum=0
            totalpeeps=0
            memberlist=""
            numdelay=0
            #instmem="```http\nINSTINCT: Levelsum="  #Use x at start of line
            #valomem="```diff\nVALOR: Levelsum="  #Use - at start of line was diff 
            #mystmem="```md\nMYSTIC: Levelsum="    #Use # at start of line
            instmem="__**INSTINCT:**__ Levelsum="  #Use x at start of line
            valomem="__**VALOR:**__ Levelsum="  #Use - at start of line was diff 
            mystmem="__**MYSTIC:**__ Levelsum="    #Use # at start of line
            instmemt=""
            valomemt=""
            mystmemt=""
            ninst=0
            nmyst=0
            nvalo=0
            linst=0
            lmyst=0
            lvalo=0
            RMname=""
            for xi in range(0,len(a.reactions)):
                useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                for yi in range(0,len(useri)):
                    namer=useri[yi]
                    #member = discord.utils.get(ctx.message.server.members, name=namer.name)
                    member = discord.utils.get(tmess.server.members, id=namer.id)
                    f=member.roles
                    team=""
                    
                    if assiRM==0:
                        if Milk in f:
                            RMname=member.display_name
                            assiRM=1
                    if assiRM==0:
                        if RaidMan in f:
                            RMname=member.display_name
                            assiRM=1
                    if assiRM==0:
                        if Ranger in f:
                            RMname=member.display_name
                            assiRM=1    
                    
                    if assiRM==0:
                        if Moder in f:
                            RMname=member.display_name
                            assiRM=1
                    if Valor in f:
                        team=" Val. "
                    elif Mystic in f:
                        team=" Mys. "
                    elif Instinct in f:
                        team=" Ins. "
                    #await self.bot.send_message(self.bot.get_channel(self.programid),namer)
                    namer2=member.display_name+str(useri[yi].discriminator)
                    #namer3=namer.name+str(useri[yi].discriminator)
                    #print(namer2)
                    #print(namer3)
                    #print(namer.name)
                    #await self.bot.send_message(self.bot.get_channel(self.programid),namer2)
                    getuserlevel= int(await subf.getuserlevel(self,namer2))
                    #print(getuserlevel)
                    if getuserlevel==-1: #They havent entered it yet
                        if user==namer:
                            await self.bot.send_message(member,member.display_name+", would you mind heading over to #raid-alerts and typing %level XX (replace XX with your trainer level), please?")
                            #await self.bot.send_message(member,member.display_name+", would you mind entering your trainer level so I can see if you all can beat this raid boss? (Enter __**1**__-__**40**__)")
                            #tata=await self.bot.wait_for_message(timeout = 30, author = user)
                            #await subf.setlevel(self,reaction,tata.content,user)
                            #await self.bot.add_reaction(a,"item_pokeball:284615009299070976")
                            #await asyncio.sleep(0.01)
                            #await self.bot.remove_reaction(a,"item_pokeball:284615009299070976",botmember)
                            #except:
                            #    a=1
                        getuserlevel=0
                    
                    if totalpeeps>0:
                        memberlist=memberlist 
                    totalpeeps+=1
                    cntt=0
                    levelsum+= getuserlevel#int(f[cntt].name[0:2])
                    try:
                        if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                            levelsum=levelsum-getuserlevel
                            #memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->200"  + "\n"
                        else:                        
                            #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                            memberlist=memberlist
                    except:
                        memberlist=memberlist
                        #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                    clevel=getuserlevel
                    #try:
                    try:
                        isspecialactive=0
                        if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                            levelsum=levelsum+400
                            memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->400"  + "\n"
                            isspecialactive=1
                        elif a.reactions[xi].emoji==self.delay:
                            levelsum=levelsum-int(clevel)
                            totalpeeps=totalpeeps-1
                            addlmess=' (Delayed) '
                            #Insert the delay code here
                            if numdelay==0:
                                argg[0]=argg[0] + "(Delay for 2 minutes for "
                            else:
                                argg[0]=argg[0] + "/"
                            argg[0]=argg[0] + member.display_name
                            numdelay=numdelay+1
                            isspecialactive=1
                            #memberlist=memberlist + member.display_name + addlmess + "     Level-" + clevel + "\n"
                    except:
                        rrr=1
                    fndemo=0
                    if isspecialactive==0:
                        #print(isspecialactive)
                        #if True:
                        try:
                            namer=member
                            for popdx in range(4):
                            #clevel=0
                                if ((a.reactions[xi].emoji))==self.shadowid[popdx]: #one
                                    namer=member
                                    uname=namer.display_name
                                    uname=uname+str(namer.discriminator)
                                    uname=namer2
                                    #print(namer2)
                                    #print(uname)
                                    df = pd.read_excel('Shadows2' + "\\" + uname + 'shadow.xlsx')
                                    fndemo=1
                                    levelsum=levelsum-int(clevel)
                                    clevel=0
                                    clevel=df.iloc[0,popdx]
                                    tnum=int(df.iloc[1,popdx])
                                    if int(clevel)>0:
                                        levelsum=levelsum+clevel
                                        if tnum==2:
                                            nvalo+=1
                                            lvalo+=clevel
                                            valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                        elif tnum==1:
                                            nmyst+=1
                                            lmyst+=clevel
                                            mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                        elif tnum==0:
                                            ninst+=1
                                            linst+=clevel
                                            instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                        #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + str(clevel) + ") " + team + "\n"
                                    else:
                                        levelsum=levelsum+0
                                        if Valor in f:
                                            nvalo+=1
                                            lvalo+=0
                                            valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                        elif Mystic in f:
                                            nmyst+=1
                                            lmyst+=0
                                            mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                        elif Instinct in f:
                                            ninst+=1
                                            linst+=0
                                            instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                        #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + "<20" + ") " + team + "\n"
                            print(fndemo)
                            if fndemo==0:  
                                #if namer2=="mikeko945239":
                                #    ninst+=1
                                #    linst+=clevel
                                #    instmemt+="^**"+"MK4694"+"**"+" (" + str(clevel) + ")\n"
                                #if member.display_name=="Haswari":
                                #    nmyst+=1
                                #    lmyst+=clevel
                                #    mystmemt+="#**"+"Eranthus"+"**"+" (" + str(clevel) + ")\n"
                                #print(member.display_name + str(clevel))
                                if Valor in f:
                                    nvalo+=1
                                    lvalo+=clevel
                                    valomemt+="-**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                elif Mystic in f:
                                    nmyst+=1
                                    lmyst+=clevel
                                    mystmemt+="#**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                elif Instinct in f:
                                    ninst+=1
                                    linst+=clevel
                                    instmemt+="^**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                        #memberlist=memberlist + member.display_name + "     (" + str(clevel) + ") " + team + "\n"
                        #else:
                        except:
                            
                            if Valor in f:
                                nvalo+=1
                                lvalo+=0
                                valomemt+="-**"+member.display_name+"**"+" (" + "<20" + ")\n"
                            elif Mystic in f:
                                nmyst+=1
                                lmyst+=0
                                mystmemt+="#**"+member.display_name+"**"+" (" + "<20" + ")\n"
                            elif Instinct in f:
                                ninst+=1
                                linst+=0
                                instmemt+="^**"+member.display_name+"**"+" (" + "<20" + ")\n"
                            #memberlist=memberlist + member.display_name + "     (" + "<20" + ") " + team + "\n"
                        cntt=cntt+1
            a2=a
        else:
        #except:
            arr=10
        
            #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 2")    
        #await self.bot.send_message(self.bot.get_channel(self.programid),str(totalpeeps)+" "+str(numdelay)+" "+str(levelsum)+" ")  
        numpeeps=totalpeeps
        if numdelay>0:
            argg[0]=argg[0] + ")"
        coloval=0xff0000
        if levelsum>0:
            #if raidlevel==5:
            crit=Bossoffset+(Bosspeeps-4)*Bossslope
            if levelsum>=1.0*crit:
                coloval=0x00ff00
                newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / HIGH CHANCE OF PASSING /' + str(numpeeps) + ' will attend'          
            elif levelsum>=0.80*crit and levelsum<1.00*crit:
                coloval=0x80ff80
                newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / REASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
            elif levelsum>=0.60*crit and levelsum<0.80*crit:
                coloval=0xffff00
                newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / UNREASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
            else:
                coloval=0xff0000
                newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / GNAT''S WING CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
        else:
            newmsg=argg[0] + ""
        memberlist3=""
        memberlist4=""   
        if ninst>0:
            #memberlist3+=instmem+"("+str(linst)+")\n"+instmemt+"```"
            memberlist3+=instmem+"("+str(linst)+")\n"+instmemt#+"```"
        if nmyst>0:
            #memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt+"```"
            memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt#+"```"
        if nvalo>0:
            #memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt+"```" 
            memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt#+"```" 
        if not memberlist=="":
            #memberlist3+="```"+memberlist+"```"   
            memberlist3+=memberlist#+"```"
        if assiRM==1:
            if RMname=="MrDonGiovanni":
                RMname="AJswagmaster420"
            if RMname=="MrMasterMiltank":
                RMname="MilkMaid"
            #memberlist4="```Assigned RM: " + RMname + "```"
            memberlist4="__**Assigned RM: " + RMname + "**__\n"
        memberlist=memberlist4+memberlist3
        if memberlist=="" and numpeeps>0:
            memberlist=str(numpeeps) + ' will attend'
            print(a.channel.name)
        newmsg=newmsg + "\n" + memberlist

        #create the modified embed here
        nm="<:team_instinct:284614748702638081>/" + "<:team_mystic:284614278709903371>/" + "  <:team_valor:284614087336525826>   -->   " + str(ninst) + "/" + str(nmyst) + "/" + str(nvalo)
        embed=discord.Embed(title=origtit, description=nm + "\n" + memberlist, color=coloval)
        await self.bot.edit_message(tmess,embed=embed)
        
        return
        
        
        
        await self.bot.edit_message(a,new_content=str(newmsg))
        #REVERT to 02092018v2 if needed
        #Find maximum number of people
        maxrxn=0
        async for msg in self.bot.logs_from(a.channel, limit=500): #Gets a list of the last 500 messages in the channel 
            rxncnt=0
            if msg.content.startswith("@Start"):
                for xi in range(0,len(msg.reactions)):
                    useri = await self.bot.get_reaction_users([x for x in msg.reactions][xi])
                    for yi in range(0,len(useri)):
                        rxncnt+=1
                if rxncnt>maxrxn:
                    maxrxn=rxncnt
        
        orignameo=a.channel.name
        if "_" in a.channel.name: #Number of people is assigned
            lgh=a.channel.name.split("_")
            orignameo=lgh[1]
        lgh=orignameo.split("---")
        newnameo=lgh[0]+ self.chanstrsp +lgh[1]
        if maxrxn>0:
            print(""+str(maxrxn)+"_"+newnameo)
            await self.bot.edit_channel(a.channel, name=str(maxrxn)+"_"+newnameo)
        else:            
            print(newnameo)
            await self.bot.edit_channel(a.channel, name=newnameo)
        
        return   

    
    
    async def genraidlistold(self,tmess,user):
        arr=10
        if tmess.channel.id in self.alllocch:
        #try:
            
            raidrestr=discord.utils.get(reaction.message.server.roles, id=self.raidrestr)
            print (user.roles)
            if raidrestr in user.roles:
                await self.bot.remove_reaction(reaction.message,reaction.emoji,user)
                
                return
            assiRM=0
            raidlevel=5 #Use this in the meantime
            #print("Here")
            message=reaction.message
            if not message.content.startswith('@Start:'):
                return
            chnid=reaction.message.channel.id
            ctx=reaction
            chnam=reaction.message.channel.name
            #channel1=discord.utils.get(ctx.message.server.channels, id=channel_id)
            #chnam=channel1.name
            #chnid=channel1.id
            argg=chnam.split('---')
            found=await subf.findboss(self,chnid)
            
            #If the channel is a raid boss specific channel, the second channel will lead with the raid boss
            if found==1:
                raidboss=argg[1]
                location=argg[0]
                namel2=raidboss + "---" +  location
            else:
                raidboss=argg[0]
                location=argg[1]
                namel2=location + "---" +  raidboss
            
            #Get the two channels
            channel1=ctx.message.channel   
            channel2 = discord.utils.get(ctx.message.server.channels, name=namel2)
            
            if "_" in  channel1.name:
                newargg=raidboss.split("_")
                raidboss=newargg[1]
            
            cnttt=0
            BossmaxCP=30.0
            Bossoffset=30.0
            Bossslope=0.0
            Bosspeeps=0.0 
            for rp in self.Bosstypes:
                if rp.upper()==raidboss.upper():
                    BossmaxCP=self.BossmaxCP[cnttt]
                    Bossemoji=self.Bossemoji[cnttt]
                    Bossoffset=self.Bossoffset[cnttt]
                    Bossslope=self.Bossslope[cnttt]*0.0
                    Bosspeeps=self.Bosspeeps[cnttt]*0.0    
                    break
                cnttt+=1
            print(Bossoffset)
            
            #Get the corresponding message from the other channel
            try:
                async for message2 in self.bot.logs_from(channel2, limit=50): #Gets a list of the last 500 messages in the channel 
                    if message2.content.startswith(message.content[0:15]):
                        break
            except:
                arr=10
            try:
                async for trigger in self.bot.logs_from(channel1, limit=50): #Gets a list of the last 500 messages in the channel 
                    if message2.content.startswith(message.content[0:15]):
                        break
            except:
                arr=10
                #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 0")
            #await self.bot.send_message(self.bot.get_channel(self.programid),message.content + " " +  message2.content)
            #Now that we have both messages, we need to tally all of the reactions
            #await self.bot.send_message(self.bot.get_channel(self.programid),message.content+" "+message2.content)
            art=1
            if art==1:
                botmember = discord.utils.get(ctx.message.server.members, id=self.botid)
                RaidMan=discord.utils.get(ctx.message.server.roles, id=self.RaidManager)
                Ranger=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
                Milk=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
                Moder=discord.utils.get(ctx.message.server.roles, id=self.POGOmod)
                Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
                Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
                Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
            #try:
                a=message
                argg=a.content.split('--> ')
                a2=argg[0].split("(Delay for 2 minutes")
                argg[0]=a2[0]
                #argg[0]=argg[0][0:16]
                #await self.bot.send_message(self.bot.get_channel(self.programid),"yt")
                #Get the list of users and their levels
                levelsum=0
                totalpeeps=0
                memberlist=""
                numdelay=0
                #instmem="```http\nINSTINCT: Levelsum="  #Use x at start of line
                #valomem="```diff\nVALOR: Levelsum="  #Use - at start of line was diff 
                #mystmem="```md\nMYSTIC: Levelsum="    #Use # at start of line
                instmem="__**INSTINCT:**__ Levelsum="  #Use x at start of line
                valomem="__**VALOR:**__ Levelsum="  #Use - at start of line was diff 
                mystmem="__**MYSTIC:**__ Levelsum="    #Use # at start of line
                instmemt=""
                valomemt=""
                mystmemt=""
                ninst=0
                nmyst=0
                nvalo=0
                linst=0
                lmyst=0
                lvalo=0
                RMname=""
                for xi in range(0,len(a.reactions)):
                    useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                    for yi in range(0,len(useri)):
                        namer=useri[yi]
                        #member = discord.utils.get(ctx.message.server.members, name=namer.name)
                        member = discord.utils.get(ctx.message.server.members, id=namer.id)
                        f=member.roles
                        team=""
                        
                        if assiRM==0:
                            if Milk in f:
                                RMname=member.display_name
                                assiRM=1
                        if assiRM==0:
                            if RaidMan in f:
                                RMname=member.display_name
                                assiRM=1
                        if assiRM==0:
                            if Ranger in f:
                                RMname=member.display_name
                                assiRM=1    
                        
                        if assiRM==0:
                            if Moder in f:
                                RMname=member.display_name
                                assiRM=1
                        if Valor in f:
                            team=" Val. "
                        elif Mystic in f:
                            team=" Mys. "
                        elif Instinct in f:
                            team=" Ins. "
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer)
                        namer2=member.display_name+str(useri[yi].discriminator)
                        #namer3=namer.name+str(useri[yi].discriminator)
                        #print(namer2)
                        #print(namer3)
                        #print(namer.name)
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer2)
                        getuserlevel= int(await subf.getuserlevel(self,namer2))
                        #print(getuserlevel)
                        if getuserlevel==-1: #They havent entered it yet
                            if user==namer:
                                await self.bot.send_message(member,member.display_name+", would you mind heading over to #raid-alerts and typing %level XX (replace XX with your trainer level), please?")
                                #await self.bot.send_message(member,member.display_name+", would you mind entering your trainer level so I can see if you all can beat this raid boss? (Enter __**1**__-__**40**__)")
                                #tata=await self.bot.wait_for_message(timeout = 30, author = user)
                                #await subf.setlevel(self,reaction,tata.content,user)
                                #await self.bot.add_reaction(a,"item_pokeball:284615009299070976")
                                #await asyncio.sleep(0.01)
                                #await self.bot.remove_reaction(a,"item_pokeball:284615009299070976",botmember)
                                #except:
                                #    a=1
                            getuserlevel=0
                        
                        if totalpeeps>0:
                            memberlist=memberlist 
                        totalpeeps+=1
                        cntt=0
                        levelsum+= getuserlevel#int(f[cntt].name[0:2])
                        try:
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum-getuserlevel
                                #memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->200"  + "\n"
                            else:                        
                                #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                                memberlist=memberlist
                        except:
                            memberlist=memberlist
                            #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                        clevel=getuserlevel
                        #try:
                        try:
                            isspecialactive=0
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum+400
                                memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->400"  + "\n"
                                isspecialactive=1
                            elif a.reactions[xi].emoji==self.delay:
                                levelsum=levelsum-int(clevel)
                                totalpeeps=totalpeeps-1
                                addlmess=' (Delayed) '
                                #Insert the delay code here
                                if numdelay==0:
                                    argg[0]=argg[0] + "(Delay for 2 minutes for "
                                else:
                                    argg[0]=argg[0] + "/"
                                argg[0]=argg[0] + member.display_name
                                numdelay=numdelay+1
                                isspecialactive=1
                                #memberlist=memberlist + member.display_name + addlmess + "     Level-" + clevel + "\n"
                        except:
                            rrr=1
                        fndemo=0
                        if isspecialactive==0:
                            #print(isspecialactive)
                            #if True:
                            try:
                                namer=member
                                for popdx in range(4):
                                #clevel=0
                                    if ((a.reactions[xi].emoji))==self.shadowid[popdx]: #one
                                        namer=member
                                        uname=namer.display_name
                                        uname=uname+str(namer.discriminator)
                                        uname=namer2
                                        #print(namer2)
                                        #print(uname)
                                        df = pd.read_excel('Shadows2' + "\\" + uname + 'shadow.xlsx')
                                        fndemo=1
                                        levelsum=levelsum-int(clevel)
                                        clevel=0
                                        clevel=df.iloc[0,popdx]
                                        tnum=int(df.iloc[1,popdx])
                                        if int(clevel)>0:
                                            levelsum=levelsum+clevel
                                            if tnum==2:
                                                nvalo+=1
                                                lvalo+=clevel
                                                valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==1:
                                                nmyst+=1
                                                lmyst+=clevel
                                                mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==0:
                                                ninst+=1
                                                linst+=clevel
                                                instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + str(clevel) + ") " + team + "\n"
                                        else:
                                            levelsum=levelsum+0
                                            if Valor in f:
                                                nvalo+=1
                                                lvalo+=0
                                                valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Mystic in f:
                                                nmyst+=1
                                                lmyst+=0
                                                mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Instinct in f:
                                                ninst+=1
                                                linst+=0
                                                instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + "<20" + ") " + team + "\n"
                                print(fndemo)
                                if fndemo==0:  
                                    #if namer2=="mikeko945239":
                                    #    ninst+=1
                                    #    linst+=clevel
                                    #    instmemt+="^**"+"MK4694"+"**"+" (" + str(clevel) + ")\n"
                                    #if member.display_name=="Haswari":
                                    #    nmyst+=1
                                    #    lmyst+=clevel
                                    #    mystmemt+="#**"+"Eranthus"+"**"+" (" + str(clevel) + ")\n"
                                    #print(member.display_name + str(clevel))
                                    if Valor in f:
                                        nvalo+=1
                                        lvalo+=clevel
                                        valomemt+="-**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                    elif Mystic in f:
                                        nmyst+=1
                                        lmyst+=clevel
                                        mystmemt+="#**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                    elif Instinct in f:
                                        ninst+=1
                                        linst+=clevel
                                        instmemt+="^**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                            #memberlist=memberlist + member.display_name + "     (" + str(clevel) + ") " + team + "\n"
                            #else:
                            except:
                                
                                if Valor in f:
                                    nvalo+=1
                                    lvalo+=0
                                    valomemt+="-**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                elif Mystic in f:
                                    nmyst+=1
                                    lmyst+=0
                                    mystmemt+="#**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                elif Instinct in f:
                                    ninst+=1
                                    linst+=0
                                    instmemt+="^**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                #memberlist=memberlist + member.display_name + "     (" + "<20" + ") " + team + "\n"
                            cntt=cntt+1
                a2=a
            else:
            #except:
                arr=10
            
                #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 2")    
            #await self.bot.send_message(self.bot.get_channel(self.programid),str(totalpeeps)+" "+str(numdelay)+" "+str(levelsum)+" ")  
            numpeeps=totalpeeps
            if numdelay>0:
                argg[0]=argg[0] + ")"
            
            if levelsum>0:
                #if raidlevel==5:
                crit=Bossoffset+(Bosspeeps-4)*Bossslope
                if levelsum>=1.0*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / HIGH CHANCE OF PASSING /' + str(numpeeps) + ' will attend'          
                elif levelsum>=0.80*crit and levelsum<1.00*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / REASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                elif levelsum>=0.60*crit and levelsum<0.80*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / UNREASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                else:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / GNAT''S WING CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
            else:
                newmsg=argg[0] + ""
            memberlist3=""
            memberlist4=""   
            if ninst>0:
                #memberlist3+=instmem+"("+str(linst)+")\n"+instmemt+"```"
                memberlist3+=instmem+"("+str(linst)+")\n"+instmemt#+"```"
            if nmyst>0:
                #memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt+"```"
                memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt#+"```"
            if nvalo>0:
                #memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt+"```" 
                memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt#+"```" 
            if not memberlist=="":
                #memberlist3+="```"+memberlist+"```"   
                memberlist3+=memberlist#+"```"
            if assiRM==1:
                if RMname=="MrDonGiovanni":
                    RMname="AJswagmaster420"
                if RMname=="MrMasterMiltank":
                    RMname="MilkMaid"
                #memberlist4="```Assigned RM: " + RMname + "```"
                memberlist4="__**Assigned RM: " + RMname + "**__\n"
            memberlist=memberlist4+memberlist3
            if memberlist=="" and numpeeps>0:
                memberlist=str(numpeeps) + ' will attend'
                print(a.channel.name)
            newmsg=newmsg + "\n" + memberlist

            await self.bot.edit_message(a,new_content=str(newmsg))
            #REVERT to 02092018v2 if needed
            #Find maximum number of people
            maxrxn=0
            async for msg in self.bot.logs_from(a.channel, limit=500): #Gets a list of the last 500 messages in the channel 
                rxncnt=0
                if msg.content.startswith("@Start"):
                    for xi in range(0,len(msg.reactions)):
                        useri = await self.bot.get_reaction_users([x for x in msg.reactions][xi])
                        for yi in range(0,len(useri)):
                            rxncnt+=1
                    if rxncnt>maxrxn:
                        maxrxn=rxncnt
            
            orignameo=a.channel.name
            if "_" in a.channel.name: #Number of people is assigned
                lgh=a.channel.name.split("_")
                orignameo=lgh[1]
            lgh=orignameo.split("---")
            newnameo=lgh[0]+ self.chanstrsp +lgh[1]
            if maxrxn>0:
                print(""+str(maxrxn)+"_"+newnameo)
                await self.bot.edit_channel(a.channel, name=str(maxrxn)+"_"+newnameo)
            else:            
                print(newnameo)
                await self.bot.edit_channel(a.channel, name=newnameo)
            
            return   
        else:
        #except:
            arrrg=10
    
    
    async def clearone(self,chid,role_everyone):
        ch=chid
        try:
            overwrite = ch.overwrites_for(role_everyone)
            if overwrite.read_messages == True:
                overwrite.read_messages = False
                await self.bot.edit_channel_permissions(ch, role_everyone, overwrite)
            return
        except:
            print(role_everyone.id + role_everyone.name + "Failed")
            return
            
    async def getchid(self,setids):
        try:
            maxpos=0
            for x in setids:
                ch=self.bot.get_channel(x)
                g=ch.position
                if g>maxpos:
                    maxpos=g
                    MTchan=x
        except:
            MTchan="0"
        #await self.box.send_message(self.bot_get_channel(self.programid),MTchan)
        return MTchan
    
    async def checksn(self,inname):
        maxpos=0
        for x in setids:
            ch=self.bot.get_channel(x)
            g=ch.position
            if g>maxpos:
                maxpos=g
                MTchan=x
        return MTChan  

        
    async def prevover(self,setids,Nameval,type,ctx):
        for x in setids:
            ch=self.bot.get_channel(x)
            if (ch.name==Nameval+ "---" + type.lower()) or (ch.name==type.lower()+ "---" +  Nameval):
                async for message in self.bot.logs_from(ch, limit=500): #Gets a list of the last 500 messages in the channel 
                    if message.content.startswith('RAID:'): #Then we need to get the ID of this message and see if it has the correct start time
                        a=message
                        arggn=a.content.split('\n')  #The second argument will be the minutes
                        argg=arggn[0].split(' ends at ')  #The second argument will be the minutes
                        
                        polltime = datetime.utcnow()+timedelta(hours=self.timez)
                        tpolltime=polltime.strftime(self.timeform)
                        tdeltat = datetime.strptime(tpolltime, self.timeform)-datetime.strptime(argg[1], self.timeform)
                        if tdeltat.days<0: #the raid has already been entered in the system
                            await self.bot.send_message(ctx.message.author,"The information you entered has already been entered by someone else.")
                            return 1
                        else:
                            return 0
        
    async def grantacc(self,channloc,channrb,role):
        if not any(xpp == channrb.id for xpp in self.allrbch):
            overwrite = channrb.overwrites_for(role)
            overwrite.read_messages = True
            await self.bot.edit_channel_permissions(channrb, role, overwrite)
        overwrite = channloc.overwrites_for(role)
        overwrite.read_messages = True
        await self.bot.edit_channel_permissions(channloc, role, overwrite)
        
    async def removeaccsing(self,channrb,role):
        overwrite = channrb.overwrites_for(role)
        overwrite.read_messages = False
        await self.bot.edit_channel_permissions(channrb, role, overwrite)
        
    async def grantRT(self,b,role):
        try:
            await self.bot.add_roles(b, role)
            return 1
        except:
            return 0
            
    async def sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky):
        #await self.bot.send_message(msgchann, "__**Raid:**__"+allmention+"\n"+origname+" ends at "+endtime+" "+ emoji + "\n"+linky+"\nVisit:" + chmention)
        msgg=await self.bot.send_message(msgchann, "__**Raid:**__"+" \n"+origname+" ends at "+endtime+" "+ emoji + "\n"+linky+"\nVisit:" + chmention)
        return msgg
    
    async def editnote(self,msgg,allmention,chmention,origname,endtime,emoji,linky):
        #await self.bot.send_message(msgchann, "__**Raid:**__"+allmention+"\n"+origname+" ends at "+endtime+" "+ emoji + "\n"+linky+"\nVisit:" + chmention)
        await self.bot.edit_message(msgg, "__**Raid:**__"+allmention+"\n"+origname+" ends at "+endtime+" "+ emoji + "\n"+linky+"\nVisit:" + chmention)
    
    @commands.command(pass_context=True)
    async def updateAR(self,ctx,oldlist,newlist,location,time):  #Use this to update the message in #active_raids
        ch=self.bot.get_channel(self.genchid)
        Milk=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
        L3=discord.utils.get(ctx.message.server.roles, id=self.L3Notify)
        async for message in self.bot.logs_from(ch, limit=10): #Gets a list of the last 500 messages in the channel 
            #if message.content.startswith('RAID:'): #Then we need to get the ID of this message and see if it has the correct start time
            argg=message.content.split(" ")
            modmess=""
            for n in argg:
                if n==L3.mention:
                    print("Foundya")
                    #Change the message notifies
                    print(n,Milk.mention)
                    modmess+=Milk.mention + " "
                    msggg=await self.bot.send_message(ch,Milk.mention) 
                    await asyncio.sleep(0.5)
                    await self.bot.delete_message(msggg) 
                    
                else:
                    modmess+=n + " "
            #await self.bot.edit_message(message,modmess)  
    
    async def qasker(self,ctx):
        while g3==0 or a3<3:
            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
            if int(msgrt.content)<6 and int(msgrt.content)>0: 
                type="Level"+msgrt.content
                g3=1
                await self.bot.send_message(ctx.message.channel,"Almost done! What is the Pokemon Go name of the gym? You only need the first 8 letters without spaces or special characters")
                msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                gymname=msgrt.content
                await self.bot.send_message(ctx.message.author,"%raid " + status + " " + type+ " "+ str(timer)+" "+ gymname)
                return 0
            else:
                await self.bot.send_message(ctx.message.channel,"Something didn't seem right there. Try again")
                a3+=1
            if a3==3:
                await self.bot.send_message(ctx.message.author,"Sorry, you entered a bad input too many times!")
                return 0
    
    async def storedata(self,Valor,Mystic,Instinct):
        #Clear reactions if older than 10 mins
        try:
            for x in self.alllocch:
                ch=self.bot.get_channel(x)
                flagch=0
                chname=ch.name
                chstuff=chname.split('---')
                async for message in self.bot.logs_from(ch, limit=1000): #Gets a list of the last 500 messages in the channel 
                #print(message.content)
                    if message.content.startswith('@Start: '): #Then we need to get the ID of this message and see if it has the correct start time
                        a=message
                        argg=a.content.split('--> ')
                        
                        a2=argg[0].split("(Delay for 2 minutes")
                        argg[0]=a2[0]
                        orig_mess=argg[0]
                        argg[0]=argg[0][8:18]
                        raidtime=argg[0]
                        #print(argg[1])
                        cctime = datetime.utcnow()+timedelta(hours=self.timez)
                        tcctime=cctime.strftime('%m/%d/%y %H:%M:%S')
                        polltime = datetime.utcnow()+timedelta(hours=self.timez)+timedelta(minutes=-12)
                        tpolltime=polltime.strftime(self.timeform)
                        tdeltat = datetime.strptime(tpolltime, self.timeform)-datetime.strptime(argg[0], self.timeform)
                        #traidtime=raidtime.strftime('%H:%M:%S')
                        #self.bot.send_message(ctx.message.author,str(argg[1])+" "+str(tdelta))
                        
                        if tdeltat.days==0:  #This raid time has expired
                            userlist=[]
                            for xi in range(0,len(a.reactions)): 
                                useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                                for yi in useri:
                                    namer=yi
                                    
                                    uname=namer.display_name
                                    uname=uname+str(namer.discriminator)
                                    #uname=namer2
                                    #print(uname)
                                    member = discord.utils.get(message.server.members, name=namer.name)
                                    f=member.roles
                                    team=""
                                    if Valor in f:
                                        team=" Val. "
                                    elif Mystic in f:
                                        team=" Mys. "
                                    elif Instinct in f:
                                        team=" Ins. "
                                    #await self.bot.send_message(self.bot.get_channel(self.programid),namer)
                                    namer2=member.display_name+str(yi.discriminator)
                                    #print(namer2)
                                    #await self.bot.send_message(self.bot.get_channel(self.programid),namer2)
                                    getuserlevel= int(await subf.getuserlevel(self,namer2))
                                    if getuserlevel==-1: #They havent entered it yet
                                        #await self.bot.send_message(member,namer2+", Please enter a level using the %level command within the pokesight alerts channel of the PurdueMon Discord")
                                        getuserlevel=-99
                                    
                                    isspecialactive=0
                                    if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                        #clevel=200
                                        team="Varies"
                                        getuserlevel=400
                                        isspecialactive=10
                                        namer2="RaidTrain"
                                    elif a.reactions[xi].emoji==self.delay:
                                        clevel=0
                                        isspecialactive=1

                                    if isspecialactive==0:
                                        try:
                                            clevel=0
                                            for idx in range(0,4):
                                                if ((a.reactions[xi].emoji))==self.shadowid[idx]: #four
                                                    uname=namer.display_name
                                                    uname=uname+str(namer.discriminator)
                                                    uname=namer2
                                                    #print(uname)
                                                    df = pd.read_excel('Shadows' + "\\" + uname + 'shadow.xlsx')
                                                    levelsum=levelsum-int(clevel)
                                                    #clevel=0
                                                    getuserlevel=int(df.iloc[0,idx])
                                                    #clevel=200
                                                    team="Varies"
                                                    getuserlevel=400
                                                    isspecialactive=12
                                                    namer2=uname+"-Shadow"+str(idx+1)
                                                    break
                                                else:
                                                    aaf=1
                                                #memberlist=memberlist + member.display_name + "     Level-" + str(clevel) + " " + team + "\n"
                                        except:
                                            aaf=1
                                            #memberlist=memberlist + member.display_name + "     Level-" + str(clevel) + " " + team + "\n"
                                        #cntt=cntt+1
                                    
                                    
                                    
                                    if not isspecialactive==1:
                                        userlist.append([tcctime,raidtime,namer2,getuserlevel,team,chstuff[0],chstuff[1]])
                            #print(tdeltat.days)
                            #print(a.content)
                            print(userlist)
                            print("Clear reactions")
                            print(orig_mess)
                            #Write the list to a file somewhere
                            #number = sum(1 for line in open('raids.txt'))+1
                            #onumber=str(number)
                            #number=str(number).zfill(4)              
                            #await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
                            #rr2=discord.utils.get(ctx.message.server.roles, id=self.RaidObserver)
                            #await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + ctx.message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
                            for idx in userlist:
                                line=idx
                                with open("raidstore.txt","a") as f:
                                    print(line,file=f)
                                #await self.bot.edit_message(a,orig_mess)
                                #await self.bot.clear_reactions(a)
                                
                            await self.bot.delete_message(a)
                        flagch=1
                #Now we need to figure out if the correct number of people is on the channel
                if flagch==1: #means that something was deleted
                    maxrxn=0
                    async for msg in self.bot.logs_from(ch, limit=500): #Gets a list of the last 500 messages in the channel 
                        rxncnt=0
                        if msg.content.startswith("@Start"):
                            for xi in range(0,len(msg.reactions)):
                                useri = await self.bot.get_reaction_users([x for x in msg.reactions][xi])
                                for yi in range(0,len(useri)):
                                    rxncnt+=1
                            if rxncnt>maxrxn:
                                maxrxn=rxncnt
                    
                    orignameo=ch.name
                    if "_" in ch.name: #Number of people is assigned
                        lgh=ch.name.split("_")
                        orignameo=lgh[1]
                    lgh=orignameo.split("---")
                    newnameo=lgh[0]+ self.chanstrsp +lgh[1]
                    if maxrxn>0:
                        print(""+str(maxrxn)+"_"+newnameo)
                        await self.bot.edit_channel(ch, name=str(maxrxn)+"_"+newnameo)
                    else:            
                        print(newnameo)
                        await self.bot.edit_channel(ch, name=newnameo)    
                    
                            
        except:
            arrr=1
    
    
        
    #@commands.command(pass_context=True)
    async def raidhelper(self,ctx):  #Use this to update the message in #active_raids
    #Now to get the stuff to update the #active_raids channel
        await self.bot.send_message(ctx.message.author,"Looks like you're trying to put in a raid. Has the raid boss hatched yet? (Y/N)")
        g1=0
        a1=0
        time=0
        status=0
        while g1==0 or a1<3:
            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="N": 
                await self.bot.send_message(ctx.message.channel,"So, it's still an egg! How much time in minutes until the egg hatches (round down)?")
                time=45
                status="1"
                g2=0
                a2=0
                while g2==0 or a2<3:
                    msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                    if int(msgrt.content)>0 and int(msgrt.content)<60: 
                        timer=int(msgrt.content)
                        time=time+int(msgrt.content)
                        g2=1
                        g3=0
                        a3=0
                        await self.bot.send_message(ctx.message.channel,"Great! What tier level is the egg?")
                        while g3==0 or a3<3:
                            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                            if int(msgrt.content)<6 and int(msgrt.content)>0: 
                                type="Level"+msgrt.content
                                g3=1
                                await self.bot.send_message(ctx.message.channel,"Almost done! What is the Pokemon Go name of the gym? You only need the first 8 letters without spaces or special characters")
                                msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                                gymname=msgrt.content
                                await self.bot.send_message(ctx.message.author,"%raid " + status + " " + type+ " "+ str(timer)+" "+ gymname)
                                return 0
                            else:
                                await self.bot.send_message(ctx.message.channel,"Something didn't seem right there. Try again")
                                a3+=1
                            if a3==3:
                                await self.bot.send_message(ctx.message.author,"Sorry, you entered a bad input too many times!")
                                return 0
                    else:
                        await self.bot.send_message(ctx.message.channel,"Something didn't seem right there. Try again")
                        a2+=1
                    if a2==3:
                        await self.bot.send_message(ctx.message.author,"Sorry, you entered a bad input too many times!")
                        return 0
            elif msgrt.content.upper()=="Y": 
                await self.bot.send_message(ctx.message.author,"So, it's a raid boss! How much time left on the raid boss?")
                time=0
                status="2"
                g2=0
                a2=0
                while g2==0 or a2<3:
                    msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                    if int(msgrt.content)>0 and int(msgrt.content)<60: 
                        timer=int(msgrt.content)
                        time=time+int(msgrt.content)
                        g2=1
                        g3=0
                        a3=0
                        await self.bot.send_message(ctx.message.channel,"Great! What is the name of the raid boss?")
                        while g3==0 or a3<3:
                            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                            g3=1
                            type=msgrt.content
                            await self.bot.send_message(ctx.message.channel,"Almost done! What is the Pokemon Go name of the gym? You only need the first 8 letters without spaces or special characters")
                            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                            gymname=msgrt.content
                            await self.bot.send_message(ctx.message.author,"%raid " + status + " " + type+ " "+ str(timer)+" "+ gymname)
                            return "%raid " + status + " " + type+ " "+ str(timer)+" "+ gymname
                    else:
                        await self.bot.send_message(ctx.message.channel,"Something didn't seem right there. Try again")
                        a2+=1
                    if a2==3:
                        await self.bot.send_message(ctx.message.author,"Sorry, you entered a bad input too many times!")
                        return 0
            else:
                a1+=1
                g1=0

            if a1==3:
                await self.bot.send_message(ctx.message.author,"Sorry, you entered a bad input too many times!")
                return 0
                
    async def getuserlevel(self,username):
        try: #If the sheet exists, open it 
            df = pd.read_excel('ExcelFiles' + "\\" + username + 'level.xlsx')
            a=df.iloc[0,0]
            return df.iloc[0,0]  
        except: #The person hasn't established a level yet
            return -1
    
class ballzy:        
    
    def __init__(self, bot,path=default_path, parse_args=True):
        self.cooldown=1
        self.numcat=1
        self.catnames=["MEWTWO RAIDS"]
        self.nchan=8
        self.timeform='%I:%M:%S%p'
        self.RTchan='419963470243692574'
        self.AlertNames=["Ralts","Snorlax","Larvitar"]
        self.AlertID=["389108657696276481","351942390400942090","351942268774776832"]
        self.Alertmesid=['410550223522365452', '410550223744532481', '410550224327540746']
        self.testalert="389805020595355649" #ID of alert for 89-94IV
        self.bot=bot
        self.CMK="345200594421547018"
        self.settings = dataIO.load_json(path)
        self.InstallDirectory = self.settings["InstallDirectory"]
        self.RaidObserver=str(self.settings["RaidObserver"]) #Role ID for the RaidObserver role #Updated for Purdue test - Final Version
        self.Admin=str(self.settings["Admin"]) #Role ID for administrator  #Updated for Purdue test - instinct
        self.RaidTrainer=str(self.settings["RaidTrainer"]) #Role ID for the RaidTrainer role #Updated for Purdue test - Final Version
        self.POGOmod=str(self.settings["POGOmod"])  #Role ID for the RaidTrainer role #Updated for Purdue test - Final Version
        self.Approved=str(self.settings["Approved"]) #Role ID for Approved 
        self.Unapproved=str(self.settings["Unapproved"]) #Role ID for Unapproved
        self.pendingApp=str(self.settings["Pending"]) #Role ID for Pending Approval
        self.questmaster=str(self.settings["questmaster"]) #Role ID for Quest Master
        self.servername=self.settings["servername"] #name of the server
        self.valor=str(self.settings["valor"]) #Role ID for valor
        self.mystic=str(self.settings["mystic"]) #Role ID for mystic
        self.instinct=str(self.settings["instinct"]) #Role ID for instinct
        self.valorch=str(self.settings["valor_ch"]) #Role ID for valor
        self.mysticch=str(self.settings["mystic_ch"]) #Role ID for mystic
        self.instinctch=str(self.settings["instinct_ch"]) #Role ID for instinct
        
        self.Milkmaid="405887565506281472"
        self.MilkMaid="405887565506281472"
        self.Ranger="284566461425647616"
        self.RaidManager="340243113454993408"
        self.RaidObserver=self.Ranger  #Allow RO functionality with Ranger role
        
        self.troubleshoot="0"
        
        #Necessary channels IDs
        self.getapproved=str(self.settings["getapproved"])  #Channel ID for approval channel
        self.genchid=str(self.settings["genchid"])  #Channel ID for general raid discussion 
        self.serverid=str(self.settings["serverid"]) #Server ID number 
        self.silphch=str(self.settings["silphch"]) #Silph Badge Channel ID
        self.programid=str(self.settings["programid"]) #Channel ID number for troubleshooting information 
        self.raidsightings=str(self.settings["raidsightings"]) #Channel ID number for raid sightings, input data here. 
        self.questsightings=str(self.settings["questsightings"]) #Channel ID number for raid sightings, input data here.
        self.setupch=str(self.settings["setupch"]) #Channel ID number for the setup channel, input data here.
        
        self.bot = bot
        self.botid=str(self.settings["botid"]) #User ID for the bot.
        
        self.mewtwoposts="362698126248771604" #Implement
        
        #channel groups
        self.g2locaid=[ str(x) for x in self.settings["g2locaid"]] #WEST LAFAYETTE AREA
        self.g3locaid=[ str(x) for x in self.settings["g3locaid"]] #LAFAYETTE AREA
        self.g1locaid=[ str(x) for x in self.settings["g1locaid"]] #PURDUE CAMPUS
        
        self.L5groupid=[ str(x) for x in self.settings["L5groupid"]] #LEGENDARY ID
        self.L4groupid=[ str(x) for x in self.settings["L4groupid"]] #LEVEL4 RAID BOSSES
        self.L3groupid=[ str(x) for x in self.settings["L3groupid"]] #LEVEL3 RAID BOSSES
        self.PSgroupid=[ str(x) for x in self.settings["PSgroupid"]] #SHINY RAID BOSSES
        self.oL5groupid=self.L5groupid
        self.oL4groupid=self.L4groupid
        self.oL3groupid=self.L3groupid
        self.oPSgroupid=self.PSgroupid
        
        stuff = dataIO.load_json("configuration/exraid.txt")
        self.mtch1id=stuff["mtch1id"]
        self.mtch2id=stuff["mtch2id"]
        self.mtch3id=stuff["mtch3id"]
        self.mtch4id=stuff["mtch4id"]
        self.mtch5id=stuff["mtch5id"]
        self.mtch6id=stuff["mtch6id"]
        self.mtch7id=stuff["mtch7id"]
        self.mtch8id=stuff["mtch8id"]
        self.mtch9id=stuff["mtch9id"]
        self.mtch10id=stuff["mtch10id"]
        self.mtch11id=stuff["mtch11id"]
        self.mtch12id=stuff["mtch12id"]
        
        
        stuff = dataIO.load_json("configuration/bannedlist.json")
        self.bannedlist=stuff["bannedlist"]
        
        #self.L5groupid=['0','0','0','0']
        #self.L4groupid=['0','0','0','0']
        #self.L3groupid=['0','0','0','0']
        #self.PSgroupid=['0','0','0','0']
        self.excludeid=[self.valor,self.mystic,self.instinct,self.Ranger,self.Milkmaid,self.RaidManager,self.Approved,self.POGOmod,self.RaidTrainer,self.RaidObserver]
        self.mewtwo=['369959279605841920','387233975359373313','387234099687063553','387234137934659586','387234333553065985','387234374292209664','387234426582597637','387234526406901771','501124866028863498','501125092852367378','501125116252520450','501125131112939540']  #These are mewtwo channels
        self.emoji_exgym="<:deoxys:492380587160764416>"
        
        
        self.settings = dataIO.load_json("configuration/RaidRoles.json")
        self.raidroles=int(self.settings["raidroles"])
        self.SilentL3=[]
        self.SilentL4=[]
        self.SilentL5=[]
        self.SilentPS=[]
        self.SilentOI=[]
        self.SilentEX=[]
        self.NotifyL3=[]
        self.NotifyL4=[]
        self.NotifyL5=[]
        self.NotifyPS=[]
        self.NotifyOI=[]
        self.NotifyEX=[]
        if self.raidroles==1:
            
            self.SilentL3=self.settings["SilentL3"]
            self.SilentL4=self.settings["SilentL4"]
            self.SilentL5=self.settings["SilentL5"]
            self.SilentPS=self.settings["SilentPS"]
            self.SilentOI=self.settings["SilentOI"]
            self.SilentEX=self.settings["SilentEX"]
            self.NotifyEX=self.settings["NotifyEX"]
            self.NotifyL5=self.settings["NotifyL5"]
            self.NotifyL4=self.settings["NotifyL4"]
            self.NotifyL3=self.settings["NotifyL3"]
            self.NotifyOI=self.settings["NotifyOI"]
            self.NotifyPS=self.settings["NotifyPS"]
        
        usefile=1
        
        if usefile==1:
            stuff = dataIO.load_json("configuration/L4bosses.txt")
            self.L4types=stuff["L4types"]
            self.L4notid=stuff["L4notid"]
            self.L4maxCP=stuff["L4maxCP"]
            self.L4slope=stuff["L4slope"]
            self.L4peeps=stuff["L4peeps"]
            self.L4offset=stuff["L4offset"]
            self.L4emoji=stuff["L4emoji"]
            self.L4emoji[0]='\U00000034\U000020e3'

        if usefile==1:
            stuff = dataIO.load_json("configuration/L5bosses.txt")
            self.L5types=stuff["L5types"]
            self.L5notid=stuff["L5notid"]
            self.L5maxCP=stuff["L5maxCP"]
            self.L5slope=stuff["L5slope"]
            self.L5peeps=stuff["L5peeps"]
            self.L5offset=stuff["L5offset"]
            self.L5emoji=stuff["L5emoji"]
            self.L5emoji[0]='\U00000035\U000020e3'     

        
        if usefile==1:
            stuff = dataIO.load_json("configuration/L3bosses.txt")
            self.L3types=stuff["L3types"]
            self.L3notid=stuff["L3notid"]
            self.L3maxCP=stuff["L3maxCP"]
            self.L3slope=stuff["L3slope"]
            self.L3peeps=stuff["L3peeps"]
            self.L3offset=stuff["L3offset"]
            self.L3emoji=stuff["L3emoji"]
            self.L3emoji[0]='\U00000033\U000020e3'
        
        
        if usefile==1:
            stuff = dataIO.load_json("configuration/PSbosses.txt")
            self.PStypes=stuff["PStypes"]
            self.PSnotid=stuff["PSnotid"]
            self.PSmaxCP=stuff["PSmaxCP"]
            self.PSslope=stuff["PSslope"]
            self.PSpeeps=stuff["PSpeeps"]
            self.PSoffset=stuff["PSoffset"]
            self.PSemoji=stuff["PSemoji"]
                
       
        if usefile==1:
            stuff = dataIO.load_json("configuration/OIbosses.txt")
            self.OItypes=stuff["OItypes"]
            self.OInotid=stuff["OInotid"]
            self.OImaxCP=stuff["OImaxCP"]
            self.OIslope=stuff["OIslope"]
            self.OIpeeps=stuff["OIpeeps"]
            self.OIoffset=stuff["OIoffset"]
            self.OIemoji=stuff["OIemoji"]
       
       #ADDL LEGENDARIES #"<a:Celebi:407703535820734464>","<a:Mew:407703534956576768>","<a:Mewtwo:407703534474100762>","<a:Rayquaza:407703535145320460>","<a:Latias:407703535053176833>","<a:Latios:407703535073886208>"
        self.notifyon=1

        self.shadowid=['\U0001F550','\U0001F551','\U0001F552','\U0001F553']  #These are the emoji for clocks
        self.shadowid=['\U00000031\U000020e3','\U00000032\U000020e3','\U00000033\U000020e3','\U00000034\U000020e3']  #These are the emoji for clocks
        self.notthresh=0.6
        self.raidrestr='493884845622034463'
        self.train='\U0001F68b'
        self.train2='\U0001F684'
        self.train3='\U0001F685'
        self.train4='\U0001F686'
        self.train5='\U0001F682'
        self.delay='\U0001F6D1'
        self.raidspacing=10
        self.raidmaxtime=45 #Duration of the egg at a gym before it hatches
        self.eggtime=60
        self.bossactivetime=45
        self.mintimerem=20 #Minimum duration allowed for data entry
        #self.eggmaxtime=60  #Duration of the egg at a gym before it hatches
        self.maxtimeslots=4
        
        stuff = dataIO.load_json("configuration/timezone.json")
        self.timez=stuff["timezone"]  #Read in the timezone from the configuration file
        
        #self.settings = dataIO.load_json("configuration/RaidLocations.json")
        self.settings = dataIO.load_json("configuration/NewRaidLocas.json")

        self.group1sn=self.settings["group1sn"]
        self.group1an=self.settings["group1an"]
        self.group1cn=self.settings["group1cn"]
        #self.group1ln=self.settings["group1ln"]
        self.group1lat=self.settings["group1lat"]
        self.group1lon=self.settings["group1lon"]
        self.group1ex=self.settings["group1ex"]
        #self.group1nn=self.group1ln
        #self.group1nn[0:len(self.group1nn)]=1
        
        self.group2sn=self.settings["group2sn"]
        self.group2an=self.settings["group2an"]
        self.group2cn=self.settings["group2cn"]
        #self.group2ln=self.settings["group2ln"]
        self.group2lat=self.settings["group2lat"]
        self.group2lon=self.settings["group2lon"]
        self.group2ex=self.settings["group2ex"]
        #self.group2nn=self.group2ln

        
        self.group3sn=self.settings["group3sn"]
        self.group3an=self.settings["group3an"]
        self.group3cn=self.settings["group3cn"]
        #self.group3ln=self.settings["group3ln"]
        self.group3lat=self.settings["group3lat"]
        self.group3lon=self.settings["group3lon"]
        self.group3ex=self.settings["group3ex"]
        #self.group3nn=self.group3ln
        
        
 
        self.AddlNotiid=[]
        self.Locbypass=[]
        
        #Concatenated groups for looping functions
        self.sngroup=self.group1sn+self.group2sn+self.group3sn
        self.angroup=self.group1an+self.group2an+self.group3an
        self.cngroup=self.group1cn+self.group2cn+self.group3cn
        self.exgroup=self.group1ex+self.group2ex+self.group3ex
        #self.lngroup=self.group1ln+self.group2ln+self.group3ln
        self.latgroup=self.group1lat+self.group2lat+self.group3lat
        self.longroup=self.group1lon+self.group2lon+self.group3lon
        #self.nngroup=self.group1nn+self.group2nn+self.group3nn
        
        print(self.exgroup)
        for n in range(0,len(self.exgroup)):
            if int(self.exgroup[n])==1:
                self.AddlNotiid.append(self.NotifyEX)
                self.Locbypass.append(self.cngroup[n])
                
        print(self.AddlNotiid)        
        print(self.Locbypass) 
        self.exroles=["439133778665799683","439133825608450069","439133841534353420","439133856684048384","439133870365868032","439133884836478987","439133899080073217","439133912804098059","501126820100309002","501127101869457409","501127128692293632","501127150460469258"]
        self.exchan=["439132862449713172","439133094809829376","439133163894210561","439133181426532362","439133199147466752","439133214808735744","439133228733825035","439133245649584140",'501124866028863498','501125092852367378','501125116252520450','501125131112939540']
        self.Bosstypes=self.L3types+self.L4types+self.L5types+self.PStypes+self.OItypes
        self.Bossnotid=self.L3notid+self.L4notid+self.L5notid+self.PSnotid+self.OInotid
        self.BossmaxCP=self.L3maxCP+self.L4maxCP+self.L5maxCP+self.PSmaxCP+self.OImaxCP
        self.Bossoffset=self.L3offset+self.L4offset+self.L5offset+self.PSoffset+self.OIoffset
        self.Bossslope=self.L3slope+self.L4slope+self.L5slope+self.PSslope+self.OIslope
        self.Bosspeeps=self.L3peeps+self.L4peeps+self.L5peeps+self.PSpeeps+self.OIpeeps
        self.Bossemoji=self.L3emoji+self.L4emoji+self.L5emoji+self.PSemoji+self.OIemoji
        self.allemoji=self.Bossemoji+["<:item_pokeball:284615009299070976>"]
        self.L3Notify=self.NotifyL3
        self.L4Notify=self.NotifyL4
        self.L5Notify=self.NotifyL5
        self.PSNotify=self.NotifyPS
        self.OINotify=self.NotifyOI
        
        
            
        
        
        self.SilentRoles=[self.SilentL3,self.SilentL4,self.SilentL5,self.SilentPS,self.SilentOI,self.SilentEX]
        self.SilentNames=["SilentL3","SilentL4","SilentL5","SilentPS","SilentOI","SilentEX"]
        self.chanstrsp="-=-=-"
        self.reactsetupnames=self.Bosstypes+self.SilentNames+self.Locbypass #names
        self.reactsetupids=self.Bossnotid+self.SilentRoles+self.AddlNotiid #IDs
        self.reactsetupmess=['409403416326963201', '409403417208029184', '409403418344423435', '409403419883995136', '409403421385424906', '409403438422556683', '409403439668264970', '409403441400774657', '409403442948472848', '409403444403896320', '409403465752903690', '409403466822451200', '409403468210765824', '409403469313867777', '409403470920286229', '409403489077166080', '409403489760968705', '409403491350478859', '409403492512432129', '409403493959598082', '409403515119730749', '409403515857797121', '409403517564878858', '409403518827626497', '409403520890961933', '409403542420455425', '409403543339008010', '409403544525864961', '409403545646006276', '409403547399225345', '409403564759187456', '409403565766082560', '409403567309324288', '409403568614014986', '409403570081890304', '409403591422640128', '409403592148254740', '409403593582706688', '409403594912169996', '409403597072105482', '409403618433957888', '409403618857582603', '409403620677779457', '409403622313689089', '409403624116977684', '409403641288589312', '409403641909215233', '409403643867955220', '409403644996354050', '409403646342594563']
        self.mutemap=0
        self.RTsize=0
        self.RTtime=10
        self.RTrealtime = datetime.utcnow()+timedelta(hours=self.timez)+timedelta(minutes=self.RTtime)
        self.lastraid=datetime.utcnow()+timedelta(hours=self.timez)
        
        
        
        self.RTgyms=[]
        #Role ID's for muting regions       
        self.muteg1="407184187804876821"
        self.muteg2="407184509008609280"
        self.muteg3="407184366897332225"
        self.reactsetupnames=["Mute Purdue","Mute West Lafayette","Mute Lafayette"]
        self.reactsetupids=[self.muteg1,self.muteg2,self.muteg3]
        self.reactsetupmess=['410424462320861184', '410424463830548480', '410424465646682112']
        self.threeleaders=[]
        #await subf.leaderbhelper(self,ctx)
        self.WL=[];
        for f in self.cngroup:
            argg=f.split(" ")
            for g in argg:
                argg2=g.split("-")
                for h in argg2:
                    self.WL.append(h)
        uniqwords=[]
        for x in self.WL:
            if x not in uniqwords:
                if len(x)>=4:
                    uniqwords.append(x) 
        self.WL=uniqwords
        scrubbed=[]
        for f in self.WL: #clean them!
            Nameval = f.replace(' ', '-').lower()
            Nameval = Nameval.replace('+', '').lower()
            Nameval = Nameval.replace('/', '').lower()
            Nameval = Nameval.replace("'", '').lower()
            Nameval =Nameval.replace(".", '').lower()
            scrubbed.append(Nameval )
        self.WL=scrubbed
        try:
            bot.remove_command('help')
        except:
            arp=1
        
        bot.loop.create_task(self.checkraidbuffer())
        bot.loop.create_task(self.checkexpraidnow())
        
        #await subf.read
        
        
        self.settings = dataIO.load_json("configuration/Stopsfile.json")
        self.stopnam=self.settings["names"]
        self.stoplat=self.settings["Lat"]
        self.stoplon=self.settings["Lon"]
        self.alllat=self.stoplat+self.latgroup
        self.alllon=self.stoplon+self.longroup
        self.sWL=[];
        for f in self.stopnam+self.cngroup:
            argg=f.split(" ")
            for g in argg:
                argg2=g.split("-")
                for h in argg2:
                    self.sWL.append(h)
        uniqwords=[]
        for x in self.sWL:
            if x not in uniqwords:
                if len(x)>=3:
                    uniqwords.append(x) 
        self.sWL=uniqwords
        scrubbed=[]
        for f in self.sWL: #clean them!
            Nameval = f.replace(' ', '-').lower()
            Nameval = Nameval.replace('+', '').lower()
            Nameval = Nameval.replace('/', '').lower()
            Nameval = Nameval.replace("'", '').lower()
            Nameval =Nameval.replace(".", '').lower()
            scrubbed.append(Nameval )
        self.sWL=scrubbed
        #print(self.WL)
        self.reward=["Stardust","Rare Candy","Encounter"]
        self.encounters=["Magikarp","Larvitar","Dratini","Tangela","Machop","Gastly","Chansey","Ninetales"]
        self.dust=["200","500","1000","1500"]
        self.questtype=[]
        self.dust1500='431539103847415809'
        self.dust1000='431538612505411604'
        self.chansey='431538480368189461'
        self.chargedtm='445920345262915585'
        self.rarecandy='431539338736697344'
        self.dratini='431539726714142745'
        self.silverpinap='486987817600417820'
        self.growlithe='474314475219189761'
        self.tangela='431539101519577088'
        self.magikarp='431539597164412938'
        self.shinyquest='446425269889400833'
        self.absol='457244505049923597'
        #set to list from file eventually
        self.settings = dataIO.load_json("configuration/shinies.txt")
        self.shinylist=self.settings["shinylist"]
        
        #For quests rewards and such
        self.settings = dataIO.load_json("configuration/questlist.txt")
        self.tasklist=self.settings["tasklist"]
        self.rewardlist=self.settings["rewardlist"]
        
        #For easter eggs in the discord
        stuff = dataIO.load_json("configuration/eastereggs.txt")
        self.EAchannels=stuff["EAchannels"]
        self.EAcommands=stuff["EAcommands"]
        self.EAuserids=stuff["EAuserids"]
        self.EAfilename=stuff["EAfilename"]
        self.EAminacclvl=stuff["EAminacclvl"]
        
        self.Basestats = pd.read_excel('BaseStats.xlsx')
        self.CPM = pd.read_excel('CPMult.xlsx')
        stuff = dataIO.load_json("configuration/setup.json")
        self.nreg=int(stuff["nreg"])
        
        self.d={}  #Make a dictionary of regions and channels for now
        try:  #This will fail in the event nothing is set up yet
            for x in range(0,self.nreg):
                name=stuff["Region"+str(x+1)+"name"]
                qty=int(stuff["Region"+str(x+1)+"chn"])
                #print(name)
                #msg+=name + " - " + str(qty) + " channels.\n"
                self.d["Region"+str(x+1)+"name"]=name
                self.d["Region"+str(x+1)+"chn"]=qty
            stuff = dataIO.load_json("configuration/Raidchannels.json")
            for x in range(0,self.nreg):
                self.d["Region"+str(x+1)+"chid"]=stuff["Region"+str(x+1)+"chid"]
                self.d["Region"+str(x+1)+"hid"]=stuff["Region"+str(x+1)+"hid"]
            self.g2locaid=[ str(x) for x in self.d["Region"+str(2)+"chid"]] #WEST LAFAYETTE AREA
            self.g3locaid=[ str(x) for x in self.d["Region"+str(3)+"chid"]] #LAFAYETTE AREA
            self.g1locaid=[ str(x) for x in self.d["Region"+str(1)+"chid"]] #PURDUE CAMPUS
            #Concatenated groups for looping functions
            self.allraidch=self.g1locaid+self.g2locaid+self.g3locaid+self.L3groupid+self.L4groupid+self.L5groupid+self.PSgroupid+self.mewtwo
            self.alllocch=self.g1locaid+self.g2locaid+self.g3locaid
            self.allrbch=self.L3groupid+self.L4groupid+self.L5groupid+self.PSgroupid
            self.allrbchms=self.L3groupid+self.L4groupid+self.L5groupid
            self.oldchan=self.oL3groupid+self.oL4groupid+self.oL5groupid+self.oPSgroupid
            self.allbutmtch=self.alllocch+self.allrbch
        except:
            self.d={}
    
    
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def delsetup(self,ctx):
        '''Deletes any created channel by the bot.'''
        self.secure=0 #Toggle this if you need to remove the channels
        if self.secure>0:
            await self.bot.send_message(ctx.message.channel,"The program has been secured, preventing me from clearing raid channels.")
            return
        try:
            stuff = dataIO.load_json("configuration/Raidchannels.json")        
            for x in range(0,self.nreg):
                self.d["Region"+str(x+1)+"chid"]=stuff["Region"+str(x+1)+"chid"]
                self.d["Region"+str(x+1)+"hid"]=stuff["Region"+str(x+1)+"hid"]
                yr=self.d["Region"+str(x+1)+"hid"]
                for y in yr:
                    yp=self.bot.get_channel(y)
                    await self.bot.delete_channel(yp)
                yr=self.d["Region"+str(x+1)+"chid"]
                for y in yr:
                    yp=self.bot.get_channel(y)
                    await self.bot.delete_channel(yp)    
        except:
            arp=10
        
        stuff = dataIO.load_json("configuration/Otherchannels.json") 
        mlist=["Raid-Sightings","Quests","Programming","Friendship","Silph-Badges"]
        for x in mlist:
            try:
                y=stuff[x]
                yp=self.bot.get_channel(y)
                await self.bot.delete_channel(yp)
            except:
                arp=10
        
    #This command sets up the channels necessary for raiding and quests
    #Ready for publication
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def dosetup(self,ctx):
        await self.bot.send_message(ctx.message.channel,"Let's get started.  There is a json document in /configuration called setup.json to create the settings.  Are you ready to continue? (Y/N)")
        msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
        if msgrt.content.upper()=="Y":
            #Do all the stuff
            detent=1
            #load the file to create the channels
            stuff = dataIO.load_json("configuration/setup.json")
            self.nreg=int(stuff["nreg"])
            
            await self.bot.send_message(ctx.message.channel,"I detected " + str(self.nreg) + " region you are creating.\nThis is a summary of what I will create for you.\n")
            msg=""
            self.d={}  #Make a dictionary of regions and channels for now
            for x in range(0,self.nreg):
                name=stuff["Region"+str(x+1)+"name"]
                qty=int(stuff["Region"+str(x+1)+"chn"])
                print(name)
                msg+=name + " - " + str(qty) + " channels.\n"
                self.d["Region"+str(x+1)+"name"]=name
                self.d["Region"+str(x+1)+"chn"]=qty
            
            gensilph=0
            genraids=0
            genfriend=0
            genquest=0
            genprogramming=0
            
            msg+="Additional channels I will use or create:\n"
            if stuff["ConfigureSilphChannel"].upper()=="YES":
                if stuff["AddSilphChannel"].upper()=="YES":
                    gensilph=1
                    msg+="__**Silph Badge Channel**__ --> " + "CREATING\n"
                else:
                    try:
                        xr=self.bot.get_channel(stuff["CurrentSilphChannel"])
                        msg+="__**Silph Badge Channel**__ --> " + "USING" + xr.mention + "\n"
                    except:
                        await self.bot.send_message(ctx.message.channel,"Silph Channel ID is invalid.")
                        return
            else:
                msg+="__**Silph Badge Channel**__ --> " + "BYPASSING\n"   
                
            if stuff["ConfigureRaidSightingsChannel"].upper()=="YES":
                if stuff["AddRaidSightingsChannel"].upper()=="YES":
                    genraids=1
                    msg+="__**Raid Sightings Channel**__ --> " + "CREATING\n"
                else:
                    try:
                        xr=self.bot.get_channel(stuff["CurrentSightingsChannel"])
                        msg+="__**Raid Sightings Channel**__ --> " + "USING" + xr.mention + "\n"
                    except:
                        await self.bot.send_message(ctx.message.channel,"Raid Sightings Channel ID is invalid.")
                        return
            else:
                msg+="__**Raid Sightings Channel**__ --> " + "BYPASSING\n"  
            
            if stuff["ConfigureFriendshipChannel"].upper()=="YES":
                if stuff["AddFriendshipChannel"].upper()=="YES":
                    genfriend=1
                    msg+="__**Friendship Channel**__ --> " + "CREATING\n"
                else:
                    try:
                        xr=self.bot.get_channel(stuff["CurrentFriendshipChannel"])
                        msg+="__**Friendship Channel**__ --> " + "USING" + xr.mention + "\n"
                    except:
                        await self.bot.send_message(ctx.message.channel,"Friendship Channel ID is invalid.")
                        return
            else:
                msg+="__**Friendship Channel**__ --> " + "BYPASSING\n"  
                
            if stuff["ConfigureProgrammingChannel"].upper()=="YES":
                if stuff["AddProgrammingChannel"].upper()=="YES":
                    genprogramming=1
                    msg+="__**Programming Channel**__ --> " + "CREATING\n"
                else:
                    try:
                        xr=self.bot.get_channel(stuff["CurrentProgrammingChannel"])
                        msg+="__**Programming Channel**__ --> " + "USING" + xr.mention  + "\n"
                    except:
                        await self.bot.send_message(ctx.message.channel,"Programming Channel ID is invalid.")
                        return
            else:
                msg+="__**Programming Channel**__ --> " + "BYPASSING\n"  
            
            if stuff["ConfigureQuestChannel"].upper()=="YES":
                if stuff["AddQuestChannel"].upper()=="YES":
                    genquest=1
                    msg+="__**Quest Channel**__ --> " + "CREATING\n"
                else:
                    try:
                        xr=self.bot.get_channel(stuff["CurrentQuestChannel"])
                        msg+="__**Quest Channel**__ --> " + "USING" + xr.mention  + "\n"
                    except:
                        await self.bot.send_message(ctx.message.channel,"Quest Channel ID is invalid.")
                        return
            else:
                msg+="__**Quest Channel**__ --> " + "BYPASSING\n" 

                        
            await self.bot.send_message(ctx.message.channel,msg + "\nDo you want me to save this and create channels? (Y/N)")
            
            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
            #Start creation of a json file for persistent variables
            txt='{\n'
            if msgrt.content.upper()=="Y":
                #Do all the things
                file = open("configuration/Raidchannels.json","w",encoding='utf-8') 
                for x in range(0,self.nreg):
                    
                    xr=await self.bot.create_channel(ctx.message.server, self.d["Region"+str(x+1)+"name"], type=4)
                    txt+='"Region' + str(x+1) + 'hid":["'+ xr.id +'"],\n'
                    txt+='"Region' + str(x+1) + 'chid":["'
                    cntt=0
                    for y in range(0,self.d["Region"+str(x+1)+"chn"]):
                        xr=await self.bot.create_channel(ctx.message.server, self.d["Region"+str(x+1)+"name"]+str(y))
                        if not cntt==0:
                            txt+=',"'
                        txt+=str(xr.id) + '"'
                        cntt+=1    
                    txt+='],\n'  
                txt=txt[:-2]+"\n}"
                file.write(txt)          
                file.close()    
                print(txt)
                
                file = open("configuration/Otherchannels.json","w",encoding='utf-8')
                txt='{\n'
                cntt=0
                
                if genraids==1:
                    xr=await self.bot.create_channel(ctx.message.server, "Raid-Sightings")
                    txt+='"Raid-Sightings":["'+ xr.id +'"],\n'
                    cntt+=1
                if genquest==1:
                    xr=await self.bot.create_channel(ctx.message.server, "Quests")
                    txt+='"Quests":["'+ xr.id +'"],\n'
                    cntt+=1
                if genprogramming==1:
                    xr=await self.bot.create_channel(ctx.message.server, "Programming")
                    txt+='"Programming":["'+ xr.id +'"],\n'
                    cntt+=1
                if genfriend==1:
                    xr=await self.bot.create_channel(ctx.message.server, "Friendship")
                    txt+='"Friendship":["'+ xr.id +'"],\n'
                    cntt+=1
                if gensilph==1:
                    xr=await self.bot.create_channel(ctx.message.server, "Silph-Badges") 
                    txt+='"Silph-Badges":["'+ xr.id +'"],\n'
                    cntt+=1
                txt=txt[:-2]+"\n}"
                file.write(txt)
                file.close()
                
                
                await self.bot.send_message(ctx.message.channel, "Reorganize your channels, and type in `%cleansetup` to complete the setup.")
            else: 
                await self.bot.send_message(ctx.message.channel, "I will not do anything then.  Bye!")
                return
        else:
            await self.bot.send_message(ctx.message.channel, "I will not do anything then.  Bye!")
            
            
    #This command sets up the channels necessary for raiding and quests
    #Ready for publication
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def dosetup2(self,ctx):
        await self.bot.send_message(ctx.message.channel,"Let's get started.  This process will take about 10 minutes, and must be done all at once. Are you ready to continue? (Y/N)")
        msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
        if not msgrt.content.upper()=="Y":
            await self.bot.send_message(ctx.message.channel, "I will not do anything then.  Bye!") 
            return
        
        success=0
        for x in range(0,3):
            await self.bot.send_message(ctx.message.channel,"How many regions do you want to have created? Enter a number between 1 and 10.")
            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
            try:
                nreg=int(msgrt.content)
                if (nreg>=1 and nreg<=10):
                    success=1
                    break
                await self.bot.send_message(ctx.message.channel, "Well that didn't work!")
            except:
                await self.bot.send_message(ctx.message.channel, "Well that didn't work!")
                
        if (success==0):
            await self.bot.send_message(ctx.message.channel, "Too many errors.  Peace out.")
            return
           
        success=0
        for x in range(0,3):
            for y in range(0,nreg):
                await self.bot.send_message(ctx.message.channel,"How many regions do you want to have created? Enter a number between 1 and 10.")
                msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                try:
                    nreg=int(msgrt.content)
                    if (nreg>=1 and nreg<=10):
                        success=1
                        break
                    await self.bot.send_message(ctx.message.channel, "Well that didn't work!")
                except:
                    await self.bot.send_message(ctx.message.channel, "Well that didn't work!")
                
        if (success==0):
            await self.bot.send_message(ctx.message.channel, "Too many errors.  Peace out.")
            return
        
        
        return
        #Do all the stuff
        detent=1
        #load the file to create the channels
        stuff = dataIO.load_json("configuration/setup.json")
        self.nreg=int(stuff["nreg"])
        
        await self.bot.send_message(ctx.message.channel,"I detected " + str(self.nreg) + " region you are creating.\nThis is a summary of what I will create for you.\n")
        msg=""
        self.d={}  #Make a dictionary of regions and channels for now
        for x in range(0,self.nreg):
            name=stuff["Region"+str(x+1)+"name"]
            qty=int(stuff["Region"+str(x+1)+"chn"])
            print(name)
            msg+=name + " - " + str(qty) + " channels.\n"
            self.d["Region"+str(x+1)+"name"]=name
            self.d["Region"+str(x+1)+"chn"]=qty
        await self.bot.send_message(ctx.message.channel,msg + "\nDo you want me to save this and create channels? (Y/N)")
        msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
        #Start creation of a json file for persistent variables
        txt='{\n'
        if msgrt.content.upper()=="Y":
            #Do all the things
            file = open("configuration/Raidchannels.json","w",encoding='utf-8') 
            for x in range(0,self.nreg):
                
                xr=await self.bot.create_channel(ctx.message.server, self.d["Region"+str(x+1)+"name"], type=4)
                txt+='"Region' + str(x+1) + 'hid":["'+ xr.id +'"],\n'
                txt+='"Region' + str(x+1) + 'chid":["'
                cntt=0
                for y in range(0,self.d["Region"+str(x+1)+"chn"]):
                    xr=await self.bot.create_channel(ctx.message.server, self.d["Region"+str(x+1)+"name"]+str(y))
                    if not cntt==0:
                        txt+=',"'
                    txt+=str(xr.id) + '"'
                    cntt+=1    
                txt+='],\n'  
            txt=txt[:-2]+"\n}"
            file.write(txt)          
            file.close()    
            print(txt)
            await self.bot.send_message(ctx.message.channel, "Reorganize your channels, and type in `%cleansetup` to complete the setup.")
        else: 
            await self.bot.send_message(ctx.message.channel, "I will not do anything then.  Bye!")
            return
    #else:
    #    await self.bot.send_message(ctx.message.channel, "I will not do anything then.  Bye!")        
    
    
    @checks.is_owner()    
    @commands.command(pass_context=True)
    async def createroles(self,ctx):
        #Only use once!  This function will create necessary raid roles so the bot doesn't error out
        server=self.bot.get_server(self.serverid)
        rolenames=['SilentL5','SilentL4','SilentL3','SilentPS','SilentOI','SilentEX','NotifyL5','NotifyL4','NotifyL3','NotifyPS','NotifyOI','NotifyEX']
        file = open("configuration/RaidRoles.json","w",encoding='utf-8')
        txt="{\n"
        txt+='"raidroles":"1",\n'
        for x in rolenames:
            nr = await self.bot.create_role(server, name=x)
            txt+='"'+x+'":' + '"' + str(nr.id) + '",\n'
         
        txt=txt[:-2]+"\n}"
        file.write(txt)          
        file.close() 
            

        
        
        
    
    #This command renames the channels necessary for raiding and quests and stores the data for future usage
    #Ready for publication
    @checks.is_owner()    
    @commands.command(pass_context=True)
    async def cleansetup(self,ctx):
        stuff = dataIO.load_json("configuration/Raidchannels.json")
        server=self.bot.get_server(self.serverid)
        for y in server.members:
            member=discord.Server.get_member(server,y.id)
            break
        for x in range(0,self.nreg):
            self.d["Region"+str(x+1)+"chid"]=stuff["Region"+str(x+1)+"chid"]
            yr=self.d["Region"+str(x+1)+"chid"]
            for y in yr:
                xr=self.bot.get_channel(y)
                await self.bot.edit_channel(xr,name='blank-0')
                #set permissions so no one can see the channels
                cnnt=0
                
                rra=member.roles[0]
                print(rra)
                
                
                
                ch=xr
                try:
                    overwrite = ch.overwrites_for(rra)
                    #if overwrite.read_messages == True:
                    overwrite.read_messages = False
                    await self.bot.edit_channel_permissions(ch, server.default_role, overwrite)
                except:
                    print(role_everyone.id + role_everyone.name + "Failed")
                if not rra==None:
                    rr=await subf.clearone(self,ch,rra)
                
                #return
                for x in self.Bossnotid+self.AddlNotiid+[self.SilentL3,self.SilentL4,self.SilentL5,self.SilentPS,self.SilentEX]:
                    
                    rra=discord.utils.get(ctx.message.server.roles, id=x)
                    if not rra==None:
                        rr=await subf.clearone(self,ch,rra)
                    cnnt+=1
                    #print(cnnt)
        #    xr=await self.bot.create_channel(ctx.message.server, self.d["Region"+str(x+1)+"name"], type=4)
        #    
        #        xr=await self.bot.create_channel(ctx.message.server, self.d["Region"+str(x+1)+"name"]+str(y))
        await self.bot.send_message(ctx.message.channel, "All of the raid channels have been initialized! Congrats, you are ready to go!")
        #Still need to create a raid-sightings channel and quest channel
        
        return      
   
    #This function loads alternative quests for quest days
    #Ready for publication
    @checks.admin()  #Only allow admins to run this command
    @commands.command(pass_context=True)
    async def loadclamp(self,ctx):
        '''Load alternative set of quests (typically used on special quest days)'''
        self.settings = dataIO.load_json("configuration/questlist_clamp.txt")
        self.tasklist=self.settings["tasklist"]
        self.rewardlist=self.settings["rewardlist"]
    
    #This function loads standard quests
    #Ready for publication
    @checks.admin()  
    @commands.command(pass_context=True)
    async def loadnormal(self,ctx):
        '''Load standard set of quests.  These can be modified from the file or by `%getquest`'''
        self.settings = dataIO.load_json("configuration/questlist.txt")
        self.tasklist=self.settings["tasklist"]
        self.rewardlist=self.settings["rewardlist"]    
    
    #This function displays a list of easter eggs
    #Ready for publication
    @checks.admin()  
    @commands.command(pass_context=True)
    async def getEA(self,ctx): #Prints off the current easter eggs
        if ctx.message.channel.id==self.programid:
            linkn="**Easter eggs can always be used in the following channels:**\n"
            for x in self.EAchannels:
                getch=self.bot.get_channel(x)
                linkn+=getch.mention + "\n"

            await self.bot.send_message(ctx.message.channel, linkn)
            linkn="**These are the current easter eggs installed in the system:**\n"
            for x in range(0,len(self.EAcommands)):
                linkn+="__**" + self.EAcommands[x] + "**__ - "
                if not self.EAuserids[x]=="0":  #If the user id is not equal to "0", tag the user
                    b=discord.Server.get_member(ctx.message.server,self.EAuserids[x]) 
                    linkn+=b.mention
                else:
                    linkn+="No tags"
                linkn+=" - " + self.EAfilename[x] + " - "
                if self.EAminacclvl[x]=="0":
                    linkn+="__**" + "Anywhere" + "**__ "
                if self.EAminacclvl[x]=="1":
                    linkn+="__**" + "EA/Raid Channels" + "**__ "
                if self.EAminacclvl[x]=="2":
                    linkn+="__**" + "Raid Channels" + "**__ "
                linkn+="\n"
            await self.bot.send_message(ctx.message.channel, linkn)
            return

    #This function displays a list of standard quests when %quest is used
    #Ready for publication
    @checks.admin()  
    @commands.command(pass_context=True)
    async def getquest(self,ctx):
        if ctx.message.channel.id==self.programid:
            linkn="**These are the default quests:**\n"
            cntt=0
            for x in self.tasklist:
                y=self.rewardlist[cntt]
                linkn+="**"+str(cntt+1)+")** "+x+" for a "+y[0]+"\n"
                cntt+=1
            await self.bot.send_message(ctx.message.channel, linkn)
    
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def addquest(self,ctx,reward,task):  #Add a quest to the default quest sightings list
        if ctx.message.channel.id==self.programid:
            await self.bot.send_message(ctx.message.channel, "OK, so you want me to add:\nGet " +  reward + " for completing "+ task + "\nCorrect? (Y/N)")
            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="Y":
                await self.bot.send_message(ctx.message.channel, "I added a default research task:\nGet " +  reward.upper() + " for completing "+ task + "")
                self.tasklist.append(task)
                self.rewardlist.append([reward.upper()])
                await subf.questwrite(self)
            else:
                await self.bot.send_message(ctx.message.channel, "I have not modified the research tasks.")
    
    @checks.mod()  
    @commands.command(pass_context=True)
    async def delquest(self,ctx,number):  #Remove a quest to the default quest sightings list
        if ctx.message.channel.id==self.programid:
            reward=self.rewardlist[int(number)-1]
            task=self.tasklist[int(number)-1]
            await self.bot.send_message(ctx.message.channel, "OK, so you want me to delete:\nGet " +  reward[0] + " for completing "+ task + "\nCorrect? (Y/N)")
            
            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
            
            if msgrt.content.upper()=="Y":
                del self.tasklist[int(number)-1]
                del self.rewardlist[int(number)-1]
                await subf.questwrite(self)
                await self.bot.send_message(ctx.message.channel, "I deleted a default research task:\nGet " +  reward[0].upper() + " for completing "+ task + "")
            else:
                await self.bot.send_message(ctx.message.channel, "I have not modified the research tasks.")
            return
            linkn="**These are the default quests:**\n"
            cntt=0
            for x in self.tasklist:
                y=self.rewardlist[cntt]
                linkn+="**"+str(cntt+1)+")** "+x+" for a "+y[0]+"\n"
                cntt+=1
            await self.bot.send_message(ctx.message.channel, linkn)
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def checkraidbuff(self,ctx):  #This restarts the raid removal loop in case of the bot getting hung up
        self.bot.loop.create_task(self.checkraidbuffer())
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def getboss(self,ctx,type):
        if ctx.message.channel.id==self.programid:
            maxspace=14
            txt=""
            if type.upper()=="4" or type.upper()=="L4" or type.upper()=="Level4":
                
                for x in range(0,len(self.L4types)):
                    rr2=None
                    lname=len(self.L4types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L4notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L4types[x].ljust(maxspace) + "-" + str(self.L4maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L4types[x].ljust(maxspace) + "-" + str(self.L4maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 4 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
                    
            if type.upper()=="5" or type.upper()=="L5" or type.upper()=="Level5":
                for x in range(0,len(self.L5types)):
                    rr2=None
                    lname=len(self.L5types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L5notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L5types[x].ljust(maxspace) + "-" + str(self.L5maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L5types[x].ljust(maxspace) + "-" + str(self.L5maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 5 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="3" or type.upper()=="L3" or type.upper()=="Level3":
                for x in range(0,len(self.L3types)):
                    rr2=None
                    lname=len(self.L3types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L3notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L3types[x].ljust(maxspace) + "-" + str(self.L3maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L3types[x].ljust(maxspace) + "-" + str(self.L3maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 3 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="PS" or type.upper()=="Shiny" or type.upper()=="PossibleShiny":
                for x in range(0,len(self.PStypes)):
                    rr2=None
                    lname=len(self.PStypes[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.PSnotid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.PStypes[x].ljust(maxspace) + "-" + str(self.PSmaxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.PStypes[x].ljust(maxspace) + "-" + str(self.PSmaxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are Possible Shiny bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="OI" or type.upper()=="Interest" or type.upper()=="OfInterest":
                for x in range(0,len(self.OItypes)):
                    rr2=None
                    lname=len(self.OItypes[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.OInotid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.OItypes[x].ljust(maxspace) + "-" + str(self.OImaxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.OItypes[x].ljust(maxspace) + "-" + str(self.OImaxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are Of Interest bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
    
    
    #Need to configure this still
    @checks.admin()  
    async def checkraidbuffer(self):
        await self.bot.wait_until_ready()
        await asyncio.sleep(5)
        return
        while True:
            #channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id="350508951806148609")
            #message=await self.bot.get_message(channre,"532299638015918081")
            #print(message.content)
            data=""
            try:
                with open(self.InstallDirectory + "raidcache.txt","r") as fin:
                    data = fin.read().splitlines(True)
                with open(self.InstallDirectory + "raidcache.txt", 'w') as fout:
                    fout.writelines(data[1:])
            except:
                arp=1
            #        await subf.raidbypass(self,message,data)
            #        #with open("raidcache.txt","r") as f:
            #        #    print(line,file=f)
            #try:
            if data=="":
                print("Cache Empty")
            else:
                try:
                    print(data[0])
                    await subf.raidbypass(self,message,data[0])
                except:
                    arp=1
            await asyncio.sleep(5)
    
    #Change settings for raids in the event of a raid day
    #Ready for publication
    @checks.admin()   #Only allow admins to run this        
    @commands.command(pass_context=True)
    async def param(self,ctx,parameter,value):
        '''parameters:
        raidspacing    -- Minutes between raid times (default:10)
        raidmaxtime    -- Minutes a boss is active (default:45)
        eggtime        -- Minutes an egg is active before hatching (default:60)
        bossactivetime -- Minutes a boss is active (default:45)
        mintimerem     -- Time remaining on hatched boss for it to be added (default:15)
        maxtimeslots   -- Number of raid time options in a channel (default:4)
        '''
        ch1=0
        if parameter=='raidspacing':
            self.raidspacing=int(value)
            await self.bot.send_message(ctx.message.channel,"raidspacing was changed to "+value)
            ch1=1
        if parameter=='raidmaxtime':
            self.raidmaxtime=int(value)
            self.bossactivetime=int(value)
            await self.bot.send_message(ctx.message.channel,"raidmaxtime was changed to "+value)
            ch1=1
        if parameter=='eggtime':
            self.eggtime=int(value)
            await self.bot.send_message(ctx.message.channel,"eggtime was changed to "+value)
            ch1=1
        
        if parameter=='bossactivetime':
            self.bossactivetime=int(value)
            self.raidmaxtime=int(value)
            await self.bot.send_message(ctx.message.channel,"bossactivetime was changed to "+value)
            ch1=1
        if parameter=='mintimerem':
            self.mintimerem=int(value)
            await self.bot.send_message(ctx.message.channel,"mintimerem was changed to "+value)
            ch1=1
        if parameter=='maxtimeslots':
            self.maxtimeslots=int(value)
            await self.bot.send_message(ctx.message.channel,"maxtimeslots was changed to "+value)
            ch1=1
        if ch1==0:
            await self.bot.send_message(ctx.message.channel,"That parameter is not available to be changed.  Contact a Milkmaid to have it changed.")
        #self.maxtimeslots=4
    
    #Add a pokestop to the dictionary
    @checks.admin()   #Only allow admins to run this   
    @commands.command(pass_context=True)
    async def addstop(self,ctx,latitude,longitude,*, name : str):
        '''Add a new pokestop to the database
           Latitude = Latitude of the pokestop location
           Longitude = Longitude of the pokestop location
           Name = pokestop name in game
        '''
        if ctx.message.channel.id==self.programid or ctx.message.channel.id=="540620184562434048":
            tmpname=""
            tmplat=latitude
            tmplon=longitude
            tmpreg=""
            tmpex=""
            tmpan=""
            tmpsn=""
            tmpcn=""
            for x in self.stopnam:
                if x==name:
                    await self.bot.send_message(ctx.message.channel,"A pokestop with the same name already exists.  Add an additional identifier to make this gym name unique.")
                    return
            tmpcn=name
            msgg="So, you want me to add a pokestop named __**" + name + "**__ to the system:\n"
            msgg+="located at " + latitude + ", " + longitude + ""
            await self.bot.send_message(ctx.message.channel,"Verify the following location with this link:\n" + "https://www.google.com/maps?q=" + latitude + "," + longitude +""+ "")
            msgg+="\nIs this correct (Y/N)?"
            await self.bot.send_message(ctx.message.channel,msgg)
            msgrt = await self.bot.wait_for_message(timeout = 45, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="Y":
                self.stopnam.append(name)
                self.stoplat.append(latitude)
                self.stoplon.append(longitude)
                await subf.addnewstop(self,name,latitude,longitude)
                self.sWL=[];
                for f in self.stopnam+self.cngroup:
                    argg=f.split(" ")
                    for g in argg:
                        argg2=g.split("-")
                        for h in argg2:
                            self.sWL.append(h)
                uniqwords=[]
                for x in self.sWL:
                    if x not in uniqwords:
                        if len(x)>=3:
                            uniqwords.append(x) 
                self.sWL=uniqwords
                scrubbed=[]
                for f in self.sWL: #clean them!
                    Nameval = f.replace(' ', '-').lower()
                    Nameval = Nameval.replace('+', '').lower()
                    Nameval = Nameval.replace('/', '').lower()
                    Nameval = Nameval.replace("'", '').lower()
                    Nameval =Nameval.replace(".", '').lower()
                    scrubbed.append(Nameval )
                self.sWL=scrubbed
                self.sngroup=self.group1sn+self.group2sn+self.group3sn
                self.angroup=self.group1an+self.group2an+self.group3an
                self.cngroup=self.group1cn+self.group2cn+self.group3cn
                self.exgroup=self.group1ex+self.group2ex+self.group3ex
                self.latgroup=self.group1lat+self.group2lat+self.group3lat
                self.longroup=self.group1lon+self.group2lon+self.group3lon
                self.alllat=self.stoplat+self.latgroup
                self.alllon=self.stoplon+self.longroup
                await self.bot.send_message(ctx.message.channel,"I will add the new pokestop to the system.  To ensure changes go through, type `$correct` now")
            else:
                await self.bot.send_message(ctx.message.channel,"I have made no changes.")
                return
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def swapteam(self,ctx,useruu,team):  
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        userm=ctx.message.mentions[0]  #This is a member
        Ranger=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
        MilkMaid=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
        isallowed=0
        server=ctx.message.server
        Valor=discord.utils.get(server.roles, id=self.valor)
        Mystic=discord.utils.get(server.roles, id=self.mystic)
        Instinct=discord.utils.get(server.roles, id=self.instinct)
        if Ranger in f: #ONLY FOR TESTING
            isallowed=1
        if MilkMaid in f:
            isallowed=1
        if isallowed==1:  
            await self.bot.remove_roles(userm,Valor)
            await asyncio.sleep(0.5)
            await self.bot.remove_roles(userm,Instinct)
            await asyncio.sleep(0.5)
            await self.bot.remove_roles(userm,Mystic)
            await asyncio.sleep(0.5)
            teamn=""
            if team.upper()=="INSTINCT" or team.upper()=="I" or team.upper()=="INS":
                teamn="INSTINCT"
                await self.bot.add_roles(userm, Instinct)
                await asyncio.sleep(0.5)
                
            if team.upper()=="MYSTIC" or team.upper()=="M" or team.upper()=="MYS":
                teamn="MYSTIC"
                await self.bot.add_roles(userm, Mystic)
                await asyncio.sleep(0.5)
                
            if team.upper()=="VALOR" or team.upper()=="V" or team.upper()=="VAL":
                teamn=":nauseated_face:"
                await self.bot.add_roles(userm, Valor)
                await asyncio.sleep(0.5)
                
            if teamn=="":
                await self.bot.send_message(ctx.message.channel,"Something went wrong here.")
                return 
            else:
                await self.bot.send_message(ctx.message.channel,userm.mention + " has been changed to team " + teamn)
                return    
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def delstop(self,ctx,*, name : str):
        '''Delete a pokestop from the database
           Name = pokestop name in game
        '''
        if ctx.message.channel.id==self.programid or ctx.message.channel.id=="540620184562434048":
            flagrem=-99
            cntt=0
            for x in self.stopnam:
                if x.upper()==name.upper():
                    flagrem=cntt
                cntt+=1
            if flagrem==-99:
                await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done." )
                return
            
            
            msgg="So, you want me to delete a pokestop named __**" + name + "**__ from the system:\n"
            msgg+="\nIs this correct (Y/N)?"
            await self.bot.send_message(ctx.message.channel,msgg)
            msgrt = await self.bot.wait_for_message(timeout = 45, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="Y":
            
                del self.stopnam[flagrem]
                del self.stoplat[flagrem]
                del self.stoplon[flagrem]
                latitude="0"
                longitude="0"
                await subf.addnewstop(self,name,latitude,longitude)
                self.sWL=[];
                for f in self.stopnam+self.cngroup:
                    argg=f.split(" ")
                    for g in argg:
                        argg2=g.split("-")
                        for h in argg2:
                            self.sWL.append(h)
                uniqwords=[]
                for x in self.sWL:
                    if x not in uniqwords:
                        if len(x)>=3:
                            uniqwords.append(x) 
                self.sWL=uniqwords
                scrubbed=[]
                for f in self.sWL: #clean them!
                    Nameval = f.replace(' ', '-').lower()
                    Nameval = Nameval.replace('+', '').lower()
                    Nameval = Nameval.replace('/', '').lower()
                    Nameval = Nameval.replace("'", '').lower()
                    Nameval =Nameval.replace(".", '').lower()
                    scrubbed.append(Nameval )
                self.sWL=scrubbed
                self.sngroup=self.group1sn+self.group2sn+self.group3sn
                self.angroup=self.group1an+self.group2an+self.group3an
                self.cngroup=self.group1cn+self.group2cn+self.group3cn
                self.exgroup=self.group1ex+self.group2ex+self.group3ex
                self.latgroup=self.group1lat+self.group2lat+self.group3lat
                self.longroup=self.group1lon+self.group2lon+self.group3lon
                self.alllat=self.stoplat+self.latgroup
                self.alllon=self.stoplon+self.longroup
                await self.bot.send_message(ctx.message.channel,"I will delete the pokestop from the system.  To ensure changes go through, type `$correct` now")
            else:
                await self.bot.send_message(ctx.message.channel,"I have made no changes.")
                return
    
    
    @commands.command(pass_context=True)
    async def loadgs(self):
        self.settings = dataIO.load_json("configuration/NewRaidLocas.json")

        self.group1sn=self.settings["group1sn"]
        self.group1an=self.settings["group1an"]
        self.group1cn=self.settings["group1cn"]
        #self.group1ln=self.settings["group1ln"]
        self.group1lat=self.settings["group1lat"]
        self.group1lon=self.settings["group1lon"]
        self.group1ex=self.settings["group1ex"]
        #self.group1nn=self.group1ln
        #self.group1nn[0:len(self.group1nn)]=1
        
        self.group2sn=self.settings["group2sn"]
        self.group2an=self.settings["group2an"]
        self.group2cn=self.settings["group2cn"]
        #self.group2ln=self.settings["group2ln"]
        self.group2lat=self.settings["group2lat"]
        self.group2lon=self.settings["group2lon"]
        self.group2ex=self.settings["group2ex"]
        #self.group2nn=self.group2ln

        
        self.group3sn=self.settings["group3sn"]
        self.group3an=self.settings["group3an"]
        self.group3cn=self.settings["group3cn"]
        #self.group3ln=self.settings["group3ln"]
        self.group3lat=self.settings["group3lat"]
        self.group3lon=self.settings["group3lon"]
        self.group3ex=self.settings["group3ex"]
        #self.group3nn=self.group3ln
        
        #Concatenated groups for looping functions
        self.allraidch=self.g1locaid+self.g2locaid+self.g3locaid+self.L3groupid+self.L4groupid+self.L5groupid+self.PSgroupid+self.mewtwo
        self.alllocch=self.g1locaid+self.g2locaid+self.g3locaid
        self.allrbch=self.L3groupid+self.L4groupid+self.L5groupid+self.PSgroupid
        self.allrbchms=self.L3groupid+self.L4groupid+self.L5groupid
        self.oldchan=self.oL3groupid+self.oL4groupid+self.oL5groupid+self.oPSgroupid
        self.allbutmtch=self.alllocch+self.allrbch
        self.sngroup=self.group1sn+self.group2sn+self.group3sn
        self.angroup=self.group1an+self.group2an+self.group3an
        self.cngroup=self.group1cn+self.group2cn+self.group3cn
        self.exgroup=self.group1ex+self.group2ex+self.group3ex
        #self.lngroup=self.group1ln+self.group2ln+self.group3ln
        self.latgroup=self.group1lat+self.group2lat+self.group3lat
        self.longroup=self.group1lon+self.group2lon+self.group3lon
        
        self.settings = dataIO.load_json("configuration/Stopsfile.json")
        self.stopnam=self.settings["names"]
        self.stoplat=self.settings["Lat"]
        self.stoplon=self.settings["Lon"]
        self.alllat=self.stoplat+self.latgroup
        self.alllon=self.stoplon+self.longroup
        self.sWL=[];
        for f in self.stopnam+self.cngroup:
            argg=f.split(" ")
            for g in argg:
                argg2=g.split("-")
                for h in argg2:
                    self.sWL.append(h)
        uniqwords=[]
        for x in self.sWL:
            if x not in uniqwords:
                if len(x)>=3:
                    uniqwords.append(x) 
        self.sWL=uniqwords
        scrubbed=[]
        for f in self.sWL: #clean them!
            Nameval = f.replace(' ', '-').lower()
            Nameval = Nameval.replace('+', '').lower()
            Nameval = Nameval.replace('/', '').lower()
            Nameval = Nameval.replace("'", '').lower()
            Nameval =Nameval.replace(".", '').lower()
            scrubbed.append(Nameval )
        self.sWL=scrubbed
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def addgym(self,ctx,region,latitude,longitude,exgym,*, name : str):
        '''Add a new gym to the database
           Region = 1 or 2 or 3
           Latitude = Latitude of the gym location
           Longitude = Longitude of the gym location
           exgym = 0/No (if not ex-gym) , 1/Yes (if ex-gym)
           Name = gym name in game
        '''
        if ctx.message.channel.id==self.programid:
            tmpname=""
            tmplat=latitude
            tmplon=longitude
            tmpreg=""
            tmpex=""
            tmpan=""
            tmpsn=""
            tmpcn=""
            for x in self.cngroup:
                if x==name:
                    await self.bot.send_message(ctx.message.channel,"A gym with the same name already exists.  Add an additional identifier to make this gym name unique.")
                    return
            tmpcn=name
            msgg="So, you want me to add __**" + name + "**__ to the system:\n"
            msgg+="A"
            if exgym=="0" or exgym=="No":
                msgg+=" Non-eligible ex-raid gym"
                tmpex="0"
            if exgym=="1" or exgym=="Yes":
                msgg+="n ex-raid eligible gym"
                tmpex="1"
            msgg+=" in "
            msgg+=self.d["Region"+str(int(region)+1)+"name"]
            if region=="2":
                #msgg+="West Lafayette"
                tmpreg="2"
            if region=="3":
                #msgg+="Lafayette"    
                tmpreg="3"
            if region=="1":
                #msgg+="Purdue Campus"
                tmpreg="1"
            #Create a short name and an altname
            tempcn=name
            Nameval = tempcn.replace(' ', '').lower()
            Nameval = Nameval.replace('-', '').lower()
            Nameval = Nameval.replace('+', '').lower()
            Nameval = Nameval.replace('/', '').lower()
            Nameval = Nameval.replace("'", '').lower()
            namev = Nameval.replace(".", '').lower()
            tmpsn=namev[0:8].upper()
            
            while len(tmpsn)<8:
                tmpsn+=" "
            tmpan=tmpsn    
            flagm=[]
            #Ensure a unique altname
            cntt=0
            for x in self.sngroup:
                if x.upper()==tmpsn.upper():
                    flagm.append(cntt)
                cntt+=1
            cgm=len(flagm)
            for y in flagm:
                print(self.cngroup[y])
            if cgm>0:
                tmpan=tmpan[0:7]+str(cgm)
            else:
                junk=1 #Do nothing
            msgg+="\nlocated at " + latitude + ", " + longitude + "\n"
            msgg+="I will give it a short name of " + tmpsn + "\n"
            msgg+="and an alternative name of " + tmpan + "\n"
            await self.bot.send_message(ctx.message.channel,"Verify the following location with this link:\n" + "https://www.google.com/maps?q=" + latitude + "," + longitude +""+ "")
            msgg+="\nIs this correct (Y/N)?"
            await self.bot.send_message(ctx.message.channel,msgg)
            msgrt = await self.bot.wait_for_message(timeout = 45, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="Y":
                #update the arrays gym info based on region
                if tmpreg=="1":
                    self.group1an.append(tmpan)
                    self.group1cn.append(tmpcn)
                    self.group1sn.append(tmpsn)
                    self.group1ex.append(tmpex)
                    self.group1lat.append(tmplat)
                    self.group1lon.append(tmplon)
                if tmpreg=="2":
                    self.group2an.append(tmpan)
                    self.group2cn.append(tmpcn)
                    self.group2sn.append(tmpsn)
                    self.group2ex.append(tmpex)
                    self.group2lat.append(tmplat)
                    self.group2lon.append(tmplon)
                if tmpreg=="3":
                    self.group3an.append(tmpan)
                    self.group3cn.append(tmpcn)
                    self.group3sn.append(tmpsn)
                    self.group3ex.append(tmpex)
                    self.group3lat.append(tmplat)
                    self.group3lon.append(tmplon)    
                #print(self.group2cn)
                #return
                
                await subf.addnewgym(self,name,region,latitude,longitude,exgym)
                self.sWL=[];
                for f in self.stopnam+self.cngroup:
                    argg=f.split(" ")
                    for g in argg:
                        argg2=g.split("-")
                        for h in argg2:
                            self.sWL.append(h)
                uniqwords=[]
                for x in self.sWL:
                    if x not in uniqwords:
                        if len(x)>=3:
                            uniqwords.append(x) 
                self.sWL=uniqwords
                scrubbed=[]
                for f in self.sWL: #clean them!
                    Nameval = f.replace(' ', '-').lower()
                    Nameval = Nameval.replace('+', '').lower()
                    Nameval = Nameval.replace('/', '').lower()
                    Nameval = Nameval.replace("'", '').lower()
                    Nameval =Nameval.replace(".", '').lower()
                    scrubbed.append(Nameval )
                self.sWL=scrubbed
                self.sngroup=self.group1sn+self.group2sn+self.group3sn
                self.angroup=self.group1an+self.group2an+self.group3an
                self.cngroup=self.group1cn+self.group2cn+self.group3cn
                self.exgroup=self.group1ex+self.group2ex+self.group3ex
                #self.lngroup=self.group1ln+self.group2ln+self.group3ln
                self.latgroup=self.group1lat+self.group2lat+self.group3lat
                self.longroup=self.group1lon+self.group2lon+self.group3lon
                self.alllat=self.stoplat+self.latgroup
                self.alllon=self.stoplon+self.longroup
                await self.bot.send_message(ctx.message.channel,"I will add the new gym to the system.  To ensure changes go through, type `$correct` now")
            else:
                await self.bot.send_message(ctx.message.channel,"I have made no changes.")
                return
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def delgym(self,ctx,*, name : str):
        '''Delete a pokestop from the database
           Name = pokestop name in game
        '''
        if ctx.message.channel.id==self.programid or ctx.message.channel.id=="540620184562434048":
            flagrem=-99
            flagrem2=-99
            gprem=-99
            cntt=0
            cntt2=0
            for x in self.cngroup:
                if x.upper()==name.upper():
                    flagrem=cntt
                    
                cntt+=1
            if flagrem==-99:
                await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done. flagrem" )
                return
            cntt2=0
            for y in self.group1cn:
                if y.upper()==self.cngroup[flagrem].upper():
                    gprem=1
                    flagrem2=cntt2
                cntt2+=1
            cntt2=0
            for y in self.group2cn:
                if y.upper()==self.cngroup[flagrem].upper():
                    gprem=2
                    flagrem2=cntt2
                cntt2+=1
            cntt2=0
            for y in self.group3cn:
                if y.upper()==self.cngroup[flagrem].upper():
                    gprem=3
                    flagrem2=cntt2
                cntt2+=1
            if flagrem2==-99:
                await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done. flagrem2" )
                return
            if gprem==-99:
                await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done. gprem" )
                return
            if gprem==1:
                await self.bot.send_message(ctx.message.channel,self.group1cn[flagrem2] + " from Purdue" + str(flagrem2))
            if gprem==2:
                await self.bot.send_message(ctx.message.channel,self.group2cn[flagrem2] + " from West Lafayette" + str(flagrem2))
            if gprem==3:
                await self.bot.send_message(ctx.message.channel,self.group3cn[flagrem2] + " from Lafayette" + str(flagrem2))
            return
            
            msgg="So, you want me to delete a pokestop named __**" + name + "**__ from the system:\n"
            #msgg+="A"
            #if exgym=="0" or exgym=="No":
            #    msgg+=" Non-eligible ex-raid gym"
            #    tmpex="0"
            #if exgym=="1" or exgym=="Yes":
            #    msgg+="n ex-raid eligible gym"
            #    tmpex="1"
            #msgg+=" in "
            #if region=="2" or region=="WL" or region=="West" or region=="West Lafayette":
            #    msgg+="West Lafayette"
            #    tmpreg="2"
            #if region=="3" or region=="L" or region=="Lafayette":
            #    msgg+="Lafayette"    
            #    tmpreg="3"
            #if region=="1" or region=="P" or region=="Purdue" or region=="Purdue Campus":
            #    msgg+="Purdue Campus"
            #    tmpreg="1"
            #Create a short name and an altname
            #tempcn=name
            #Nameval = tempcn.replace(' ', '').lower()
            #Nameval = Nameval.replace('-', '').lower()
            #Nameval = Nameval.replace('+', '').lower()
            #Nameval = Nameval.replace('/', '').lower()
            #Nameval = Nameval.replace("'", '').lower()
            #namev = Nameval.replace(".", '').lower()
            #tmpsn=namev[0:8].upper()
            
            #while len(tmpsn)<8:
            #    tmpsn+=" "
            #tmpan=tmpsn    
            #flagm=[]
            ##Ensure a unique altname
            #cntt=0
            #for x in self.sngroup:
            #    if x.upper()==tmpsn.upper():
            #        flagm.append(cntt)
            #    cntt+=1
            #cgm=len(flagm)
            #for y in flagm:
            #    print(self.cngroup[y])
            #if cgm>0:
            #    tmpan=tmpan[0:7]+str(cgm)
            #else:
            #    junk=1 #Do nothing
            #msgg+="located at " + latitude + ", " + longitude + ""
            #msgg+="I will give it a short name of " + tmpsn + "\n"
            #msgg+="and an alternative name of " + tmpan + "\n"
            #await self.bot.send_message(ctx.message.channel,"Verify the following location with this link:\n" + "https://www.google.com/maps?q=" + latitude + "," + longitude +""+ "")
            msgg+="\nIs this correct (Y/N)?"
            await self.bot.send_message(ctx.message.channel,msgg)
            msgrt = await self.bot.wait_for_message(timeout = 45, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="Y":
            #    #update the arrays gym info based on region
            #    if tmpreg=="1":
            #        self.group1an.append(tmpan)
            #        self.group1cn.append(tmpcn)
            #        self.group1sn.append(tmpsn)
            #        self.group1ex.append(tmpex)
            #        self.group1lat.append(tmplat)
            #        self.group1lon.append(tmplon)
            #    if tmpreg=="2":
            #        self.group2an.append(tmpan)
            #        self.group2cn.append(tmpcn)
            #        self.group2sn.append(tmpsn)
            #        self.group2ex.append(tmpex)
            #        self.group2lat.append(tmplat)
            #        self.group2lon.append(tmplon)
            #    if tmpreg=="3":
            #        self.group3an.append(tmpan)
            #        self.group3cn.append(tmpcn)
            #        self.group3sn.append(tmpsn)
            #        self.group3ex.append(tmpex)
            #        self.group3lat.append(tmplat)
            #        self.group3lon.append(tmplon)    
            #    #print(self.group2cn)
            #    #return
            #    
                #update the arrays gym info based on region
                if tmpreg=="1":
                    #del self.group1an.append(tmpan)
                    self.group1cn.append(tmpcn)
                    self.group1sn.append(tmpsn)
                    self.group1ex.append(tmpex)
                    self.group1lat.append(tmplat)
                    self.group1lon.append(tmplon)
                if tmpreg=="2":
                    self.group2an.append(tmpan)
                    self.group2cn.append(tmpcn)
                    self.group2sn.append(tmpsn)
                    self.group2ex.append(tmpex)
                    self.group2lat.append(tmplat)
                    self.group2lon.append(tmplon)
                if tmpreg=="3":
                    self.group3an.append(tmpan)
                    self.group3cn.append(tmpcn)
                    self.group3sn.append(tmpsn)
                    self.group3ex.append(tmpex)
                    self.group3lat.append(tmplat)
                    self.group3lon.append(tmplon)    
                del self.stopnam[flagrem]
                del self.stoplat[flagrem]
                del self.stoplon[flagrem]
                #self.stopnam.append(name)
                #self.stoplat.append(latitude)
                #self.stoplon.append(longitude)
                latitude="0"
                longitude="0"
                await subf.addnewstop(self,name,latitude,longitude)
                self.sWL=[];
                for f in self.stopnam+self.cngroup:
                    argg=f.split(" ")
                    for g in argg:
                        argg2=g.split("-")
                        for h in argg2:
                            self.sWL.append(h)
                uniqwords=[]
                for x in self.sWL:
                    if x not in uniqwords:
                        if len(x)>=3:
                            uniqwords.append(x) 
                self.sWL=uniqwords
                scrubbed=[]
                for f in self.sWL: #clean them!
                    Nameval = f.replace(' ', '-').lower()
                    Nameval = Nameval.replace('+', '').lower()
                    Nameval = Nameval.replace('/', '').lower()
                    Nameval = Nameval.replace("'", '').lower()
                    Nameval =Nameval.replace(".", '').lower()
                    scrubbed.append(Nameval )
                self.sWL=scrubbed
                self.sngroup=self.group1sn+self.group2sn+self.group3sn
                self.angroup=self.group1an+self.group2an+self.group3an
                self.cngroup=self.group1cn+self.group2cn+self.group3cn
                self.exgroup=self.group1ex+self.group2ex+self.group3ex
                #self.lngroup=self.group1ln+self.group2ln+self.group3ln
                self.latgroup=self.group1lat+self.group2lat+self.group3lat
                self.longroup=self.group1lon+self.group2lon+self.group3lon
                self.alllat=self.stoplat+self.latgroup
                self.alllon=self.stoplon+self.longroup
                await self.bot.send_message(ctx.message.channel,"I will delete the pokestop from the system.  To ensure changes go through, type `$correct` now")
            else:
                await self.bot.send_message(ctx.message.channel,"I have made no changes.")
                return
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def addboss(self,ctx,type,name,maxcp,levelsum,rolev):
        if ctx.message.channel.id==self.programid:
            maxspace=14
            txt=""
            
            if type.upper()=="4" or type.upper()=="L4" or type.upper()=="Level4":
                temptype=self.L4types
                tempmaxCP=self.L4maxCP
                tempnotid=self.L4notid
                tempslope=self.L4slope
                tempoffset=self.L4offset
                tempemoji=self.L4emoji
                temppeeps=self.L4peeps
                errored=0
                try:
                    temptype.append(name.upper())
                except:
                    errored=1
                
                try:
                    tempmaxCP.append(int(maxcp))
                except:
                    errored=1
                
                try:
                    tid=re.sub("[^0-9]", "", rolev)
                    tempnotid.append(tid)
                    print (tid + "Hi")
                except:
                    errored=1
                
                try:
                    tempoffset.append(int(levelsum))
                except:
                    errored=1
                
                try:
                    #print(emoji)
                    #print(emoji.name)
                    tempemoji.append("<:item_pokeball:284615009299070976>")
                except:
                    errored=1
                
                try:
                    tempslope.append(15)
                    temppeeps.append(4)
                except:
                    errored=1
                    
                if errored==1:
                    await self.bot.send_message(ctx.message.channel,"__**I just ran into an error**__" )
                    return
                
                self.L4types=temptype
                self.L4maxCP=tempmaxCP
                self.L4notid=tempnotid
                self.L4slope=tempslope
                self.L4offset=tempoffset
                self.L4emoji=tempemoji
                self.L4peeps=temppeeps
                
                await subf.L4bosswrite(self)
                
                for x in range(0,len(self.L4types)):
                    rr2=None
                    lname=len(self.L4types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L4notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L4types[x].ljust(maxspace) + "-" + str(self.L4maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L4types[x].ljust(maxspace) + "-" + str(self.L4maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 4 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
                    
            if type.upper()=="5" or type.upper()=="L5" or type.upper()=="Level5":
                temptype=self.L5types
                tempmaxCP=self.L5maxCP
                tempnotid=self.L5notid
                tempslope=self.L5slope
                tempoffset=self.L5offset
                tempemoji=self.L5emoji
                temppeeps=self.L5peeps
                errored=0
                try:
                    temptype.append(name.upper())
                except:
                    errored=1
                
                try:
                    tempmaxCP.append(int(maxcp))
                except:
                    errored=1
                
                try:
                    tid=re.sub("[^0-9]", "", rolev)
                    tempnotid.append(tid)
                    print (tid + "Hi")
                except:
                    errored=1
                
                try:
                    tempoffset.append(int(levelsum))
                except:
                    errored=1
                
                try:
                    #print(emoji)
                    #print(emoji.name)
                    tempemoji.append("<:item_pokeball:284615009299070976>")
                except:
                    errored=1
                
                try:
                    tempslope.append(15)
                    temppeeps.append(4)
                except:
                    errored=1
                    
                if errored==1:
                    await self.bot.send_message(ctx.message.channel,"__**I just ran into an error**__" )
                    return
                
                self.L5types=temptype
                self.L5maxCP=tempmaxCP
                self.L5notid=tempnotid
                self.L5slope=tempslope
                self.L5offset=tempoffset
                self.L5emoji=tempemoji
                self.L5peeps=temppeeps
                
                await subf.L5bosswrite(self)
                
                for x in range(0,len(self.L5types)):
                    rr2=None
                    lname=len(self.L5types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L5notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L5types[x].ljust(maxspace) + "-" + str(self.L5maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L5types[x].ljust(maxspace) + "-" + str(self.L5maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 5 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="3" or type.upper()=="L3" or type.upper()=="Level3":
                temptype=self.L3types
                tempmaxCP=self.L3maxCP
                tempnotid=self.L3notid
                tempslope=self.L3slope
                tempoffset=self.L3offset
                tempemoji=self.L3emoji
                temppeeps=self.L3peeps
                errored=0
                try:
                    temptype.append(name.upper())
                except:
                    errored=1
                
                try:
                    tempmaxCP.append(int(maxcp))
                except:
                    errored=1
                
                try:
                    tid=re.sub("[^0-9]", "", rolev)
                    tempnotid.append(tid)
                    print (tid + "Hi")
                except:
                    errored=1
                
                try:
                    tempoffset.append(int(levelsum))
                except:
                    errored=1
                
                try:
                    #print(emoji)
                    #print(emoji.name)
                    tempemoji.append("<:item_pokeball:284615009299070976>")
                except:
                    errored=1
                
                try:
                    tempslope.append(15)
                    temppeeps.append(4)
                except:
                    errored=1
                    
                if errored==1:
                    await self.bot.send_message(ctx.message.channel,"__**I just ran into an error**__" )
                    return
                
                self.L3types=temptype
                self.L3maxCP=tempmaxCP
                self.L3notid=tempnotid
                self.L3slope=tempslope
                self.L3offset=tempoffset
                self.L3emoji=tempemoji
                self.L3peeps=temppeeps
                
                await subf.L3bosswrite(self)
                
                for x in range(0,len(self.L3types)):
                    rr2=None
                    lname=len(self.L3types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L3notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L3types[x].ljust(maxspace) + "-" + str(self.L3maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L3types[x].ljust(maxspace) + "-" + str(self.L3maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 3 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="OI" or type.upper()=="Interest" or type.upper()=="OfInterest":
                temptype=self.OItypes
                tempmaxCP=self.OImaxCP
                tempnotid=self.OInotid
                tempslope=self.OIslope
                tempoffset=self.OIoffset
                tempemoji=self.OIemoji
                temppeeps=self.OIpeeps
                errored=0
                try:
                    temptype.append(name.upper())
                except:
                    errored=1
                
                try:
                    tempmaxCP.append(int(maxcp))
                except:
                    errored=1
                
                try:
                    tid=re.sub("[^0-9]", "", rolev)
                    tempnotid.append(tid)
                    print (tid + "Hi")
                except:
                    errored=1
                
                try:
                    tempoffset.append(int(levelsum))
                except:
                    errored=1
                
                try:
                    #print(emoji)
                    #print(emoji.name)
                    tempemoji.append("<:item_pokeball:284615009299070976>")
                except:
                    errored=1
                
                try:
                    tempslope.append(15)
                    temppeeps.append(4)
                except:
                    errored=1
                    
                if errored==1:
                    await self.bot.send_message(ctx.message.channel,"__**I just ran into an error**__" )
                    return
                
                self.OItypes=temptype
                self.OImaxCP=tempmaxCP
                self.OInotid=tempnotid
                self.OIslope=tempslope
                self.OIoffset=tempoffset
                self.OIemoji=tempemoji
                self.OIpeeps=temppeeps
                
                await subf.OIbosswrite(self)
                for x in range(0,len(self.OItypes)):
                    rr2=None
                    lname=len(self.OItypes[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.OInotid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.OItypes[x].ljust(maxspace) + "-" + str(self.OImaxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.OItypes[x].ljust(maxspace) + "-" + str(self.OImaxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are Of Interest bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
                
            if type.upper()=="PS" or type.upper()=="Shiny" or type.upper()=="PossibleShiny":
                temptype=self.PStypes
                tempmaxCP=self.PSmaxCP
                tempnotid=self.PSnotid
                tempslope=self.PSslope
                tempoffset=self.PSoffset
                tempemoji=self.PSemoji
                temppeeps=self.PSpeeps
                errored=0
                try:
                    temptype.append(name.upper())
                except:
                    errored=1
                
                try:
                    tempmaxCP.append(int(maxcp))
                except:
                    errored=1
                
                try:
                    tid=re.sub("[^0-9]", "", rolev)
                    tempnotid.append(tid)
                    print (tid + "Hi")
                except:
                    errored=1
                
                try:
                    tempoffset.append(int(levelsum))
                except:
                    errored=1
                
                try:
                    #print(emoji)
                    #print(emoji.name)
                    tempemoji.append("<:item_pokeball:284615009299070976>")
                except:
                    errored=1
                
                try:
                    tempslope.append(15)
                    temppeeps.append(4)
                except:
                    errored=1
                    
                if errored==1:
                    await self.bot.send_message(ctx.message.channel,"__**I just ran into an error**__" )
                    return
                
                self.PStypes=temptype
                self.PSmaxCP=tempmaxCP
                self.PSnotid=tempnotid
                self.PSslope=tempslope
                self.PSoffset=tempoffset
                self.PSemoji=tempemoji
                self.PSpeeps=temppeeps
                
                await subf.PSbosswrite(self)
                for x in range(0,len(self.PStypes)):
                    rr2=None
                    lname=len(self.PStypes[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.PSnotid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.PStypes[x].ljust(maxspace) + "-" + str(self.PSmaxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.PStypes[x].ljust(maxspace) + "-" + str(self.PSmaxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are Possible Shiny bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
    
    @commands.command(pass_context=True)
    async def exwrite(self):
        await subf.exraidwrite(self)
    
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def delboss(self,ctx,type,name):
        if ctx.message.channel.id==self.programid:
            maxspace=14
            txt=""
            
            if type.upper()=="4" or type.upper()=="L4" or type.upper()=="Level4":
                
                #find index of pokemon
                cntt=0
                flagrem=-99
                for x in self.L4types:
                    if x.upper()==name.upper():
                        flagrem=cntt
                    cntt+=1
                if flagrem==-99:
                    await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done." )
                    return
                if flagrem==0:
                    await self.bot.send_message(ctx.message.channel,"I can't delete the category title.  Nothing will be done." )
                    return
                del self.L4types[flagrem]
                del self.L4maxCP[flagrem]
                del self.L4notid[flagrem]
                del self.L4slope[flagrem]
                del self.L4offset[flagrem]
                del self.L4emoji[flagrem]
                del self.L4peeps[flagrem]
                
                await subf.L4bosswrite(self)
                
                for x in range(0,len(self.L4types)):
                    rr2=None
                    lname=len(self.L4types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L4notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L4types[x].ljust(maxspace) + "-" + str(self.L4maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L4types[x].ljust(maxspace) + "-" + str(self.L4maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 4 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
                    
            if type.upper()=="5" or type.upper()=="L5" or type.upper()=="Level5":
                #find index of pokemon
                cntt=0
                flagrem=-99
                for x in self.L5types:
                    if x.upper()==name.upper():
                        flagrem=cntt
                    cntt+=1
                if flagrem==-99:
                    await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done." )
                    return
                if flagrem==0:
                    await self.bot.send_message(ctx.message.channel,"I can't delete the category title.  Nothing will be done." )
                    return
                del self.L5types[flagrem]
                del self.L5maxCP[flagrem]
                del self.L5notid[flagrem]
                del self.L5slope[flagrem]
                del self.L5offset[flagrem]
                del self.L5emoji[flagrem]
                del self.L5peeps[flagrem]
                
                await subf.L5bosswrite(self)
                
                for x in range(0,len(self.L5types)):
                    rr2=None
                    lname=len(self.L5types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L5notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L5types[x].ljust(maxspace) + "-" + str(self.L5maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L5types[x].ljust(maxspace) + "-" + str(self.L5maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 5 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="3" or type.upper()=="L3" or type.upper()=="Level3":
                #find index of pokemon
                cntt=0
                flagrem=-99
                for x in self.L3types:
                    if x.upper()==name.upper():
                        flagrem=cntt
                    cntt+=1
                if flagrem==-99:
                    await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done." )
                    return
                if flagrem==0:
                    await self.bot.send_message(ctx.message.channel,"I can't delete the category title.  Nothing will be done." )
                    return
                del self.L3types[flagrem]
                del self.L3maxCP[flagrem]
                del self.L3notid[flagrem]
                del self.L3slope[flagrem]
                del self.L3offset[flagrem]
                del self.L3emoji[flagrem]
                del self.L3peeps[flagrem]
                
                await subf.L3bosswrite(self)
                
                for x in range(0,len(self.L3types)):
                    rr2=None
                    lname=len(self.L3types[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.L3notid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.L3types[x].ljust(maxspace) + "-" + str(self.L3maxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.L3types[x].ljust(maxspace) + "-" + str(self.L3maxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are level 3 bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="OI" or type.upper()=="Interest" or type.upper()=="OfInterest":
                #find index of pokemon
                cntt=0
                flagrem=-99
                for x in self.OItypes:
                    if x.upper()==name.upper():
                        flagrem=cntt
                    cntt+=1
                if flagrem==-99:
                    await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done." )
                    return
                if flagrem==0:
                    await self.bot.send_message(ctx.message.channel,"I can't delete the category title.  Nothing will be done." )
                    return
                del self.OItypes[flagrem]
                del self.OImaxCP[flagrem]
                del self.OInotid[flagrem]
                del self.OIslope[flagrem]
                del self.OIoffset[flagrem]
                del self.OIemoji[flagrem]
                del self.OIpeeps[flagrem]
                
                await subf.OIbosswrite(self)
                for x in range(0,len(self.OItypes)):
                    rr2=None
                    lname=len(self.OItypes[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.OInotid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.OItypes[x].ljust(maxspace) + "-" + str(self.OImaxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.OItypes[x].ljust(maxspace) + "-" + str(self.OImaxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are Of Interest bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
            if type.upper()=="PS" or type.upper()=="Shiny" or type.upper()=="PossibleShiny":
                #find index of pokemon
                cntt=0
                flagrem=-99
                for x in self.PStypes:
                    if x.upper()==name.upper():
                        flagrem=cntt
                    cntt+=1
                if flagrem==-99:
                    await self.bot.send_message(ctx.message.channel,"I couldn't find that one.  Nothing will be done." )
                    return
                if flagrem==0:
                    await self.bot.send_message(ctx.message.channel,"I can't delete the category title.  Nothing will be done." )
                    return
                del self.PStypes[flagrem]
                del self.PSmaxCP[flagrem]
                del self.PSnotid[flagrem]
                del self.PSslope[flagrem]
                del self.PSoffset[flagrem]
                del self.PSemoji[flagrem]
                del self.PSpeeps[flagrem]
                
                await subf.PSbosswrite(self)
                for x in range(0,len(self.PStypes)):
                    rr2=None
                    lname=len(self.PStypes[x])
                    try:
                        #'{0:{fill}{align}16}'.format(text, fill=align, align=align)
                        rr2=discord.utils.get(ctx.message.channel.server.roles, id=self.PSnotid[x])
                        #txt += "`" + textwrap.fill(self.L4types[x], 16) + "`" + "    " + str(self.L4maxCP[x]) + "    " + rr2.mention + "\n"
                        
                        txt += "`" + self.PStypes[x].ljust(maxspace) + "-" + str(self.PSmaxCP[x]).ljust(7) + "-`" + rr2.mention + "\n"
                    except:
                        #role not found
                        txt += "`" + self.PStypes[x].ljust(maxspace) + "-" + str(self.PSmaxCP[x]).ljust(7) + "-" + "No role`" + "\n"
                await self.bot.send_message(ctx.message.channel,"__**Here are Possible Shiny bosses:**__" )
                await self.bot.send_message(ctx.message.channel,"" + txt + "")
    
    #Print a list of the shiny pokemon for quests in the programming channel
    @checks.admin()  
    @commands.command(pass_context=True)
    async def getshiny(self,ctx):
        if ctx.message.channel.id==self.programid:
            await self.bot.send_message(ctx.message.channel,self.shinylist) 
    
    #Update the shiny list by adding a pokemon
    #Ready for publication
    @checks.admin()   #Only admins have the power
    @commands.command(pass_context=True)
    async def addshiny(self,ctx,pokemon):
        if ctx.message.channel.id==self.programid:
            try:
                self.shinylist.append(pokemon.upper())
                await self.bot.send_message(ctx.message.channel,self.shinylist)             
                await subf.shinywrite(self)
            except:
                await self.bot.send_message(ctx.message.channel,"Error: Something went wrong!") 
    
    #Update the shiny list by deleting a pokemon
    #Ready for publication
    @checks.admin()   #Only admins have the power  
    @commands.command(pass_context=True)
    async def delshiny(self,ctx,pokemon):
        if ctx.message.channel.id==self.programid:
            try:
                self.shinylist.remove(pokemon.upper())
                await self.bot.send_message(ctx.message.channel,self.shinylist) 
                await subf.shinywrite(self)
            except:
                await self.bot.send_message(ctx.message.channel,"Error: Something went wrong!") 
    
    #Calculate the level for a given pokemon given IVs
    #Ready for publication
    @commands.command(pass_context=True)
    async def pokedex(self,ctx,pokename="Junk",levelval=1.0,attIV=15,defeIV=15,stamIV=15):
        if not (ctx.message.channel.id==self.setupch): #Only allow in the setup channel
            await self.bot.delete_message(ctx.message)
            return
        if (pokename=="Junk"):
            await self.bot.send_message(ctx.message.channel,"Here's how to use this:\n%pokedex pokemon_name level attackIV defenseIV staminaIV\n\n__**Example:**__  %pokedex Metagross 25 15 15 8")
        #pokename,hp,att,defense):
        attIV=float(attIV)
        defeIV=float(defeIV)
        stamIV=float(stamIV)
        level=float(levelval)
        nument=len(self.Basestats.index)
        numlev=len(self.CPM.index)
        nameval=""
        type2=""
        for x in range(0,nument):
            if (self.Basestats.iloc[x,1].upper()==pokename.upper()):
                print(self.Basestats.iloc[x,1])
                nameval=self.Basestats.iloc[x,1]
                pokenum=self.Basestats.iloc[x,0]
                att=self.Basestats.iloc[x,2]
                defe=self.Basestats.iloc[x,3]
                stam=self.Basestats.iloc[x,4]
                type1=self.Basestats.iloc[x,5]
                type2=self.Basestats.iloc[x,6]
                
                levnum=int(math.floor(float(level)*2.0))
                if levnum<0:
                    levnum=0
                CPmult=self.CPM.iloc[levnum-2,1]
                CPlev=self.CPM.iloc[levnum-2,0]
                
                CPvalu=math.floor((att+attIV) * (math.pow((defe+defeIV),0.5) * math.pow((stam+stamIV),0.5) * math.pow(CPmult,2.0)) / 10.0)
                break
        if not nameval=="":
            if not type2=="":
                typetext="\nPokemon Types:" + type1 + "/" +type2
            else:
                typetext="\nPokemon Type:" + type1
            #if 
            addltxt="\n IVs provided (Att/Def/HP):" + str(int(attIV)) + "/"+ str(int(defeIV)) + "/"+ str(int(stamIV)) + "\nCP:" + str(CPvalu) +" at level " + str(CPlev)
            CPm40=self.CPM.iloc[numlev-1,1]
            CPv40=math.floor((att+attIV) * (math.pow((defe+defeIV),0.5) * math.pow((stam+stamIV),0.5) * math.pow(CPm40,2.0)) / 10.0)
            maxl1500=1
            maxl2500=1
            for x in range(0,numlev):
                templev=self.CPM.iloc[x,0]
                tempmult=self.CPM.iloc[x,1]
                CPcal=math.floor((att+attIV) * (math.pow((defe+defeIV),0.5) * math.pow((stam+stamIV),0.5) * math.pow(tempmult,2.0)) / 10.0)
                if CPcal<1500:
                    maxl1500=templev
                if CPcal<2500:
                    maxl2500=templev
            addltxt2="\nMax level for <1500CP:" + str(maxl1500) + "\nMax level for <2500CP:" + str(maxl2500) 
            await self.bot.send_message(ctx.message.channel,"Heres the info you wanted on " + pokename + "\nPokemon: " + str(pokenum) +" - " +nameval + "\nBase Attack:" + str(att) + "\nBase Defense:" + str(defe)+ "\nBase Stamina:" + str(stam) + typetext + addltxt + addltxt2)
    
    #Use this function to create text files for each user with their currently assigned roles
    #Ready for publication
    @checks.is_owner() #Only allow an owner to do this
    @commands.command(pass_context=True)
    async def graballproles(self,ctx):
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        for y in server.members:
            member=discord.Server.get_member(server,y.id)
            with open('Roles_files' + "\\"+ member.id + ".txt","w") as g:
                txt=unidecode(str(member.name))
                print(txt,file=g)
            for x in member.roles:
                print(x.name)
                with open('Roles_files' + "\\"+ member.id + ".txt","a") as g:
                    print(x.name,file=g)

                    
    @commands.command(pass_context=True)
    async def resetraids(self,ctx):
        #await self.bot.delete_message(ctx.message)
        self.lastraid=datetime.utcnow()+timedelta(hours=self.timez)
            
    @commands.command(pass_context=True)
    async def writeme(self,ctx):        
        txt='{\n'
        for f in range(0,12):
            txt+='"mtch' +  str(f+1) + 'id":['
            print(("self.mtch" + str(f+1) + "id"))
            exec("self.junk=self.mtch" + str(f+1) + "id")
            print(self.junk)
            if len(self.junk)>0:
                for g in self.junk:
                    txt+='"' + g + '",'
                txt=txt[:-1]
            else:
                txt+='""'
            txt+='],\n'
        txt=txt[:-2]
        txt+='\n}'
        file = open("configuration/exraid.txt","w",encoding='utf-8') 
        file.write(txt)          
        file.close()    
    
    @commands.command(pass_context=True)
    async def readme(self,ctx):        
        stuff = dataIO.load_json("configuration/exraid.txt")
        self.mtch1id=stuff["mtch1id"]
        self.mtch2id=stuff["mtch2id"]
        self.mtch3id=stuff["mtch3id"]
        self.mtch4id=stuff["mtch4id"]
        self.mtch5id=stuff["mtch5id"]
        self.mtch6id=stuff["mtch6id"]
        self.mtch7id=stuff["mtch7id"]
        self.mtch8id=stuff["mtch8id"]
        self.mtch9id=stuff["mtch9id"]
        self.mtch10id=stuff["mtch10id"]
        self.mtch11id=stuff["mtch11id"]
        self.mtch12id=stuff["mtch12id"]
     
    #Clears the quest channel each day and resets the raid timer (until the fix is implemented)
    #Ready for publication
    @checks.admin()  #Only bot admins can run this comamnd
    @commands.command(pass_context=True)
    async def questicles(self,ctx):
        self.lastraid=datetime.utcnow()+timedelta(hours=self.timez)
        server=ctx.message.server
        ch=ctx.message.channel
        b=discord.Server.get_member(ctx.message.server,self.botid)
        mess=b.mention
        c=self.bot.get_channel(self.raidsightings)
        mess2=c.mention
        if not ch.id==self.questsightings:
            return
        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 5000 messages in the channel 
                await self.bot.delete_message(message)
        await self.bot.send_message(ch,"Use this channel to post sightings for quests.  You may either enter the quest manually here, enter them in " + mess2 +" or DM "+mess+ " the `%quest` command.  To find quests by reward (for quests entered via DM) use `%findquest *reward*`. \n")
        Questrole=discord.utils.get(server.roles, id=self.questmaster) #People who have found cool quests will be reset now
        for yy in ctx.message.server.members:
            if Questrole in yy.roles:
                await self.bot.remove_roles(yy,Questrole)
                print(yy.name)
        
    #Do we need this
    @commands.command(pass_context=True)
    async def delCD(self,ctx):
        if not ctx.message.author.id==self.CMK:
            await self.bot.send_message(ctx.message.channel,"NOT STINKPOT")
            return
        if not ctx.message.channel.id=="463433170784878592":
            await self.bot.send_message(ctx.message.channel,"INCORRECT CHANNEL")
            return
        #await self.bot.send_message(ctx.message.channel,"Would delete this.")
        async for message in self.bot.logs_from(ctx.message.channel, limit=100): #Gets a list of the last 500 messages in the channel     
            await self.bot.delete_message(message)
    
    
    @commands.command(pass_context=True)
    async def findquest(self,ctx,*,keywords:str=""):
        try:
            await self.bot.delete_message(ctx.message)
        except:
            a=1
        if keywords=="":
            await self.bot.send_message(ctx.message.author,"Type `%findquest *reward*` for me to perform a search for you.")
            return
            alltimeout=30
            await self.bot.send_message(ctx.message.channel,"What reward are you searching for?\n`1) Stardust    \n2) Rare Candy \n3) Encounter  `")
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            rewardn=msgrt.content
            return
        else: #We need to parse this out and try finding what it is
            indkey=keywords.split(" ")
            fndval=0
            rewardc=0
            dustc=0
            encc=0
            encm=[]
            dustm=[]
            rewardm=[]
            for x in indkey:
                #try finding a reward type
                for y in self.reward:
                    if x.upper() in y.upper():
                        #This is the reward
                        fndval+=1
                        rewardc+=1
                        rewardm.append(y.upper())
                for y in self.dust:
                    if x.upper() in y.upper():
                        #This is an amount of dust
                        fndval+=1
                        dustc+=1
                        dustm.append(y.upper())
                for y in self.encounters:
                    if x.upper() in y.upper():
                        #This is an encounter
                        fndval+=1
                        encc+=1
                        encm.append(y.upper())
                    
            if fndval==0:
                await self.bot.send_message(ctx.message.author,"I didn't find anything for you. Encourage trainers to share info about their quests!")
                return
            else:
                #await self.bot.send_message(ctx.message.channel,"I'm searching for some quests!")
                print(str(rewardc)+str(dustc)+str(encc))
                msgout="Here is what I found:\n"
                
                with open("quests.txt","r") as fr:
                    for line in fr:
                        t = line
                        cntt=0
                        for x in t.split(' ~ '):
                            if cntt==0: #pokestop location
                                stopnum=int(x)
                            elif cntt==1: #Trainer name
                                skip=1
                            elif cntt==2: #date/time
                                datestuff=x
                            elif cntt==3: #reward
                                reward=x.upper()
                            elif cntt==4: #quest
                                quest=x.upper()
                            cntt+=1
                            #now see if the reward is in the line
                        #print(datestuff)
                        hatpolltime = datetime.utcnow()+timedelta(hours=self.timez)
                        hatpolltime=hatpolltime.strftime("%Y-%m-%d")
                        hatdeltat = datetime.strptime(hatpolltime, "%Y-%m-%d")-datetime.strptime(datestuff, ('%Y-%m-%d %H:%M:%S.%f'))
                        
                        #print(hatdeltat.days)
                        #print(hatpolltime)
                        if hatdeltat.days<0:
                            timestt=str(datetime.utcnow()+timedelta(hours=self.timez))
                            
                            for y in rewardm:
                                #print (y + " " + reward)
                                if y in reward:
                                    msgout+="" + reward + " at " + self.stopnam[stopnum] + " via " + quest + "\n"
                                    print("" + reward + " at " + self.stopnam[stopnum])
                            for y in dustm:
                                #print (y + " " + reward)
                                if y in reward:
                                    msgout+="" + reward + " at " + self.stopnam[stopnum] + " via " + quest +"\n"
                                    print("" + reward + " at " + self.stopnam[stopnum])
                            for y in encm:
                                #print (y + " " + reward)
                                if y in reward:
                                    msgout+="" + reward + " at " + self.stopnam[stopnum] + " via " + quest +"\n"
                                    print("" + reward + " at " + self.stopnam[stopnum])
                if len(msgout)>1980:
                    msgout=msgout[0:1979]
                print(len(msgout))
                if len(msgout)==22:
                    msgout+="Nothing :("
                else:
                    msgout+=""
                await self.bot.send_message(ctx.message.author,msgout)
                return
    
    
    @commands.command(pass_context=True)
    async def changename(self,ctx,oldname,newname):
        #need to change RT, Shadows, old RT_data
        uname=oldname
        uname=uname+str(ctx.message.author.discriminator)
        for filename in os.listdir("."):
            if filename.startswith(uname):
                a=1
                #os.rename(filename, filename[7:])
        #df = pd.read_excel('ExcelFiles' + "\\" + uname + 'level.xlsx')
    
    #Update permissions to the exraid channels (This will be removed in future releases)
    #rework for dictionary usage
    @checks.admin()  #Only allow admins to run this
    @commands.command(pass_context=True)
    async def recache(self,ctx):  #rebuild
        await self.bot.delete_message(ctx.message)
        ch=ctx.message.channel
        async for message in self.bot.logs_from(ch, limit=100): #Gets a list of the last 500 messages in the channel 
            tmess=message
            if message.id in self.mtch1id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[0])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role) 
            if message.id in self.mtch2id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[1])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch3id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[2])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch4id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[3])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch5id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[4])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch6id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[5])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch7id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[6])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch8id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[7])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch9id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[8])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch10id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[9])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch11id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[10])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)
            if message.id in self.mtch12id:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                    role=discord.utils.get(tmess.server.roles, id=self.exroles[11])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if not role in member.roles:
                            await self.bot.add_roles(member,role)                

    
    #Create a silly pokemon haiku
    #No restriction
    #Ready for publication
    @commands.command(pass_context=True)
    async def haiku(self,ctx):  
        wordList1 = ["Pikachu", "Bulbasaur", "Ash Ketchum", "Celebi"]
        wordList2 = ["catches", "chuckles", "battles", "does raids"]
        wordList3 = ["pokeballs", "max revives", "ultra balls", "item space", "poke stops","Niantic"]
        wordList4 = ["showing", "award", "provide", "spinning","walking"]
        wordList5 = ["glory","rebirth", "items","healing","with death","buddy"]
        wordList6 = ["unstoppable", "maybe hatched more", "gotta catch them"]
        wordList7 = ["pow'r", "death", "bird", "eggs"]
                
        wordIndex1=randint(0, len(wordList1)-1)
        wordIndex2=randint(0, len(wordList2)-1)
        wordIndex3=randint(0, len(wordList3)-1)
        wordIndex4=randint(0, len(wordList4)-1)
        wordIndex5=randint(0, len(wordList5)-1)
        wordIndex6=randint(0, len(wordList6)-1)
        wordIndex7=randint(0, len(wordList7)-1)

        haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n" 
        haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
        haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

        await self.bot.send_message(ctx.message.channel,haiku)
    
    
    #Clears a given ex-raid channel (MewTwoclear)
    
    @checks.admin()  #Only allow admins to run this functions
    @commands.command(pass_context=True)
    async def mtclear(self,ctx,rn):  #rebuild
        await self.bot.delete_message(ctx.message)
        ch=ctx.message.channel
        rn=int(rn)-1
        if ch.id==self.exchan[rn]:
            role=discord.utils.get(ctx.message.server.roles, id=self.exroles[rn])
            for user in ctx.message.server.members:
                if not user.display_name=="MrMasterMiltank":
                    if role in user.roles:
                        await self.bot.remove_roles(user,role)
                        print(user.name)
            async for message in self.bot.logs_from(ch, limit=1000):
                tmess=message
                await self.bot.delete_message(tmess)
            await self.bot.edit_channel(ch,name="channel-"+str(rn+1))
            exec("self.mtch" + str(rn+1) + "id=[]")
        await subf.exraidwrite(self)  #Use the help function
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def mtrolecall(self,ctx,rn,msgid=""):  #rebuild
        
        await self.bot.delete_message(ctx.message)
        ch=ctx.message.channel
        rn=int(rn)-1
        inst=""
        myst=""
        valo=""
        inst2=""
        myst2=""
        valo2=""
        Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
        Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
        Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
        vallist=[]
        myslist=[]
        inslist=[]
        val2list=[]
        mys2list=[]
        ins2list=[]
        
        role=discord.utils.get(ctx.message.server.roles, id=self.exroles[rn])
        for user in ctx.message.server.members:
            if not user.display_name=="MrMasterMiltank":
                if role in user.roles:
                    #print(user.name)
                    if Valor in user.roles:
                        vallist.append(user.display_name)
                    if Mystic in user.roles:
                        myslist.append(user.display_name)
                    if Instinct in user.roles:
                        inslist.append(user.display_name)
        chx=self.bot.get_channel("362698126248771604")
        async for message in self.bot.logs_from(chx, limit=500): #Gets a list of the last 500 messages in the channel 
            if message.id == msgid:
                for xi in range(0,len(message.reactions)): 
                    useri = await self.bot.get_reaction_users([x for x in message.reactions][xi])
                    role=discord.utils.get(message.server.roles, id=self.exroles[1])
                    for user in useri:
                        member = discord.utils.get(message.server.members, id=user.id)
                        if Valor in member.roles:
                            val2list.append(member.display_name)
                        if Mystic in member.roles:
                            mys2list.append(member.display_name)
                        if Instinct in member.roles:
                            ins2list.append(member.display_name)
        
        for g in inslist:
            if g in ins2list:
                inslist.remove(g)
        for g in myslist:
            if g in mys2list:
                myslist.remove(g)        
        for g in vallist:
            if g in val2list:
                vallist.remove(g)
        print(inslist)
        print(ins2list)
        
        for g in inslist:
            inst+= g + "\n"
        for g in myslist:
            myst+= g + "\n"
        for g in vallist:
            valo+= g + "\n"
        for g in ins2list:
            inst2+= g + "\n"
        for g in mys2list:
            myst2+= g + "\n"
        for g in val2list:
            valo2+= g + "\n"
        
        
        if msgid=="":
            await self.bot.send_message(ctx.message.channel,"__**Valor:**__ \n" + valo + "" + "__**Mystic:**__ \n" + myst + "" + "__**Instinct:**__ \n" + inst + "")
        else:
            await self.bot.send_message(ctx.message.channel,"__**First Group:**__\n__**Valor:**__ \n" + valo + "" + "__**Mystic:**__ \n" + myst + "" + "__**Instinct:**__ \n" + inst + "")
            await self.bot.send_message(ctx.message.channel,"__**Late Group:**__\n__**Valor:**__ \n" + valo2 + "" + "__**Mystic:**__ \n" + myst2 + "" + "__**Instinct:**__ \n" + inst2 + "")
        
        return
        
        
        if ch.id==self.exchan[rn]: #"439132862449713172": #"439132862449713172":
            role=discord.utils.get(ctx.message.server.roles, id=self.exroles[rn])
            for user in ctx.message.server.members:
                if not user.display_name=="MrMasterMiltank":
                    if role in user.roles:
                        print(user.name)
                        if Valor in user.roles:
                            valo+= user.display_name + "\n"
                        if Mystic in user.roles:
                            myst+= user.display_name + "\n"
                        if Instinct in user.roles:
                            inst+= user.display_name + "\n"
            if msgid=="":
                await self.bot.send_message(ctx.message.channel,"__**Valor:**__ \n" + valo + "" + "__**Mystic:**__ \n" + myst + "" + "__**Instinct:**__ \n" + inst + "")
            else:
                await self.bot.send_message(ctx.message.channel,"First Group:\n__**Valor:**__ \n" + valo + "" + "__**Mystic:**__ \n" + myst + "" + "__**Instinct:**__ \n" + inst + "")
                await self.bot.send_message(ctx.message.channel,"Late Group:\n__**Valor:**__ \n" + valo2 + "" + "__**Mystic:**__ \n" + myst2 + "" + "__**Instinct:**__ \n" + inst2 + "")
            
            #print ("__**Valor:**__ \n" + valo + "" + "__**Mystic:**__ \n" + myst + "" + "__**Instinct:**__ \n" + inst + "")          
                #member = discord.utils.get(message.server.members, id=user.id)
                #if not role in member.roles:
                #    await self.bot.add_roles(member,role) 
        return
        if message.id in self.mtch2id:
            for xi in range(0,len(message.reactions)): 
                useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                role=discord.utils.get(tmess.server.roles, id=self.exroles[1])
                for user in useri:
                    member = discord.utils.get(message.server.members, id=user.id)
                    if not role in member.roles:
                        await self.bot.add_roles(member,role)
        if message.id in self.mtch3id:
            for xi in range(0,len(message.reactions)): 
                useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                role=discord.utils.get(tmess.server.roles, id=self.exroles[2])
                for user in useri:
                    member = discord.utils.get(message.server.members, id=user.id)
                    if not role in member.roles:
                        await self.bot.add_roles(member,role)
        if message.id in self.mtch4id:
            for xi in range(0,len(message.reactions)): 
                useri = await self.bot.get_reaction_users([x for x in tmess.reactions][xi])
                role=discord.utils.get(tmess.server.roles, id=self.exroles[3])
                for user in useri:
                    member = discord.utils.get(message.server.members, id=user.id)
                    if not role in member.roles:
                        await self.bot.add_roles(member,role)
    
    
    #Get a list of people attending a raid at a given time.  It will sort the group by team
    #Only required if the bot has crashed before everyone has reacted
    #Ready for publication
    @commands.command(pass_context=True)
    async def rollcall(self,ctx,minute):  #rebuild
        await self.bot.delete_message(ctx.message)
        ch=ctx.message.channel
        inst=""
        myst=""
        valo=""
        inst2=""
        myst2=""
        valo2=""
        Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
        Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
        Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
        vallist=[]
        myslist=[]
        inslist=[]
        val2list=[]
        mys2list=[]
        ins2list=[]    
        async for message in self.bot.logs_from(ch, limit=500): #Gets a list of the last 500 messages in the channel    
            if message.content.startswith("@Start:"):  #This is possibly a reservation time
                a=message
                argg=a.content.split(":")
                if int(argg[2])==int(minute):
                    for xi in range(0,len(message.reactions)): 
                        useri = await self.bot.get_reaction_users([x for x in message.reactions][xi])
                        #role=discord.utils.get(message.server.roles, id=self.exroles[1])
                        for user in useri:
                            member = discord.utils.get(message.server.members, id=user.id)
                            if Valor in member.roles:
                                val2list.append(member.display_name)
                            if Mystic in member.roles:
                                mys2list.append(member.display_name)
                            if Instinct in member.roles:
                                ins2list.append(member.display_name)
                    for g in ins2list:
                        inst2+= g + "\n"
                    for g in mys2list:
                        myst2+= g + "\n"
                    for g in val2list:
                        valo2+= g + "\n"
                    await self.bot.send_message(ctx.message.channel,"__**Valor:**__ \n" + valo2 + "" + "__**Mystic:**__ \n" + myst2 + "" + "__**Instinct:**__ \n" + inst2 + "")
    
        
    #FUNCTION: listexgyms
    #Description: Creates a list of ex-raid gyms in the system
    #User restrictions : None
    #Channel restrictions : None
    #Comments: FULLY OPTIMIZED
    @commands.command(pass_context=True)
    async def listexgyms(self,ctx):  
        msg="The following gyms are Ex-Raid eligible gyms that I am aware of:\n`"
        for x in self.Locbypass:
            msg+=x+"\n"
        msg+="`"
        await self.bot.send_message(ctx.message.channel,msg)
        await self.bot.delete_message(ctx.message)
    
    #This function allows admins to change the timezone (helpful at daylight savings time
    #Ready for publication
    @checks.admin() #Only allow admins to change this setting
    @commands.command(pass_context=True,no_pm=False)
    async def timezone(self,ctx,timezone):
        '''Set the timezone for the server and make it persistent'''
        timezval=int(timezone);
        #Need to write the bannedlist file
        file = open("configuration/timezone.json","w",encoding='utf-8')
        txt='{\n  "timezone" : '
        txt += str(timezval)
        txt += "\n}" 
        file.write(txt)
        file.close()
        
        await self.bot.send_message(ctx.message.channel,"The timezone has been set to " + str(timezval))
        
    #This function allows admins to change the timezone (helpful at daylight savings time)
    #Ready for publication
    @checks.admin() #Only allow admins to change this setting
    @commands.command(pass_context=True,no_pm=False)
    async def DST(self,ctx,direction):
        '''Set the timezone for the server and make it persistent
        Direction="forward" or "backward"'''
        flag=0
        if direction.upper()=="FORWARD":
            self.timez=self.timez+1
            flag=1
        if direction.upper()=="BACKWARD":
            self.timez=self.timez-1
            flag=1
        if flag==0:
            await self.bot.send_message(ctx.message.channel,"I didn't understand the direction.")    
            return
        timezval=int(self.timez);
        file = open("configuration/timezone.json","w",encoding='utf-8')
        txt='{\n  "timezone" : '
        txt += str(timezval)
        txt += "\n}" 
        file.write(txt)
        file.close()
        
        await self.bot.send_message(ctx.message.channel,"The timezone has been set to " + str(timezval))    
    
    
    @commands.command(pass_context=True,no_pm=False)
    async def delmsg(self,ctx,msgid):
        #ch=self.bot.get_channel(chid)
        await self.bot.delete_message(ctx.message)
        try:
            a=await self.bot.get_message(ctx.message.channel, msgid)
            await self.bot.delete_message(a)
        except:
            ar=1
        
    #FUNCTION: pemoji
    #Description: Displays all raid boss specific emoji
    #User restrictions : Raid Managers,Ranger, and Stinkpot Only
    #Channel restrictions : None 
    #Comments: FULLY OPTIMIZED    
    @commands.command(pass_context=True)
    async def pemoji(self,ctx): 
        role1=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
        role2=discord.utils.get(ctx.message.server.roles, id=self.RaidManager)
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles 
        displist=""
        for x in self.Bossemoji:
            displist+=x
        if any(xpp == role1 for xpp in f):
            await self.bot.send_message(ctx.message.channel, " " + displist)
            return
        if any(xpp == role2 for xpp in f):
            await self.bot.send_message(ctx.message.channel, " " + displist)
            return
        if ctx.message.author.id=="345200594421547018":
            await self.bot.send_message(ctx.message.channel, " " + displist)
            return

    #FUNCTION: badge
    #Description: Displays all raid boss specific emoji
    #User restrictions : Raid Managers,Ranger, and Stinkpot Only
    #Channel restrictions : None  
    @commands.command(pass_context=True)
    async def badge(self,ctx,location,level):   
        """Location is based on the first 8 letters of the Pokemon Go gym name
           Level is a number: 
                1)Gym has been spun but not bronze 
                2)Bronze
                3)Silver
                4)Gold
        """
        await self.bot.send_message(ctx.message.channel,"STOP FUCKING USING THIS COMMAND")
        return
        uname=ctx.message.author.display_name
        uname=uname+str(ctx.message.author.discriminator)
        #First verify that the username and display name match previous records
        
        #await self.bot.send_message(ctx.message.channel,uname)
        #value  = (df.sheets(1).cell(5,4).value)
        #await self.bot.send_message(ctx.message.channel,df)
        #await self.bot.send_message(ctx.message.author,uname + ", you entered an invalid badge level." + level)
        #await self.bot.send_file(ctx.message.author, 'StinkpotMcGoo.xlsx')
        
        xp=int(level)
        level=xp
        if level:
            if level<=0 | level>=5:
                await self.bot.send_message(ctx.message.author,uname + ", you entered an invalid badge level (error 2). " + str(level))
            else:
                cntt=0
                uniq=0
                grid=0
                if len(location)<8:
                    for x in range(0,8-len(location)):
                        location=location + " "
                loc=location[0:8]
                for x in self.sngroup:
                    if loc.upper()==x.upper():
                        uniq=uniq+1
                        grid=1
                        Nameval=self.cngroup[cntt]
                        intval=cntt
                        #linkn=self.lngroup[cntt]
                        gymlat=self.latgroup[cntt]
                        gymlon=self.longroup[cntt]
                        linkn= "" + gymlat + "," + gymlon +""+ ""
                        linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                    cntt=cntt+1
                if uniq>1:
                    optnum=1
                    cntt=0
                    ncha=0
                    Nameval=''
                    LVal=[]
                    for x in self.sngroup:
                        if loc.upper()==x.upper():
                            Nameval=Nameval + str(optnum) + ")" + self.cngroup[cntt] + "\n"#: Use '" + self.angroup[cntt] + "'\n"
                            optnum=optnum+1
                            LVal.append(self.angroup[cntt])
                            ncha=ncha+1
                        cntt=cntt+1
                
                    if ncha==0:  #Channel name isn't in alt or shortname
                        await self.bot.say("`The gym name you entered is not available in the system`")
                        return
                    elif ncha>1: #Unique Channel name doesn't exist
                        await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by retyping the command with one of the following gym names:\n")
                        await self.bot.say("`{}`".format(Nameval))
                        msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                        try:
                            loc=LVal[int(msgrt.content)-1]
                        except:
                            return
                cntt=0
                uniq=0
                grid=0
                for x in self.angroup:
                    if loc.upper()==x.upper():
                        uniq=uniq+1
                        grid=1
                        Nameval=self.cngroup[cntt]
                        #linkn=self.lngroup[cntt]
                        gymlat=self.latgroup[cntt]
                        gymlon=self.longroup[cntt]
                        linkn= "" + gymlat + "," + gymlon +""+ ""
                        linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                    cntt=cntt+1
                
                
                if uniq==0:
                    await self.bot.say("`The gym name you entered is not available in the system`")
                    return
                elif uniq==1:
                #else:
                    try:
                        df = pd.read_excel('Gyms' + "\\" + uname + '.xlsx')
                        df[['Bronze','Gold','Silver','Not Bronze']] = df[['Bronze','Gold','Silver','Not Bronze']].astype(str)
                    except:
                        df = pd.read_excel('Gyms' + "\\" + 'Blank' + '.xlsx')
                        df[['Bronze','Gold','Silver','Not Bronze']] = df[['Bronze','Gold','Silver','Not Bronze']].astype(str)
                        #await self.bot.send_message(ctx.message.channel,df.iloc[intval,0:])
                        df[df=="nan"]=np.NaN
                        ##df.replace("nan", "")
                        #await self.bot.send_message(ctx.message.channel,df.iloc[intval,0:])
                        #afef
                    #await self.bot.send_message(ctx.message.channel,df.iloc[intval,0])
                    str_time = datetime.utcnow()+timedelta(hours=self.timez)
                    str_time = str_time.strftime('%Y-%m-%d %H:%M:%S')
                    #await self.bot.send_message(ctx.message.channel,df.iloc[intval,0:])
                    #await self.bot.send_message(ctx.message.channel,df.columns)
                    if level==1:
                        levtxt="not quite bronze!"
                    elif level==2:
                        levtxt="bronze!"
                    elif level==3:
                        levtxt="silver!"
                    elif level==4:
                        levtxt="gold!"
                    if df.iloc[intval,0]==Nameval:
                        if level==4:
                            #df.iloc[intval,4]=""
                            for x in range(1,level+1):
                                if str(df.iloc[intval,x])==str(np.NaN) :
                                   df.iat[intval,x]=str(str_time)
                            df.iat[intval,level]=str(str_time)
                        else:
                            for x in range(level,4+1):
                                df.iat[intval,x]=""
                                a=1
                            for x in range(1,level):
                                #await self.bot.send_message(ctx.message.channel,str(df.iloc[intval,x]))
                                if str(df.iloc[intval,x])==str(np.NaN) :
                                   df.iat[intval,x]=str(str_time) 
                            df.iat[intval,level]=str(str_time)
                        
                        #remove "nan" from df
                        df[df=="NaT"]=np.NaN
                        df[df=="nan"]=np.NaN
                        #await self.bot.send_message(ctx.message.channel,df.iloc[intval,0:])
                        pd.set_option('max_colwidth', 400)
                        writer = pd.ExcelWriter('Gyms' + "\\" +uname + '.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='Sheet1',index=False)
                        workbook  = writer.book
                        worksheet = writer.sheets['Sheet1']
                        # Note: It isn't possible to format any cells that already have a format such
                        # as the index or headers or any cells that contain dates or datetimes.

                        # Set the column width and format.
                        worksheet.set_column('B:E', 18, None)

                        # Set the format but not the column width.
                        worksheet.set_column('A:A', 46, None)

                        # Close the Pandas Excel writer and output the Excel file.
                        writer.save()


                        
                        await self.bot.send_message(ctx.message.channel,uname + ", I have updated your badge for " + Nameval + " to *" + levtxt + "*")
                    else:
                        await self.bot.send_message(ctx.message.channel,"The name of the gyms got messed up.  Contact a programmer with the command you used.")
        else:
            await self.bot.send_message(ctx.message.channel,uname + ", you entered an invalid badge level (error 1).")
    
    @commands.command(pass_context=True)
    async def gyms(self,ctx):
        uname=ctx.message.author.display_name
        uname=uname+str(ctx.message.author.discriminator)
        try:
            await self.bot.send_file(ctx.message.author, 'Gyms' + "\\" + uname +'.xlsx')
        except:
            await self.bot.send_message(ctx.message.author,"Sorry, but you haven't entered any gym badge information yet.")
    
    @commands.command(pass_context=True)
    async def listgyms(self,ctx):
        msg="Here is a list of Purdue Campus gyms:\n"
        for x in self.group1cn:
            msg+=x+"\n"
        await self.bot.send_message(ctx.message.channel,msg)
        msg="Here is a list of West Lafayette gyms:\n"
        for x in self.group2cn:
            msg+=x+"\n"
        await self.bot.send_message(ctx.message.channel,msg)
        msg="Here is a list of Lafayette gyms:\n"
        for x in self.group3cn:
            msg+=x+"\n"
        await self.bot.send_message(ctx.message.channel,msg)
    
    
    #FUNCTION: test100IV
    #Description: A Testing function to collect the IDs of all users signed up for 100IV role
    #User restrictions : None
    #Channel restrictions : None  
    #Comments: FULLY OPTIMIZED
    @commands.command(pass_context=True)
    async def test100IV(self,ctx): 
        rolePS = discord.utils.get(ctx.message.server.roles, id=self.testalert)
        cntt=0
        for f in ctx.message.server.members:
            if not f==None:
                if any(xpp == rolePS for xpp in f.roles): #Member is approved
                    print("Signedup:"+f.name+" "+f.id)
                    with open("Alerts\\100IV.txt","a") as g:
                        print(f.id,file=g)
                    cntt+=1
        print("Signedup Count="+str(cntt))
    
    @commands.command(pass_context=True)
    async def testmute(self,ctx): 
        rolePS = discord.utils.get(ctx.message.server.roles, id=self.muteg1)
        cntt=0
        for f in ctx.message.server.members:
            if not f==None:
                if any(xpp == rolePS for xpp in f.roles): #Member is approved
                    print("Signedup:"+f.name+" "+f.id)
                    with open("Alerts\\muteg1.txt","a") as g:
                        print(f.id,file=g)
                    cntt+=1
        print("Signedup Count="+str(cntt))
    
    @commands.command(pass_context=True)
    async def t100IV(self,ctx): 
        #memlist=[]
        #with open("Alerts\\100IV.txt","r") as fr:
        #    for line in fr:
        #        t = line
        #        nt=t.split('\n')
        #        memlist.append(discord.Server.get_member(ctx.message.server,nt[0]))
        memlist=await subf.getmemlist(self,ctx,self.testalert)
        mutelist=await subf.getmemlist(self,ctx,self.muteg3)
        
        #print(mutelist)
        #return
        #mutelist=[]
        #rolePS = discord.utils.get(ctx.message.server.roles, id=self.muteg1)
        #cntt=0
        #for f in ctx.message.server.members:
        #    if not f==None:
        ##        if any(xpp == rolePS for xpp in f.roles): #Member is on mute list
        #            mutelist.append(f)
        
        #Place the notifications in a given channel
        ch=self.bot.get_channel("408330312125382656")
        
        meat=ctx.message.content[8::]
        cntt=0
        msg=""
        for f in memlist:
            if not f in mutelist:
                msg+=f.name
                if len(msg)>1500:
                    tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg)
                    await asyncio.sleep(0.2)
                    #await self.bot.edit_message(tms,meat)
                    await self.bot.delete_message(tms)
                    msg=""

        if len(msg)>0:
            tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg)
            await asyncio.sleep(0.2)
            #await self.bot.edit_message(tms,meat)
    
    @commands.command(pass_context=True)
    async def createbossfile(self,ctx): 
        await subf.writebossfile(self,ctx)
    
    @commands.command(pass_context=True)
    async def readbossfile(self,ctx): 
        await subf.readbosses(self)
        print(self.L4maxCP)
        await self.bot.send_message(ctx.message.channel,"All of the new raid boss data has been read in!")
        #await self.bot.send_message(ctx.message.channel,int(self.L4maxCP))
        return
        stuff = dataIO.load_json("configuration/crapola.json")
        self.L4types2=stuff["L4types"]
        self.L4notid2=stuff["L4notid"]
        self.L4maxCP3=stuff["L4maxCP"]
        self.L4slope3=stuff["L4slope"]
        self.L4peeps3=stuff["L4peeps"]
        self.L4offset3=stuff["L4offset"]
        self.L4emoji2=stuff["L4emoji"]
        self.L3types2=stuff["L3types"]
        self.L3notid2=stuff["L3notid"]
        self.L3maxCP3=stuff["L3maxCP"]
        self.L3slope3=stuff["L3slope"]
        self.L3peeps3=stuff["L3peeps"]
        self.L3offset3=stuff["L3offset"]
        self.L3emoji2=stuff["L3emoji"]
        self.L5types2=stuff["L5types"]
        self.L5notid2=stuff["L5notid"]
        self.L5maxCP3=stuff["L5maxCP"]
        self.L5slope3=stuff["L5slope"]
        self.L5peeps3=stuff["L5peeps"]
        self.L5offset3=stuff["L5offset"]
        self.L5emoji2=stuff["L5emoji"]
        self.L4maxCP2=[]
        self.L4slope2=[]
        self.L4peeps2=[]
        self.L4offset2=[]
        for n in self.L4maxCP3:
            self.L4maxCP2.append(int(n))
        for n in self.L4slope3:    
            self.L4slope2.append(int(n))
        for n in self.L4peeps3:        
            self.L4peeps2.append(int(n))
        for n in self.L4offset3: 
            self.L4offset2.append(int(n))
        

        self.L5maxCP2=[]
        self.L5slope2=[]
        self.L5peeps2=[]
        self.L5offset2=[]
        for n in self.L5maxCP3:
            self.L5maxCP2.append(int(n))
        for n in self.L5slope3:    
            self.L5slope2.append(int(n))
        for n in self.L5peeps3:        
            self.L5peeps2.append(int(n))
        for n in self.L5offset3: 
            self.L5offset2.append(int(n))

        self.L3maxCP2=[]
        self.L3slope2=[]
        self.L3peeps2=[]
        self.L3offset2=[]
        for n in self.L3maxCP3:
            self.L3maxCP2.append(int(n))
        for n in self.L3slope3:    
            self.L3slope2.append(int(n))
        for n in self.L3peeps3:        
            self.L3peeps2.append(int(n))
        for n in self.L3offset3: 
            self.L3offset2.append(int(n))
        
        await self.bot.send_message(ctx.message.channel,int(self.L4maxCP2))
    
    @commands.command(pass_context=True)
    async def addnewboss(self,ctx): 
        #Verify the person is a RaidObserver
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        contin=0
        for idx in f: 
            if idx.id==self.RaidObserver:   
                contin=1   
        if contin==0:
            return
        
        alltimeout=30        
        attempt=0
        success=0
        await self.bot.send_message(ctx.message.channel,"There's a new boss in town! \nBefore you start: Have a role created for the new raid boss (i.e. r-Scyther) and a designated emoji.\n  What tier level is it? \nPress 'q' to quit at any time.")
        while success==0 and attempt<3:
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="Q": 
                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                return
            levelv=int(msgrt.content)
            success=1
            
        attempt=0
        success=0
        await self.bot.send_message(ctx.message.channel,"What is the name of the boss?")
        while success==0 and attempt<3:
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            typev=msgrt.content
            if msgrt.content.upper()=="Q": 
                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                return
            success=1
        
        attempt=0
        success=0
        await self.bot.send_message(ctx.message.channel,"What is the role associated with this boss?")
        while success==0 and attempt<3:
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            
            if msgrt.content.upper()=="Q": 
                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                return
            roler=msgrt.content    
            rolev=msgrt.role_mentions
            success=1
        
        #attempt=0
        #success=0
        #await self.bot.send_message(ctx.message.channel,"What emoji do you want to have displayed #for this raid boss?")
        #while success==0 and attempt<3:
        #    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = #ctx.message.author, channel = ctx.message.channel)
        #    emojiv=msgrt.content
        #    if msgrt.content.upper()=="Q": 
        #        await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
        #        return
        #    success=1
        emojiv="<:item_pokeball:284615009299070976>"
        
        attempt=0
        success=0
        await self.bot.send_message(ctx.message.channel,"Last question, what is it's max CP?")
        while success==0 and attempt<3:
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            
            if msgrt.content.upper()=="Q": 
                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                return
            maxcp=int(msgrt.content)
            success=1
        
        await self.bot.send_message(ctx.message.channel,"Based on what you told me: You're adding a "+ str(levelv)+" raid boss named " + typev + " with a max CP of " + str(maxcp) + " is to be added. It will have a role " + roler + " with an emoji of " + emojiv +  ". Is this correct? (Y/N)")
        attempt=0
        success=0
        while success==0 and attempt<3:
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content.upper()=="N": 
                await self.bot.send_message(ctx.message.channel,"Looks like you may have entered something wrong then.  How about you try again.")
                success=1
                return
            elif msgrt.content.upper()=="Y": 
                success=1
            elif msgrt.content.upper()=="Q": 
                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                return
            else: 
                await self.bot.send_message(ctx.message.channel, "Please answer the question, did I get that right (Y/N)?")
                attempt+=1
        if attempt>2:
            await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
            return   
        #print(rolev[0].id)
        #return
        #Now append what we need and write the file
        if levelv==3:
            self.L3types.append(typev.upper())
            self.L3notid.append(rolev[0].id)
            self.L3maxCP.append(maxcp)
            self.L3slope.append(15)
            self.L3peeps.append(4)
            self.L3offset.append(50)
            self.L3emoji.append(emojiv)
        elif levelv==4:
            self.L4types.append(typev.upper())
            self.L4notid.append(rolev[0].id)
            self.L4maxCP.append(maxcp)
            self.L4slope.append(15)
            self.L4peeps.append(4)
            self.L4offset.append(120)
            self.L4emoji.append(emojiv)
        elif levelv==5:
            self.L5types.append(typev.upper())
            self.L5notid.append(rolev[0].id)
            self.L5maxCP.append(maxcp)
            self.L5slope.append(15)
            self.L5peeps.append(4)
            self.L5offset.append(300)
            self.L5emoji.append(emojiv)
        
        await subf.writebossfile(self,ctx,"crapola.json")
        print(self.L5emoji)
        
    @commands.command(pass_context=True)
    @checks.is_owner()
    async def set1(self,ctx): 
        await self.bot.send_message(ctx.message.channel,"This function has been deactivated")
        return 
        await self.bot.send_message(ctx.message.channel,"This will perform channel setup")
        server=self.bot.get_server(self.serverid)
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        for idx in f: 
            if idx.id==self.Approved:   
                role_everyone = idx                
        role_pogomod=discord.utils.get(ctx.message.server.roles, id=self.POGOmod)  
        for sheet_name in range(0,self.numcat):

            #xr=await self.bot.create_channel(server, self.catnames[sheet_name], type=4)
            strr=""
            cntt=0
            for x in range(0,self.nchan):
                Nameval=self.catnames[sheet_name].replace(' ', '-').lower()
                rt=await self.bot.create_channel(server, Nameval + str(cntt))
                await asyncio.sleep(5)
                ch = discord.utils.get(server.channels, name=Nameval + str(cntt))
                if ch==None:
                    await self.bot.send_message(ctx.message.channel,"BAD")
                    return
                overwrite = ch.overwrites_for(role_everyone)
                overwrite.read_messages = False
                #overwrite.read_message_history = False
                #overwrite.add_reactions = False
                await self.bot.edit_channel_permissions(ch, role_everyone, overwrite)
                overwrite = ch.overwrites_for(role_pogomod)
                overwrite.read_messages = False
                await self.bot.edit_channel_permissions(ch, role_pogomod, overwrite)
                overwrite = ch.overwrites_for(f[0])
                overwrite.read_messages = False
                #overwrite.read_message_history = False
                #overwrite.add_reactions = False
                await self.bot.edit_channel_permissions(ch, f[0], overwrite)
                strr+="'"+ch.id+"'"+","
                cntt+=1
                #deleted=await self.bot.purge_from(ch, limit=100)
                #await self.bot.edit_channel(ch, name='blank-' + str(maxpos))
            await self.bot.send_message(ctx.message.channel,self.catnames[sheet_name]+" IDs: " + strr)    
            xr=await self.bot.create_channel(server, self.catnames[sheet_name], type=4)
            await asyncio.sleep(0.5)
            ch = discord.utils.get(server.channels, name=self.catnames[sheet_name])
            if ch==None:
                await self.bot.send_message(ctx.message.channel,"BAD")
                return
            overwrite = ch.overwrites_for(role_everyone.id)
            overwrite.read_messages = False
            #overwrite.read_message_history = False
            #overwrite.add_reactions = False
            await self.bot.edit_channel_permissions(ch, role_everyone, overwrite)
            overwrite = ch.overwrites_for(role_pogomod)
            overwrite.read_messages = False
            await self.bot.edit_channel_permissions(ch, role_pogomod, overwrite)
            overwrite = ch.overwrites_for(f[0])
            overwrite.read_messages = False
            #overwrite.read_message_history = False
            #overwrite.add_reactions = False
            await self.bot.edit_channel_permissions(ch, f[0], overwrite)
            await self.bot.move_channel(ch, 0)

    
    #FUNCTION: helpme
    #Description: Provides a DM to a user with help information
    #User restrictions : None
    #Channel restrictions : None  
    #Comments: FULLY OPTIMIZED
    @commands.command(pass_context=True)
    async def helpme(self,ctx):
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        member = discord.utils.get(server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(server,ctx.message.author.id)
        f=b.roles
        msg=""
        msg+="Telling everyone you will be at a given raid is pretty simple; place `*any*` emoji you want at the corresponding time you will be there.  A list of everyone attending will automatically be generated.  There are a few *special* emoji that you may want/need to use from time to time.\n :train2:,:train:,:  `train2` --> If you are a member of the raid train and want to let people know when you are going to show, place this emoji in the corresponding time.\n:octagonal_sign: `octagonal_sign` --> When you are running late and you need an extra 2 minutes to get there, put this next to your emoji to let everyone know you need a few minutes.  The raid will only be delayed 2 minutes.\n:one:-:four: `one`-`four` --> Telling everyone the other people you will bring with you.  Set these up by using the `%shadow` command in `#poke_sight_alert`.  Using this outside that channel will not save your data.\n\n"
        msg+="Here is a list of functions for everyone: \nIf you need a description of how to use any of the __**bolded**__ functions, just type in the command without any inputs.  The remaining functions are questionaires that will guide you through the process\n        __**%level**__   --> Set your trainer level in the system\n        __**%shadow**__  --> Set the level of up to four people you raid with\n        __**%whereis**__ --> Receive a DM with a pin for a given gym location\n        `%mute`    --> Set notification muting        `%raid`    --> Enter information about a raid at a gym location\n        `%update`  --> Update the raid boss at a gym once a raid has been entered\n         `%showallraids`  -->  Show all types of raids without receiving notifications\n         `%hideallraids`  -->  Hide all types of raids (you will see no raid channels if not signed up for alerts).\n__**`%RIP`**__ --> Inform members that a raid is being cancelled.\n         `%invite`  --> Generate a message to show the invite link for the Discord server\n"
        await self.bot.send_message(ctx.message.author,msg)
        RO=discord.utils.get(server.roles, id=self.RaidTrainer)
        if any(xpp == RO for xpp in f): #If a raid trainer
            msg="Here is a list of functions for Raid Trainers:\n         __**%addtime**__ --> Add an additional time to a raid\n"
        RO=discord.utils.get(server.roles, id=self.RaidObserver)
        await self.bot.send_message(ctx.message.channel,"A DM has been sent to you with your role-specific functions!")
        await self.bot.send_message(ctx.message.author,msg)
        if any(xpp == RO for xpp in f): #If a raid observer
            msg2="Here is a list of functions for Raid Observers:\n        __**%accept**__  --> Accept the data entry from a RaidTrainer so it can be shown in the system\n        __**%decline**__ --> Decline the data entry from a RaidTrainer due to a data entry error\n        __**%delraid**__ --> Delete the raid reservation at a given gym location\n        __**%addtime**__ --> Add an additional time to a raid\n"
            await self.bot.send_message(ctx.message.author,msg2)
        RO=discord.utils.get(server.roles, id=self.RaidObserver)
        if any(xpp == RO for xpp in f): #If a raid observer
            msg2="Here is a list of functions for Bot Modifiers:\n        __**%accept**__  --> Accept the data entry from a RaidTrainer so it can be shown in the system\n        __**%decline**__ --> Decline the data entry from a RaidTrainer due to a data entry error\n        __**%delraid**__ --> Delete the raid reservation at a given gym location\n        __**%addtime**__ --> Add an additional time to a raid\n"
            await self.bot.send_message(ctx.message.author,msg2)
        #RO=discord.utils.get(ctx.message.server.roles, id=self.RaidObserver)
        #if any(xpp == RO for xpp in f): #If a raid observer
        #Here is a list of functions for admins of the RM system
        #%modify  --> Modify the parameters of a raid if an error was made during entry (will be made RO available)
    
    #FUNCTION: help
    #Description: Provides a DM to a user with help information
    #User restrictions : None
    #Channel restrictions : None  
    #Comments: FULLY OPTIMIZED
    @commands.command(pass_context=True)
    async def help(self,ctx):
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        member = discord.utils.get(server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(server,ctx.message.author.id)
        f=b.roles
        msg=""
        msg+="Telling everyone you will be at a given raid is pretty simple; place `*any*` emoji you want at the corresponding time you will be there.  A list of everyone attending will automatically be generated.  There are a few *special* emoji that you may want/need to use from time to time.\n :train2:,:train:,:  `train2` --> If you are a member of the raid train and want to let people know when you are going to show, place this emoji in the corresponding time.\n:octagonal_sign: `octagonal_sign` --> When you are running late and you need an extra 2 minutes to get there, put this next to your emoji to let everyone know you need a few minutes.  The raid will only be delayed 2 minutes.\n:one:-:four: `one`-`four` --> Telling everyone the other people you will bring with you.  Set these up by using the `%shadow` command in `#poke_sight_alert`.  Using this outside that channel will not save your data.\n\n"
        msg+="Here is a list of functions for everyone: \nIf you need a description of how to use any of the __**bolded**__ functions, just type in the command without any inputs.  The remaining functions are questionaires that will guide you through the process\n        __**%level**__   --> Set your trainer level in the system\n        __**%shadow**__  --> Set the level of up to four people you raid with\n        __**%whereis**__ --> Receive a DM with a pin for a given gym location\n        `%mute`    --> Set notification muting\n        `%raid`    --> Enter information about a raid at a gym location\n        `%update`  --> Update the raid boss at a gym once a raid has been entered\n         `%showallraids`  -->  Show all types of raids without receiving notifications\n         `%hideallraids`  -->  Hide all types of raids (you will see no raid channels if not signed up for alerts).\n        __**%RIP**__ --> Inform members that a raid is being cancelled.\n         `%invite`  --> Generate a message to show the invite link for the Discord server\n"
        await self.bot.send_message(ctx.message.author,msg)
        RO=discord.utils.get(server.roles, id=self.RaidTrainer)
        if any(xpp == RO for xpp in f): #If a raid trainer
            msg="Here is a list of functions for Raid Trainers:\n         __**%addtime**__ --> Add an additional time to a raid\n"
        RO=discord.utils.get(server.roles, id=self.RaidObserver)
        await self.bot.send_message(ctx.message.channel,"A DM has been sent to you with your role-specific functions!")
        await self.bot.send_message(ctx.message.author,msg)
        if any(xpp == RO for xpp in f): #If a raid observer
            msg2="Here is a list of functions for Raid Observers:\n        __**%accept**__  --> Accept the data entry from a RaidTrainer so it can be shown in the system\n        __**%decline**__ --> Decline the data entry from a RaidTrainer due to a data entry error\n        __**%delraid**__ --> Delete the raid reservation at a given gym location\n        __**%addtime**__ --> Add an additional time to a raid\n"
            await self.bot.send_message(ctx.message.author,msg2)
        
        #RO=discord.utils.get(ctx.message.server.roles, id=self.RaidObserver)
        #if any(xpp == RO for xpp in f): #If a raid observer
        #Here is a list of functions for admins of the RM system
        #%modify  --> Modify the parameters of a raid if an error was made during entry (will be made RO available)
    
    
    #FUNCTION: subscribed
    #Description: Provides a DM to a user of the roles they are subscribed to
    #User restrictions : None
    #Channel restrictions : Debug channel, #raid_alerts, and #poke_sight_alert  
    #Comments: FULLY OPTIMIZED
    @commands.command(pass_context=True)
    async def subscribed(self,ctx):
        if ctx.message.channel.id==self.programid or ctx.message.channel.id=="403939414977413122" or ctx.message.channel.id=="351944459115560991":
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles
            mess=b.mention +", you are currently subscribed to the following roles:"
            for xx in f[1::]:
                if not any(xxp==xx.id for xxp in self.excludeid): 
                    mess+="\n"+xx.name
            await self.bot.send_message(ctx.message.channel,"I have sent you a direct message of your current subscribed alerts!")
            await self.bot.send_message(ctx.message.author,mess)
    
    @commands.command(pass_context=True)
    async def checkperms(self,ctx):  #Fully optimized & function works    
        try:
            await self.bot.wait_until_ready()
            #cron = CronTab('*/5 * * * * * *')
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles
            for idx in f: 
                if idx.id==self.Approved:   
                    role_everyone = idx
            role_pogomod=discord.utils.get(ctx.message.server.roles, id=self.POGOmod)   
            channel=self.bot.get_channel(self.programid)
            #await self.bot.send_message(channel, "HILLELFO" )#+ str(rrx.days))       
            maxpos=0
            #try:
            text="Cron is working"
            for x in self.allbutmtch:
                
                rrx=await subf.singlechan(self,x,role_everyone,ctx)
                #await self.bot.send_message(channel, text + x + str(rrx))
                if rrx==0:
                    ch=self.bot.get_channel(x)
                    print(ch.name)
                    overwrite = ch.overwrites_for(role_everyone)
                    overwrite.read_messages = False
                    await self.bot.edit_channel_permissions(ch, role_everyone, overwrite)
                    #overwrite = ch.overwrites_for(role_pogomod)
                    #overwrite.read_messages = False
                    #await self.bot.edit_channel_permissions(ch, role_pogomod, overwrite)
                    role_RO=discord.utils.get(ctx.message.server.roles, id=self.RaidObserver)
                    overwrite = ch.overwrites_for(role_RO)
                    overwrite.read_messages = False
                    await self.bot.edit_channel_permissions(ch, role_RO, overwrite)
                    deleted=await self.bot.purge_from(ch, limit=100)
                    await self.bot.edit_channel(ch, name='blank-' + str(maxpos))     
            await asyncio.sleep(180)
        except:
            arpr=10
    
    @commands.command(pass_context=True,no_pm=False)
    async def reactor(self,ctx,msgid,emoji):
        #ch=self.bot.get_channel(chid)
        try:
            a=await self.bot.get_message(ctx.message.channel, msgid)
            await self.bot.add_reaction(a,emoji)
        except:
            ar=1
        await self.bot.delete_message(ctx.message)
        
    #Show all raid channels
    #Anyone can use this function
    #Ready for publication
    @commands.command(pass_context=True)
    async def showallraids(self,ctx):
        userf=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        SilentL5=discord.utils.get(ctx.message.server.roles, id=self.SilentL5)
        SilentL4=discord.utils.get(ctx.message.server.roles, id=self.SilentL4)
        SilentL3=discord.utils.get(ctx.message.server.roles, id=self.SilentL3)
        SilentPS=discord.utils.get(ctx.message.server.roles, id=self.SilentPS)
        SilentEX=discord.utils.get(ctx.message.server.roles, id=self.SilentEX)

        await self.bot.add_roles(userf, SilentL3 )
        await asyncio.sleep(0.25)
        await self.bot.add_roles(userf, SilentL4 )
        await asyncio.sleep(0.25)
        await self.bot.add_roles(userf, SilentL5 )
        await asyncio.sleep(0.25)
        await self.bot.add_roles(userf, SilentPS )
        await asyncio.sleep(0.25)
        await self.bot.add_roles(userf, SilentEX )
        await asyncio.sleep(0.25)
        await self.bot.send_message(ctx.message.channel,userf.name+", you can now see all raids!")
    
    #Hide all raid channels
    #Anyone can use this function
    #Ready for publication
    @commands.command(pass_context=True)
    async def hideallraids(self,ctx):
        userf=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        SilentL5=discord.utils.get(ctx.message.server.roles, id=self.SilentL5)
        SilentL4=discord.utils.get(ctx.message.server.roles, id=self.SilentL4)
        SilentL3=discord.utils.get(ctx.message.server.roles, id=self.SilentL3)
        SilentPS=discord.utils.get(ctx.message.server.roles, id=self.SilentPS)
        SilentEX=discord.utils.get(ctx.message.server.roles, id=self.SilentEX)

        await self.bot.remove_roles(userf, SilentL3 )
        await asyncio.sleep(0.25)
        await self.bot.remove_roles(userf, SilentL4 )
        await asyncio.sleep(0.25)
        await self.bot.remove_roles(userf, SilentL5 )
        await asyncio.sleep(0.25)
        await self.bot.remove_roles(userf, SilentPS )
        await asyncio.sleep(0.25)
        await self.bot.remove_roles(userf, SilentEX )
        await asyncio.sleep(0.25)
        await self.bot.send_message(ctx.message.channel,userf.name+", you can now see no raids!")

        
    #Allows a trainer to react for someone else when they raid together using :one: through :four:
    #
    @commands.command(pass_context=True)
    async def shadow(self,ctx,number,level,team):
        """When you want to let people know the levels of others you are bringing, you should setup the levels of accounts that you will be bringing with you.  For example, if you are level 35 team instinct and the other person is 25 team valor, you should set up your level with the command *%level 35*.  The other account should be setup as %shadow 1 25 Valor.  This way the level estimator will function properly.  Up to 4 shadows can be created per account.  Configure shadows using this command in the #poke_sight_alert channel or they will not be saved.
        examples
        %shadow 1 25 Mystic
        %shadow 2 34 Instinct
        """
        if not (team.upper()=="MYSTIC" or team.upper()=="VALOR" or team.upper()=="INSTINCT"):
            await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", the team name must be Mystic, Instinct or Valor.")
            return
        retflag1=0
        retflag2=0
        
        if not (ctx.message.channel.id==self.programid or ctx.message.channel.id=="403939414977413122" or ctx.message.channel.id=='351944459115560991'):
            retflag1=1
        if not ctx.message.channel.id in self.allbutmtch:
            retflag2=1
        
        if retflag1==1 and retflag2==1:        
            return
        
        if team.upper()=="INSTINCT":
            tnum=0
        if team.upper()=="MYSTIC":
            tnum=1
        if team.upper()=="VALOR":
            tnum=2
        try:
            #Add validation that the person is DMing
            uname=ctx.message.author.display_name
            uname=uname+str(ctx.message.author.discriminator)
            try:
                numv=float(number)
                numv=int(numv)
                if numv>4 or numv<1:
                    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", the shadow account must be either 1, 2, 3, or 4.")  
            except:
                await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", the shadow account must be a number: either 1, 2, 3, or 4.") 
            try:
                #make sure the level is a valid number and/or clean it
                newlev=float(level)
                newlev=int(newlev)
                posid=min(40,max(newlev,1))
                
                #open the sheet and see if the person exists
                try: #If the sheet exists, open it 
                    df = pd.read_excel('Shadows2' + "\\" + uname + 'shadow.xlsx')
                    currlev=df.iloc[0,numv-1]
                    df.iloc[0,numv-1]=posid   
                    df.iloc[1,numv-1]=tnum  
                    df[df=="nan"]=np.NaN
                    writer = pd.ExcelWriter('Shadows2' + "\\" +uname + 'shadow.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", shadow account " +str(numv) + " has been set to level " +  str(posid)+ " team "+team.upper())
                except: #The person hasn't established a level yet
                    df = pd.read_excel('Shadows2' + "\\" + 'shadows' + '.xlsx')
                    #print("Here")
                    df.iloc[0,numv-1]=posid
                    df.iloc[1,numv-1]=tnum                    
                    df[df=="nan"]=np.NaN                
                    writer = pd.ExcelWriter('Shadows2' + "\\" +uname + 'shadow.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    #print(df)
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", shadow account " +str(numv) + " has been set to level " +  str(posid)+ " team "+team.upper())
            except:
                await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", please stop being an idiot and enter a number already!")
                
            return
            
        except:
            arpr=10
        
   
    @commands.command(pass_context=True)
    async def whereis(self,ctx,*, stopname : str):  #Need to optimize & function works
        reason = stopname
        Lvalue=reason
        if reason.upper()=="DICK":
            await self.bot.send_message(ctx.message.channel,"You're nasty.\n")
            return
        if ctx.message.channel.id=="431521987676864512":
            await self.bot.delete_message(ctx.message)
            await self.bot.send_message(ctx.message.author,"Hey, type that command over here.\n")
            return
        if ctx.message.channel.id:#=="429291825212293130" or ctx.message.channel.id=="403550523984183296" or ctx.message.channel.id=="385196778779049999" or ctx.message.channel.id=="431521987676864512":
            #print(self.sWL)
            scrubmess=await subf.filtNameval(self,Lvalue.upper())          
            locn=""
            #Try finding the names of the gyms
            loclist=[]
            for y in reason.split(' '):
                for x in self.sWL:
                    if y.upper() == x.upper(): 
                        loclist.append(x)
            #Xref the list with the gym names
            if len(loclist)==0:
                await self.bot.send_message(ctx.message.channel,"I found no pokestops with any words you typed in.  Try again.\n")
                return
            print(loclist)
            #if ctx.message.channel.id=="403550523984183296":
            #    return
            possn=[]
            maxcom=0
            gyml=""
            cntt=0
            gymlist=[]
            suggch=[]
            
            for y in self.stopnam+self.cngroup:
                comwords=0
                tpp=await subf.filtNameval(self,y)
                for x in loclist:
                    if x.upper() in tpp.upper():
                        comwords+=1
                        gymlist.append(y)
                if comwords>maxcom:
                    addlt=""
                    if y in self.stopnam:
                        addlt="Pokestop-"
                    if y in self.cngroup:
                        addlt="Gym-"
                    suggch.append(y)
                    #gyml=self.lngroup[cntt]
                    gyml="HELLO"
                    maxcom=comwords
                cntt+=1
            
            gymlist=[]
            gymlist2=[]
            suggch=[]
            #print (maxcom)
            #print (loclist)
            for y in self.stopnam+self.cngroup:
                comwords=0
                tpp=await subf.filtNameval(self,y)
                for x in loclist:
                    if x.upper() in tpp.upper():
                        comwords+=1
                        print(x.upper() + tpp.upper())
                        #gymlist.append(y)
                if comwords==maxcom:
                    print(y)
                    addlt=""
                    if y in self.stopnam:
                        addlt="Pokestop-"
                    if y in self.cngroup:
                        addlt="Gym-"
                    gymlist.append(y)
                    gymlist2.append(addlt)
                    #gyml=self.lngroup[cntt]
                    #gyml="HELLO"
                    #maxcom=comwords
                cntt+=1
            
            #get unique gyms names only
            ugym=[]
            ugympr=[]
            #print (gymlist)
            #print ("HELLO CHIRST")
            for x in range(0,len(gymlist)):
                xp=gymlist[x]
                xpr=gymlist2[x]
                if xp not in ugym:
                    ugym.append(xp) 
                    ugympr.append(xpr+xp)
            print (ugym)
            print (gymlist)
            
            if len(ugym)==0:
                await self.bot.send_message(ctx.message.channel,"I found no pokestops with any words you typed in.  Try again.\n")
                return
                
            
            txt="`"
            cntr=1
            for x in ugympr:
                txt+=str(cntr)+ ") " +x +" \n"
                cntr+=1
            txt+="`"
            #User selects which gym if confused
            alltimeout=30
            attempt=0
            
            if len(ugym)>1:
                if len(ugym)<=20:
                    await self.bot.send_message(ctx.message.channel,"I got confused. \nPlease clarify which stop you wanted by typing in the number for the stop:\n")
                    try:
                        await self.bot.send_message(ctx.message.channel,txt)
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    except:
                        #b=discord.Server.get_member(ctx.message.server,self.CMK)
                        #await self.bot.send_message(ctx.message.channel,b.mention)
                        #await self.bot.send_message(ctx.message.channel,"I need to summon my master.  Hey " + b.mention + ", something really bad happened.")
                        return
                    try:
                        loclist=ugym[int(msgrt.content)-1]
                        print(loclist)
                        #newloca=loc
                        #print(loc)
                    except:
                        attempt+=1
                        dontcont=1
                        return
                else:
                    await self.bot.send_message(ctx.message.channel,"You need to be just a bit more specific.\n")
                    return
            #elif len(ugym)>20:
            #    await self.bot.send_message(ctx.message.channel,"You need to be just a bit more specific.\n")
            #    return
            else:
                loclist=ugym[0]
            
            
            
            cntt=0

        
            for y in self.stopnam+self.cngroup:
                if loclist==y:
                    #gyml=self.lngroup[cntt]
                    gymlat=self.alllat[cntt]
                    gymlon=self.alllon[cntt]
                cntt+=1
            print(gymlat)
            print(gymlon)
            print(loclist)
            #linkn="Directions to " + loclist + " can be found here:\n " + "https://www.google.com/maps/place/" + gymlat + "+" + gymlon +""+ ""
            linkn="Directions to " + loclist + " can be found here:\n " + "https://www.google.com/maps?q=" + str(gymlat) + "," + str(gymlon) +""+ ""
            await self.bot.send_message(ctx.message.channel, linkn) 
            print(loclist)
        
        
        
            return
        #else:
        #    await self.bot.send_message(ctx.message.channel, "Use this command ")
        
        
        if Lvalue.upper()=="STINKPOT":
            await self.bot.send_message(ctx.message.channel, "You are silly, he's at a computer!") 
            return
        if Lvalue.upper()=="MILTANK" or Lvalue.upper()=="MRMASTERMILTANK":
            await self.bot.send_message(ctx.message.channel, "You are silly, he's at a computer!") 
            return
        if Lvalue.upper()=="HELP":
            await self.bot.send_message(ctx.message.channel, "Seek and ye shall find!") 
            return
        if Lvalue.upper()=="YOURMOM":
            await self.bot.send_message(ctx.message.channel, "You don't want me to go there!") 
            return
        
        return
        try:#See if its the old entry system first:
            location=Lvalue

            cntt=0
            uniq=0
            grid=0
            if len(location)<8:
                for x in range(0,8-len(location)):
                    location=location + " "
            loc=location[0:8]
            for x in self.group1sn:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=1
                    Nameval=self.group1cn[cntt]
                    #linkn=self.group1ln[cntt]
                    gymlat=self.group1lat[cntt]
                    gymlon=self.group1lon[cntt]
                    linkn= "" + gymlat + "," + gymlon +""+ ""
                    linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                cntt=cntt+1
            cntt=0
            for x in self.group2sn:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=2
                    Nameval=self.group2cn[cntt]
                    #linkn=self.group2ln[cntt]
                    gymlat=self.group2lat[cntt]
                    gymlon=self.group2lon[cntt]
                    linkn= "" + gymlat + "," + gymlon +""+ ""
                    linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                cntt=cntt+1
            cntt=0
            for x in self.group3sn:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=3
                    Nameval=self.group3cn[cntt]
                    #linkn=self.group3ln[cntt]
                    gymlat=self.group1lat[cntt]
                    gymlon=self.group1lon[cntt]
                    linkn= "" + gymlat + "," + gymlon +""+ ""
                    linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                    cntt=cntt+1
            #print (Lvalue.lower())
            #print(self.WL)
            if Lvalue.lower() in self.WL:
                uniq=0 #need to use the new system
            if uniq>1:
                optnum=1
                cntt=0
                ncha=0
                Nameval=''
                LVal=[]
                for x in self.group1sn:
                    if loc.upper()==x.upper():
                        Nameval=Nameval + str(optnum) + ")" + self.group1cn[cntt] + "\n"#: Use '" + self.group1an[cntt] + "'\n"
                        optnum=optnum+1
                        LVal.append(self.group1an[cntt])
                        ncha=ncha+1
                    cntt=cntt+1
                cntt=0
                for x in self.group2sn:
                    if loc.upper()==x.upper():
                        Nameval=Nameval + str(optnum) + ")" + self.group2cn[cntt] + "\n"#: Use '" + self.group2an[cntt] + "'\n"
                        optnum=optnum+1
                        LVal.append(self.group2an[cntt])
                        ncha=ncha+1
                    cntt=cntt+1
                cntt=0
                for x in self.group3sn:
                    if loc.upper()==x.upper():
                        Nameval=Nameval + str(optnum) + ")" + self.group3cn[cntt] + "\n"#: Use '" + self.group3an[cntt] + "'\n"
                        optnum=optnum+1
                        LVal.append(self.group3an[cntt])
                        ncha=ncha+1
                    cntt=cntt+1
            
                if ncha==0:  #Channel name isn't in alt or shortname 
                    #add awesomeness here
                    scrubmess=await subf.filtNameval(self,Lvalue.upper())          
                    locn=""
                    #Try finding the names of the gyms
                    loclist=[]
                    for x in self.WL:
                        if x.upper() in Lvalue.upper(): 
                            loclist.append(x)
                    #Xref the list with the gym names
                    possn=[]
                    maxcom=0
                    gyml=""
                    cntt=0
                    gymlist=[]
                    suggch=[]
                    
                    for y in self.cngroup:
                        comwords=0
                        tpp=await subf.filtNameval(self,y)
                        for x in loclist:
                            if x.upper() in tpp.upper():
                                comwords+=1
                                gymlist.append(y)
                        if comwords>maxcom:
                            suggch.append(y)
                            #gyml=self.lngroup[cntt]
                            gymlat=self.latgroup[cntt]
                            gymlon=self.longroup[cntt]
                            gyml="" + gymlat + "," + gymlon + ""
                            maxcom=comwords
                        cntt+=1
                    #get unique gyms names only
                    ugym=[]
                    for x in gymlist:
                        if x not in ugym:
                            ugym.append(x) 
                    print (ugym)
                    print (gymlist)
                    
                    txt="`"
                    cntr=1
                    for x in ugym:
                        txt+=str(cntr)+ ") " +x +" \n"
                        cntr+=1
                    txt+="`"
                    #User selects which gym if confused
                    alltimeout=30
                    if len(ugym)>1:
                        await self.bot.send_message(ctx.message.channel,"I got confused. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                        await self.bot.send_message(ctx.message.channel,txt)
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        try:
                            loclist=ugym[int(msgrt.content)-1]
                            #newloca=loc
                            #print(loc)
                        except:
                            attempt+=1
                            dontcont=1
                            return
                    else:
                        loclist=ugym[0]
                    
                    
                    
                    cntt=0

                
                    for y in self.cngroup:
                        if loclist==y:
                            #gyml=self.lngroup[cntt]
                            gymlat=self.latgroup[cntt]
                            gymlon=self.longroup[cntt]
                            gyml= "" + gymlat + "," + gymlon +""+ ""
                        cntt+=1
                    linkn="Directions to " + loclist + " can be found here:\n " + "https://www.google.com/maps?q=" + gyml + ""
                    await self.bot.send_message(ctx.message.channel, linkn) 
                    print(loclist) 
                    
                    return
                    
                    
                    
                elif ncha>1: #Unique Channel name doesn't exist
                    await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by typing in a number below:\n")
                    await self.bot.say("`{}`".format(Nameval))
                    msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
                    try:
                        loc=LVal[int(msgrt.content)-1]
                    except:
                        return
            elif uniq==0:
                scrubmess=await subf.filtNameval(self,Lvalue.upper())          
                locn=""
                #Try finding the names of the gyms
                loclist=[]
                for x in self.WL:
                    if x.upper() in Lvalue.upper(): 
                        loclist.append(x)
                #Xref the list with the gym names
                possn=[]
                maxcom=0
                gyml=""
                cntt=0
                gymlist=[]
                suggch=[]
                
                for y in self.cngroup:
                    comwords=0
                    tpp=await subf.filtNameval(self,y)
                    for x in loclist:
                        if x.upper() in tpp.upper():
                            comwords+=1
                            gymlist.append(y)
                    if comwords>maxcom:
                        suggch.append(y)
                        #gyml=self.lngroup[cntt]
                        gymlat=self.latgroup[cntt]
                        gymlon=self.longroup[cntt]
                        gyml= "" + gymlat + "," + gymlon +""+ ""
                        maxcom=comwords
                    cntt+=1
                #get unique gyms names only
                ugym=[]
                for x in gymlist:
                    if x not in ugym:
                        ugym.append(x) 
                print (ugym)
                print (gymlist)
                
                txt="`"
                cntr=1
                for x in ugym:
                    txt+=str(cntr)+ ") " +x +" \n"
                    cntr+=1
                txt+="`"
                #User selects which gym if confused
                alltimeout=30
                if len(ugym)>1:
                    await self.bot.send_message(ctx.message.channel,"I got confused. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                    await self.bot.send_message(ctx.message.channel,txt)
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    try:
                        loclist=ugym[int(msgrt.content)-1]
                        #newloca=loc
                        #print(loc)
                    except:
                        attempt+=1
                        dontcont=1
                        return
                else:
                    loclist=ugym[0]
                
                
                
                cntt=0

            
                for y in self.cngroup:
                    if loclist==y:
                        #gyml=self.lngroup[cntt]
                        gymlat=self.latgroup[cntt]
                        gymlon=self.longroup[cntt]
                        gyml= "" + gymlat + "," + gymlon +""+ ""
                    cntt+=1
                linkn="Directions to " + loclist + " can be found here:\n " + "https://www.google.com/maps?q=" + gyml + ""
                await self.bot.send_message(ctx.message.channel, linkn) 
                print(loclist) 
                
                return
            cntt=0
            uniq=0
            grid=0
            for x in self.group1an:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=1
                    Nameval=self.group1cn[cntt]
                    #linkn=self.group1ln[cntt]
                    gymlat=self.group1lat[cntt]
                    gymlon=self.group1lon[cntt]
                    linkn= "" + gymlat + "," + gymlon +""+ ""
                    linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                cntt=cntt+1
            cntt=0
            for x in self.group2an:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=2
                    Nameval=self.group2cn[cntt]
                    #linkn=self.group2ln[cntt]
                    gymlat=self.group2lat[cntt]
                    gymlon=self.group2lon[cntt]
                    linkn= "" + gymlat + "," + gymlon +""+ ""
                    linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                cntt=cntt+1
            cntt=0
            for x in self.group3an:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=3
                    Nameval=self.group3cn[cntt]
                    #linkn=self.group3ln[cntt]
                    gymlat=self.group3lat[cntt]
                    gymlon=self.group3lon[cntt]
                    linkn= "" + gymlat + "," + gymlon +""+ ""
                    linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                cntt=cntt+1
            
            if uniq==0:
                await self.bot.say("`The gym name you entered is not available in the system`")
                return
            elif uniq==1:
                await self.bot.send_message(ctx.message.channel, linkn) 
        except:
            await self.bot.send_message(ctx.message.channel, "You must have done something really bad.") 
        
        
        
        
        
        
        
   
    @commands.command(pass_context=True)
    async def clearRM(self,ctx):  #Fully optimized & function works
        role_RM=discord.utils.get(ctx.message.server.roles, id="340243113454993408")
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        isallowed=0
        for findl in range(1,len(f)):
            if f[findl].id=="340243113454993408": #ONLY RM MAY DO THIS
                isallowed=1
        if isallowed==0:
            await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord for this function")        
            return
        
        ch=self.bot.get_channel("350159777512423424") #3-4 discussion 350159777512423424   
        for ppr in range(0,50):
            deleted=await self.bot.purge_from(ch, limit=100)
        #ch=self.bot.get_channel("369962982408454144") #TTAR discussion 369962982408454144
        #for ppr in range(0,50):
        #    deleted=await self.bot.purge_from(ch, limit=100)
        #ch=self.bot.get_channel("401532930049966081") #Kyogre discussion 401532930049966081
        #for ppr in range(0,50):
        #    deleted=await self.bot.purge_from(ch, limit=100)
        ch=self.bot.get_channel("411197782448406536") #legendary discussion 411197782448406536  
        for ppr in range(0,50):
            deleted=await self.bot.purge_from(ch, limit=100)
        return
    
    @commands.command(pass_context=True)
    async def clearAR(self,ctx):  #Fully optimized & function works
        role_Admin=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        isallowed=0
        for findl in range(1,len(f)):
            if f[findl].id==self.Milkmaid:
                isallowed=1
        if isallowed==0:
            await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of raid information.  Contact a RaidObserver to gain access.")        
            return
        ch=self.bot.get_channel(self.raidsightings)
        meid=discord.utils.get(ctx.message.server.members, id=self.botid)
        for idx in range(0,50):
            arr=1
            #deleted=await self.bot.purge_from(ch, limit=100)
        msgg=await self.bot.send_message(ch,"To provide a raid notification for all trainers to see, simply type in %raid and " +meid.mention +" will ask you some questions about the raid.")
        await self.bot.pin_message(msgg)
    
    @commands.command(pass_context=True)
    async def genallids(self,ctx):  #Fully optimized & function works
        for idx in ctx.message.server.roles:
            print(idx.name + " " + idx.id)
    
    
    @commands.command(pass_context=True)
    async def checkexpraid(self,ctx):  #Fully optimized & function works
        await self.bot.send_message(ctx.message.channel,"This function has been removed")
        return
        try:
            await self.bot.wait_until_ready()
            #cron = CronTab('*/5 * * * * * *')
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles 
            channel=self.bot.get_channel(self.programid)
            chnot=self.bot.get_channel(self.genchid)
            self.Allroles=[]
            for x in self.Bossnotid+self.AddlNotiid+self.SilentRoles:
                self.Allroles.append(discord.utils.get(ctx.message.server.roles, id=x))
            print(self.Allroles)
            #await self.bot.send_message(channel, "HILLELFO" )#+ str(rrx.days))       
            maxpos=0
            Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
            Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
            Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
            
            while True:
                #try:
                cnnt=0
                text="Cron is working"
                for x in self.alllocch:
                    rrx=await subf.singlechan(self,x,self.Allroles[0],ctx)
                    if rrx==0:
                        ch=self.bot.get_channel(x)
                        #ch=self.bot.get_channel(ll)
                        cntt=0
                        await self.bot.edit_channel(ch, name='blank-' + str(0))
                        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
                            cntt+=1 #await self.bot.delete_message(message)
                        for ppr in range(0,cntt%100+1):
                            try:
                                deleted=await self.bot.purge_from(ch, limit=100)
                            except:
                                apr=1
                        for rra in self.Allroles:
                            if not rra==None:
                                rr=await subf.clearone(self,ch,rra)
                        
                    
                    #print(cnnt) 
                
                for x in self.allrbchms+self.PSgroupid:
                    try:
                        ch=self.bot.get_channel(x)
                        cntt=0
                        await self.bot.edit_channel(ch, name='blank-' + str(0))
                        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
                            cntt+=1 #await self.bot.delete_message(message)
                        for ppr in range(0,cntt%100+1):
                            try:
                                deleted=await self.bot.purge_from(ch, limit=100)
                            except:
                                arpp=1
                    except:
                        arpp=1
                async for message in self.bot.logs_from(self.bot.get_channel(self.genchid), limit=500): #Gets a list of the last 500 messages in the channel 
                    #print(message.content)
                    if message.content.startswith("__**Raid"): 
                        #Its raid notification and grab the time
                        a=message
                        arggn=a.content.split('\n')  #The second argument will be the minutes
                        argg=arggn[1].split(' ends at ')  #The second argument will be the minutes
                        endtt=argg[1]
                        endtt=endtt.split(' ')
                        endtt=endtt[0]
                        polltime = datetime.utcnow()+timedelta(hours=self.timez)
                        tpolltime=polltime.strftime('%I:%M:%S%p')
                        tdeltat = datetime.strptime(tpolltime, '%I:%M:%S%p')-datetime.strptime(endtt, '%I:%M:%S%p')

                        if tdeltat.days==0:
                            await self.bot.delete_message(message)
                
                await subf.storedata(self,Valor,Mystic,Instinct)

                print("Heartbeat for checkexpraid")        
                await asyncio.sleep(300)        
                        
                        
        except:
            await self.bot.send_message(channel, "The program failed")        
    
    #This function is not callable
    async def checkexpraidnow(self):  
        #try:
            
            await self.bot.wait_until_ready()
            channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
            server = self.bot.get_server(id=self.serverid)
            #server=channre.server
            #ctx=self.bot.get_message(channre,"532299638015918081")
            async for message in self.bot.logs_from(channre, limit=1): #Gets a list of the last 500 messages in the channel 
                ctx=message
            channel=self.bot.get_channel(self.programid)
            chnot=self.bot.get_channel(self.genchid)
            self.Allroles=[]
            for x in self.Bossnotid+self.AddlNotiid+self.SilentRoles:
                self.Allroles.append(discord.utils.get(server.roles, id=x))
            print(self.Allroles)
                   
            maxpos=0
            Valor=discord.utils.get(server.roles, id=self.valor)
            Mystic=discord.utils.get(server.roles, id=self.mystic)
            Instinct=discord.utils.get(server.roles, id=self.instinct)
            
            while True:
                #try:
                cnnt=0
                text="Cron is working"
                for x in self.alllocch:
                    rrx=await subf.singlechan(self,x,self.Allroles[0],ctx)
                    if rrx==0:
                        ch=self.bot.get_channel(x)
                        #ch=self.bot.get_channel(ll)
                        cntt=0
                        await self.bot.edit_channel(ch, name='blank-' + str(0))
                        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
                            cntt+=1 #await self.bot.delete_message(message)
                        for ppr in range(0,cntt%100+1):
                            try:
                                deleted=await self.bot.purge_from(ch, limit=100)
                            except:
                                apr=1
                        for rra in self.Allroles:
                            if not rra==None:
                                rr=await subf.clearone(self,ch,rra)
                        
                    
                    #print(cnnt) 
                
                for x in self.allrbchms+self.PSgroupid:
                    try:
                        ch=self.bot.get_channel(x)
                        cntt=0
                        await self.bot.edit_channel(ch, name='blank-' + str(0))
                        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
                            cntt+=1 #await self.bot.delete_message(message)
                        for ppr in range(0,cntt%100+1):
                            try:
                                deleted=await self.bot.purge_from(ch, limit=100)
                            except:
                                arpp=1
                    except:
                        arpp=1
                async for message in self.bot.logs_from(self.bot.get_channel(self.genchid), limit=500): #Gets a list of the last 500 messages in the channel 
                    #print(message.content)
                    if message.content.startswith("__**Raid"): 
                        #Its raid notification and grab the time
                        a=message
                        arggn=a.content.split('\n')  #The second argument will be the minutes
                        argg=arggn[1].split(' ends at ')  #The second argument will be the minutes
                        endtt=argg[1]
                        endtt=endtt.split(' ')
                        endtt=endtt[0]
                        polltime = datetime.utcnow()+timedelta(hours=self.timez)
                        tpolltime=polltime.strftime('%I:%M:%S%p')
                        tdeltat = datetime.strptime(tpolltime, '%I:%M:%S%p')-datetime.strptime(endtt, '%I:%M:%S%p')

                        if tdeltat.days==0:
                            await self.bot.delete_message(message)
                
                await subf.storedata(self,Valor,Mystic,Instinct)

                print("Heartbeat for checkexpraid" + str(datetime.utcnow()+timedelta(hours=self.timez)))        
                await asyncio.sleep(60)        
                        
                        
        #except:
        #    await self.bot.send_message(channel, "The program failed")
    
    
    @commands.command(pass_context=True)
    async def invite(self,ctx): #Anyone can use
        """Create a message with the invite link"""
        await self.bot.send_message(ctx.message.channel,"You can extend an invite to anyone in the world using the following weblink:\n http://tiny.cc/purduepogo or https://discordapp.com/invite/SwyDC2c")
        
    
    @commands.command(pass_context=True)
    async def edittime(self,ctx,timeold="",time=""): #RO/RT function only
        """Modify a time in a given raid channel.
        This function can only be used in a raid reservation channel.
        timeold --> The value for the minutes of the entry to be changed
        time --> HH:MM in __**24 hour format**__ for the new time to be added"""
        await self.bot.delete_message(ctx.message)
        if timeold=="" or time=="":
            await self.bot.send_message(ctx.message.author,"You didn't enter the command properly.  It should be\n `%edittime <timeold> <time>\ntimeold --> The value for the minutes of the entry to be changed\ntime --> HH:MM in __**24 hour format**__ for the new time to be added.`")
            return
        
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        isallowed=0
        for idx in f: 
            if idx.id==self.RaidTrainer or idx.id==self.RaidObserver:   
                isallowed=1
        if isallowed==0:
            await self.bot.send_message(ctx.message.author,"You must be a Raid Trainer or Raid Observer to add a time to this raid")
            return
        
        if not any(x==ctx.message.channel.id for x in self.allbutmtch): #It is a raid channel and the bot needs to allow this
            await self.bot.send_message(ctx.message.author,"You can only enter this function in a raid channel!")
            return
        
        #Now to allow time to be added - Verify a reasonable format
        argg=time.split(':')
        if len(argg)>2 or len(argg)<2:
            await self.bot.send_message(ctx.message.author,"Please enter the time in HH:MM format for the start time!")
            return
        if int(argg[0])<0 or int(argg[0])>23: 
            await self.bot.send_message(ctx.message.author,"Hour must be between 0 and 23, inclusive!")
            return
        if int(argg[1])<0 or int(argg[1])>59: 
            await self.bot.send_message(ctx.message.author,"Minute must be between 00 and 59, inclusive!")
            return
            
        
        specmess=0
        timehere=0
        chmsg1=None 
        chmsg2=None
        async for message in self.bot.logs_from(ctx.message.channel, limit=500): #Gets a list of the last 500 messages in the channel 
            if message.content.startswith("@Start:"):
                #See if the time has already been entered
                arggu=message.content.split(':')
                print(arggu)
                if int(arggu[2])==int(timeold):
                    chmsg1=message
        
        if chmsg1==None:
            await self.bot.send_message(ctx.message.author,"I couldn't find that raid time in the channel.")
            return
        
        #modify the time format
        ampm=""
        if int(argg[0])>12:
            argg[0]=str(int(argg[0])-12)
            ampm="PM"
        elif int(argg[0])==12:
            #argg[0]=str(int(argg[0])-12)
            ampm="PM"
        elif int(argg[0])<12:
            #argg[0]=str(int(argg[0])-12)
            ampm="AM"
        time=argg[0].zfill(2) + ":" + argg[1].zfill(2)+":00" + ampm
        
        #await self.bot.edit_message(chmsg1,"Non-standard start times:")
        await self.bot.edit_message(chmsg1,"@Start: "+time)
        return
        
        
        return
        
        
        
    @commands.command(pass_context=True)
    async def addtime(self,ctx,time): #RO/RT function only
        """Add an additional time to a given raid channel.
        This function can only be used in a raid reservation channel.
        time --> HH:MM in __**24 hour format**__ for the new time to be added"""
        #return
        #Verify the person is RT/RO
        await self.bot.delete_message(ctx.message)
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        isallowed=0
        for idx in f: 
            if idx.id==self.RaidTrainer or idx.id==self.RaidObserver:   
                isallowed=1
        if isallowed==0:
            await self.bot.send_message(ctx.message.author,"You must be a Raid Trainer or Raid Observer to add a time to this raid")
            return
        
        if not any(x==ctx.message.channel.id for x in self.allbutmtch): #It is a raid channel and the bot needs to allow this
            await self.bot.send_message(ctx.message.author,"You can only enter this function in a raid channel!")
            return
        
        #Now to allow time to be added - Verify a reasonable format
        argg=time.split(':')
        if len(argg)>2 or len(argg)<2:
            await self.bot.send_message(ctx.message.author,"Please enter the time in HH:MM format for the start time!")
            return
        if int(argg[0])<0 or int(argg[0])>23: 
            await self.bot.send_message(ctx.message.author,"Hour must be between 0 and 23, inclusive!")
            return
        if int(argg[1])<0 or int(argg[1])>59: 
            await self.bot.send_message(ctx.message.author,"Minute must be between 00 and 59, inclusive!")
            return
        if int(argg[0])<12:
            await self.bot.send_message(ctx.message.channel,"Did you mean \n__**(1):**__ "+ argg[0] + ":" + argg[1]+ "AM or \n__**(2):**__"+ argg[0] + ":" + argg[1]+ "PM?")
            msgrt = await self.bot.wait_for_message(timeout = 30, author = ctx.message.author, channel = ctx.message.channel)
            if msgrt.content=="1":
                argg[0]=str(int(argg[0]))
            elif msgrt.content=="2":
                argg[0]=str(int(argg[0])+12)
        
        specmess=0
        timehere=0
        chmsg1=None 
        chmsg2=None
        async for message in self.bot.logs_from(ctx.message.channel, limit=500): #Gets a list of the last 500 messages in the channel 
            print(message.content)
            if message.content.startswith("Non-standard start times:"):
                specmess=1
                await self.bot.send_message(ctx.message.author,"A non-standard start time has already been entered! Use `%edittime` to remove the reaction and edit a start time.")
                return
            if message.content.startswith("@Start:"):
                #See if the time has already been entered
                arggu=message.content.split(':')
                #print(arggu)
                if int(arggu[1])==int(argg[0]) and int(arggu[2])==int(argg[1]):
                    specmess=1
                    await self.bot.send_message(ctx.message.author,"That time has already been entered!")
                    return
            if message.content.startswith("_Use `%addtime` to create a new time_"):
                #and %addtime hasn't been used yet
                chmsg1=message
            if message.content.startswith("_^^^^^^^^^^^^^_"):
                #and %addtime hasn't been used yet
                chmsg2=message
        
        if chmsg1==None or chmsg2==None:
            await self.bot.send_message(ctx.message.author,"A non-standard start time has already been entered! Use %edittime to remove the reaction and edit a start time.")
            return
        
        #Get the name of this channel and see if there is an additional channel
        chnid=ctx.message.channel.id
        arggx=ctx.message.channel.name.split('---')
        found=await subf.findchidloca2(self,await subf.filtNameval(self,arggx[0]))
        #If the channel is a raid boss specific channel, the second channel will lead with the raid boss
        if found==1:
            raidboss=arggx[1]
            location=arggx[0]
            namel2=raidboss + "---" +  location
            newname2=raidboss + "---" +  location
            newname1=location + "---" +  raidboss 
        else:
            raidboss=arggx[0]
            location=arggx[1]
            namel2=location + "---" +  raidboss
            newname2=location + "---" +  raidboss 
            newname1=raidboss + "---" +  location                 

        #Boss should be in the system unless its an addlnotify raid
        channel1 = ctx.message.channel
        channel2 = discord.utils.get(ctx.message.server.channels, name=namel2)  
        
        #modify the time format
        ampm=""
        if int(argg[0])>12:
            argg[0]=str(int(argg[0])-12)
            ampm="PM"
        elif int(argg[0])==12:
            #argg[0]=str(int(argg[0])-12)
            ampm="PM"
        elif int(argg[0])<12:
            #argg[0]=str(int(argg[0])-12)
            ampm="AM"
        time=argg[0].zfill(2) + ":" + argg[1].zfill(2)+":00" + ampm
        
        await self.bot.edit_message(chmsg1,"Non-standard start times:")
        await self.bot.edit_message(chmsg2,"@Start: "+time)
        return
        
        if specmess==0:
            await self.bot.send_message(channel1,"Non-standard start times:")
            try:
                await self.bot.send_message(channel2,"Non-standard start times:")
            except: 
                a=1
        #See if time has been added yet
        
        
        
        
        
        
        #Now add the time
        await self.bot.send_message(channel1,"@Start: "+time)
        try:
            await self.bot.send_message(channel2,"@Start: "+time)
        except: 
            a=1
        
        await self.bot.delete_message(ctx.message)
        
        
    @commands.command(pass_context=True)
    async def guide(self, ctx): #This will guide a user through the setup proces
        #try:
            if not ctx.message.channel.is_private==True:
                await self.bot.send_message(ctx.message.channel,"Sorry, you need to DM that command to me. Click on my name and send me a message.")
                return
            server=self.bot.get_server(self.serverid)
            memberr=discord.utils.get(server.members, id=ctx.message.author.id)
            await self.bot.send_message(ctx.message.author,"Hey, Traveller! I'm Purdue Pollster, and I'm gonna help get you set up to raid.  Just follow me through the process as I send you messages. Are you ready (Y/N)?")
            g3=0
            a3=0
            while g3==0 and a3<3:
                msgrt = await self.bot.wait_for_message(timeout = 3600*24*30, author = ctx.message.author, channel = ctx.message.channel)
                if msgrt.content.upper()=="N":
                    await self.bot.send_message(ctx.message.author,"Looks like you didn't need the help after all! Have a good one.")
                    return
                elif msgrt.content.upper()=="Y":
                    await self.bot.send_message(ctx.message.channel,"Awesome! Let's get started. Follow me to the setup channel within the " + self.servername + " Discord. I just tagged you there!")
                    g3=1
                else:
                    await self.bot.send_message(ctx.message.channel,"Something didn't seem right there. Try again")
                    a3+=1
                if a3>2:
                    await self.bot.send_message(ctx.message.channel,"Looks like you're not entering what I ask. I'm always here to help if you want it.")
                    return
            ch=self.bot.get_channel(self.setupch) #Pokesight alert
            #ch=self.bot.get_channel(self.programid) #Pokesight alert
            good=0
            att=0
            while good==0:
                await self.bot.send_message(ch,ctx.message.author.mention + ", you need to enter you trainer level here to make a raid reservation.  Just type in `%level XX` with XX being replaced by your trainer level.  (Ex. %level 26)")
                await self.bot.wait_for_message(timeout = 3600*24*30, author = ctx.message.author, channel = ch)
                
                await asyncio.sleep(5)
                #See if the level file exists
                try:
                
                    uname=memberr.display_name
                    uname=uname+str(memberr.discriminator)
                    print(uname)
                    df = pd.read_excel('ExcelFiles' + "\\" + uname + 'level.xlsx')
                    #await subf.levelhelper(self,ctx.message,level)
                    good=1
                except:
                    await self.bot.send_message(ch,"Something didn't seem right there. Try again")
                    att+=1
                if att>2:
                    await self.bot.send_message(ch,"Looks like you're not entering what I ask. I'm always here to help if you want it.")
                    return
            #ch=self.bot.get_channel("403939414977413122") #raid alert
            ch=self.bot.get_channel(self.setupch) #Pokesight alert
            #ch=self.bot.get_channel(self.programid) #Pokesight alert
            await self.bot.send_message(ch,ctx.message.author.mention + ", it looks like you're all ready to go.  You can sign up for as many or as few notifications as you would like.  If you need further help on using the system, type in `%helpme`.  Good luck, traveller! Dont forget to sign up for raid roles to see active raids.")
            return
            return
            good=0
            att=0
            while good==0:
                await self.bot.send_message(ch,ctx.message.author.mention + ", to see any raids, now you'll need to sign up for some raid notifications.  `?raids` will let you see all of the raid bosses.  `?raid RAIDBOSSNAME` will sign you up for a raid boss (ex. `?raid Level5`).  Entering the same raid boss again, will remove you from the notification.  \n\n__**Sign up for Level5 raid boss alerts by typing in `?raid Level5`**__")
                re=await self.bot.wait_for_message(timeout = 3600*24*30, author = ctx.message.author, channel = ch)
                await asyncio.sleep(3)
                #See if the level file exists
                #try:
                #Test if this member is has role level5
                rr2=discord.utils.get(ch.server.roles, id=self.L5Notify)
                member = discord.utils.get(ch.server.members, name=re.author.name)
                b=discord.Server.get_member(ch.server,re.author.id)
                f=b.roles
                print (f)
                if rr2 in f:
                    good=1
                else:
                    await self.bot.send_message(ch,"Doesn't look like you signed up for Level 5 notifications")
               
                if att>2:
                    await self.bot.send_message(ch,"Looks like you're not entering what I ask. I'm always here to help if you want it.")
                    return
            #await self.bot.send_message(ch,"Done ")
            await self.bot.send_message(ch,ctx.message.author.mention + ", it looks like you're all ready to go.  You can sign up for as many or as few notifications as you would like.  If you need further help on using the system, type in `%helpme`.  Good luck, traveller!")
            return
            g3=0
            a3=0
            while g3==0 and a3<3:
                msgrt = await self.bot.wait_for_message(timeout = 3600*24*30, author = ctx.message.author, channel = ctx.message.channel)
                print(msgrt.content)
                if msgrt.content=="N":
                    await self.bot.send_message(ctx.message.author,"Looks like you didn't need the help after all! Have a good one.")
                    return
                elif msgrt.content=="Y":
                    await self.bot.send_message(ctx.message.channel,"Awesome! Let's get started.")
                    g3=1
                else:
                    await self.bot.send_message(ctx.message.channel,"Something didn't seem right there. Try again")
                    a3+=1
                if a3>2:
                    await self.bot.send_message(cta.message.channel,"Looks like you're not entering what I ask. I'm always here to help if you want it.")
                    return   
    
    @commands.command(pass_context=True)
    async def setupmewtwo(self,ctx,location,date,time):
        """Location is based on the first 8 letters of the Pokemon Go gym name
           Enter the date in MM/DD/YY format
           Time should contain the leading zeros (i.e. 09:45 if 9:45am, or 15:30 if 3:30pm)
        """
        
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        for findl in range(1,len(f)):
            #try: #await self.bot.send_message(ctx.message.channel,f[findl].id + "&" + self.RaidObserver)
                if f[findl].id==self.RaidObserver:
                    #Find the last channel in the list
                    maxpos=0
                    for x in range(0,len(self.mewtwo)):
                        ch=self.bot.get_channel(self.mewtwo[x])
                        g=ch.position
                        #await self.bot.send_message(ctx.message.channel,g)
                        if g>maxpos:
                            maxpos=g
                            MTchan=x
                    
                    cntt=0
                    uniq=0
                    if len(location)<8:
                        for x in range(0,8-len(location)):
                            location=location + " "
                    loc=location[0:8]
                    for x in self.altname:
                        if loc.upper()==x.upper():
                            uniq=uniq+1
                            Nameval=self.channame[cntt]
                            IDval=self.chanid[cntt]
                            linkn=self.links[cntt]
                            linkn="Directions to this gym can be found here:\n" + "https://www.google.com/maps/place/" + linkn + ""
                            #break
                        cntt=cntt+1
                    
                    if uniq<1:
                        optnum=1
                        cntt=0
                        ncha=0
                        Nameval=''
                        
                        for x in self.chanshort:
                            if loc.upper()==x.upper():
                                Nameval=Nameval + str(optnum) + ")" + self.channame[cntt] + ": Use '" + self.altname[cntt] + "'\n"
                                optnum=optnum+1
                                ncha=ncha+1
                                #IDval=self.chanid[cntt]
                                #linkn=self.links[cntt]
                                #linkn="Directions to this gym can be found here:\n" + "https://www.google.com/maps/place/" + linkn + ""
                                #break
                            cntt=cntt+1
                        
                    
                        if ncha==0:  #Channel name isn't in alt or shortname
                            await self.bot.say("`The gym name you entered is not available in the system`")
                            break
                        elif ncha>1: #Unique Channel name doesn't exist
                            await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by typing the number:\n")
                            await self.bot.say("`{}`".format(Nameval))
                            break
                    Origname=Nameval
                    Nameval = Nameval.replace(' ', '-').lower()
                    Nameval = Nameval.replace('+', '').lower()
                    Nameval = Nameval.replace("'", '').lower()
                    Nameval = Nameval.replace(".", '').lower()
                    #Nameval = Nameval.replace(' ', '-').lower()
                    #Nameval = Nameval.replace(' ', '-').lower()
                    
                    await self.bot.move_channel(self.bot.get_channel(self.mewtwo[MTchan]), 0)
                    await self.bot.edit_channel(self.bot.get_channel(self.mewtwo[MTchan]), name='Mewtwo-at-' + Nameval)
                    await self.bot.send_message(self.bot.get_channel(self.mewtwo[MTchan]),linkn)
                    argg=time.split(':')
                    str_time=datetime.strptime(argg[0] + ":" + argg[1] + ":0", '%H:%M:%S')-datetime.strptime("0:0:0", '%H:%M:%S')
                    addlstr="\n\n The CP for a 100IV " + "MEWTWO" + " is " + str(2275)
                    for x in range (0,5):
                        await self.bot.send_message(self.bot.get_channel(self.mewtwo[MTchan]),'Start Time: ' + str(str_time) + " on " + date)
                        str_time += timedelta(minutes=10)
                    await self.bot.send_message(self.bot.get_channel(self.mewtwo[MTchan]), "`" + "MEWTWO" + " RAID BOSS ALERT!\n" + "A " + "MEWTWO" + " raid boss/egg was spotted at " + Origname + ".\nReact to a given time to participate in this raid. \nPlease be courteous to others since they are depending on you being there too!`" + addlstr)
                    
                    #await self.bot.send_message(ctx.message.channel,"You are a raid observer.")
                    break
        
        #str_time = datetime.utcnow()+timedelta(hours=self.timez)
        #str_time += timedelta(minutes=45)
        #argg=timeleft.split(':')
        #str_time += timedelta(minutes=int(argg[0]))
        #str_time += timedelta(seconds=int(argg[1]))
        #str_time = str_time.strftime('%H:%M:%S')
        
        #await self.bot.move_channel(self.bot.get_channel(IDval), self.numChannels)
        #await self.bot.send_message(self.bot.get_channel(IDval),linkn)
        #for x in range(0,5):
            
            
        #    await self.bot.send_message(self.bot.get_channel(IDval),'Start Time: ' + tpoll)
        #    await asyncio.sleep(0.5)
        #    polltime += timedelta(minutes=10)
        #    tpoll = polltime.strftime('%H:%M:%S')
        
        
        #await self.bot.send_message(ctx.message.channel, "`" + "MEWTWO" + " RAID BOSS ALERT!\n" + "A " + "MEWTWO" + " raid boss/egg was spotted at " + "FiveBucks (Lafayette)" + ".\nReact to a given time to participate in this raid. \nPlease be courteous to others since they are depending on you being there too!`")
        #for x in range (0,5):
        #    await self.bot.send_message(ctx.message.channel,'Start Time: ' + "12:00pm " + " on " + "10/27/17")
        #await self.bot.send_message(ctx.message.channel,'Start Time: ' + "12:00pm " + " on " + "10/27/17")
        #await self.bot.send_message(ctx.message.channel,'Start Time: ' + "12:00pm " + " on " + "10/27/17")
        #await self.bot.send_message(ctx.message.channel,'Start Time: ' + "12:00pm " + " on " + "10/27/17")
        #await self.bot.send_message(ctx.message.channel,'Start Time: ' + "12:00pm " + " on " + "10/27/17")
        #await self.bot.send_message(ctx.message.channel,'Start Time: ' + "12:00pm " + " on " + "10/27/17")
    
    @commands.command(pass_context=True)
    async def removemewtwo(self,ctx): 
        #This will hide the channel, but not delete it
        maxpos=0
        for x in range(0,len(self.mewtwo)):
            ch=self.bot.get_channel(self.mewtwo[x])
            g=ch.position
            #await self.bot.send_message(ctx.message.channel,g)
            if ch.id==ctx.message.channel.id:
                #maxpos=g
                MTchan=x
        await self.bot.edit_channel(ctx.message.channel, name='blank' + str(MTchan))
        deleted=await self.bot.purge_from(ctx.message.channel, limit=50)
    
    @commands.command(pass_context=True)
    async def execute(self, ctx, text): #Ready for publication
    #execute is a function to allow easter eggs to be used and potentially tag someone within the discord.
        #stuff = dataIO.load_json("configuration/eastereggs.txt")
        #self.EAchannels=stuff["L5types"]
        #self.L5types=stuff["L5types"]
        #self.L5types=stuff["L5types"]
        #self.L5types=stuff["L5types"]
        #self.EAchannels=["284568059107344386","284614711121674240"] #channel ids to allow easter eggs regardless
        #self.EAcommands=["ORDER","GYM","BANNED","FLOOF","CHRISTONABORK","RICKROLL","INSTINCT","BELDUMB","BORK","ABSOL","CHRISTONABIKE"] #These are the key words for %execute
        #self.EAuserids=["211862221225984000","0","0","0","0","147553893310660612","0","343017572763172865","0","147553893310660612","0"] #Tag a single user when the execute command is used
        #self.EAfilename=['order66.png','PR.gif','samuel-l-jackson-banned.gif','FLOOF.png','christonabork.gif','rickroll.gif','thes.jpg','beldum.jpg','killbork.gif','absol.jpg','christ.gif']  #Filenames of the images 
        #self.EAminacclvl=["1","0","0","0","0","0","1","1","1","1","1"]
        
        allow=0
        for x in self.EAchannels:  #If the message is in an Easter-egg allowable channel, set access to 1
            if ctx.message.channel.id==x:
                allow=1
        if ctx.message.channel.id in self.allraidch:  #If within a raid channel, always allow the function to be used
            allow=2
        if ctx.message.author.id==self.CMK:  #If admin, always allow the function to be used
            allow=2
        
        
        for x in range(0,len(self.EAcommands)):
            if self.EAcommands[x].upper()==text.upper(): #If a command matches a preset command
                if allow>=int(self.EAminacclvl[x]): # execute the command if access level is high enough
                    with open(self.EAfilename[x], 'rb') as f:  #Grab the filename first
                        await self.bot.send_file(ctx.message.channel, f) #send the file to the channel of the command
                        if not self.EAuserids[x]=="0":  #If the user id is not equal to "0", tag the user
                            b=discord.Server.get_member(ctx.message.server,self.EAuserids[x]) 
                            await self.bot.send_message(ctx.message.channel,b.mention)
        await self.bot.delete_message(ctx.message) #delete any trace of the original message
                
                    
    @commands.command(pass_context=True)
    async def oldexecute(self, ctx, text): #Nearly Optimized
        allow=0
        if ctx.message.channel.id=="284568059107344386" or ctx.message.channel.id=="284614711121674240":
            allow=1
        if ctx.message.channel.id in self.allraidch:
            allow=2
        if ctx.message.author.id==self.CMK:
            allow=2
        if allow>0:
            if text.upper()=="ORDER":
                with open('order66.png', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    b=discord.Server.get_member(ctx.message.server,"211862221225984000")
                    await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
        if allow>=0:
            if text.upper()=="GYM":
                with open('PR.gif', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    #b=discord.Server.get_member(ctx.message.server,"211862221225984000")
                    #await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
            if text.upper()=="BANNED":
                with open('samuel-l-jackson-banned.gif', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    #b=discord.Server.get_member(ctx.message.server,"211862221225984000")
                    #await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
            if text.upper()=="FLOOF":
                with open('FLOOF.png', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    #b=discord.Server.get_member(ctx.message.server,"211862221225984000")
                    #await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
        if allow>=0:
            if text.upper()=="CHRISTONABORK":
                with open('christonabork.gif', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    #b=discord.Server.get_member(ctx.message.server,"211862221225984000")
                    #await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
            if text.upper()=="RICKROLL":
                with open('rickroll.gif', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    b=discord.Server.get_member(ctx.message.server,"147553893310660612")
                    await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
        if allow==2:
            if text.upper()=="INSTINCT":
                with open('thes.jpg', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    #b=discord.Server.get_member(ctx.message.server,"286714847989858305")
                    #await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
            if text.upper()=="INSTINCT2":
                with open('thes.jpg', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    #b=discord.Server.get_member(ctx.message.server,"329466745263882240")
                    #await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
            if text.upper()=="BELDUMB":
                with open('beldum.jpg', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    b=discord.Server.get_member(ctx.message.server,"343017572763172865")
                    await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
            if text.upper()=="BORK":
                with open('killbork.gif', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    #b=discord.Server.get_member(ctx.message.server,"182282837284749312")
                    #await self.bot.send_message(ctx.message.channel,b.mention)
                    await self.bot.delete_message(ctx.message)
            if text.upper()=="ABSOLEY1":
                #if ctx.message.author.id==self.CMK:
                await self.bot.delete_message(ctx.message)
                with open('absol.jpg', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    b=discord.Server.get_member(ctx.message.server,"147553893310660612")
                    await self.bot.send_message(ctx.message.channel,b.mention)
                    
                #else:
                #    await self.bot.send_message(ctx.message.channel,"Purdue Pollster hates dogs")
                #    await self.bot.delete_message(ctx.message)
            if text.upper()=="CHRISTONABIKE":
                with open('christ.gif', 'rb') as f:
                    await self.bot.send_file(ctx.message.channel, f)
                    await self.bot.delete_message(ctx.message)
    
    
    
    #This program allows for trainers to specify their level
    
    @commands.command(pass_context=True)
    async def level(self, ctx, level): #Optimized
        await subf.levelhelper(self,ctx.message,level)
        return
        
    

    @commands.command(pass_context=True)
    async def checklevel(self, ctx): #Nearly Optimized
        #await self.bot.process_commands(ctx.message) or ctx.message.channel.id=='284552964352245760'
        await subf.checklevelhelper(self,ctx.message)
        return
        chv=self.bot.get_channel('403939414977413122')
        try:
            if not (ctx.message.channel.id==self.programid or ctx.message.channel.id=='351944459115560991' or ctx.message.channel.id=='403939414977413122'):
                await self.bot.delete_message(ctx.message)
                await self.bot.send_message(chv,ctx.message.author.mention +", enter that command over here!")
                return
            uname=ctx.message.author.display_name
            uname=uname+str(ctx.message.author.discriminator)
            try:
                newlev=float(level)
                newlev=int(newlev)
                posid=min(40,max(newlev,1))
                #open the sheet and see if the person exists
                try: #If the sheet exists, open it 
                    df = pd.read_excel('ExcelFiles' + "\\" + uname + 'level.xlsx')
                    currlev=df.iloc[0,0]
                    df.loc[0]=posid    
                    writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", your level has been changed from " + str(currlev) + " to " + str(posid))
                except: #The person hasn't established a level yet
                    df = pd.read_excel('ExcelFiles' + "\\" + 'level' + '.xlsx')
                    df.loc[0]=posid    
                    writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", your new assigned level is " + str(posid))
            except:
                await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name +", please stop being an idiot and enter a number already!")
        except:
            arpr=10    
    
    
    @commands.command(pass_context=True)
    async def hidech(self,ctx):  #Function is depricated
        #try:
            #await self.bot.send_message(ctx.message.channel,"This command no longer exists!")
            #return
            await self.bot.delete_message(ctx.message)
            if not ctx.message.channel.id in self.allbutmtch:
                print (ctx.message.channel.id)
                return
            print("Here.")
            member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles 
            cnnt=0
            for findl in f:
                if findl.id==self.POGOmod or findl.id==self.RaidManager:
                    #ch=self.bot.get_channel(ll)
                    cntt=0
                    ch=ctx.message.channel
                    async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
                        cntt+=1 #await self.bot.delete_message(message)
                    for ppr in range(0,cntt%100+1):
                        deleted=await self.bot.purge_from(ch, limit=100)
                    await self.bot.edit_channel(ch, name='blank-' + str(0))
                    for x in self.Bossnotid+self.AddlNotiid+[self.SilentL3,self.SilentL4,self.SilentL5,self.SilentPS,self.SilentEX]:
                        rra=discord.utils.get(ctx.message.server.roles, id=x)
                        if not rra==None:
                            rr=await subf.clearone(self,ctx.message.channel,rra)
                        cnnt+=1
                        print(cnnt)
                    
                    return 
    
    
    @commands.command(pass_context=True)
    async def getallIDS(self,ctx):  #Function is depricated
        #for x in 
        a=1
    
    
    @commands.command(pass_context=True)
    async def showall45(self,ctx):  #Function is depricated
        try:
            #await self.bot.send_message(ctx.message.channel,"This command no longer exists!")
            #return
            member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles
            #role_everyone=discord.utils.get(ctx.message.server.roles, id=self.Approved)  
            #role_everyone2=discord.utils.get(ctx.message.server.roles, id=self.RaidTrainer)  
            role_everyone3=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)  
            for findl in f:
                if findl.id==self.Milkmaid:
                    #rr=await subf.clearset(self,self.allbutmtch,role_everyone)
                    #rr=await subf.showset(self,self.allbutmtch,role_everyone2)
                    rr=await subf.showset(self,self.alllocch+self.oldchan,role_everyone3)
                    return
        except:
            arpr=10
    
    @commands.command(pass_context=True)
    async def quote(self,ctx,mid):  #Function is depricated
        #if not ctx.message.author.id=="345200594421547018":
        #    await self.bot.send_message(ctx.message.channel,"I'm not listening to you.  I listen only to Master Stinkwad")
        #    return
        a=await self.bot.get_message(ctx.message.channel, mid)
        await self.bot.send_message(ctx.message.channel,"`'"+a.content+"'` - `"  +a.author.name+"`")
        #await self.bot.delete_message(a)
    
    @commands.command(pass_context=True)
    async def hideall45(self,ctx):  #Function is depricated
        #try:
            #await self.bot.send_message(ctx.message.channel,"This command no longer exists!")
            #return
            member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles
            #role_everyone=discord.utils.get(ctx.message.server.roles, id=self.Approved)  
            #role_everyone2=discord.utils.get(ctx.message.server.roles, id=self.RaidTrainer)  
            role_everyone3=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)  
            for findl in f:
                if findl.id==self.Milkmaid:
                    #rr=await subf.clearset(self,self.allbutmtch,role_everyone)
                    #rr=await subf.showset(self,self.allbutmtch,role_everyone2)
                    rr=await subf.hideset(self,self.alllocch+self.oldchan,role_everyone3)
                    return
        #except:
        #    arpr=10 
        
    
    @commands.command(pass_context=True)
    async def revokestrike(self, ctx, user):
        """Use this command to issue a strike to someone on the discord
        user  --> the @DiscordUser Tag"""
        aa=1
        if aa==1:
        #try:
            if not (ctx.message.channel.id=="284600376148099072" or ctx.message.channel.id=="403550523984183296" or ctx.message.channel.id=="429291825212293130"):
                await self.bot.send_message(ctx.message.channel,"Ummm, you can't do that command here.")
                await self.bot.delete_message(ctx.message)
                return
            print(user)
            print(user)
            if "!" in user:
                userf=discord.Server.get_member(ctx.message.server,user[3:len(user)-1])
            else:
                userf=discord.Server.get_member(ctx.message.server,user[2:len(user)-1])
            uname=userf.display_name
            await self.bot.send_message(ctx.message.channel,uname + " has been deactivated.")
    
    @commands.command(pass_context=True)
    async def strike(self, ctx, user, *, reason : str):
        """Use this command to issue a strike to someone on the discord
        user  --> the @DiscordUser Tag
        reason--> The reason for issuing a strike"""
        aa=1
        if aa==1:
        #try:
            if not (ctx.message.channel.id=="284600376148099072" or ctx.message.channel.id=="403550523984183296" or ctx.message.channel.id=="429291825212293130"):
                await self.bot.send_message(ctx.message.channel,"Ummm, you can't do that command here.")
                await self.bot.delete_message(ctx.message)
                return
            #if ctx.message.author.id=="330830919604633604":
            #    await self.bot.send_message(ctx.message.channel,"You have been a pleb and can no longer use the %strike command.")
            #    return
            print(user)
            if "!" in user:
                userf=discord.Server.get_member(ctx.message.server,user[3:len(user)-1])
            else:
                userf=discord.Server.get_member(ctx.message.server,user[2:len(user)-1])
            uname=userf.display_name
            #if uname=="MrMasterMiltank" or uname=="Purdue Pollster":
            if uname=="Purdue Pollster":
                await self.bot.send_message(ctx.message.channel,"You can't harm Master Stinkpot or me.")
                return
            #must be a ranger or milk maid to use this
            member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles
            Ranger=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
            MilkMaid=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
            isallowed=0
            if Ranger in f:
                isallowed=1
            if MilkMaid in f:
                isallowed=1 
            if isallowed==0:
                await self.bot.send_message(ctx.message.channel,"You do not have a role on this Discord that allows entry of strike information. Please let a Ranger or RaidManager know if you had a problem at a raid.")
                return 
            #if ctx.message.author.id=="270022947513565184":
            #    await self.bot.send_message(ctx.message.channel,"I won't listen to you doofus!")
            #    return
            #uname=uname+str(ctx.message.author.discriminator)
            #ap=10
            #if ap==10:
            str_time = datetime.utcnow()+timedelta(hours=self.timez)
            str_time = str_time.strftime('%m/%d/%y %H:%M:%S')
            try: #If the sheet exists, open it 
                df = pd.read_excel('Strikes' + "\\" + uname + 'Strikes.xlsx')
                #df2=df[0]
                #df.append=[str_time    ,ctx.message.author.name,reason]
                df.loc[df.shape[0]]=[str_time    ,ctx.message.author.name,reason]
                #df.iat[df.shape[0],1]=ctx.message.author.name  
                #df.iat[df.shape[0],2]=reason 
                writer = pd.ExcelWriter('Strikes' + "\\" +uname + 'Strikes.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                    #print('Here99',df.iat[0,0],df.iat[0,0])
                #print(df)    
            #else:
            except: #The person hasn't established a level yet
                df = pd.read_excel('Strikes' + "\\" + 'Strikes' + '.xlsx')
                df.iloc[0,0]=str_time
                df.iloc[0,1]=ctx.message.author.name 
                df.iloc[0,2]=reason             
                writer = pd.ExcelWriter('Strikes' + "\\" +uname + 'Strikes.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
            await self.bot.send_message(ctx.message.channel,"The strike has been issued.")    
        else:
        #except:
            await self.bot.send_message(ctx.message.channel,"The user name must be in the form of a tag.")
    
    @commands.command(pass_context=True)
    async def strikes(self, ctx, user):
        """Use this command to view strikes issued to someone on the discord
        user  --> the @DiscordUser Tag"""
        if not (ctx.message.channel.id=="284600376148099072" or ctx.message.channel.id=="403550523984183296"):
            await self.bot.send_message(ctx.message.channel,"Ummm, you can't do that command here.")
            await self.bot.delete_message(ctx.message)
            return
        print (user)
        if "!" in user:
            userf=discord.Server.get_member(ctx.message.server,user[3:len(user)-1])
        else:
            userf=discord.Server.get_member(ctx.message.server,user[2:len(user)-1])
        uname=userf.display_name
        #must be a ranger or milk maid to use this
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        Ranger=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
        MilkMaid=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
        isallowed=0
        if Ranger in f:
            isallowed=1
        if MilkMaid in f:
            isallowed=1 
        if isallowed==0:
            await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of strike information. Please let a Ranger or RaidManager know if you had a problem at a raid.")
            return 
        #uname=uname+str(ctx.message.author.discriminator)
        #ap=10
        #if ap==10:
        str_time = datetime.utcnow()+timedelta(hours=self.timez)
        str_time = str_time.strftime('%m/%d/%y %H:%M:%S')
        try: #If the sheet exists, open it 
            msg="`      Date/Time         Issued By          Reason\n"
            df = pd.read_excel('Strikes' + "\\" + uname + 'Strikes.xlsx')
            for idx in range(0,df.shape[0]):
                msg+=df.iat[idx,0] + " " + df.iat[idx,1] + "      " + df.iat[idx,2]+ " \n"
            
            #df=df.replace({r'\\n': ''}, regex=True)
            #msg+=df
            msg+="`"
            #df.loc[df.shape[0]]=[str_time    ,ctx.message.author.name,reason]
            #df.iat[df.shape[0],1]=ctx.message.author.name  
            #df.iat[df.shape[0],2]=reason 
            await self.bot.send_message(ctx.message.channel,msg) 
        #else:
        except: #The person hasn't established a level yet
            await self.bot.send_message(ctx.message.channel,"This person has no strikes.") 
    
    @commands.command(pass_context=True)
    async def exraid(self, ctx):
        """Create a new raid announcement!"""
        mutelist=[]
        a11=1
        if a11==1:
        #try:
            alltimeout=30
            if not (ctx.message.channel.id==self.raidsightings or ctx.message.channel.id==self.programid or ctx.message.channel.id=="408330312125382656"):# or ctx.message.channel.id==self.raidsightings or      ctx.message.channel.id==self.RaidNotifier):
                chh=self.bot.get_channel(self.raidsightings)
                await self.bot.send_message(ctx.message.channel,"Sorry, trainer. Please go to "+chh.mention+"  to enter this command.")
                return
            #await self.bot.send_message(ctx.message.channel,"A system update is being performed.  Data entry will be enabled in 5 minutes.")
            #return
            member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles
            isRO=0
            for findl in range(1,len(f)):
                if f[findl].id==self.RaidObserver:
                    isRO=1
                    break
            
            try:
                await asyncio.sleep(0.5)
                attempt=0
                success=0
                extra="Looks like you're trying to tell everyone about an Ex-Raid. If you need to quit at any time, press `q`.\n"
                while attempt<3 and success==0:
                    await self.bot.send_message(ctx.message.channel,extra+"__**What is the Pokemon Go gym name?**__ \nYou only need the first 8 letters without spaces or special characters (i.e. A+ Storage Mural = astorage)")
                    extra=""
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    location=msgrt.content
                    newloca=location
                    if "%exraid" in location:
                        await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                        return
                    if msgrt.content.upper()=="Q": 
                        await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                        return
                    cntt=0
                    uniq=0
                    grid=0
                    dontcont=0
                    if len(location)<8:
                        for x in range(0,8-len(location)):
                            location=location + " "
                    loc=location[0:8]
                    
                    for x in self.sngroup:
                        if loc.upper()==x.upper():
                            uniq=uniq+1
                            Nameval=self.cngroup[cntt]
                            #linkn=self.lngroup[cntt]
                            gymlat=self.latgroup[cntt]
                            gymlon=self.longroup[cntt]
                            linkn= "" + gymlat + "," + gymlon +""+ ""
                            olink=linkn
                            #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                        cntt=cntt+1
                    cntt=0
                    
                    if uniq>1:
                        optnum=1
                        cntt=0
                        ncha=0
                        LVal=[]
                        Nameval=''
                        for x in self.sngroup:
                            if loc.upper()==x.upper():
                                Nameval=Nameval + str(optnum) + ")" + self.cngroup[cntt] + "\n"#": Use '" + self.angroup[cntt] + "'\n"
                                LVal.append(self.angroup[cntt])
                                optnum=optnum+1
                                ncha=ncha+1
                            cntt=cntt+1
                    
                        if ncha==0:  #Channel name isn't in alt or shortname  
                            await self.bot.say("`The gym name you entered is not available in the system`")
                            dontcont=1
                            attempt+=1
                            #return
                        elif ncha>1: #Unique Channel name doesn't exist
                            await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.say("`{}`".format(Nameval))
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                            try:
                                loc=LVal[int(msgrt.content)-1]
                                #print(loc)
                            except:
                                attempt+=1
                                dontcont=1
                                #return
                    elif uniq==0: #see if keyword
                        scrubmess=await subf.filtNameval(self,location.upper())          
                        locn=""
                        #Try finding the names of the gyms
                        loclist=[]
                        for x in self.WL:
                            if x.upper() in location.upper(): 
                                loclist.append(x)
                        #Xref the list with the gym names
                        possn=[]
                        maxcom=0
                        gyml=""
                        cntt=0
                        gymlist=[]
                        suggch=[]
                        
                        for y in self.cngroup:
                            comwords=0
                            tpp=await subf.filtNameval(self,y)
                            for x in loclist:
                                if x.upper() in tpp.upper():
                                    comwords+=1
                                    gymlist.append(y)
                            if comwords>maxcom:
                                suggch.append(y)
                                #gyml=self.lngroup[cntt]
                                gymlat=self.latgroup[cntt]
                                gymlon=self.longroup[cntt]
                                gyml= "" + gymlat + "," + gymlon +""+ ""
                                maxcom=comwords
                            cntt+=1
                        #get unique gyms names only
                        ugym=[]
                        for x in gymlist:
                            if x not in ugym:
                                ugym.append(x) 
                        print (ugym)
                        print (gymlist)
                        
                        txt="`"
                        cntr=1
                        for x in ugym:
                            txt+=str(cntr)+ ") " +x +" \n"
                            cntr+=1
                        txt+="`"
                        #User selects which gym if confused
                        alltimeout=30
                        bypassq=0
                        if len(ugym)>1:
                            await self.bot.send_message(ctx.message.channel,"I got confused. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.send_message(ctx.message.channel,txt)
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                            try:
                                loclist=ugym[int(msgrt.content)-1]
                                #bypassq=1
                                #newloca=loc
                                #print(loc)
                            except:
                                attempt+=1
                                dontcont=1
                                bypassq=1
                        elif len(ugym)==0:
                            #no keyword found
                            attempt+=1
                            dontcont=1
                            bypassq=1
                        else:                            
                            loclist=ugym[0]
                        
                        #print(bypassq)
                        if bypassq==0:
                            cntt=0

                        
                            for y in self.cngroup:
                                if loclist==y:
                                    gyml=self.angroup[cntt]
                                    #gyml=self.lngroup[cntt]
                                cntt+=1
                            
                            #now find the gym in the lists
                            cntt=0
                            uniq=0
                            grid=0
                            
                            for x in self.group1an:
                                if gyml.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=1
                                    Nameval=self.group1cn[cntt]
                                    #linkn=self.group1ln[cntt]
                                    gymlat=self.group1lat[cntt]
                                    gymlon=self.group1lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ "" 
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg1)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group2an:
                                if gyml.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=2
                                    Nameval=self.group2cn[cntt]
                                    #linkn=self.group2ln[cntt]
                                    gymlat=self.group2lat[cntt]
                                    gymlon=self.group2lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ "" 
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg2)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group3an:
                                if gyml.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=3
                                    Nameval=self.group3cn[cntt]
                                    #linkn=self.group3ln[cntt]
                                    gymlat=self.group3lat[cntt]
                                    gymlon=self.group3lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ "" 
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg3)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            print(uniq)
                        #uniq=0
                    #print(loc)
                    if dontcont==0:
                        cntt=0
                        uniq=0
                        grid=0
                        
                        for x in self.group1an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=1
                                Nameval=self.group1cn[cntt]
                                #linkn=self.group1ln[cntt]
                                gymlat=self.group1lat[cntt]
                                gymlon=self.group1lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ "" 
                                mutelist=await subf.getmemlist(self,ctx,self.muteg1)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group2an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=2
                                Nameval=self.group2cn[cntt]
                                #linkn=self.group2ln[cntt]
                                gymlat=self.group2lat[cntt]
                                gymlon=self.group2lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ "" 
                                mutelist=await subf.getmemlist(self,ctx,self.muteg2)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group3an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=3
                                Nameval=self.group3cn[cntt]
                                #linkn=self.group3ln[cntt]
                                gymlat=self.group3lat[cntt]
                                gymlon=self.group3lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ "" 
                                mutelist=await subf.getmemlist(self,ctx,self.muteg3)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                    if uniq==0:    
                        await self.bot.say("`The gym name you entered is not available in the system`")
                        attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                #print("Made to return")
                #print(Nameval)
                RaidBossfound=0
                isLoc=0
                if any(xpp == Nameval for xpp in self.Locbypass): #We need to allow this boss to be entered anyway
                    RaidBossfound=1    
                    isLoc=1
                

                #Raid already entered - here
                #if chch1==None and chch2==None: #The channels haven't been created yet, and continue
                #    rpp=1
                #else:
                #    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid was already created!")
                #    return
                tempNameval=await subf.filtNameval(self,Nameval)
                
                for x in self.allbutmtch:
                    rdd=self.bot.get_channel(x)
                    try:
                        xrd=rdd.name.split('---')
                        if xrd[0]==tempNameval or xrd[1]==tempNameval:
                    #if tempNameval in rdd.name:
                            await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid was already created!")
                            return
                    except:
                        allowcont=1
                
                attempt=0
                success=0
                #time=0
                status=0
                extra="So ex-raid passes were distributed for "+Nameval
                while success==0 and attempt<3:
                    await self.bot.send_message(ctx.message.channel, extra+ ". What date is the egg for (MM/DD/YY)?")
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    tvar=msgrt.content.split("/")
                    print(tvar)
                    if "%exraid" in msgrt.content:
                        await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                        return
                    if msgrt.content.upper()=="Q": 
                        await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                        return
                    print(len(tvar))
                    if len(tvar)==3:
                        check1=0
                        if int(tvar[0])>0 and int(tvar[0])<13:
                            check1+=1
                        if int(tvar[1])>0 and int(tvar[1])<32:
                            check1+=1
                        if int(tvar[2])>14 and int(tvar[2])<32:
                            check1+=1
                        if check1==3:
                            success=1
                    #if msgrt.content.upper()=="N": 
                    #    await self.bot.send_message(ctx.message.channel,"So, it's still an egg! How many minutes until the egg hatches (round down)?")
                    #    #time=45
                    #    status="1"
                    #    success=1
                    #elif msgrt.content.upper()=="Y": 
                    #    await self.bot.send_message(ctx.message.channel,"So, it's a boss ready to get taken down! How many minutes until the raid boss leaves (round down)?")
                    #    #time=0
                    #    status="2"
                    #    success=1
                    else: 
                        extra="I didn't quite get that"
                        attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                success=0
                datev=msgrt.content
                attempt=0
                extra=""
                while success==0 and attempt<3:
                    await self.bot.send_message(ctx.message.channel, extra+ " What time does the raid start on "+datev +" (HH:MM)? __**(Use 24 hour format)**__")
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    tvar=msgrt.content.split(":")
                    
                    if "%exraid" in msgrt.content:
                        await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                        return
                    if msgrt.content.upper()=="Q": 
                        await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                        return
                    if len(tvar)==2:
                        check1=0
                        if int(tvar[0])>-1 and int(tvar[0])<24:
                            check1+=1
                        if int(tvar[1])>-1 and int(tvar[1])<60:
                            check1+=1
                        
                        if check1==2:
                            success=1;
                    #if msgrt.content.upper()=="N": 
                    #    await self.bot.send_message(ctx.message.channel,"So, it's still an egg! How many minutes until the egg hatches (round down)?")
                    #    #time=45
                    #    status="1"
                    #    success=1
                    #elif msgrt.content.upper()=="Y": 
                    #    await self.bot.send_message(ctx.message.channel,"So, it's a boss ready to get taken down! How many minutes until the raid boss leaves (round down)?")
                    #    #time=0
                    #    status="2"
                    #    success=1
                    else: 
                        extra="I didn't quite get that."
                        attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return                
                 
                
                timev=msgrt.content
                #if status=="1":  #If an egg
                await self.bot.send_message(ctx.message.channel,"Based on what you told me: \nAn Ex-Raid will occur at "+Nameval+" on "+datev+" at "+timev+". \nDid I understand you correctly (Y/N)?")
               
                attempt=0
                success=0
                while success==0 and attempt<3:
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    if msgrt.content.upper()=="N": 
                        await self.bot.send_message(ctx.message.channel,"Looks like you may have entered something wrong then.  How about you try again.")
                        success=1
                        return
                    elif msgrt.content.upper()=="Y": 
                        success=1
                    else: 
                        await self.bot.send_message(ctx.message.channel, "Please answer the question, did I get that right (Y/N)?")
                        attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return    
            except:
                await self.bot.say("Purdue Pollster fell asleep while waiting for a reply, but you can always try again!")
                return
            await self.bot.send_message(ctx.message.channel,"The ex-raid notification has been made! Thank you.")
            #origmessv="%raid " + status + " " + type.upper() + " " + str(timeleft) + " " + location
            chpost=self.bot.get_channel(self.mewtwoposts)
            #chpost=self.bot.get_channel(self.programid)

            scrubmess=await subf.filtNameval(self,Nameval)
            
            
            
            
           

            
            
            
            arggs=datev.split("/")
            mm=0
            dd=0
            yy=0
            cntt=0
            for x in arggs:
                argg2=x.split(" ")
                print(argg2[len(argg2)-1] + " " + argg2[0])
                for y in argg2:
                    if cntt==0: ##MM
                        mm=int(argg2[len(argg2)-1])
                    elif cntt==1: ##MM
                        dd=int(argg2[0])
                    elif cntt==2: ##YY
                        yy=int(argg2[0])
                cntt+=1
            if yy<2000:
                yy+=2000
            
            if mm==1:
                mon="January"
                mon2="Jan"
            elif mm==2:
                mon="February"
                mon2="Feb"
            elif mm==3:
                mon="March"
                mon2="Mar"
            elif mm==4:
                mon="April"
                mon2="Apr"
            elif mm==5:
                mon="May"
                mon2="May"
            elif mm==6:
                mon="June"
                mon2="Jun"
            elif mm==7:
                mon="July"
                mon2="Jul"
            elif mm==8:
                mon="August"
                mon2="Aug"
            elif mm==9:
                mon="September"
                mon2="Sept"
            elif mm==10:
                mon="October"
                mon2="Oct"
            elif mm==11:
                mon="November"    
                mon2="Nov"
            elif mm==12:
                mon="December"    
                mon2="Dec"
                
            #Try finding the time of the raid
            #loclist=suggch
            arggs=timev.split(":")
            hashour=0
            hour=0
            minute=0
            for x in arggs:
                argg2=x.split(" ")
                for y in argg2:
                    try:
                        if hashour==0:
                            hour=int(y)
                            hashour=1
                        else:
                            minute=int(y)
                            #hashour=1
                    except:
                        notnum=1
            #Get raid start time
            minute_12=minute+5
            hour_12=hour
            if minute_12>=60:
                minute_12-=60
                hour_12+=1
            #Create second time
            minute1=minute+20
            hour1=hour
            if minute1>=60:
                minute1-=60
                hour1+=1
                
            minute_22=minute1+5
            hour_22=hour
            if minute_22>=60:
                minute_22-=60
                hour_22+=1
            baseti1=str(hour).zfill(2)+":"+str(minute).zfill(2)+":00"
            rpubtime1=datetime.strptime(baseti1,"%H:%M:%S").strftime(self.timeform)  
            
            baseti2=str(hour1).zfill(2)+":"+str(minute1).zfill(2)+":00"
            rpubtime2=datetime.strptime(baseti2,"%H:%M:%S").strftime(self.timeform)  
            
            baseti21=str(hour1).zfill(2)+":"+str(minute_12).zfill(2)+":00"
            rpubtime21=datetime.strptime(baseti21,"%H:%M:%S").strftime(self.timeform)  
            
            baseti22=str(hour1).zfill(2)+":"+str(minute_22).zfill(2)+":00"
            rpubtime22=datetime.strptime(baseti22,"%H:%M:%S").strftime(self.timeform)  
            
            await self.bot.send_message(chpost,"__**EX-RAID:**__ "+ mon + " "+str(dd)+","+str(yy) + " at " + Nameval)
            # + "\n" +"https://goo.gl/" + linkn + "\n")
            await self.bot.send_message(chpost,"Please react _**ONLY**_ if you have received the in-game invitation for this raid.")
            mgssav1=await self.bot.send_message(chpost,"React for Check-in " + str(rpubtime1) + "(Raid Start: " + str(rpubtime21) + "):")
            #await self.bot.send_message(chpost,"React for Start Time: " + str(rpubtime1))# + str(mm).zfill(2) + " "+str(dd).zfill(2)+","+str(yy))
            #msgg2=await self.bot.send_message(chpost,"React for Start Time: " + str(hour).zfill(2)+":"+str(minute).zfill(2)+":00")
            #await self.bot.send_message(chpost,"React for Late Start: " + str(rpubtime2))
            mgssav2=await self.bot.send_message(chpost,"React for Late Start: " + str(rpubtime2) + "(Raid Start: " + str(rpubtime22) + "):")
            msgg4=await self.bot.send_message(chpost,"**--------------------------------**")
            #msgg=await self.bot.send_message(chpost,tmess.content)
            #rtt=await self.bot.pin_message(msgg)
            #
            #get a channel created
            leave=0
            chv=0
            server=ctx.message.server
            for yy in self.exchan:
                
                if leave==0:
                    yy2=self.bot.get_channel(yy)
                    gymnas=yy2.name
                    if gymnas.startswith("channel"):
                        #Use this channel
                        await self.bot.edit_channel(yy2, name=mon2 + "-" + str(dd) + "-" + scrubmess)
                        iscampus=0
                        for xx in self.group1cn:
                            
                            tlcomp=await subf.filtNameval(self,xx)
                            if tlcomp==scrubmess:
                                iscampus=1
                        rollv=discord.utils.get(ctx.message.server.roles, id=self.exroles[chv])
                        if iscampus==0:
                            msgvv=rollv.mention+",  please use this channel to discuss ex-raid stuff for the "+ Nameval +" raid at "+ str(rpubtime1) +" on "+ mon + " "+str(dd) +".  Note that with this ex-raid not being located on campus and with how few people from this discord have ex-passes, PLEASE get to this location a few minutes before the raid start time.  It is likely that others at this raid will not wait up for even a minute, so please anticipate this and go with what the majority of trainers at the location are doing.  Thanks!"
                            await self.bot.send_message(yy2,msgvv)
                        else:
                            msgvv=rollv.mention+", please use this channel to discuss ex-raid stuff for the "+ Nameval +" raid at "+ str(rpubtime1) +" on "+ mon + " "+str(dd)+"."
                            await self.bot.send_message(yy2,msgvv)
                        #b=discord.Server.get_member(server,self.CMK)
                        chh=self.bot.get_channel(self.programid)
                        #await self.bot.send_message(chh,b.mention + "\nRaid Channel: " + str(chv+1) + "\n['" + mgssav1.id + "','" + mgssav2.id +"']") 
                        await self.bot.send_message(chh,"\nRaid Channel: " + str(chv+1) + "\n['" + mgssav1.id + "','" + mgssav2.id +"']")
                        
                        if chv==0:
                            self.mtch1id=[mgssav1.id,mgssav2.id]
                        if chv==1:                       
                            self.mtch2id=[mgssav1.id,mgssav2.id]
                        if chv==2:                        
                            self.mtch3id=[mgssav1.id,mgssav2.id]
                        if chv==3:                        
                            self.mtch4id=[mgssav1.id,mgssav2.id]
                        if chv==4:
                            self.mtch5id=[mgssav1.id,mgssav2.id]
                        if chv==5:
                            self.mtch6id=[mgssav1.id,mgssav2.id]
                        if chv==6:                        
                            self.mtch7id=[mgssav1.id,mgssav2.id]
                        if chv==7:                        
                            self.mtch8id=[mgssav1.id,mgssav2.id]
                        if chv==8:                        
                            self.mtch9id=[mgssav1.id,mgssav2.id] 
                        if chv==9:                        
                            self.mtch10id=[mgssav1.id,mgssav2.id] 
                        if chv==10:                        
                            self.mtch11id=[mgssav1.id,mgssav2.id] 
                        if chv==11:                        
                            self.mtch12id=[mgssav1.id,mgssav2.id] 

                        
                        #Create persistent file
                        await subf.exraidwrite(self)
                        
                        
                        leave=1
                chv+=1
            
            async for ms in self.bot.logs_from(chpost, limit=10): #Gets a list of the last 500 messages in the channel 
                if ms.type==discord.MessageType.pins_add:
                    b=1
                    #await self.bot.delete_message(ms)
            #await self.bot.delete_message(message)
            return
    
    #Allow anyone to use this command
    #Ready for publication
    @commands.command(pass_context=True)
    async def shiny(self,ctx,seen,shinies,probability): 
        """seen - the number of pokemon seen of a given type
        shinies- the number of shinies youve seen
        probability - a decimal equating the odds of a shiny"""
        try:
            rrt= sum(np.random.binomial(int(seen), float(probability), 20000) == int(shinies))/20000.*100.
            await self.bot.send_message(ctx.message.channel,"The chance of you getting " + str(shinies) + " shinies in " + seen + " seen is " + str(rrt) + "%")
        except:
            ara=1
    
    @commands.command(pass_context=True)
    async def togglemute(self,ctx):
        if self.mutemap==1:
            self.mutemap=0
            await self.bot.send_message(ctx.message.channel,"muting is now off")
        else:
            self.mutemap=1
            await self.bot.send_message(ctx.message.channel,"muting is now on")
    
    @commands.command(pass_context=True)
    async def silph(self,ctx,url):
        if not ctx.message.channel.is_private:  
            await self.bot.send_message(ctx.message.author, "Please enter that over here!")
            return
        if not "SIL.PH" in url.upper():
           await self.bot.send_message(ctx.message.author, "That is not a silph road badge url.") 
           return
        upperurl=url.upper()
        if not upperurl.startswith("HTTP"):
            upperurl="https://" + upperurl
        upperurl=upperurl.lower()
        chh=self.bot.get_channel(self.silphch)  #
        await self.bot.send_message(chh,ctx.message.author.mention + "         " + upperurl)
        
        
        
    @commands.command(pass_context=True)
    async def getlast(self, ctx, number):
        await self.bot.delete_message(ctx.message)
        if not ctx.message.channel.id==self.programid:
            return
        return
        print(ctx.message.author.name)
        fileHandle = open ( 'raids_ALL.txt',"r" )
        lineList = fileHandle.readlines()
        fileHandle.close()
        #print lineList)
        #print "The last line is:"
        #print lineList[len(lineList)-1]
        # or simply
        #await self.bot.send_message(ctx.message.channel,lineList[-1:-number])
        stuff=lineList[-int(number):]
        newstuff=''
        for yi in range(1,int(number)+1):
            print(lineList[len(lineList)-yi]) 
            newstuff+=lineList[len(lineList)-yi]
            #print (newstuff)
        stuff=newstuff
        print(stuff)
        #stuff = stuff.replace('[', '')
        #stuff = stuff.replace(']', '')
        #stuff = stuff.replace("'", '')
        if len(stuff)>1900:
            await self.bot.send_message(ctx.message.channel,"Data Overload :sob:.  Choose fewer previous raids.")
        else:
            await self.bot.send_message(ctx.message.channel,stuff)
    
    @commands.command(pass_context=True)
    async def getidname(self, ctx):
        if not ctx.message.author.id==self.CMK:
            return
        server=self.bot.get_server(self.serverid)
        print(server.id)
        with open("roles1.txt","w") as f:     
            for x in server.roles:
                print(x.name)
                print(x.name,file=f)
    
    
    
    @commands.command(pass_context=True)
    async def raid(self, ctx):
        """Create a new raid announcement!"""
        #if not ctx.message.author.id==self.CMK:
        #    await self.bot.send_message(ctx.message.channel,"Stinkpot is trying to fix something.  Just tell #him the name of the gym and the #necessary raid info so he can test.  Thanks")
        #     return
        thespid='286714847989858305'
        if ctx.message.author.id=="472097807113650186":
            await self.bot.send_message(ctx.message.channel,"Trainer, could you please upload a screen capture of the raid boss? Thanks!")
            return
        #if ctx.message.author.id=="286714847989858305":
        #    await self.bot.send_message(ctx.message.channel,"Sorry, trainer. You have #exceeded your daily allotment of raid entering.  Try again tomorrow!")
        #    return
        #server=self.bot.server
        #if self.lastraid
        #self.lastraid = datetime.utcnow()+timedelta(hours=self.timez)
        #checktime = datetime.utcnow()+timedelta(hours=self.timez)+timedelta(seconds=self.cooldown)
        #tpolltime=self.lastraid.strftime(self.timeform)
        #tdeltat = datetime.strptime(tpolltime, self.timeform)-datetime.strptime(checktime, self.timeform)
        #self.bot.send_message(ctx.message.author,str(argg[1])+" "+str(tdelta))
        #print(tdeltat.days)
        #if (tdeltat.days<0):
        #    await self.bot.send_message(ctx.message.channel,"I need a few seconds before I can add another raid.  Try again in 5 seconds.")
        #    return
        
        #self.lastraid=datetime.utcnow()+timedelta(hours=self.timez)+timedelta(seconds=self.cooldown)
        checktime = datetime.utcnow()+timedelta(hours=self.timez)
        checktime=checktime.strftime(self.timeform)
        tpolltime=self.lastraid+timedelta(seconds=self.cooldown)
        tpolltime=tpolltime.strftime(self.timeform)
        tdeltat =datetime.strptime(checktime, self.timeform)-datetime.strptime(tpolltime, self.timeform)
        #self.bot.send_message(ctx.message.author,str(argg[1])+" "+str(tdelta))
        print(datetime.strptime(tpolltime, self.timeform))
        print(datetime.strptime(checktime, self.timeform))
        if (tdeltat.days<0):
            await self.bot.send_message(ctx.message.channel,"I need a few seconds before I can add another raid.  Try again in 5 seconds.")
            return
        self.lastraid=datetime.utcnow()+timedelta(hours=self.timez)#+timedelta(seconds=self.cooldown)
        
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=self.bot.get_server(id=self.serverid)
        #print(server)
        mutelist=[]
        a11=1
        if a11==1:
        #try:
            if ctx.message.channel.id==self.programid:
                await self.bot.send_message(ctx.message.channel,"Im here.")
            alltimeout=30
            if ctx.message.channel.is_private==True:
                donada=1
            else:
                if not (ctx.message.channel.id==self.raidsightings or ctx.message.channel.id==self.programid):# or ctx.message.channel.id==self.raidsightings or      ctx.message.channel.id==self.RaidNotifier):
                    chh=self.bot.get_channel(self.raidsightings)
                    await self.bot.send_message(ctx.message.channel,"Sorry, trainer. Please go to "+chh.mention+"  to enter this command.")
                    return
            #await self.bot.send_message(ctx.message.channel,"A system update is being performed.  Data entry will be enabled in 5 minutes.")
            #return
            ara=self.mutemap
            if ara==1:
                try:
                    if (ctx.message.author.id=="341977078213902336"):
                        await self.bot.send_message(ctx.message.channel,"To continue, please post a screen capture of the raid boss.")
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        if len(msgrt.attachments)==0:
                            await self.bot.send_message(ctx.message.channel,"This is not a gym screen capture.  Please start over.")
                            return
                        if "%raid" in msgrt.content:
                            await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                            return
                except:
                    arrr=1
                    await self.bot.send_message(ctx.message.channel,"I need a screen capture of the gym to continue.  Please start over.") 
                    return
            member = discord.utils.get(server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(server,ctx.message.author.id)
            f=b.roles
            isRO=0
            for findl in range(1,len(f)):
                if f[findl].id==self.RaidObserver:
                    isRO=0
                    break
            if any(xpp == ctx.message.author.display_name for xpp in self.threeleaders):
                isRO=0

            #See if this message just needs to be parsed
            oneline=0
            maxatt=3
            arff=ctx.message.content.split(" ")
            if len(arff)>=5:
                oneline=1
                maxatt=1
                location=""
                for y in arff[4:]:
                    location+=y + " "
                status=arff[1]  #1=egg 2=hatched
                if status=="1":
                    if not "LEVEL" in arff[2].upper():  
                        await self.bot.send_message(ctx.message.channel,"To input a raid egg, you must say `LevelX`!")
                        return
                    type=arff[2]    #ensure the bossname starts with level
                    timeleft=int(arff[3])
                    if (timeleft)>self.eggtime or (timeleft)<0:
                        await self.bot.send_message(ctx.message.channel,"The number of minutes on an egg must be between 0 and 60")
                        return
                if status=="2":
                    type=arff[2]    #if 
                    timeleft=int(arff[3])
                    if (timeleft)>self.bossactivetime or (timeleft)<0:
                        await self.bot.send_message(ctx.message.channel,"The number of minutes on a boss must be between 0 and 45")
                        return
                print("%raid " + status + " " + type + " " + str(timeleft) + " " + str(location))
            #return            
            
            sill=1
            if sill==1:
            #try:
                await asyncio.sleep(0.5)
                attempt=0
                #maxatt=3
                success=0
                extra="Looks like you're trying to tell everyone about a raid. If you need to quit at any time, press `q`.\n"
                while attempt<maxatt and success==0:
                    
                    if oneline==0:
                        await self.bot.send_message(ctx.message.channel,extra+"__**What is the Pokemon Go gym name?**__ \nYou may enter *a keyword* or the first 8 letters without spaces or special characters (i.e. A+ Storage Mural = astorage)")
                        extra=""
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        location=msgrt.content
                    else:
                        success=1
                        print (location)
                        #location=msgrt.content
                    loc=location
                    newloca=location
                    if oneline==0:
                        if "%raid" in location:
                            await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                            return
                        if msgrt.content.upper()=="Q": 
                            await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                            return
                    #print(location)
                    cntt=0
                    uniq=0
                    grid=0
                    dontcont=0
                    if len(location)<8:
                        for x in range(0,8-len(location)):
                            location=location + " "
                    loc=location[0:8]
                    
                    for x in self.sngroup:
                        if loc.upper()==x.upper():
                            uniq=uniq+1
                            Nameval=self.cngroup[cntt]
                            #print(Nameval+"WTF")
                            #linkn=self.lngroup[cntt]
                            gymlat=self.latgroup[cntt]
                            gymlon=self.longroup[cntt]
                            linkn= "" + gymlat + "," + gymlon +""+ "" 
                            olink=linkn
                            #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                        cntt=cntt+1
                    cntt=0
                    
                    if uniq>1:
                        optnum=1
                        cntt=0
                        ncha=0
                        LVal=[]
                        Nameval=''
                        newloca=''
                        for x in self.sngroup:
                            if loc.upper()==x.upper():
                                Nameval=Nameval + str(optnum) + ")" + self.cngroup[cntt] + "\n"#: Use '" + self.angroup[cntt] + "'\n"
                                LVal.append(self.angroup[cntt])
                                optnum=optnum+1
                                ncha=ncha+1
                            cntt=cntt+1
                    
                        if ncha==0:  #Channel name isn't in alt or shortname
                            await self.bot.say("`The gym name you entered is not available in the system`")
                            dontcont=1
                            attempt+=1
                            #return
                        elif ncha>1: #Unique Channel name doesn't exist
                            await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.say("`{}`".format(Nameval))
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                            try:
                                loc=LVal[int(msgrt.content)-1]
                                #Nameval=loc
                                newloca=loc
                                print(loc+"Hello")
                            except:
                                attempt+=1
                                dontcont=1
                                #return
                    elif uniq==0: #see if keyword
                        scrubmess=await subf.filtNameval(self,location.upper())          
                        locn=""
                        #Try finding the names of the gyms
                        loclist=[]
                        for x in self.WL:
                            if x.upper() in location.upper(): 
                                loclist.append(x)
                        #Xref the list with the gym names
                        possn=[]
                        maxcom=0
                        gyml=""
                        cntt=0
                        gymlist=[]
                        suggch=[]
                        
                        for y in self.cngroup:
                            comwords=0
                            tpp=await subf.filtNameval(self,y)
                            for x in loclist:
                                if x.upper() in tpp.upper():
                                    comwords+=1
                                    gymlist.append(y)
                            if comwords>maxcom:
                                suggch.append(y)
                                #gyml=self.lngroup[cntt]
                                gymlat=self.latgroup[cntt]
                                gymlon=self.longroup[cntt]
                                gyml= "" + gymlat + "," + gymlon +""+ "" 
                                maxcom=comwords
                            cntt+=1
                        #get unique gyms names only
                        ugym=[]
                        for x in gymlist:
                            if x not in ugym:
                                ugym.append(x) 
                        print (ugym)
                        print (gymlist)
                        
                        txt="`"
                        cntr=1
                        for x in ugym:
                            txt+=str(cntr)+ ") " +x +" \n"
                            cntr+=1
                        txt+="`"
                        #User selects which gym if confused
                        alltimeout=30
                        bypassq=0
                        if len(ugym)>1:
                            await self.bot.send_message(ctx.message.channel,"I got confused. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.send_message(ctx.message.channel,txt)
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                            try:
                                loclist=ugym[int(msgrt.content)-1]
                                Nameval=loclist
                                newloca=loclist
                                #bypassq=1
                                #newloca=loc
                                print(loclist)
                            except:
                                attempt+=1
                                dontcont=1
                                bypassq=1
                        elif len(ugym)==0:
                            #no keyword found
                            attempt+=1
                            dontcont=1
                            bypassq=1
                        else:                            
                            loclist=ugym[0]
                            newloca=loclist
                            Nameval=loclist
                        
                        #print(bypassq)
                        if bypassq==0:
                            cntt=0

                            #print(loclist+"GOOD")
                            for y in self.cngroup:
                                if loclist==y:
                                    #gyml=self.lngroup[cntt]
                                    gymlat=self.latgroup[cntt]
                                    gymlon=self.longroup[cntt]
                                    gyml= "" + gymlat + "," + gymlon +""+ "" 
                                    newloca=self.angroup[cntt]
                                    Nameval=self.cngroup[cntt]
                                    print(newloca)
                                    #gyml=self.lngroup[cntt]
                                cntt+=1
                            
                            #now find the gym in the lists
                            cntt=0
                            uniq=0
                            grid=0
                            
                            for x in self.group1an:
                                if newloca.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=1
                                    Nameval=self.group1cn[cntt]
                                    #linkn=self.group1ln[cntt]
                                    gymlat=self.group1lat[cntt]
                                    gymlon=self.group1lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ "" 
                                    #newloca=self.group1an[cntt]
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg1)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group2an:
                                if newloca.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=2
                                    Nameval=self.group2cn[cntt]
                                    #linkn=self.group2ln[cntt]
                                    gymlat=self.group2lat[cntt]
                                    gymlon=self.group2lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ "" 
                                    #newloca=self.group2an[cntt]
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg2)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group3an:
                                if newloca.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=3
                                    Nameval=self.group3cn[cntt]
                                    #linkn=self.group3ln[cntt]
                                    gymlat=self.group3lat[cntt]
                                    gymlon=self.group3lon[cntt]
                                    linkn= "" + gymlat + "," + gymlon +""+ "" 
                                    #newloca=self.group3an[cntt]
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg3)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            print(uniq)
                        #uniq=0
                    #print(loc)
                    if dontcont==0:
                        cntt=0
                        uniq=0
                        grid=0
                        
                        for x in self.group1an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=1
                                Nameval=self.group1cn[cntt]
                                #linkn=self.group1ln[cntt]
                                gymlat=self.group1lat[cntt]
                                gymlon=self.group1lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ "" 
                                mutelist=await subf.getmemlist(self,ctx,self.muteg1)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group2an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=2
                                Nameval=self.group2cn[cntt]
                                #linkn=self.group2ln[cntt]
                                gymlat=self.group2lat[cntt]
                                gymlon=self.group2lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ "" 
                                mutelist=await subf.getmemlist(self,ctx,self.muteg2)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group3an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=3
                                Nameval=self.group3cn[cntt]
                                #linkn=self.group3ln[cntt]
                                gymlat=self.group3lat[cntt]
                                gymlon=self.group3lon[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ "" 
                                mutelist=await subf.getmemlist(self,ctx,self.muteg3)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                    
                        #if uniq==0:
                            
                            
                                
                                #linkn="Directions to " + loclist + " can be found here:\n " + "https://goo.gl/" + gyml + ""
                                #await self.bot.send_message(ctx.message.channel, linkn) 
                                #print(loclist) 
                            
                    if uniq==0:
                        await self.bot.say("`The gym name you entered is not available in the system`")
                        attempt+=1
                            #else:
                            #    success=1
                            #return
                
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                #print("Made to return")
                #print(Nameval)
                RaidBossfound=0
                isLoc=0
                if any(xpp == Nameval for xpp in self.Locbypass): #We need to allow this boss to be entered anyway
                    RaidBossfound=1    
                    isLoc=1
                

                #Raid already entered - here
                #if chch1==None and chch2==None: #The channels haven't been created yet, and continue
                #    rpp=1
                #else:
                #    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid was already created!")
                #    return
                tempNameval=await subf.filtNameval(self,Nameval)
                
                for x in self.allbutmtch:
                    rdd=self.bot.get_channel(x)
                    try:
                        xrd=rdd.name.split('---')
                        if xrd[0]==tempNameval or xrd[1]==tempNameval:
                    #if tempNameval in rdd.name:
                            await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid was already created!")
                            return
                    except:
                        allowcont=1
                
                attempt=0
                
                success=0
                #time=0
                
                extra="So there's a raid about to start at "+Nameval
                #if Nameval=="John Purdue Fountain":
                #    if not ctx.message.author=="330830919604633604":
                #        await self.bot.send_message(ctx.message.channel, "CRITICAL ERROR.")
                #        return
                while success==0 and attempt<maxatt:
                    if oneline==0:
                        status=0
                        await self.bot.send_message(ctx.message.channel, extra+ ". Has the egg hatched yet (Y/N)?")
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        
                    else:
                        success=1
                    if oneline==0:
                        if "%raid" in msgrt.content:
                            await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                            return
                        if msgrt.content.upper()=="Q": 
                            await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                            return
                        if msgrt.content.upper()=="N": 
                            await self.bot.send_message(ctx.message.channel,"So, it's still an egg! How many minutes until the egg hatches (round down)?")
                            #time=45
                            status="1"
                            success=1
                        elif msgrt.content.upper()=="Y": 
                            await self.bot.send_message(ctx.message.channel,"So, it's a boss ready to get taken down! How many minutes until the raid boss leaves (round down)?")
                            #time=0
                            status="2"
                            success=1
                        else: 
                            extra="I didn't quite get that."
                            attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                    
                 
                
                if status=="1":  #If an egg
                    attempt=0
                    success=0
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            timeleft=0
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        else: 
                            success=1
                        if oneline==0:                        
                            try:
                                if "%raid" in msgrt.content:
                                    await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                    return
                                if msgrt.content.upper()=="Q": 
                                    await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                                    return
                                if int(msgrt.content)<self.eggtime and int(msgrt.content)>0: 
                                    timeleft=int(msgrt.content)
                                    if timeleft>30 and isRO==1:
                                        areaf=1
                                        await self.bot.send_message(ctx.message.channel, "Top 3 on the leaderboard cannot enter data yet for this raid (wait 30 minutes).  Please wait for 15 minutes to elapse.  HINT, HINT, WINK, WINK for those who want to try %raid!")
                                        #return
                                    success=1
                                else:
                                    attempt+=1
                                    #extra="Something doesn't look right there. The time should be between 0 and 60 minutes."
                                    #await self.bot.send_message(ctx.message.channel, extra+ " \nHow many minutes until the egg hatches (round down)?")
                                    #attempt+=1
                            except:
                                extra="Something doesn't look right there. The time should be between 0 and 60 minutes."
                                await self.bot.send_message(ctx.message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                attempt+=1
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return

                    attempt=0
                    success=0
                    if oneline==0:
                        await self.bot.send_message(ctx.message.channel,"Last question! What tier level is the egg?")
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        else:
                            success=1
                        
                        if oneline==0:
                            try:
                                if "%raid" in msgrt.content:
                                    await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                    return
                                if msgrt.content.upper()=="Q": 
                                    await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                                    return
                                if int(msgrt.content)<6 and int(msgrt.content)>0: 
                                    if isLoc==1:
                                        type="Level"+msgrt.content
                                        success=1
                                    else:
                                        if int(msgrt.content)<6 and int(msgrt.content)>2:
                                            type="Level"+msgrt.content
                                            success=1
                                        else:
                                            await self.bot.send_message(ctx.message.channel, "I can only notify everyone about Level 3,4,and 5 eggs unless it's at an ex-raid gym.  Sorry.")
                                            return
                                else:
                                    extra="Something doesn't look right there. The tier should be between 1 and 5, inclusive."
                                    await self.bot.send_message(ctx.message.channel, extra+ " \nWhat tier level is the egg?")
                                    attempt+=1
                            except:
                                extra="Something doesn't look right there. What tier level is the egg?"
                                await self.bot.send_message(ctx.message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                attempt+=1
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return
                
                elif status=="2":  #If a boss
                    attempt=0
                    success=0
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            msgrt2 = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        else:
                            success=1
                        #print (int(msgrt2.content))
                        if oneline==0:
                            try:
                                if "%raid" in msgrt.content:
                                    await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                    return
                                if msgrt2.content.upper()=="Q": 
                                    await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                                    return
                                #print (int(msgrt2.content))
                                if int(msgrt2.content)<self.bossactivetime and int(msgrt2.content)>=15: 
                                        timeleft=int(msgrt2.content)
                                        success=1
                                elif int(msgrt2.content)<15:
                                    xtra="Doesn't seem fair to not give people sufficient time to get to a raid.  I can't let you enter that in good conscience (15 mins required)."
                                    await self.bot.send_message(ctx.message.channel, xtra)
                                    attempt+=1
                                    return
                                else:
                                    extra="Something doesn't look right there. The time should be between 0 and 45 minutes."
                                    await self.bot.send_message(ctx.message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                    attempt+=1
                                    
                            except:
                                extra="Something doesn't look right there. The time should be between 0 and 45 minutes."
                                await self.bot.send_message(ctx.message.channel, extra+ " \nHow many minutes until the raid boss leaves (round down)??")
                                attempt+=1
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return
                    print("Before Raid Boss")
                    attempt=0
                    success=0
                    if oneline==0:
                        await self.bot.send_message(ctx.message.channel,"Last question! What is the name of the raid boss?")
                    while success==0 and attempt<maxatt:
                        if oneline==0:
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        else:
                            success=1
                        if oneline==0:
                            if "%raid" in msgrt.content:
                                await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
                                return
                            if msgrt.content.upper()=="Q": 
                                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                                return
                            type=msgrt.content
                        
                        raidn=0
                        for x in range(0,len(self.L4types)):
                            if type.upper()==self.L4types[x].upper():
                                RaidBossfound=1
                                raidn=4
                        for x in range(0,len(self.L5types)):
                            if type.upper()==self.L5types[x].upper():
                                RaidBossfound=1    
                                raidn=5                
                        for x in range(0,len(self.L3types)):
                            if type.upper()==self.L3types[x].upper():
                                RaidBossfound=1    
                                raidn=3 
                        for x in range(0,len(self.PStypes)):
                            if type.upper()==self.PStypes[x].upper():
                                RaidBossfound=1    
                                raidn=6                
                        for x in range(0,len(self.OItypes)):
                            if type.upper()==self.OItypes[x].upper():
                                RaidBossfound=1    
                                raidn=7 
                        #Origname
                        
                        if RaidBossfound==0:
                            await self.bot.send_message(ctx.message.channel,"I couldn't find that raid boss. What's the name of the raid boss?")
                            attempt+=1
                        else:
                            success=1
                        
                        
                        
                        
                        
                    if attempt>2:
                        await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                        return
                
                #if oneline==0:
                if status=="1":  #If an egg
                    await self.bot.send_message(ctx.message.channel,"Based on what you told me: \nA "+type+" egg will hatch in "+str(timeleft)+" minutes at "+Nameval+". \nDid I understand you correctly (Y/N)?")
                elif status=="2":  #If an egg
                    await self.bot.send_message(ctx.message.channel,"Based on what you told me: \nA "+type+" will be at "+Nameval+" for the next "+str(timeleft)+" minutes. \nDid I understand you correctly (Y/N)?")
                attempt=0
                success=0
                #if oneline==0:
                while success==0 and attempt<maxatt:
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    if msgrt.content.upper()=="N": 
                        await self.bot.send_message(ctx.message.channel,"Looks like you may have entered something wrong then.  How about you try again.")
                        success=1
                        return
                    elif msgrt.content.upper()=="Y": 
                        success=1
                    else: 
                        await self.bot.send_message(ctx.message.channel, "Please answer the question, did I get that right (Y/N)?")
                        attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return    
            else:
            #except:
                await self.bot.say("Purdue Pollster fell asleep while waiting for a reply, but you can always try again!")
                return
            
            #await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%raid` while I'm asking you questions.  I'm gonna have to have to start over.")
            await self.bot.send_message(ctx.message.channel,"The raid notification has been made! Thank you.")
            print(status)
            print(type.upper())
            print(str(timeleft))
            print(newloca[0:8])
            origmessv="%raid " + status + " " + type.upper() + " " + str(timeleft) + " " + newloca[0:8]
            #origmessv2=type.ljust(8) + " " + str(timeleft).ljust(5)+ " " +newloca[0:8].ljust(8)+ " "+ " " +ctx.message.author.display_name
            #print (origmessv2)
            #return
            #return
            #argg=timeleft.split(':')
            #if len(argg)>1:
            #    await self.bot.say("`Please do not include seconds within the time remaining!`")
                 
            if status == "1": 
                statmess=" Egg"
            elif status=="2":
                statmess="Boss"
            else:
                await self.bot.say("The status must be `1` or `2`")
                return
            str_time = datetime.utcnow()+timedelta(hours=self.timez)
            hatch_time= str_time
            if status=="1":
                #str_time += timedelta(minutes=self.raidmaxtime)
                str_time += timedelta(minutes=self.bossactivetime)
            else:
                #hatch_time+= timedelta(minutes=-self.raidmaxtime)
                hatch_time+= timedelta(minutes=-self.bossactivetime)
            argg=timeleft
            str_time += timedelta(minutes=int(argg))
            hatch_time+= timedelta(minutes=int(argg))
            str_time = str_time.strftime(self.timeform)
            hatch_time = hatch_time.strftime(self.timeform)
            #hatch_time = hatch_time.strftime('%H:%M:%S')
            #hatch_time2 = hatch_time.strftime('%I:%M:%S')
            endtime1=str_time
            oendtime=str_time
            linkn="__**RAID:**__ A " + type.upper() + " raid boss ends at "
            linkn+= str_time +"\n(Hatch time of : "+ hatch_time +")\n" + "https://www.google.com/maps?q=" + olink + "\n"
            
            #Get the appropriate ID here for location. Find the last channel in the list
            if grid==1:
                IDval_loc=await subf.getchid(self,self.g1locaid)
            elif grid==2:
                IDval_loc=await subf.getchid(self,self.g2locaid)
            elif grid==3:
                IDval_loc=await subf.getchid(self,self.g3locaid)
                
            Origname=Nameval
            Orignamo=Nameval
            Nameval=await subf.filtNameval(self,Nameval)       
            
            channloc=self.bot.get_channel(IDval_loc)
            print(channloc)
            
            #if not 'blank-0' in channloc.name:
            #    await self.bot.say("This raid cannot be entered because the maximum number of channels has been exceeded. Sorry.")
            #    return
                
            
            raidn=0
            for x in range(0,len(self.L4types)):
                if type.upper()==self.L4types[x].upper():
                    RaidBossfound=1
                    raidn=4
            for x in range(0,len(self.L5types)):
                if type.upper()==self.L5types[x].upper():
                    RaidBossfound=1    
                    raidn=5                
            for x in range(0,len(self.L3types)):
                if type.upper()==self.L3types[x].upper():
                    RaidBossfound=1    
                    raidn=3 
            for x in range(0,len(self.PStypes)):
                if type.upper()==self.PStypes[x].upper():
                    RaidBossfound=1    
                    raidn=6
            for x in range(0,len(self.OItypes)):
                if type.upper()==self.OItypes[x].upper():
                    RaidBossfound=1    
                    raidn=7
            #Get the boss channel ID here
            modv=0
            isPS=0
            
            if raidn==3:
                IDval_rb=await subf.getchid(self,self.L3groupid)
                modv=1
            elif raidn==4:
                IDval_rb=await subf.getchid(self,self.L4groupid)
                modv=1
            elif raidn==5:
                IDval_rb=await subf.getchid(self,self.L5groupid)
                modv=1
            elif raidn==6:  #It could be shiny
                isPS=1
                IDval_rb=await subf.getchid(self,self.PSgroupid)
                modv=1
            elif raidn==7:  #It could be shiny
                isPS=0
                IDval_rb=await subf.getchid(self,self.PSgroupid)
                modv=1
            if modv==0: #Then this is a forced raid boss entry
                channrb=channloc
            else:
                channrb=self.bot.get_channel(IDval_rb)    

            
             #If the channel is unique, find it to see if the data has been entered already
            counter = 0
            ####################################################################################
            #If either channel name exists and hasn't ended yet, prevent it from being added
            ####################################################################################
            rrx=0
            try:
                if raidn==3:
                    rrx=await subf.prevover(self,self.L3groupid,Nameval,type,ctx)
                elif raidn==4:
                    rrx=await subf.prevover(self,self.L4groupid,Nameval,type,ctx)
                elif raidn==5:
                    rrx=await subf.prevover(self,self.L5groupid,Nameval,type,ctx)
                elif raidn==6:
                    rrx=await subf.prevover(self,self.PSgroupid,Nameval,type,ctx)
                elif raidn==7:
                    rrx=await subf.prevover(self,self.PSgroupid,Nameval,type,ctx)
            except:
                arerfe=1
            if rrx==1:
                return
                
            chch1=discord.utils.get(server.channels, name=Nameval+ "---" + type.lower())
            chch2=discord.utils.get(server.channels, name=type.lower() + "---" + Nameval)
            if chch1==None and chch2==None: #The channels haven't been created yet, and continue
                rpp=1
            else:
                await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid was already created!")
                return
            try:
                for x in self.allbutmtch:
                    rdd=self.bot.get_channel(x)
                    if Nameval in rdd.name:
                        await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid was already created!")
                        return
            except:
                afere=1
            
            member = discord.utils.get(server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(server,ctx.message.author.id)
            f=b.roles
            #if ctx.message.author.id=="4286714847989858305" or ctx.message.author.id=="339901930098917377":
            #    await self.bot.send_message(ctx.message.channel,"Something seemed to have gone horribly wrong.  Please try again.")
            #    return
            isallowed=0
            bypassa=1
            role_RT=discord.utils.get(server.roles, id=self.RaidTrainer) 
            role_RO=discord.utils.get(server.roles, id=self.RaidObserver) 
            if any(xpp == role_RT for xpp in f):
                bypassa=1
            if any(xpp == role_RO for xpp in f):
                bypassa=1
            
            
            #for findl in range(1,len(f)):
                #try: #await self.bot.send_message(ctx.message.channel,f[findl].id + "&" + self.RaidObserver)
                #if f[findl].id==self.RaidObserver or f[findl].id==self.RaidTrainer:
            if bypassa==1:
                isallowed=1
                await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", your entry will be added momentarily. Thank you!")
                try:
                    await self.bot.move_channel(channrb, 0)
                    await self.bot.edit_channel(channrb, name=Nameval+ self.chanstrsp + type.upper() )
                except:
                    arefef=1
                await self.bot.move_channel(channloc, 0)
                await self.bot.edit_channel(channloc, name=type.upper() + self.chanstrsp + Nameval)
                #Need to set permissions for the channel now
                for idx in f: 
                    if idx.id==self.Approved:   
                        role_everyone = idx
                plopp=00
                if plopp==1:
                    role_pogomod=discord.utils.get(server.roles, id=self.POGOmod)  
                    overwrite = channloc.overwrites_for(role_everyone)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channloc, role_everyone, overwrite)
                    overwrite = channrb.overwrites_for(role_everyone)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channrb, role_everyone, overwrite)
                    overwrite = channloc.overwrites_for(role_pogomod)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channloc, role_pogomod, overwrite)
                    overwrite = channrb.overwrites_for(role_pogomod)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channrb, role_pogomod, overwrite)
                    role_RO=discord.utils.get(server.roles, id=self.RaidObserver)
                    overwrite = channloc.overwrites_for(role_RO)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channloc, role_RO, overwrite)
                    overwrite = channrb.overwrites_for(role_RO)
                    overwrite.read_messages = True
                    await self.bot.edit_channel_permissions(channrb, role_RO, overwrite)
                CPmax=0
                bossemo=[]
                for x in range(0,len(self.L4types)):
                    if type.upper()==self.L4types[x].upper():
                        CPmax=self.L4maxCP[x]
                        bossemo.append(self.L4emoji[x])
                for x in range(0,len(self.L5types)):
                    if type.upper()==self.L5types[x].upper():
                        CPmax=self.L5maxCP[x]
                        bossemo.append(self.L5emoji[x])
                for x in range(0,len(self.L3types)):
                    if type.upper()==self.L3types[x].upper():
                        CPmax=self.L3maxCP[x]
                        bossemo.append(self.L3emoji[x])
                for x in range(0,len(self.PStypes)):
                    if type.upper()==self.PStypes[x].upper():
                        CPmax=self.PSmaxCP[x]
                        bossemo.append(self.PSemoji[x])
                for x in range(0,len(self.OItypes)):
                    if type.upper()==self.OItypes[x].upper():
                        CPmax=self.OImaxCP[x]
                        bossemo.append(self.OIemoji[x])
                if len(bossemo)==0:
                    bossemo=["<:item_pokeball:284615009299070976>"]
                addlstr=""
                #print (CPmax)
                CPmax=int(CPmax)
                if CPmax>0:        
                    addlstr="\nThe CP for a 100IV " + type.upper() + " is " + str(CPmax)
                
                polltime = datetime.utcnow()+timedelta(hours=self.timez)
                if status=="1":
                    polltime += timedelta(minutes=self.bossactivetime)
                argg=timeleft
                polltime += timedelta(minutes=int(argg))
                tpolltime=polltime.strftime('%H:%M:%S')
                
                tdeltat = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime("0:0:0", '%H:%M:%S')
                hours, remainder = divmod(tdeltat.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                
                polltime += timedelta(seconds=int(60-seconds))
                polltime += timedelta(minutes=1)
                #polltime += timedelta(hours=-1)
                polltime += timedelta(minutes=-self.bossactivetime)
                #polltime += timedelta(hours=-1)
                #polltime += timedelta(minutes=15)
                #Should be replaced with self.bossactivetime
                trrta=polltime.strftime('%H:%M:%S')
                             
                tdeltat3 = datetime.strptime(trrta, '%H:%M:%S')-datetime.strptime("0:0:0", '%H:%M:%S')
                hours1, remainder1 = divmod(tdeltat3.total_seconds(), 3600)
                minutes1, seconds1 = divmod(remainder1, 60)
                                
                                
                d3=timedelta(minutes=-(minutes1 % 10)+10)
                polltime=polltime + d3
                
                weathertime=0
                d3we=timedelta(minutes=-(minutes1 % 60)+60-5-4)
                weatherpoll=polltime + d3we
                
                
                tpollwe = weatherpoll.strftime('%H:%M:' + "00")
                if (minutes1 % 60)<45:
                    weathertime=1
                #print('@Start: ' + tpollwe)
                #tpoll = polltime.strftime('%H:%M:'+"00")
                #for x in range(0,self.maxtimeslots):
                #    print('@Start: ' + tpoll)
                #    #if not channrb==channloc:
                #    #    msggr2=await self.bot.send_message(channrb,'@Start: ' + tpoll)
                #    #await asyncio.sleep(0.25)
                #    polltime += timedelta(minutes=self.raidspacing)
                #    tpoll = polltime.strftime('%H:%M:%S')
                #return
                tpoll = polltime.strftime('%I:%M:'+"00"+"%p")
                #clear the channel first
                deleted=await self.bot.purge_from(channloc, limit=100)
                await self.bot.move_channel(channloc, 0)
                channrb=channloc #ADDED 01292018
                
                
                memlist=[]
                #Add logic here for the shiny notification
                shinynot=discord.utils.get(server.roles, id=self.PSNotify)
                shinyemo=""
                if isPS==0:
                    shinyn=""
                else:
                    shinyn=shinynot.mention
                    await subf.grantacc(self,channloc,channrb,shinynot)
                    shinyemo=self.PSemoji[0]
                    memlist+=await subf.getmemlist(self,ctx,self.PSNotify)
                #Get the ID of the correct notify
                cntt=0
                Addlloc=0
                for xpp in self.Locbypass: #We need to allow this boss to be entered anyway
                    if xpp == Origname:
                        Addlloc=cntt
                        break
                    cntt+=1
                print(Addlloc)
                print(self.AddlNotiid)
                Locnot=discord.utils.get(server.roles, id=self.AddlNotiid[Addlloc])
                Locnot2=discord.utils.get(server.roles, id=self.SilentEX)
                locatemo=""
                if isLoc==0:
                    Locan=""
                else:
                    Locan=Locnot.mention
                    await subf.grantacc(self,channloc,channrb,Locnot)
                    await asyncio.sleep(0.05)
                    await subf.grantacc(self,channloc,channrb,Locnot2)
                    locatemo=self.emoji_exgym
                
                type=type.upper()
                xrs=channloc
                if not channrb==channloc:
                    xrs2=channrb
                else:
                    xrs2=xrs
                cntt=0
                mentioned=0
                msgchann = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.genchid)
                #msgchann=self.bot.get_channel(self.genchid)
                origname=Orignamo
                endtime=oendtime
                if not channrb==channloc:
                    chmention = xrs.mention + " or\n          " + xrs2.mention
                else:
                    chmention = xrs.mention
                linky="(Hatch time of : "+ hatch_time +")   https://www.google.com/maps?q="+olink + addlstr
                
                uniqemo=[]
                for x in bossemo:
                    if x not in uniqemo:
                        uniqemo.append(x) 
                emoji=uniqemo
                
                outp=""
                for x in emoji:
                    outp+=x
                
                emoji=outp+ shinyemo + locatemo
                
                allmention=""
                msgg6=None
                for x in self.L3types:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentL3)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.L3Notify)
                        memlist+=await subf.getmemlist(self,ctx,self.L3Notify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        
                        nid=self.L3notid[cntt]
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist(self,ctx,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention +" "+ rr5.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(, rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan+ ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        else:
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention  +" "+Locan+" "+shinyn + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                    cntt+=1
                cntt=0
                for x in self.L4types:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentL4)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.L4Notify)
                        memlist+=await subf.getmemlist(self,ctx,self.L4Notify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        nid=self.L4notid[cntt]
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist(self,ctx,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention +" "+ rr5.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        else:
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention  +" "+Locan+" "+shinyn + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                    cntt+=1
                cntt=0
                for x in self.L5types:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentL5)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.L5Notify)
                        memlist+=await subf.getmemlist(self,ctx,self.L5Notify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        nid=self.L5notid[cntt]
                        print (nid)
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist(self,ctx,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention +" "+ rr5.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        else:
                            if self.notifyon==1:
                                allmention = Locan + " " + shinyn + " "+ rr2.mention
                                msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+shinyn + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                    cntt+=1
                if mentioned==0: #Maybe its a shiny
                    cntt=0
                    for x in self.PStypes:
                        if type==x.upper():
                            mentioned=1
                            #Show to Silent only
                            rr2=discord.utils.get(server.roles, id=self.SilentPS)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            #and hold on to the notify version
                            rr2=discord.utils.get(server.roles, id=self.PSNotify)
                            memlist+=await subf.getmemlist(self,ctx,self.PSNotify)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            nid=self.PSnotid[cntt]
                            if not nid=="0":
                                rr5=discord.utils.get(server.roles, id=nid)
                                memlist+=await subf.getmemlist(self,ctx,nid)
                                await subf.grantacc(self,channloc,channrb,rr5)
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention +" "+ rr5.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention  +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                            else:
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+Locan+ ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        cntt+=1
                if mentioned==0: #Maybe its a shiny
                    cntt=0
                    for x in self.OItypes:
                        if type==x.upper():
                            mentioned=1
                            #Show to Silent only
                            rr2=discord.utils.get(server.roles, id=self.SilentOI)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            #and hold on to the notify version
                            rr2=discord.utils.get(server.roles, id=self.OINotify)
                            memlist+=await subf.getmemlist(self,ctx,self.OINotify)
                            await subf.grantacc(self,channloc,channrb,rr2)
                            nid=self.OInotid[cntt]
                            if not nid=="0":
                                rr5=discord.utils.get(server.roles, id=nid)
                                memlist+=await subf.getmemlist(self,ctx,nid)
                                await subf.grantacc(self,channloc,channrb,rr5)
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention +" "+ rr5.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention  +" "+Locan + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                            else:
                                if self.notifyon==1:
                                    allmention = Locan + " "+ rr2.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+Locan+ ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        cntt+=1
                if mentioned==0: #If still not mentioned, its a special location raid.  Its not shiny or a system raid boss
                    cntt=0
                    for x in self.Locbypass:
                        if Origname==x:
                            mentioned=1
                            rr2=discord.utils.get(server.roles, id=self.AddlNotiid[cntt])
                            await subf.grantacc(self,channloc,channrb,rr2)
                            #nid=self.PSnotid[cntt]
                            nid="0"
                            if not nid=="0":
                                rr5=discord.utils.get(server.roles, id=nid)
                                await subf.grantacc(self,channloc,channrb,rr5)
                                if self.notifyon==1:
                                    allmention = rr2.mention +" "+ rr5.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention + rr5.mention + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                            else:
                                if self.notifyon==1:
                                    allmention = rr2.mention
                                    msgg6=await subf.sendnote(self,msgchann,allmention,chmention,origname,endtime,emoji,linky)
                                    #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention + ", a " + type + " raid boss is about to start at " + Nameval + " and begins at " + tpoll + ". For more details visit " + xrs.mention + " " + xrs2.mention)
                        cntt+=1
                #Now to get the stuff to update the #active_raids channel
                #ch=self.bot.get_channel(self.genchid)
                print("Made it here")
                ch = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.genchid)
                print(ch)
                #First we have to find the message in the channel searching for o
                olocation=Origname
                #newlist=""
                #print(olocation)
                #print(ch)
                #await self.bot.send_message(ctx.message.channel, "Your update request has been processed!  Thank you.")
                
                #newlist=Milk.mention + " " + L3.mention +" "+Spec.mention
                #async for message in self.bot.logs_from(ch, limit=100): #Gets a list of the last 500 messages in the channel 
                    #print(message.content)
                #    if olocation in message.content: #This channel is the one needing updating
                        #print(message.content)
                if msgg6==None:
                    msgg6=await subf.sendnote(self,msgchann,"",chmention,origname,endtime,emoji,linky)
                message=msgg6
                argg=message.content.split("\n")
                #"__**Raid:**__"+allmention is on the first line
                arggn=argg[0].split("**__")
                oldmention=arggn[1]
            
                argg6=argg[1].split("ends at ")
                timeplusoldemo=argg6[1]
                
                argg7=timeplusoldemo.split(" ")
                oldemo=argg7[1]
                
                modmessp2=""
                for x in argg[2::]:
                    modmessp2+="\n" + x 
                
                #Now we need to reconstruct the message with the new mentions
                try:
                    #modmess=arggn[0] + "**__" + newlist + "\n" + argg6[0]+ "ends at " + argg7[0] + " " + emoji + modmessp2
                    meat=arggn[0] + "**__" + "\n" + argg6[0]+ "ends at " + argg7[0] + " " + emoji 
                    #We need unique members of the memlist
                    uniqmem=[]
                    for x in memlist:
                        if x not in uniqmem:
                            uniqmem.append(x) 
                    memlist=uniqmem
                    
                    mutelist=await subf.timemute(self,ctx,mutelist)
                    
                    
                    #Supress notifies to members of the mutegroup
                    msg=""
                    for f in memlist:
                        if not f in mutelist:
                            msg+=f.mention
                            if len(msg)>1000:
                                tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg)
                                await asyncio.sleep(1.0)
                                #await self.bot.edit_message(tms,meat)
                                await self.bot.delete_message(tms)
                                msg=""#

                    if len(msg)>=0:
                        tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg+Locan)
                        await asyncio.sleep(1.0)
                        #await self.bot.edit_message(tms,meat)
                        await self.bot.delete_message(tms)
                    
                    #msggg=await self.bot.send_message(ch,newlist) 
                    #await asyncio.sleep(2.0)
                    #await self.bot.delete_message(msggg)
                    #await self.bot.edit_message(message,modmess) 
                except:
                    modmess=message.content
                    
                    
                if not channrb==channloc:
                    await self.bot.send_message(channloc,linkn + "\n"+ channrb.mention)
                else:
                    if "olores" in Nameval:
                        await self.bot.send_message(channloc,linkn + "__**NOTE: DO NOT RAID IN FRONT OF THE EMERGENCY ROOM ENTRANCE**__\n")
                    if "CEMETERY" in Nameval.upper():
                        await self.bot.send_message(channloc,linkn + "__**NOTE: BE RESPECTFUL AS THIS IS A CEMETERY.  PLEASE REFRAIN FROM RAIDING IF A SERVICE IS ONGOING.**__\n")
                    if "GREENBUSH" in Nameval.upper():
                        await self.bot.send_message(channloc,linkn + "__**DO NOT BLOCK ALLEYWAYS. The cemetery gate on 12 is usually open for respectful visitors.**__\n")
                    if "CHURCH" in Nameval.upper():
                        await self.bot.send_message(channloc,linkn + "__**NOTE: BE RESPECTFUL AS THIS IS A PLACE OF WORSHIP.**__\n")
                    #if "olores" in Nameval:
                    #    await self.bot.send_message(channloc,linkn + "__**NOTE: DO NOT RAID IN FRONT OF THE EMERGENCY ROOM ENTRANCE**__\n")
                    #elif "elight" in Nameval:
                    #    await self.bot.send_message(channloc,linkn + "__**NOTE: Be aware that the alleyway is under construction. Do not obstruct the sidewalk!**__\n")
                    else:
                        await self.bot.send_message(channloc,linkn)
                msggr=await self.bot.send_message(channloc, "\n" + "\nReact to one of the following times with any emoji:")
                #delm=await self.bot.pin_message(msggr)
                #delm=await self.bot.delete_message(delm)
                
                if not channrb==channloc:
                    deleted=await self.bot.purge_from(channrb, limit=100)
                    await self.bot.move_channel(channrb, 0)
                    await self.bot.send_message(channrb,linkn+ "\n"+ channloc.mention)
                    msggr=await self.bot.send_message(channrb, "\n" + "\nReact to one of the following times with any emoji:")
                    #delm=await self.bot.pin_message(msggr)
                    #delm=await self.bot.delete_message(delm)
                await asyncio.sleep(0.25)
                msggr=await self.bot.send_message(channloc,'@Start: ' + hatch_time)
                if not channrb==channloc:
                    msggr2=await self.bot.send_message(channrb,'@Start: ' + hatch_time)
                await asyncio.sleep(0.25)
                for x in range(0,self.maxtimeslots):
                    
                    
                    msggr=await self.bot.send_message(channloc,'@Start: ' + tpoll)
                    if not channrb==channloc:
                        msggr2=await self.bot.send_message(channrb,'@Start: ' + tpoll)
                    await asyncio.sleep(0.25)
                    polltime += timedelta(minutes=self.raidspacing)
                    tpoll = polltime.strftime(self.timeform)
                try:
                    delm=await self.bot.pin_message(msggr)
                    delm=await self.bot.pin_message(msggr2)
                except:
                    uppo=1
                polltime += timedelta(minutes=-self.maxtimeslots* self.raidspacing)
                tpoll = polltime.strftime('%H:%M:%S')
                if weathertime==1:
                    arp=1
                    #msggr=await self.bot.send_message(channloc,"Pre-weather change raid time:\n")
                    #msggr=await self.bot.send_message(channloc,'@Start: ' + tpollwe)
                msggr=await self.bot.send_message(channloc,"_Use `%addtime` to create a new time_")
                msggr=await self.bot.send_message(channloc,"_^^^^^^^^^^^^^_")
                msggr=await self.bot.send_message(channloc,"RaidTrain: N/A")
                #return
                #delete the system pin messages, but keep the pin
                async for message in self.bot.logs_from(channrb, limit=500): #Gets a list of the last 500 
                    if message.type==discord.MessageType.pins_add:
                        await self.bot.delete_message(message)
                async for message in self.bot.logs_from(channloc, limit=500): #Gets a list of the last 500 
                    if message.type==discord.MessageType.pins_add:
                        await self.bot.delete_message(message)
                self.lastraid = datetime.utcnow()+timedelta(hours=self.timez)
                
                
                
                
                
                await subf.editnote(self,msgg6,allmention,chmention,origname,endtime,emoji,linky)
                polltimez = datetime.utcnow()+timedelta(hours=self.timez)
                tpolltimez=polltimez.strftime('%m/%d/%y %H:%M:%S')
                number = sum(1 for line in open('raids_ALL.txt'))+1
                onumber=str(number)
                number=str(number).zfill(4)              
                #await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
                #rr2=discord.utils.get(server.roles, id=self.RaidObserver)
                #await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + ctx.message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
                
                line=(("RAID {}    {}     {}    {}    {}   {}   {}""".format(number.ljust(4),statmess,type.ljust(8),str(timeleft).ljust(5),newloca[0:8].ljust(8),tpolltimez,ctx.message.author.display_name)))
                with open("raids_ALL.txt","a") as f:
                    print(line,file=f)
                
                
                #break        
            else:
                isallowed=1
                #Reiterate the information
                number = sum(1 for line in open('raids.txt'))+1
                onumber=str(number)
                number=str(number).zfill(4)              
                await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
                rr2=discord.utils.get(server.roles, id=self.RaidObserver)
                await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + ctx.message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
                
                line=(("{}    {}     {}    {}    {}   {}   {}""".format(number.ljust(4),statmess,type.ljust(8),str(timeleft).ljust(5),newloca[0:8].ljust(8),str_time,ctx.message.author.display_name)))
                with open("raids.txt","a") as f:
                    print(line,file=f)
                polltime = datetime.utcnow()+timedelta(hours=self.timez)
                if status=="1":
                    polltime += timedelta(minutes=45)
                argg=timeleft
                polltime += timedelta(minutes=int(argg))
                tpolltime=polltime.strftime('%H:%M:%S')
                
                tdeltat = datetime.strptime(tpolltime, '%H:%M:%S')-datetime.strptime("0:0:0", '%H:%M:%S')
                hours, remainder = divmod(tdeltat.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                
                polltime += timedelta(seconds=int(60-seconds))
                polltime += timedelta(minutes=1)
                polltime += timedelta(hours=-1)
                polltime += timedelta(minutes=15)
                tpoll = polltime.strftime('%H:%M:'+"00")
                for x in range(0,5):
                    polltime += timedelta(minutes=10)
                    tpoll = polltime.strftime('%H:%M:%S')
                polltime += timedelta(minutes=-50)
                tpoll = polltime.strftime('%H:%M:%S')
                polltimez = datetime.utcnow()+timedelta(hours=self.timez)
                tpolltimez=polltimez.strftime('%m/%d/%y %H:%M:%S')
                number = sum(1 for line in open('raids_ALL.txt'))+1
                onumber=str(number)
                number=str(number).zfill(4)              
                #await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
                #rr2=discord.utils.get(server.roles, id=self.RaidObserver)
                #await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + ctx.message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
                
                line=(("RAID {}    {}     {}    {}    {}   {}   {}""".format(number.ljust(4),statmess,type.ljust(8),str(timeleft).ljust(5),newloca[0:8].ljust(8),tpolltimez,ctx.message.author.display_name)))
                with open("raids_ALL.txt","a") as f:
                    print(line,file=f)#break             
            #if isallowed==0:
            uname=ctx.message.author.display_name
            uname=uname+str(ctx.message.author.discriminator)
            userid=ctx.message.author.id
            uname=await subf.getusernick(self,ctx,userid)
            #ap=10
            #if ap==10:
            return  #Only continue if we want to store user's data entries (will be released later)
            
            try: #If the sheet exists, open it 
                df = pd.read_excel('RaidTrainer' + "\\" + uname + 'rt.xlsx')
                df.iloc[0,0]+=1    
                writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                #print('Here99',df.iat[0,0],df.iat[0,0])
                if df.iloc[0,0]>1 and df.iloc[0,1]>=1:
                    notta=1
                    rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                    if not rrL in b.roles:
                        fr=await subf.grantRT(self,b,rrL)
                elif df.iloc[0,0]==1 and df.iloc[0,1]==1:
                    rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                    fr=await subf.grantRT(self,b,rrL)
                    if fr==1:
                        arp=1
                        #await self.bot.send_message(ctx.message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                    else:
                        arp=1
                        #await self.bot.send_message(ctx.message.author,uname+", please pester an RO to give you access NOW!  We need your help!") 
                else:
                    arp=1
                    #await self.bot.send_message(ctx.message.author,"It looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer and won't get this annoying message. If you have already met this requirement, pester a RaidObserver to give you access.")
            #else:
            except: #The person hasn't established a level yet
                df = pd.read_excel('RaidTrainer' + "\\" + 'rt' + '.xlsx')
                df.iloc[0,0]+=1    
                writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                if df.iat[0,0]==1 and df.iat[0,1]==1:
                    rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                    fr=await subf.grantRT(self,b,rrL)
                    if fr==1:
                        arp=1
                        #await self.bot.send_message(ctx.message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                    else:
                        arp=1
                        #await self.bot.send_message(ctx.message.author,uname+", please pester an RO to give you access NOW!  We need your help!") 
                else:
                    #print('Here2')
                    arp=1
                    #await self.bot.send_message(ctx.message.author,"It looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer and won't get this annoying message. If you have already met this requirement, pester a RaidObserver to give you access.")   
            return
        else:
            arpr=1
        #except:
        #    arpr=10
    
    
    @commands.command(pass_context=True)
    async def mutereg(self,ctx):
        """This function allows muting of notifications during a window of the user's choice"""
        #if not ctx.message.channel.is_private==True:
        #    await self.bot.send_message(ctx.message.channel,"Sorry, you need to DM that command to me. Click on my name and send me a message.")
        #    return
        alltimeout=30
        uname=ctx.message.author.id
        #uname=uname+str(ctx.message.author.discriminator)
        attempt=0
        success=0
        extra="Seems like you want to silence some notifications. If you need to quit at any time, press `q`.\n"
        while attempt<3 and success==0:
            await self.bot.send_message(ctx.message.channel,extra+"__**When is the earliest you want to receive raid notifications?**__\n Enter a time in XX:XX 24-hour format.")
            extra=""
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author,channel=ctx.message.channel)
            timeval=msgrt.content
            if msgrt.content.upper()=="Q": 
                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                return
            if "%mute" in timeval:
                await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%mute` while I'm asking you questions.  I'm gonna have to have to start over.")
                return
            if ":" in timeval:  #This could be a time
                textv=""
                argg=timeval.split(":")
                if int(argg[0])<0 or int(argg[0])>23: #The hour is wrong...
                    textv+="The hours number needs to be between 00 and 23, inclusive!  "#await self.bot.say("The hours number needs to be between 00 and 23!")
                if int(argg[1])<0 or int(argg[1])>59: #The hour is wrong...
                    textv+="The minutes number needs to be between 00 and 59, inclusive!  "#await self.bot.say("The hours number needs to be between 00 and 23!")
                if len(textv)>0:
                    await self.bot.say(textv)
                    attempt+=1
                else:  #Save the time in a user file
                    with open('ExcludeTime' + "\\" + uname + 'mute.txt','w') as g:
                        print(timeval,file=g)
                    success=1  
        if attempt>2:
            await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
            return
        attempt=0
        success=0
        extra="Great!\n"
        while attempt<3 and success==0:
            await self.bot.send_message(ctx.message.channel,extra+"__**When is the latest you want to receive raid notifications?**__\n Enter a time in XX:XX 24-hour format.")
            extra=""
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author,channel=ctx.message.channel)
            timeval2=msgrt.content
            if msgrt.content.upper()=="Q": 
                await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                return
            if "%mute" in timeval2:
                await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%mute` while I'm asking you questions.  I'm gonna have to have to start over.")
                return
            if ":" in timeval2:  #This could be a time
                textv=""
                argg2=timeval2.split(":")
                if int(argg2[0])<0 or int(argg2[0])>23: #The hour is wrong...
                    textv+="The hours must be between 00 and 23, inclusive!\n"#await self.bot.say("The hours number needs to be between 00 and 23!")
                if int(argg2[1])<0 or int(argg2[1])>59: #The hour is wrong...
                    textv+="The minutes must be between 00 and 59, inclusive!\n"#await self.bot.say("The hours number needs to be between 00 and 23!")
                if int(argg2[0])*60+int(argg[0])<int(argg[0])*60+int(argg[0]):
                    textv+="The end time for notifications must be after the start time!"
                if len(textv)>0:
                    await self.bot.say(textv)
                    attempt+=1
                else:  #Save the time in a user file
                    with open('ExcludeTime' + "\\" + uname + 'mute.txt','a') as g:
                        print(timeval2,file=g)
                    success=1  
        if attempt>2:
            await self.bot.send_message(ctx.message.channel,"Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
            return
        #await subf.timemute(self,ctx,[])
        await self.bot.send_message(ctx.message.channel,"You will only receive raid alerts between "+timeval+ " and "+timeval2)
    
    
    
    @checks.admin()  
    @commands.command(pass_context=True)
    async def modify(self,ctx,type=None,input1=None):
        """Change parameters of a raid
        location=Short name of the location
        type --> BOSS Change the raid boss [Bossname required]
             --> TIME Shift the end time by [Minutes required (can be negative)]
             --> STATUS Change the boss status from when you entered it [1=Egg 2=Boss])"""
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        isallowed=0
        for findl in range(1,len(f)):
            if f[findl].id==self.RaidObserver:
                isallowed=1
        if isallowed==0:
            await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of raid information.  Contact a RaidObserver to gain access.")        
            return
        print("ok")    
        #Verify this is a raid channel or escape
        israidch=0
        idv=ctx.message.channel.id
        majorg=self.alllocch+self.allrbch
        if any(x==idv for x in majorg): #It is a raid channel and the bot needs to delete user messages
            israidch=1
        if israidch==0:
            await self.bot.send_message(ctx.message.author,"That command was not entered in a raid channel.")
            return
        
        if type==None or input1==None:
            await self.bot.send_message(ctx.message.author,"This command must have three inputs:\n %modify X ARG\nX=boss --> Change the raid boss [ARG=New Raid Boss Name]\nX=status --> Change the boss status from when you entered it [1=Entered Boss, meant egg / 2=Entered Egg, meant boss].")
            return
        
        #Get the name of this channel and see if there is an additional channel
        chnid=ctx.message.channel.id
        argg=ctx.message.channel.name.split('---')
        found=await subf.findchidloca2(self,await subf.filtNameval(self,argg[0]))
        #If the channel is a raid boss specific channel, the second channel will lead with the raid boss
        await self.bot.delete_message(ctx.message)
        #print(ctx.message.channel.name)
        #return
        if found==1:
            raidboss=argg[1]
            location=argg[0]
            namel2=raidboss + "-_-" +  location
            newname2=input1 + "-=-=-" +  location
            newname1=location + "-=-=-" +  input1 
        else:
            raidboss=argg[0]
            location=argg[1]
            namel2=location + "-_-" +  raidboss
            newname2=location + "-=-=-" +  input1 
            newname1=input1 + "-=-=-" +  location                 
        
        
        #return
        #Boss should be in the system unless its an addlnotify raid
        
        channel1 = ctx.message.channel
        channel2 = discord.utils.get(ctx.message.server.channels, name=namel2)    
        
        onech=0
        if channel2==None: #the channel wasn't found
            channel2=channel1 
            onech=1  #Flag indicating only one channel is to be modified
        
        if type.upper()=="BOSS": #Change the raid boss of a raid at this location

            await self.bot.send_message(self.bot.get_channel(self.programid),input1.upper())
            rrL=""
            rrrb=""
            rrL2=""
            rrrb2=""
            #Before changing the boss, we need to get the old notifies:
            #NEEDOPTO
            cntt=0
            for x in self.L5types:
                if x==raidboss.upper():
                    rrL=discord.utils.get(ctx.message.server.roles, id=self.L5Notify).mention
                    rrrb=discord.utils.get(ctx.message.server.roles, id=self.L5notid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.L4types:
                if x==raidboss.upper():
                    rrL=discord.utils.get(ctx.message.server.roles, id=self.L4Notify).mention
                    rrrb=discord.utils.get(ctx.message.server.roles, id=self.L4notid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.L3types:
                if x==raidboss.upper():
                    rrL=discord.utils.get(ctx.message.server.roles, id=self.L3Notify).mention
                    rrrb=discord.utils.get(ctx.message.server.roles, id=self.L3notid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.PStypes:
                if x==raidboss.upper():
                    rrL2=discord.utils.get(ctx.message.server.roles, id=self.PSNotify).mention
                    rrrb2=discord.utils.get(ctx.message.server.roles, id=self.PSnotid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.OItypes:
                if x==raidboss.upper():
                    rrL2=discord.utils.get(ctx.message.server.roles, id=self.OINotify).mention
                    rrrb2=discord.utils.get(ctx.message.server.roles, id=self.OInotid[cntt]).mention
                cntt+=1
            cntt=0
            
            #Change the channel names
            await self.bot.edit_channel(channel1, name=newname1)
            if onech==0:
                await self.bot.edit_channel(channel2, name=newname2) 
            #await self.bot.send_message(self.bot.get_channel(self.programid),str(namel2))
            
            #We need to update the Notification for the boss updated
            nrrL=""
            nrrrb=""
            nrrL2=""
            nrrrb2=""
            #Before changing the boss, we need to get the old notifies:
            #NEEDOPTO
            #await self.bot.send_message(self.bot.get_channel(self.programid),input1.upper())
            cntt=0
            for x in self.L5types:
                if x==input1.upper():
                    nrrL=discord.utils.get(ctx.message.server.roles, id=self.L5Notify).mention
                    nrrrb=discord.utils.get(ctx.message.server.roles, id=self.L5notid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.L4types:
                if x==input1.upper():
                    nrrL=discord.utils.get(ctx.message.server.roles, id=self.L4Notify).mention
                    nrrrb=discord.utils.get(ctx.message.server.roles, id=self.L4notid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.L3types:
                if x==input1.upper():
                    nrrL=discord.utils.get(ctx.message.server.roles, id=self.L3Notify).mention
                    nrrrb=discord.utils.get(ctx.message.server.roles, id=self.L3notid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.PStypes:
                if x==input1.upper():
                    nrrL2=discord.utils.get(ctx.message.server.roles, id=self.PSNotify).mention
                    nrrrb2=discord.utils.get(ctx.message.server.roles, id=self.PSnotid[cntt]).mention
                cntt+=1
            cntt=0
            for x in self.OItypes:
                if x==input1.upper():
                    nrrL2=discord.utils.get(ctx.message.server.roles, id=self.OINotify).mention
                    nrrrb2=discord.utils.get(ctx.message.server.roles, id=self.OInotid[cntt]).mention
                cntt+=1
            cntt=0
            if rrL + rrL2 + rrrb + rrrb2 == "":
                rrL=raidboss.capitalize()
            if nrrL + nrrL2 + nrrrb + nrrrb2 == "":   
                nrrL=input1.capitalize()
            #await self.bot.send_message(self.bot.get_channel(self.genchid), "The "+rrL + rrL2 + rrrb + rrrb2 + " raid boss at `" + location.capitalize() + "` has been switched to " +nrrL + nrrL2 + nrrrb + nrrrb2)
            
        elif type.upper()=="STATUS": #Change the status of the egg/
            #Get Both channels here
            
            channel=self.bot.get_channel(self.programid)  
            if onech==1:
                chans=[channel1]
            else:
                chans=[channel1,channel2]
            #Repeat the following for both channels
            for ch in chans:
                async for message in self.bot.logs_from(ch, limit=100): #Gets a list of the last 500 messages in the channel 
                    if message.content.startswith('RAID:'): #Then we need to get the ID of this message and see if it has the correct start time
                        a=message
                        arggn=a.content.split('\n')  
                        argg=arggn[0].split(' ends at ')  
                        
                        polltime = datetime.utcnow()+timedelta(hours=self.timez)
                        tpolltime=polltime.strftime('%H:%M:%S')
                        if input1=="1":
                            tdeltat = datetime.strptime(argg[1], '%H:%M:%S')+timedelta(minutes= self.raidmaxtime)
                        elif input1=="2":
                            tdeltat = datetime.strptime(argg[1], '%H:%M:%S')+timedelta(minutes=-self.raidmaxtime)
                        tdeltat=tdeltat.strftime('%H:%M:%S')
                        
                        #Now rewrite the data
                        arrs=""
                        if "\n" in a.content:
                            arrs="-->"
                        try:
                            await self.bot.edit_message(a,argg[0] + ' ends at ' + str(tdeltat) + '\n' + arggn[1] + '\n' + arggn[2] + '\n' + arggn[3])
                        except:
                            await self.bot.edit_message(a,argg[0] + ' ends at ' + str(tdeltat) + '\n' + arggn[1] + '\n' + arggn[2] + '\n' + arggn[3])
     
                    elif message.content.startswith('@Start:'): #Then we need to get the ID of this message and see if it has the correct start time
                        a=message
                        arggn=a.content.split('-->')  #The second argument will be the minutes
                        arggn2=arggn[0].split(' ')  #The second argument will be the minutes
                        argg=arggn2[1]

                        polltime = datetime.utcnow()+timedelta(hours=self.timez)
                        tpolltime=polltime.strftime('%H:%M:%S')
                        if input1=="1":
                            tdeltat = datetime.strptime(argg, '%H:%M:%S')+timedelta(minutes= self.raidmaxtime)
                        elif input1=="2":
                            tdeltat = datetime.strptime(argg, '%H:%M:%S')+timedelta(minutes=-self.raidmaxtime)
                        tdeltat=tdeltat.strftime('%H:%M:%S')
                        
                        #Now rewrite the data
                        arrs=""
                        if "-->" in a.content:
                            arrs="-->"
                        try:
                            await self.bot.edit_message(a,arggn2[0] + " " + str(tdeltat) + arrs + arggn[1])
                        except:
                            await self.bot.edit_message(a,arggn2[0] + " " + str(tdeltat) + arrs)
        elif type.upper()=="TIME": #Change the start time of the egg/
            #Get Both channels here
            shifttime=int(input1)
            print(shifttime)
            channel=self.bot.get_channel(self.programid)  
            if onech==1:
                chans=[channel1]
            else:
                chans=[channel1,channel2]
            #Repeat the following for both channels
            for ch in chans:
                async for message in self.bot.logs_from(ch, limit=100): #Gets a list of the last 500 messages in the channel 
                    if message.content.startswith('__**RAID:'): #Then we need to get the ID of this message and see if it has the correct start time
                        a=message
                        arggn=a.content.split('\n')  
                        argg=arggn[0].split(' ends at ')  
                        print (argg)
                        polltime = datetime.utcnow()+timedelta(hours=self.timez)
                        tpolltime=polltime.strftime(self.timeform)
                        #if input1=="1":
                        tdeltat = datetime.strptime(argg[1], self.timeform)+timedelta(minutes= shifttime)
                        #elif input1=="2":
                        #    tdeltat = datetime.strptime(argg[1], '%H:%M:%S')+timedelta(minutes=-self.raidmaxtime)
                        tdeltat=tdeltat.strftime(self.timeform)
                        
                        #Now rewrite the data
                        arrs=""
                        if "\n" in a.content:
                            arrs="-->"
                        try:
                            await self.bot.edit_message(a,argg[0] + ' ends at ' + str(tdeltat) + '\n' + arggn[1] + '\n' + arggn[2] + '\n' + arggn[3])
                        except:
                            try:
                                await self.bot.edit_message(a,argg[0] + ' ends at ' + str(tdeltat) + '\n' + arggn[1] + '\n' + arggn[2])# + '\n' + arggn[3])
                            except:
                                await self.bot.edit_message(a,argg[0] + ' ends at ' + str(tdeltat) + '\n' + arggn[1])# + '\n' + arggn[2] + '\n' + arggn[3])
                            #await self.bot.edit_message(a,argg[0] + ' ends at ' + str(tdeltat) + '\n' + arggn[1] + '\n' + arggn[2] + '\n' + arggn[3])
     
                    elif message.content.startswith('@Start:'): #Then we need to get the ID of this message and see if it has the correct start time
                        a=message
                        arggn=a.content.split('-->')  #The second argument will be the minutes
                        arggn2=arggn[0].split(' ')  #The second argument will be the minutes
                        argg=arggn2[1]

                        polltime = datetime.utcnow()+timedelta(hours=self.timez)
                        tpolltime=polltime.strftime(self.timeform)
                        #if input1=="1":
                        tdeltat = datetime.strptime(argg, self.timeform)+timedelta(minutes= shifttime)
                        #elif input1=="2":
                        #    tdeltat = datetime.strptime(argg, '%H:%M:%S')+timedelta(minutes=-self.raidmaxtime)
                        tdeltat=tdeltat.strftime(self.timeform)
                        
                        #Now rewrite the data
                        arrs=""
                        if "-->" in a.content:
                            arrs="-->"
                        try:
                            await self.bot.edit_message(a,arggn2[0] + " " + str(tdeltat) + arrs + arggn[1])
                        except:
                            await self.bot.edit_message(a,arggn2[0] + " " + str(tdeltat) + arrs)
            
            #await self.bot.send_message(self.bot.get_channel(self.programid),"Type 2 Entered")
        else:
            await self.bot.send_message(self.bot.get_channel(self.programid),"Type bad Entered")

        #Delete the message
        try:
            await self.bot.delete_message(ctx.message)
        except:
            AAA=1    
    
    @checks.admin()
    @commands.command(pass_context=True)
    async def delraid(self,ctx,location):
        """Deletes a raid for a given location
        Location --> Enter the name of the gym (First 8 letters without spaces or symbols)"""
        ar=1
        if ar==1:
        #try:
            self.Allroles=[]
            for x in self.Bossnotid+self.AddlNotiid+self.SilentRoles:
                self.Allroles.append(discord.utils.get(ctx.message.server.roles, id=x))
            member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
            f=b.roles
            for idx in f: 
                if idx.id==self.Approved:   
                    role_everyone = idx
            role_pogomod=discord.utils.get(ctx.message.server.roles, id=self.POGOmod)  
            isallowed=0
            for findl in range(1,len(f)):
                if f[findl].id==self.RaidObserver:
                    isallowed=1
            if isallowed==0:
                await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of raid information.  Contact a RaidObserver to gain access.")        
                return
            
                    #We need to find the 2 channels first
            cntt=0
            uniq=0
            grid=0
            if len(location)<8:
                for x in range(0,8-len(location)):
                    location=location + " "
            loc=location[0:8]
            for x in self.group1sn:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=1
                    Nameval=self.group1cn[cntt]
                cntt=cntt+1
            cntt=0
            for x in self.group2sn:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=2
                    Nameval=self.group2cn[cntt]
                cntt=cntt+1
            cntt=0
            for x in self.group3sn:
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=3
                    Nameval=self.group3cn[cntt]
                cntt=cntt+1
            if uniq>1:
                optnum=1
                cntt=0
                ncha=0
                Nameval=''
                
                for x in self.group1sn:
                    if loc.upper()==x.upper():
                        Nameval=Nameval + str(optnum) + ")" + self.group1cn[cntt] #+ ": Use '" + self.group1an[cntt] + "'\n"
                        optnum=optnum+1
                        ncha=ncha+1
                    cntt=cntt+1
                cntt=0
                for x in self.group2sn:
                    if loc.upper()==x.upper():
                        Nameval=Nameval + str(optnum) + ")" + self.group2cn[cntt] #+ ": Use '" + self.group2an[cntt] + "'\n"
                        optnum=optnum+1
                        ncha=ncha+1
                    cntt=cntt+1
                cntt=0
                for x in self.group3sn:
                    if loc.upper()==x.upper():
                        Nameval=Nameval + str(optnum) + ")" + self.group3cn[cntt] #+ ": Use '" + self.group3an[cntt] + "'\n"
                        optnum=optnum+1
                        ncha=ncha+1
                    cntt=cntt+1
                
            
                if ncha==0:  #Channel name isn't in alt or shortname
                    await self.bot.say("`The gym name you entered is not available in the system`")
                    return
                elif ncha>1: #Unique Channel name doesn't exist
                    await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by retyping the command with one of the following gym names:\n")
                    await self.bot.say("`{}`".format(Nameval))
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    try:
                        loc=LVal[int(msgrt.content)-1]
                    except:
                        return
            
            
            cntt=0
            uniq=0
            grid=0
            for x in self.group1an:
                #await self.bot.send_message(self.bot.get_channel(self.programid),str(uniq)+loc.upper()+x)
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=1
                    Nameval=self.group1cn[cntt]
                    #linkn=self.group1ln[cntt]
                    #linkn="Summary: A " + type.upper() + " raid boss ends at "+ str_time +"\n\nDirections to this gym can be found here:\n" + "https://www.google.com/maps/place/" + linkn + ""
                cntt=cntt+1
            cntt=0
            for x in self.group2an:
                #await self.bot.send_message(self.bot.get_channel(self.programid),str(uniq)+loc.upper()+x)
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=2
                    Nameval=self.group2cn[cntt]
                    #linkn=self.group2ln[cntt]
                    #linkn="Summary: A " + type.upper() + " raid boss ends at "+ str_time +"\n\nDirections to this gym can be found here:\n" + "https://www.google.com/maps/place/" + linkn + ""
                cntt=cntt+1
            cntt=0
            for x in self.group3an:
                #await self.bot.send_message(self.bot.get_channel(self.programid),str(uniq)+loc.upper()+x)
                if loc.upper()==x.upper():
                    uniq=uniq+1
                    grid=3
                    Nameval=self.group3cn[cntt]
                    #linkn=self.group3ln[cntt]
                    #linkn="Summary: A " + type.upper() + " raid boss ends at "+ str_time +"\n\nDirections to this gym can be found here:\n" + "https://www.google.com/maps/place/" + linkn + ""
                cntt=cntt+1
            
            if uniq==0:
                await self.bot.say("`The gym name you entered is not available in the system`")
                return
            
            Origname=Nameval
            Nameval=await subf.filtNameval(self,Nameval)
            
            channel1=None  
            channel2=None         
            #Now with the location, find the channels and clear them
            for x in self.g1locaid:
                ch=self.bot.get_channel(x)
                if Nameval in ch.name:
                    channel1=ch
                    break
            for x in self.g2locaid:
                ch=self.bot.get_channel(x)
                if Nameval in ch.name:
                    channel1=ch
                    break
            for x in self.g3locaid:
                ch=self.bot.get_channel(x)
                if Nameval in ch.name:
                    channel1=ch
                    break
            for x in self.L3groupid:
                ch=self.bot.get_channel(x)
                if Nameval in ch.name:
                    channel2=ch
                    break
            for x in self.L4groupid:
                ch=self.bot.get_channel(x)
                if Nameval in ch.name:
                    channel2=ch
                    break
            for x in self.L5groupid:
                ch=self.bot.get_channel(x)
                if Nameval in ch.name:
                    channel2=ch
                    break
            for x in self.PSgroupid:
                ch=self.bot.get_channel(x)
                if Nameval in ch.name:
                    channel2=ch
                    break
            
            #print(channel1,channel2)
            #return
            if channel1==None:
                await self.bot.send_message(ctx.message.channel,"A raid at that location hasn't been entered!")
                return
            #role_RO=discord.utils.get(ctx.message.server.roles, id=self.RaidObserver)
            #await subf.clearone(self,channel1.id,role_everyone)
            #await subf.clearone(self,channel1.id,role_RO)
            #await subf.clearone(self,channel1.id,role_pogomod)
            for rra in self.Allroles:
                if not rra==None:
                    rr=await subf.clearone(self,channel1,rra)
            cntt=0
            async for message in self.bot.logs_from(channel1, limit=5000): #Gets a list of the last 500 messages in the channel 
                cntt+=1 #await self.bot.delete_message(message)
            for ppr in range(0,cntt%100+1):
                deleted=await self.bot.purge_from(channel1, limit=100)
            await self.bot.edit_channel(channel1, name='blank-' + str(0))
            if channel2==None:            
                return
            #await subf.clearone(self,channel2.id,role_everyone)
            #await subf.clearone(self,channel2.id,role_RO)
            #await subf.clearone(self,channel2.id,role_pogomod)
            for rra in self.Allroles:
                if not rra==None:
                    rr=await subf.clearone(self,channel2,rra)
            cntt=0
            async for message in self.bot.logs_from(channel2, limit=5000): #Gets a list of the last 500 messages in the channel 
                cntt+=1 #await self.bot.delete_message(message)
            for ppr in range(0,cntt%100+1):
                deleted=await self.bot.purge_from(channel2, limit=100)
            await self.bot.edit_channel(channel2, name='blank-' + str(0))
        else:
        #except:
            arpr=10
                      
    
    #This is the atomic option, in the event the bot crashed in the middle of a day
    #It deletes all messages in raid channels, and recreates the messages so people can react to them again
    #Ready for publication
    @checks.admin() #Can only be used by admins
    @commands.command(pass_context=True)
    async def reseter(self,ctx):
        #Revise all current messages in raid channels if any exist to build a cache
        for f in self.allbutmtch: #Limit this function to raid channels only
            ch = discord.utils.get(ctx.message.server.channels, id=f) 
            async for message in self.bot.logs_from(ch, limit=1000, reverse=True): #Gets a list of the last 500 messages in the channel 
                a=message
                await  self.bot.send_message(a.channel,a.content)
                await  self.bot.delete_message(a)
        await self.bot.send_message(ctx.message.channel,"done")
    
    #This command resets only one channel, similar to %reseter
    #Ready for publication
    @checks.admin() #Can only be used by admins
    @commands.command(pass_context=True)
    async def resetch(self,ctx):
        #Revise all current messages in raid channels if any exist to build a cache
        ch=ctx.message.channel   
        cnt=1
        async for message in self.bot.logs_from(ch, limit=1000, reverse=True): #Gets a list of the last 500 messages in the channel 
            a=message
            if cnt<=10:
                await  self.bot.send_message(a.channel,a.content)
            await self.bot.delete_message(a)
            cnt+=1
        await self.bot.send_message(ctx.message.channel,"done") 
    
    #An alert message to remind trainers that the raid time is approaching
    #Anyone can use this function
    #Ready for publication
    @commands.command(pass_context=True)
    async def buzz(self,ctx,minute): #Modify this to rework the original message
        """Use this function to alert trainers who signed for a certain raid time. This function will only work within the last 10 minutes prior to the scheduled raid time.  
        minute--> the digits of the minute corresponding to the raid time.  (i.e. 10:50 --> 50)"""
        #This function will let users ensure time is nearing
        ch=ctx.message.channel
        #Make sure the users weren't buzzed already
        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel
            if message.content.startswith("BUZZ: "):  #This is possibly a buzz
                a=message
                argg=a.content.split(".")
                mins=argg[0].split(":")
                if int(mins[2])==int(minute): #They were buzzed
                    await self.bot.send_message(ch,"A buzz has already been used for this reservation time.")
                    return     
        #find the message with the correct minutes
        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
            if message.content.startswith("@Start:"):  #This is possibly a reservation time
                a=message
                argg=a.content.split(":")
                if int(argg[2])==int(minute):
                    #Ensure we are within a 10 minute window of the raid time
                    polltime = datetime.utcnow()+timedelta(hours=self.timez)
                    hrs=argg[1]
                    tpolltime=polltime.strftime('%H:%M:%S')
                    tdeltat = datetime.strptime(hrs[1::]+":"+argg[2]+":00", '%H:%M:%S')-datetime.strptime(tpolltime, '%H:%M:%S')
                    days = tdeltat.days
                    hours, remainder = divmod(tdeltat.seconds, 3600)
                    minutes1, seconds = divmod(remainder, 60)
                    if minutes1<=10 and minutes1>=-5:
                        memlist=[]
                        for xi in range(0,len(a.reactions)):
                            useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                            for yi in range(0,len(useri)):
                                namer=useri[yi]
                                member = discord.utils.get(ctx.message.server.members, name=namer.name)
                                memlist.append(member)
                        
                        uniqemo=[]
                        for x in memlist:
                            if x not in uniqemo:
                                uniqemo.append(x) 
                        memlist=uniqemo
                        #Generate a message with recipients
                        newmsg="BUZZ: "
                        for x in memlist:
                            newmsg+=x.mention
                        if len(memlist)==0:
                            await self.bot.send_message(ch,"You do realize no one is signed up for that time, right?")
                            return
                        newmsg+=", the raid time you requested will start at"+argg[1]+":"+argg[2]+". Please make sure you'll show up on time, or please remove your reservation.  Thanks!"
                        await self.bot.send_message(ch,newmsg)
                    else:
                        await self.bot.send_message(ch,"Buzzing for that time is not available right now.  Please wait until 10 minutes before the raid time starts.")
            
        return    
    
    #An customizable alert message to remind trainers who reacted for a given raid time
    #Anyone can use this function
    #Ready for publication
    @commands.command(pass_context=True)
    async def alert(self,ctx,minute,*,content : str): #Modify this to rework the original message
        """Use this function to alert trainers who signed for a certain raid time. This function will only work within the last 10 minutes prior to the scheduled raid time.  
        minute--> the digits of the minute corresponding to the raid time.  (i.e. 10:50 --> 50)"""
        #This function will let users ensure time is nearing
        ch=ctx.message.channel   
        #find the message with the correct minutes
        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
            #print(message.content)
            if message.content.startswith("@Start:"):  #This is possibly a reservation time
                a=message
                argg=a.content.split(":")
                if int(argg[2])==int(minute):
                    #Ensure we are within a 10 minute window of the raid time
                    polltime = datetime.utcnow()+timedelta(hours=self.timez)
                    hrs=argg[1]
                    tpolltime=polltime.strftime('%H:%M:%S')
                    tdeltat = datetime.strptime(hrs[1::]+":"+argg[2]+":00", '%H:%M:%S')-datetime.strptime(tpolltime, '%H:%M:%S')
                    days = tdeltat.days
                    hours, remainder = divmod(tdeltat.seconds, 3600)
                    minutes1, seconds = divmod(remainder, 60)
                    memlist=[]
                    for xi in range(0,len(a.reactions)):
                        useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                        for yi in range(0,len(useri)):
                            namer=useri[yi]
                            member = discord.utils.get(ctx.message.server.members, name=namer.name)
                            memlist.append(member)
                                       
                    uniqemo=[]
                    for x in memlist:
                        if x not in uniqemo:
                            uniqemo.append(x) 
                    memlist=uniqemo

                    #Generate a message with recipients
                    newmsg="ALERT: "
                    for x in memlist:
                        newmsg+=x.mention
                    if len(memlist)==0:
                        await self.bot.send_message(ch,"You do realize no one is signed up for that time, right?")
                        return
                    newmsg+= " " + content
                    await self.bot.send_message(ch,newmsg)
        return 
    
    #Send a message to people who reacted for a raid time that it is being cancelled
    #Anyone can use this
    #Ready for publication
    @commands.command(pass_context=True)
    async def RIP(self,ctx,minute): #Modify this to rework the original message
        """Use this function to cancel a certain raid. 
        minute--> the digits of the minute corresponding to the raid time.  (i.e. 10:50 --> 50)"""
        ch=ctx.message.channel
        #Make sure the users weren't cancelled on already
        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel
            if message.content.startswith("CANCEL: "):  #This is possibly a cancel notification
                a=message
                argg=a.content.split(".")
                mins=argg[0].split(":")
                minr=mins[2][0:2]
                #print(minr)
                if int(minr)==int(minute): #They were buzzed
                    #print('Used')
                    await self.bot.send_message(ch,"A cancellation has already been used for this reservation time.")
                    return       
        #find the message with the correct minutes
        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
            #print(message.content)
            if message.content.startswith("@Start:"):  #This is possibly a reservation time
                a=message
                argg=a.content.split(":")
                
                
                
                if int(argg[2])==int(minute):
                    #Ensure we are within a 10 minute window of the raid time
                    polltime = datetime.utcnow()+timedelta(hours=self.timez)
                    hrs=argg[1]
                    tpolltime=polltime.strftime('%H:%M:%S')
                    tdeltat = datetime.strptime(hrs[1::]+":"+argg[2]+":00", '%H:%M:%S')-datetime.strptime(tpolltime, '%H:%M:%S')
                    days = tdeltat.days
                    hours, remainder = divmod(tdeltat.seconds, 3600)
                    minutes1, seconds = divmod(remainder, 60)

                    if minutes1<=90 and minutes1>=0:
                        memlist=[]
                        for xi in range(0,len(a.reactions)):
                            useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                            for yi in range(0,len(useri)):
                                namer=useri[yi]
                                member = discord.utils.get(ctx.message.server.members, name=namer.name)
                                memlist.append(member)
                                
                        
                        uniqemo=[]
                        for x in memlist:
                            if x not in uniqemo:
                                uniqemo.append(x) 
                        memlist=uniqemo

                        #print(memlist)
                        #Generate a message with recipients
                        newmsg="CANCEL: "
                        for x in memlist:
                            newmsg+=x.mention
                        if len(memlist)==0:
                            await self.bot.send_message(ch,"You do realize no one is signed up for that time, right?")
                            return
                        newmsg+=", the raid time you requested at"+argg[1]+":"+argg[2]+" is being cancelled by " + ctx.message.author.display_name+ "! If you still want to do this raid, you may need to find more people"
                        await self.bot.send_message(ch,newmsg)
                    else:
                        await self.bot.send_message(ch,"Cancelling this raid is not available.  You can't cancel after the scheduled raid time.")
            
        return 
    
    #Alert users in the event a raid needs to be evacuated
    #Allow anyone to use this function
    #Ready for publication
    @commands.command(pass_context=True)
    async def back(self,ctx,minute): #Modify this to rework the original message
        """Use this function to alert trainers who signed for a certain raid time. This function will only work between two minutes before and ten minutes after the scheduled raid time.  
        minute--> the digits of the minute corresponding to the raid time.  (i.e. 10:50 --> 50)"""
        ch=ctx.message.channel
        
        async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
            if message.content.startswith("@Start:"):  #This is possibly a reservation time
                a=message
                argg=a.content.split(":")
                if int(argg[2])==int(minute):
                    #Ensure we are within a 10 minute window of the raid time
                    polltime = datetime.utcnow()+timedelta(hours=self.timez)
                    hrs=argg[1]
                    tpolltime=polltime.strftime('%H:%M:%S')
                    tdeltat = datetime.strptime(hrs[1::]+":"+argg[2]+":00", '%H:%M:%S')-datetime.strptime(tpolltime, '%H:%M:%S')
                    days = tdeltat.days
                    hours, remainder = divmod(tdeltat.seconds, 3600)
                    minutes1, seconds = divmod(remainder, 60)

                    if minutes1<=2:
                        memlist=[]
                        for xi in range(0,len(a.reactions)):
                            useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                            for yi in range(0,len(useri)):
                                namer=useri[yi]
                                member = discord.utils.get(ctx.message.server.members, name=namer.name)
                                memlist.append(member)
                                
                        
                        uniqemo=[]
                        for x in memlist:
                            if x not in uniqemo:
                                uniqemo.append(x) 
                        memlist=uniqemo

                        newmsg="BACK OUT!! "
                        for x in memlist:
                            newmsg+=x.mention
                        if len(memlist)==0:
                            await self.bot.send_message(ch,"You do realize no one is signed up for that time, right?")
                            return
                        newmsg+=", something happened during the raid!  Leave the lobby now!"
                        await self.bot.send_message(ch,newmsg)
                    else:
                        await self.bot.send_message(ch,"The raid should not have started yet, you cant use this function.")
            
        return
     
    #This provides an overall assesment of the number of people who have used the server for raids
    @checks.admin() #Only Admins can run this
    @commands.command(pass_context=True)
    async def trainerstats(self,ctx):
        nlevel=-1
        msg=""
        for filename in os.listdir('ExcelFiles\\'):
            nlevel+=1 
        msg+=str(nlevel) + " Trainers have assigned levels.\n"
        await self.bot.send_message(ctx.message.channel,msg)
        await self.bot.delete_message(ctx.message) 
    
    #THIS REQUIRES A LOT OF WORK
    
    @commands.command(pass_context=True)
    async def update(self,ctx): #Modify this to rework the original message
        """This function updates the raid boss at a given gym.
        Location --> Enter the name of the gym (First 8 letters without spaces or symbols)
        Type --> Pokemon raid boss name (i.e. Victreebel)"""

        aa1=0
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        server=channre.server
        if ctx.message.channel.is_private:
            allowa=1
            aa1=10
        else:
            if (ctx.message.channel.id==self.raidsightings or ctx.message.channel.id==self.programid): 
                aa1=10
            elif ctx.message.channel.id in self.allbutmtch:
                aa1=9
            else:
                chh=self.bot.get_channel(self.raidsightings)
                await self.bot.send_message(ctx.message.channel,"Sorry, trainer. Please go to "+chh.mention+"  to enter this command.")
                return
        alltimeout=30
        mutelist=[]
        
        if aa1==9:
            raidn=0
            #await self.bot.send_message(ctx.message.channel,"This about about to get really cool!")
            #grab the gymname
            member = discord.utils.get(server.members, name=ctx.message.author.name)
            b=discord.Server.get_member(server,ctx.message.author.id)
            f=b.roles
            isallowed=1
            isRO=0
            for findl in range(1,len(f)):
                if f[findl].id==self.RaidObserver:
                    isallowed=1
                    isRO=1
                if f[findl].id==self.RaidTrainer:
                    isallowed=1    
            isRO=0
            if any(xpp == ctx.message.author.display_name for xpp in self.threeleaders):
                isRO=0
            
            namv=ctx.message.content
            findboss=namv.split(' ')
            if len(findboss)==1:
                await self.bot.send_message(ctx.message.channel,"I need the name of the boss.  Type in `%update bossname` to update this raid.")
                return
            type=findboss[1]
            namv=ctx.message.channel.name
            tempnam=namv.split('---')
            lvltxt=tempnam[0]
            cntt=0
            for x in self.cngroup:
                Orignamec=x
                Namevalc=await subf.filtNameval(self,x)
                if tempnam[1].upper()==Namevalc.upper():
                    Nameval=self.cngroup[cntt]
                    #linkn=self.lngroup[cntt]
                    gymlat=self.latgroup[cntt]
                    gymlon=self.longroup[cntt]
                    linkn = "" + gymlat + "," + gymlon + ""
                    olink=linkn
                    #break
                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                cntt=cntt+1
            RaidBossfound=0
            isLoc=0
            if any(xpp == Nameval for xpp in self.Locbypass): #We need to allow this boss to be entered anyway
                RaidBossfound=1    
                isLoc=1
            print(isLoc)
        elif aa1==10:
        #try:
            #if aa1==10:
            try:
                await asyncio.sleep(0.5)
                member = discord.utils.get(server.members, name=ctx.message.author.name)
                b=discord.Server.get_member(server,ctx.message.author.id)
                f=b.roles
                isallowed=0
                isRO=0
                for findl in range(1,len(f)):
                    if f[findl].id==self.RaidObserver:
                        isallowed=1
                        isRO=1
                    if f[findl].id==self.RaidTrainer:
                        isallowed=1    
                isRO=0
                if any(xpp == ctx.message.author.display_name for xpp in self.threeleaders):
                    isRO=0
                
                ara=self.mutemap
                if ara==1:
                    try:
                        if (ctx.message.author.id=="341977078213902336"):
                            await self.bot.send_message(ctx.message.channel,"To continue, please post a screen capture of the raid boss.")
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                            if len(msgrt.attachments)==0:
                                await self.bot.send_message(ctx.message.channel,"This is not a gym screen capture.  Please start over.")
                                return
                            if "%update" in msgrt.content:
                                await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%update` while I'm asking you questions.  I'm gonna have to have to start over.")
                                return
                    except:
                        arrr=1
                        await self.bot.send_message(ctx.message.channel,"I need a screen capture of the gym to continue.  Please start over.")                    
                        return                    
                attempt=0
                success=0
                extra="Looks like you're trying to tell everyone about an update to a raid. If you need to quit at any time, press `q`.\n"
                while attempt<3 and success==0:
                    await self.bot.send_message(ctx.message.channel,extra+"__**What is the Pokemon Go gym name?**__\n You may enter *a keyword* or the first 8 letters without spaces or special characters (i.e. A+ Storage Mural = astorage)")
                    extra=""
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    location=msgrt.content
                    if msgrt.content.upper()=="Q": 
                        await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                        return
                    if "%update" in location:
                        await self.bot.send_message(ctx.message.channel,"Are you trying to have me chase my tail? There's no need to type `%update` while I'm asking you questions.  I'm gonna have to have to start over.")
                        return
                    #print(location)
                    cntt=0
                    uniq=0
                    grid=0
                    dontcont=0
                    if len(location)<8:
                        for x in range(0,8-len(location)):
                            location=location + " "
                    loc=location[0:8]
                    
                    for x in self.sngroup:
                        if loc.upper()==x.upper():
                            uniq=uniq+1
                            Nameval=self.cngroup[cntt]
                            #linkn=self.lngroup[cntt]
                            gymlat=self.latgroup[cntt]
                            gymlon=self.longroup[cntt]
                            linkn = "" + gymlat + "," + gymlon + ""
                            olink=linkn
                            #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                        cntt=cntt+1
                    cntt=0
                    
                    if uniq>1:
                        optnum=1
                        cntt=0
                        ncha=0
                        LVal=[]
                        Nameval=''
                        for x in self.sngroup:
                            if loc.upper()==x.upper():
                                Nameval=Nameval + str(optnum) + ")" + self.cngroup[cntt] + "\n"#": Use '" + self.angroup[cntt] + "'\n"
                                LVal.append(self.angroup[cntt])
                                optnum=optnum+1
                                ncha=ncha+1
                            cntt=cntt+1
                    
                        if ncha==0:  #Channel name isn't in alt or shortname  
                            await self.bot.say("`The gym name you entered is not available in the system`")
                            dontcont=1
                            attempt+=1
                            #return
                        elif ncha>1: #Unique Channel name doesn't exist
                            await self.bot.say("More than 1 gym corresponds to that location. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.say("`{}`".format(Nameval))
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                            try:
                                loc=LVal[int(msgrt.content)-1]
                                #print(loc)
                            except:
                                attempt+=1
                                dontcont=1
                                #return
                    elif uniq==0: #see if keyword
                        scrubmess=await subf.filtNameval(self,location.upper())          
                        locn=""
                        #Try finding the names of the gyms
                        loclist=[]
                        for x in self.WL:
                            if x.upper() in location.upper(): 
                                loclist.append(x)
                        #Xref the list with the gym names
                        possn=[]
                        maxcom=0
                        gyml=""
                        cntt=0
                        gymlist=[]
                        suggch=[]
                        
                        for y in self.cngroup:
                            comwords=0
                            tpp=await subf.filtNameval(self,y)
                            for x in loclist:
                                if x.upper() in tpp.upper():
                                    comwords+=1
                                    gymlist.append(y)
                            if comwords>maxcom:
                                suggch.append(y)
                                #gyml=self.lngroup[cntt]
                                gymlat=self.latgroup[cntt]
                                gymlon=self.longroup[cntt]
                                gyml = "" + gymlat + "," + gymlon + ""
                                maxcom=comwords
                            cntt+=1
                        #get unique gyms names only
                        ugym=[]
                        for x in gymlist:
                            if x not in ugym:
                                ugym.append(x) 
                        print (ugym)
                        print (gymlist)
                        
                        txt="`"
                        cntr=1
                        for x in ugym:
                            txt+=str(cntr)+ ") " +x +" \n"
                            cntr+=1
                        txt+="`"
                        #User selects which gym if confused
                        alltimeout=30
                        bypassq=0
                        if len(ugym)>1:
                            await self.bot.send_message(ctx.message.channel,"I got confused. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                            await self.bot.send_message(ctx.message.channel,txt)
                            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                            try:
                                loclist=ugym[int(msgrt.content)-1]
                                #bypassq=1
                                #newloca=loc
                                #print(loc)
                            except:
                                attempt+=1
                                dontcont=1
                                bypassq=1
                        elif len(ugym)==0:
                            #no keyword found
                            attempt+=1
                            dontcont=1
                            bypassq=1
                        else:                            
                            loclist=ugym[0]
                        
                        #print(bypassq)
                        if bypassq==0:
                            cntt=0

                        
                            for y in self.cngroup:
                                if loclist==y:
                                    #gyml=self.lngroup[cntt]
                                    gymlat=self.latgroup[cntt]
                                    gymlon=self.longroup[cntt]
                                    gyml = "" + gymlat + "," + gymlon + ""
                                    gyma=self.angroup[cntt]
                                    #gyml=self.lngroup[cntt]
                                cntt+=1
                            
                            #now find the gym in the lists
                            cntt=0
                            uniq=0
                            grid=0
                            
                            for x in self.group1an:
                                if gyma.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=1
                                    Nameval=self.group1cn[cntt]
                                    #linkn=self.group1ln[cntt]
                                    gymlat=self.group1lat[cntt]
                                    gymlon=self.group1lon[cntt]
                                    linkn = "" + gymlat + "," + gymlon + ""
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg1)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group2an:
                                if gyma.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=2
                                    Nameval=self.group2cn[cntt]
                                    #linkn=self.group2ln[cntt]
                                    gymlat=self.group2lat[cntt]
                                    gymlon=self.group2lon[cntt]
                                    linkn = "" + gymlat + "," + gymlon + ""
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg2)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            cntt=0
                            for x in self.group3an:
                                if gyma.upper()==x.upper():
                                    uniq=uniq+1
                                    grid=3
                                    Nameval=self.group3cn[cntt]
                                    #linkn=self.group3ln[cntt]
                                    gymlat=self.group3lat[cntt]
                                    gymlon=self.group3lon[cntt]
                                    linkn = "" + gymlat + "," + gymlon + ""
                                    mutelist=await subf.getmemlist(self,ctx,self.muteg3)
                                    olink=linkn
                                    dontcont=1
                                    #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                    success=1
                                cntt=cntt+1
                            print(uniq)
                        #uniq=0
                    #print(loc)
                    if dontcont==0:
                        cntt=0
                        uniq=0
                        grid=0
                        
                        for x in self.group1an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=1
                                Nameval=self.group1cn[cntt]
                                #linkn=self.group1ln[cntt]
                                gymlat=self.group1lat[cntt]
                                gymlon=self.group1lon[cntt]
                                linkn = "" + gymlat + "," + gymlon + ""
                                mutelist=await subf.getmemlist(self,ctx,self.muteg1)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group2an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=2
                                Nameval=self.group2cn[cntt]
                                #linkn=self.group2ln[cntt]
                                gymlat=self.group2lat[cntt]
                                gymlon=self.group2lon[cntt]
                                linkn = "" + gymlat + "," + gymlon + ""
                                mutelist=await subf.getmemlist(self,ctx,self.muteg2)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                        cntt=0
                        for x in self.group3an:
                            if loc.upper()==x.upper():
                                uniq=uniq+1
                                grid=3
                                Nameval=self.group3cn[cntt]
                                #linkn=self.group3ln[cntt]
                                gymlat=self.group3lat[cntt]
                                gymlon=self.group3lon[cntt]
                                linkn = "" + gymlat + "," + gymlon + ""
                                mutelist=await subf.getmemlist(self,ctx,self.muteg3)
                                olink=linkn
                                #linknt="__**RAID:**__ A " + type.upper() + " raid boss ends at "
                                success=1
                            cntt=cntt+1
                    
                            
                            
                    if uniq==0:    
                        await self.bot.say("`The gym name you entered is not available in the system`")
                        attempt+=1
                    #return
                
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                
                
                
                #print("Made to return")
                #print(Nameval)
                RaidBossfound=0
                isLoc=0
                if any(xpp == Nameval for xpp in self.Locbypass): #We need to allow this boss to be entered anyway
                    RaidBossfound=1    
                    isLoc=1
                #print(location)
                
                
                tempNameval=await subf.filtNameval(self,Nameval)
                foundch=0
                RBN=''
                for x in self.allbutmtch:
                    rdd=self.bot.get_channel(x)
                    if '---' in rdd.name:
                        xrd=rdd.name.split('---')
                        if (xrd[1]==tempNameval):
                            foundch=1
                            RBN=xrd[0]
                            break
                            #if tempNameval in rdd.name:
                            #await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid doesn't exist yet! You may want to use `%raid`")
                            #return

                if foundch==0:
                    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid doesn't exist yet! You may want to use `%raid`")
                    return
                if not 'level' in RBN:
                    await self.bot.send_message(ctx.message.channel,ctx.message.author.display_name+", looks like that raid was already updated.")
                    return
                
                
                
                attempt=0
                success=0
                await self.bot.send_message(ctx.message.channel,"Last question! What is the name of the raid boss at " + Nameval+"?")
                while success==0 and attempt<3:
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    type=msgrt.content
                    if msgrt.content.upper()=="Q": 
                        await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                        return
                    raidn=0
                    for x in range(0,len(self.L4types)):
                        if type.upper()==self.L4types[x].upper():
                            RaidBossfound=1
                            lvltxt="level4"
                            raidn=4
                    for x in range(0,len(self.L5types)):
                        if type.upper()==self.L5types[x].upper():
                            RaidBossfound=1
                            lvltxt="level5"
                            raidn=5                
                    for x in range(0,len(self.L3types)):
                        if type.upper()==self.L3types[x].upper():
                            RaidBossfound=1
                            lvltxt="level3"
                            raidn=3 
                    #for x in range(0,len(self.PStypes)):
                    #    if type.upper()==self.PStypes[x].upper():
                    ##        RaidBossfound=1    
                     #       raidn=6                
                    #Origname
                    
                    if RaidBossfound==0:
                        await self.bot.send_message(ctx.message.channel,"I couldn't find that raid boss. What's the name of the raid boss?")
                        attempt+=1
                    else:
                        success=1
                    
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
                
                await self.bot.send_message(ctx.message.channel,"Based on what you told me: \nA "+type+" hatched from the egg at "+Nameval+". \nDid I understand you correctly (Y/N)?")
                attempt=0
                success=0
                while success==0 and attempt<3:
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                    if msgrt.content.upper()=="N": 
                        await self.bot.send_message(ctx.message.channel,"Looks like you may have entered something wrong then.  How about you try again.")
                        success=1
                        return
                    elif msgrt.content.upper()=="Y": 
                        success=1
                    elif msgrt.content.upper()=="Q": 
                        await self.bot.send_message(ctx.message.channel,"Feeling sad now... :frowning:")
                        return
                    else: 
                        await self.bot.send_message(ctx.message.channel, "Please answer the question, did I get that right (Y/N)?")
                        attempt+=1
                if attempt>2:
                    await self.bot.say("Looks like you just made too many errors for me.  It's alright though.  You can always try again!")
                    return
            #else:
        
            except:
                await self.bot.say("Purdue Pollster fell asleep while waiting for a reply, but you can always try again!")
                return
        if aa1>0:        
            #print("done")
            #return
            #Standardize the channels names
            Origname=Nameval
            Nameval=await subf.filtNameval(self,Nameval)
            
            #isLoc=0
            #RaidBossfound=0
            #for x in range(0,len(self.L4types)):
            #    if type.upper()==self.L4types[x].upper():
            #        RaidBossfound=1
            #        raidn=4
            #        lvltxt="level4"
            #for x in range(0,len(self.L5types)):
            #    if type.upper()==self.L5types[x].upper():
            #        RaidBossfound=1    
            #        raidn=5
            #        lvltxt="level5"                
            #for x in range(0,len(self.L3types)):
            #    if type.upper()==self.L3types[x].upper():
            #        RaidBossfound=1    
            #        raidn=3 
            #        lvltxt="level3" 
            
            #if any(xpp == Origname for xpp in self.Locbypass): #We need to allow this boss to be entered anyway
            #    RaidBossfound=1    
            #    isLoc=1

            #if RaidBossfound==0:
            #    await self.bot.send_message(ctx.message.channel,"That raid boss is not available in the system.")
            #    return
            print(Nameval)
            print(isLoc)
            if isLoc==1: #We need to allow this boss to be entered anyway
                #Find channels with the location
                chidloc=await subf.findchidloca(self,Nameval)
                print(chidloc)
                if chidloc==0:
                    await self.bot.send_message(ctx.message.channel,"That raid doesn't have information posted.")
                    return
                channel1 = self.bot.get_channel(chidloc)
                channel2=channel1
                print(channel1)
                print (channel1==None)
                print (channel2==None)
                #chidloc=await subf.findchidboss(self,Nameval)
                #if chidloc==0:
                
                #else:
                #    channel2 = self.bot.get_channel(chidloc)
            else:   
                namel1=lvltxt + "---" + Nameval
                channel1 = discord.utils.get(server.channels, name=namel1)
                namel2=Nameval + "---" +  lvltxt 
                channel2 = discord.utils.get(server.channels, name=namel2)
            
            #If either of the channels wasn't found, then stop the code here
            if channel1==None and channel2==None:  #CMK was 'or' changed on 1/24
                await self.bot.send_message(ctx.message.channel,"That raid has already been updated!")
                return  
            print("Here")
            isPS=0
            isLoc=0
            RaidBossfound=0
            bossemo=[]
            #raidn=await findraidn(self,type)
            for x in range(0,len(self.PStypes)):
                if type.upper()==self.PStypes[x].upper():
                    RaidBossfound=1
                    bossemo.append(self.PSemoji[x])
                    isPS=1                
                    raidn=6         
            for x in range(0,len(self.OItypes)):
                if type.upper()==self.OItypes[x].upper():
                    RaidBossfound=1
                    bossemo.append(self.OIemoji[x])
                    isPS=0                
                    raidn=7
            for x in range(0,len(self.L4types)):
                if type.upper()==self.L4types[x].upper():
                    RaidBossfound=1
                    bossemo.append(self.L4emoji[x])
                    raidn=4
            for x in range(0,len(self.L5types)):
                if type.upper()==self.L5types[x].upper():
                    RaidBossfound=1    
                    bossemo.append(self.L5emoji[x])
                    raidn=5                
            for x in range(0,len(self.L3types)):
                if type.upper()==self.L3types[x].upper():
                    RaidBossfound=1   
                    bossemo.append(self.L3emoji[x])
                    raidn=3 
            
            if any(xpp == Origname for xpp in self.Locbypass): #We need to allow this boss to be entered anyway
                RaidBossfound=1    
                isLoc=1
            if RaidBossfound==0:
                await self.bot.send_message(ctx.message.channel,"That raid boss is not available in the system.")
                return
            if len(bossemo)==0:
                bossemo=["<:item_pokeball:284615009299070976>"]
            #Allow for new users to enter raids and have it count
            
            
            
            
            chtr=channel1
            if channel1.id=="31":
                xtra="This channel cannot be updated due to system maintenance.  "
                await self.bot.send_message(ctx.message.channel, xtra)
                return
            
            
            
            async for message in self.bot.logs_from(chtr, limit=1000): #Gets a list of the last 500 messages in the channel 
                #print(message.content)
                if message.content.startswith('__**RAID:**__'): #Then we need to get the ID of this message and see if it has the correct start time
                    a=message
                    arggn=a.content.split('\n')  #The second argument will be the minutes
                    argg=arggn[0].split(' ends at ')  #The second argument will be the minutes
                    #print(argg[1])
                    polltime = datetime.utcnow()+timedelta(hours=self.timez)+timedelta(minutes=15)
                    tpolltime=polltime.strftime(self.timeform)
                    tdeltat = datetime.strptime(tpolltime, self.timeform)-datetime.strptime(argg[1], self.timeform)
                    polltimeRO = datetime.utcnow()+timedelta(hours=self.timez)+timedelta(minutes=40)
                    tpolltimeRO=polltimeRO.strftime(self.timeform)
                    tdeltatRO = datetime.strptime(tpolltimeRO, self.timeform)-datetime.strptime(argg[1], self.timeform)
                    hatpolltime = datetime.utcnow()+timedelta(hours=self.timez)+timedelta(minutes=self.bossactivetime+2)
                    hatpolltime=hatpolltime.strftime(self.timeform)
                    hatdeltat = datetime.strptime(hatpolltime, self.timeform)-datetime.strptime(argg[1], self.timeform)
                    print(tdeltat.days)
                    print(tdeltatRO.days)
                    print(hatdeltat.days)
                    break
                #if message.content.startswith("The raid boss at "):  #This channel was updated...leave
                #    await self.bot.send_message(ctx.message.channel,"That raid has already been updated!")
                #    return 
            
            #if int(msgrt2.content)<20:
            #xtra="Doesn't seem fair to not give people sufficient time to get to a raid.  I can't let you enter that in good conscience."
            #await self.bot.send_message(ctx.message.channel, xtra)
            #attempt+=1
            #return
            allownot=1
            if (hatdeltat.days<0):
                xtra="That egg hasn't hatched yet! Please try again *after* it hatches."
                await self.bot.send_message(ctx.message.channel, xtra)
                return
            if (tdeltat.days==0):
                #xtra="Doesn't seem fair to not give people sufficient time to get to a raid.  I can't let you enter that in good conscience (15 mins required))"
                xtra="I'll update this raid for you, but can't send out notifications this close to the end of a raid.  I hope you understand."
                allownot=0
                await self.bot.send_message(ctx.message.channel, xtra)
                #return
            if (tdeltatRO.days<0 and isRO==1):
                xtra="The top 3 trainers on the leaderboard must wait 5 minutes after hatch to update a raid boss."
                await self.bot.send_message(ctx.message.channel, xtra)
                return
                areaf=1
            #return
            #xtra="Updates cannot be performed due to system maintenance.  Gimme 5 minutes and you'll be good to go. "
            #await self.bot.send_message(ctx.message.channel, xtra)
            #return
            #if (tdeltatRO.days==0 and isRO==1):
            #    xtra="RaidObservers must wait 5 minutes after hatch to update a raid boss."
            #    await self.bot.send_message(ctx.message.channel, xtra)
            #    return
            #await self.bot.send_message(ctx.message.channel,"The update system is down for maintenance.  Give it 5 mins.")
            #return
            if isallowed>-10:
                uname=ctx.message.author.display_name
                uname=uname+str(ctx.message.author.discriminator)
                userid=ctx.message.author.id
                uname=await subf.getusernick(self,ctx,userid)
                
                
                #aar=1
                #if aar==1:
                try: #If the sheet exists, open it 
                    df = pd.read_excel('RaidTrainer' + "\\" + uname + 'rt.xlsx')
                    print(df)
                    df.iloc[0,1]+=1    
                    writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    #print('balh',df.iloc[0,0],df.iloc[0,1])
                    if df.iloc[0,0]>=1 and df.iloc[0,1]>1:
                        notta=1
                        rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                        if not rrL in b.roles:
                            fr=await subf.grantRT(self,b,rrL)
                    elif df.iloc[0,0]==1 and df.iloc[0,1]==1:
                        rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                        
                        fr=await subf.grantRT(self,b,rrL)
                        #print('balh')
                        if fr==1:
                            arp=1
                            #await self.bot.send_message(ctx.message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                        else:
                            arp=1
                            #await self.bot.send_message(ctx.message.author,uname+", please pester an RO to give you access NOW!  We need your help!") 
                    else:
                        arp=1
                        #await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of raid information without being reviewed, but it looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer. If you have already met this requirement, pester a RaidObserver to give you access.")
                        #return
                #else:
                except: #The person hasn't established a level yet
                    df = pd.read_excel('RaidTrainer' + "\\" + 'rt' + '.xlsx')
                    df.iloc[0,1]=1   
                    writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    if df.iat[0,0]==1 and df.iat[0,1]==1:
                        rrL=discord.utils.get(server.roles, id=self.RaidTrainer)
                        fr=await subf.grantRT(self,b,rrL)
                        if fr==1:
                            arp=1
                            #await self.bot.send_message(ctx.message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                        else:
                            arp=1
                            #await self.bot.send_message(ctx.message.author,uname+", please pester an RO to give you access NOW!  We need your help!")
                    else:
                        arp=1
                        #await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of raid information without a bit of review, but it looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer. If you have already met this requirement, pester a RaidObserver to give you access.")        
                        #return
            
            
            
            CPmax=await subf.getcpmax(self,type)               
            addlstr=""
            if CPmax>0:        
                addlstr="\n\n The CP for a 100IV " + type.upper() + " is " + str(CPmax) + " (Weather-boost " + str(CPmax*1.25) + ")."
            
            await self.bot.send_message(channel1, "The raid boss at " + Nameval+ " has been updated to " + type.upper() + "!" + addlstr)
            
            #Get number of people with reactions
            addlname=""
            if "_" in channel1.name:
                lgh=channel1.name.split("_")
                addlname=lgh[0]+"_"
            
            await self.bot.edit_channel(channel1, name=addlname+type.upper() + self.chanstrsp + Nameval)
            channel2=channel1
            if not channel2==channel1:
                await self.bot.send_message(channel2, "The raid boss at " + Nameval+ " has been updated to " + type.upper() + "!" + addlstr)        
                await self.bot.edit_channel(channel2, name=Nameval+ self.chanstrsp + type.upper() )
            
            
            channrb=channel2
            channloc=channel1
            ##print(channloc)
            #print(channrb)
            #channloc=channrb  #ADDED 01292018
            
            
            
            #Grab the time here and see if sufficient time remains for updating
            memlist=[]
            #Create a notification for those in the corresponding Notify list
            shinynot=discord.utils.get(server.roles, id=self.PSNotify)
            shinyemo=""
            if isPS==0:
                shinyn=""
            else:
                shinyn=shinynot.mention
                await subf.grantacc(self,channloc,channrb,shinynot)
                shinyemo="<a:Shiny:407702531645505537>"
                memlist+=await subf.getmemlist(self,ctx,self.PSNotify)
            
            
            
            cntt=0
            locatemo=""
            Addlloc=0
            for xpp in self.Locbypass: #We need to allow this boss to be entered anyway
                if xpp == Origname:
                    Addlloc=cntt
                    break
                cntt+=1
            Locnot=discord.utils.get(server.roles, id=self.AddlNotiid[Addlloc])
            Locnot2=discord.utils.get(server.roles, id=self.SilentEX)
            if isLoc==0:
                Locan=""
            else:
                Locan=Locnot.mention
                await subf.grantacc(self,channloc,channrb,Locnot)
                await asyncio.sleep(0.05)
                await subf.grantacc(self,channloc,channrb,Locnot2)
                locatemo=self.emoji_exgym
            
            uniqemo=[]
            for x in bossemo:
                if x not in uniqemo:
                    uniqemo.append(x) 
            emoji=uniqemo
            print(emoji)
            outp=""
            for x in emoji:
                outp+=x
            print(outp)
            print(shinyemo)
            print(locatemo)
            emoji= outp + shinyemo + locatemo

            rr5=""
            rr2=""
            type=type.upper()
            cntt=0
            mentioned=0
            for x in self.L3types:
                if type==x.upper():
                    mentioned=1
                    #Show to Silent only
                    rr2=discord.utils.get(server.roles, id=self.SilentL3)
                    await subf.grantacc(self,channloc,channrb,rr2)
                    #and hold on to the notify version
                    rr2=discord.utils.get(server.roles, id=self.L3Notify)
                    memlist+=await subf.getmemlist(self,ctx,self.L3Notify)
                    await subf.grantacc(self,channloc,channrb,rr2)
                    nid=self.L3notid[cntt]
                    if not nid=="0":
                        rr5=discord.utils.get(server.roles, id=nid)
                        memlist+=await subf.getmemlist(self,ctx,nid)
                        await subf.grantacc(self,channloc,channrb,rr5)
                        if self.notifyon==1 and allownot==1:
                            newlist=rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan
                            #newlist=memlist
                            #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                    else:
                        if self.notifyon==1 and allownot==1:
                            newlist=rr2.mention +" "+shinyn +" "+Locan
                            #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+shinyn+" "+Locan  + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                cntt+=1
            cntt=0
            for x in self.L4types:
                if type==x.upper():
                    mentioned=1
                    #Show to Silent only
                    rr2=discord.utils.get(server.roles, id=self.SilentL4)
                    await subf.grantacc(self,channloc,channrb,rr2)
                    #and hold on to the notify version
                    rr2=discord.utils.get(server.roles, id=self.L4Notify)
                    memlist+=await subf.getmemlist(self,ctx,self.L4Notify)
                    await subf.grantacc(self,channloc,channrb,rr2)
                    nid=self.L4notid[cntt]
                    if not nid=="0":
                        rr5=discord.utils.get(server.roles, id=nid)
                        memlist+=await subf.getmemlist(self,ctx,nid)
                        await subf.grantacc(self,channloc,channrb,rr5)
                        if self.notifyon==1 and allownot==1:
                            newlist=rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan
                            #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                    else:
                        if self.notifyon==1 and allownot==1:
                            newlist=rr2.mention +" "+shinyn +" "+Locan
                            #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+shinyn +" "+Locan + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                cntt+=1
            cntt=0
            for x in self.L5types:
                if type==x.upper():
                    mentioned=1
                    #Show to Silent only
                    rr2=discord.utils.get(server.roles, id=self.SilentL5)
                    await subf.grantacc(self,channloc,channrb,rr2)
                    #and hold on to the notify version
                    rr2=discord.utils.get(server.roles, id=self.L5Notify)
                    memlist+=await subf.getmemlist(self,ctx,self.L5Notify)
                    await subf.grantacc(self,channloc,channrb,rr2)
                    nid=self.L5notid[cntt]
                    if not nid=="0":
                        rr5=discord.utils.get(server.roles, id=nid)
                        memlist+=await subf.getmemlist(self,ctx,nid)
                        await subf.grantacc(self,channloc,channrb,rr5)
                        if self.notifyon==1 and allownot==1:
                            newlist=rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan
                            #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+shinyn +" "+Locan + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                    else:
                        if self.notifyon==1 and allownot==1:
                            newlist=rr2.mention  +" "+shinyn +" "+Locan
                            #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+shinyn +" "+Locan + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                cntt+=1
            if mentioned==0:
                cntt=0
                for x in self.PStypes:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentPS)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.PSNotify)
                        memlist+=await subf.getmemlist(self,ctx,self.PSNotify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        nid=self.PSnotid[cntt]
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist(self,ctx,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1 and allownot==1:
                                newlist=rr2.mention +" "+ rr5.mention +" "+Locan
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+Locan+ ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                        else:
                            if self.notifyon==1 and allownot==1:
                                newlist=rr2.mention +" "+Locan
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+Locan+ ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                    cntt+=1
            if mentioned==0:
                cntt=0
                for x in self.OItypes:
                    if type==x.upper():
                        mentioned=1
                        #Show to Silent only
                        rr2=discord.utils.get(server.roles, id=self.SilentOI)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #and hold on to the notify version
                        rr2=discord.utils.get(server.roles, id=self.OINotify)
                        memlist+=await subf.getmemlist(self,ctx,self.OINotify)
                        await subf.grantacc(self,channloc,channrb,rr2)
                        nid=self.OInotid[cntt]
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist(self,ctx,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1 and allownot==1:
                                newlist=rr2.mention +" "+ rr5.mention +" "+Locan
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+ rr5.mention +" "+Locan+ ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                        else:
                            if self.notifyon==1 and allownot==1:
                                newlist=rr2.mention +" "+Locan
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention +" "+Locan+ ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                    cntt+=1
            if mentioned==0: #If still not mentioned, its a special location raid.  Its not shiny or a system raid boss
                cntt=0
                for x in self.Locbypass:
                    if Origname==x:
                        mentioned=1
                        rr2=discord.utils.get(server.roles, id=self.AddlNotiid[cntt])
                        await subf.grantacc(self,channloc,channrb,rr2)
                        #nid=self.PSnotid[cntt]
                        nid="0"
                        if not nid=="0":
                            rr5=discord.utils.get(server.roles, id=nid)
                            memlist+=await subf.getmemlist(self,ctx,nid)
                            await subf.grantacc(self,channloc,channrb,rr5)
                            if self.notifyon==1 and allownot==1:
                                newlist=rr2.mention + " " +  rr5.mention
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention + rr5.mention + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                        else:
                            if self.notifyon==1 and allownot==1:
                                newlist=rr2.mention
                                #await self.bot.send_message(self.bot.get_channel(self.genchid), rr2.mention + ", the raid boss at " + Nameval+ " has been updated to " + type + "!" )
                    cntt+=1
            
            #Remove emoji for the bad raid bosses
            #async for message in self.bot.logs_from(chtr, limit=1000): #Gets a list of the last 500 messages in the channel 
                #print(message.content)
            #    if message.content.startswith('@Start:'): #Then we need to get the ID of this message and see if it has the correct start time
            #        atp=1
            print (raidn)
            if raidn==5:
                exc=0
                if exc==0:
                    #leglist=['<:Latias_static:405776494288175134>','<:legendary2_hooh:339593270072049664>']
                    #if type.upper()=="HO-OH" or type.upper()=="HOOH":
                    #    dellist=['<:Latias_static:405776494288175134>']
                    #if type.upper()=="LATIAS":
                    #    dellist=['<:legendary2_hooh:339593270072049664>']
                    
                    #leglist=['<:Groudon_static:405777239670784001>','<:Kyogre_static:405777325725319169>']
                    leglist=['<:Latios_static:405776501569617920>','<:giratina_o:567371600819781632>']
                    #leglist=['<:legendary9_articuno:339592371748601857>','<:legendary8_zapdos:339592414589353994>','<:legendary7_moltres:339592445417357322>']
                    dellist=[]
                    #if type.upper()=="ARTICUNO":
                    #    dellist=['<:legendary8_zapdos:339592414589353994>','<:legendary7_moltres:339592445417357322>']
                    #if type.upper()=="MOLTRES":
                    #    dellist=['<:legendary9_articuno:339592371748601857>','<:legendary8_zapdos:339592414589353994>']
                    #if type.upper()=="ZAPDOS":
                    #    dellist=['<:legendary9_articuno:339592371748601857>','<:legendary7_moltres:339592445417357322>']
                   
                    #if type.upper()=="REGIROCK":
                    #    dellist=['<:legendary9_articuno:339592371748601857>','<:legendary8_zapdos:339592414589353994>','<:legendary7_moltres:339592445417357322>'] #leglist=['<:Groudon_static:405777239670784001>','<:Kyogre_static:405777325725319169>','<:Rayquaza_static:405777431421779979>']
                    if type.upper()=="LATIOS":
                        dellist=['<:giratina_o:567371600819781632>']
                        #dellist=[]
                    if type.upper()=="GIRATINA":
                        dellist=['<:Groudon_static:405777239670784001>','<:Rayquaza_static:405777431421779979>']
                        dellist=['<:Latios_static:405776501569617920>']
                    #if type.upper()=="GROUDON":
                    #    dellist=['<:Kyogre_static:405777325725319169>','<:Rayquaza_static:405777431421779979>']
                    #    dellist=['<:Kyogre_static:405777325725319169>']
                    #if type.upper()=="KYOGRE":
                    #    dellist=['<:Groudon_static:405777239670784001>','<:Rayquaza_static:405777431421779979>']
                    #    dellist=['<:Groudon_static:405777239670784001>']
                    #if type.upper()=="RAYQUAZA":
                        #dellist=['<:Groudon_static:405777239670784001>','<:Kyogre_static:405777325725319169>']
                    msg=''
                    async for message in self.bot.logs_from(chtr, limit=1000): #Gets a list of the last 500 messages in the channel 
                        #print(message.content)
                        
                        if message.content.startswith('@Start:'): #Then we need to get the ID of this message and see if it has the correct start time
                            for xi in message.reactions:
                                
                                if str(xi.emoji) in leglist:
                                    if str(xi.emoji) in dellist:  
                                        useri = await self.bot.get_reaction_users(xi)
                                        for yi in useri:
                                            await self.bot.remove_reaction(message, xi.emoji, yi)
                                            msg+=yi.mention
                    
                    if not msg=="":
                        await self.bot.send_message(chtr,msg + " your reaction for this raid was removed since it is not the raid boss you desire. Please react again to reserve your time.")
               
            if raidn==4:
                exc=0
                if exc==0:
                    leglist=["<:Tyranitar:439633895194099712>","<:Absol:435658016994623499>"]#,":middle_finger","<a:Absol:407693507684466690>","<a:Aggron:407700314402062346>"]
                    dellist=["<:Tyranitar:439633895194099712>","<:Absol:435658016994623499>"]
                    if type.upper()=="TYRANITAR":
                        #nothing to do
                        dellist=["<:Absol:435658016994623499>"]
                    if type.upper()=="ABSOL":
                        #nothing to do
                        dellist=["<:Tyranitar:439633895194099712>"]   #dellist=[":middle_finger","<a:Absol:407693507684466690>","<a:Aggron:407700314402062346>"]
                    print (dellist)
                    #if type.upper()=="ABSOL":
                    #    dellist=["<a:Tyranitar:407677462324051968>",":middle_finger","<a:Aggron:407700314402062346>"]
                    #if type.upper()=="AGGRON":
                    #    dellist=["<a:Tyranitar:407677462324051968>",":middle_finger","<a:Absol:407693507684466690>"]
                    #if type.upper()=="CHARIZARD":
                    #    dellist=["<a:Tyranitar:407677462324051968>","<a:Absol:407693507684466690>","<a:Aggron:407700314402062346>"]
                    
                        
                    msg=''
                    async for message in self.bot.logs_from(chtr, limit=1000): #Gets a list of the last 500 messages in the channel 
                        #print(message.content)
                        
                        if message.content.startswith('@Start:'): #Then we need to get the ID of this message and see if it has the correct start time
                            for xi in message.reactions:
                                
                                if str(xi.emoji) in leglist:
                                    if str(xi.emoji) in dellist:  
                                        useri = await self.bot.get_reaction_users(xi)
                                        for yi in useri:
                                            await self.bot.remove_reaction(message, xi.emoji, yi)
                                            msg+=yi.mention
                    print (msg)
                    if not msg=="":
                        await self.bot.send_message(chtr,msg + " your reaction for this raid was removed since it is not the raid boss you desire. Please react again to reserve your time.")        
            
            #Now to get the stuff to update the #active_raids channel
            print("Made it here. UPDATE")
            ch = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.genchid)
            print(ch)
            #First we have to find the message in the channel searching for o
            olocation=Origname
            #newlist=""
            print(olocation)
            print(ch) 
            await self.bot.send_message(ctx.message.channel, "Your update request has been processed!  Thank you.")
            
            #newlist=Milk.mention + " " + L3.mention +" "+Spec.mention
            polltimez = datetime.utcnow()+timedelta(hours=self.timez)
            tpolltimez=polltimez.strftime('%m/%d/%y %H:%M:%S')
            number = sum(1 for line in open('raids_ALL.txt'))+1
            onumber=str(number)
            number=str(number).zfill(4)              
            #await self.bot.say("`I placed a notification in the {} forum for approval!`""".format("Raid-Notifier"))
            #rr2=discord.utils.get(server.roles, id=self.RaidObserver)
            #await self.bot.send_message(self.bot.get_channel(self.RaidNotifier),rr2.mention + ', ' + ctx.message.author.display_name + ' has input the following raid information. Please verify type %accept ' + onumber + ' to approve or %decline ' + (onumber) + '!\n ' + origmessv )
            
            line=(("UPDATE {}    {}     {}    {}    {}   {}   {}""".format(number.ljust(4),"UPDATE",type.ljust(8),str(0).ljust(5),Nameval.ljust(20),tpolltimez,ctx.message.author.display_name)))
            with open("raids_ALL.txt","a") as f:
                print(line,file=f)
            async for message in self.bot.logs_from(ch, limit=5000): #Gets a list of the last 500 messages in the channel 
                print(message.content)
                if olocation in message.content: #This channel is the one needing updating
                    #print(message.content)
                    argg=message.content.split("\n")
                    #"____**Raid:**__"+allmention is on the first line
                    #"____**Raid:**__"+allmention is on the first line
                    arggn=argg[0].split("**__")
                    oldmention=arggn[1]
                
                    argg6=argg[1].split("ends at ")
                    timeplusoldemo=argg6[1]
                    
                    argg7=timeplusoldemo.split(" ")
                    oldemo=argg7[1]
                    
                    modmessp2=""
                    for x in argg[2::]:
                        modmessp2+="\n" + x 
                    
                    #Now we need to reconstruct the message with the new mentions
                    #areae=1
                    #if areae==1:
                    try:
                        modmess=arggn[0] + "**__" + newlist + "\n" + argg6[0]+ "ends at " + argg7[0] + " " + emoji + modmessp2
                        meat=arggn[0] + "**__" + "\n" + argg6[0]+ "ends at " + argg7[0] + " " + emoji 
                        #We need unique members of the memlist
                        uniqmem=[]
                        for x in memlist:
                            if x not in uniqmem:
                                uniqmem.append(x) 
                        memlist=uniqmem
                        
                        mutelist=await subf.timemute(self,ctx,mutelist)
                        
                        #Supress notifies to members of the mutegroup
                        msg=""
                        for f in memlist:
                            if not f in mutelist:
                                msg+=f.mention
                                if len(msg)>1000:
                                    tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg)
                                    await asyncio.sleep(1.0)
                                    #await self.bot.edit_message(tms,meat)
                                    await self.bot.delete_message(tms)
                                    msg=""#

                        if len(msg)>=0:
                            tms=await self.bot.send_message(ch,meat+"\n\n\n\n"+msg+Locan)
                            await asyncio.sleep(1.0)
                            #await self.bot.edit_message(tms,meat)
                            await self.bot.delete_message(tms)
                        
                        #msggg=await self.bot.send_message(ch,newlist) 
                        #await asyncio.sleep(2.0)
                        #await self.bot.delete_message(msggg)
                        await self.bot.edit_message(message,modmess) 
                    #else:
                    except:
                        modmess=message.content
                     
                    
                
                    return
        #await self.bot.send_message(ctx.message.channel,"That message couldn't be found")  
            
            
            return 
        else:
            arar=10
    
    
    @commands.command(pass_context=True)
    async def assignexch(self,ctx,msgid,idn):
        if not ctx.message.author.id==self.CMK:
            return
        ch=self.bot.get_channel("362698126248771604")
        print(self.exroles[int(idn)-1])
        exrole=discord.utils.get(ctx.message.server.roles, id=self.exroles[int(idn)-1])
        print (exrole.id)
        await self.bot.delete_message(ctx.message)
        #try:
        a=await self.bot.get_message(ch, msgid)
        for xi in a.reactions:
            useri = await self.bot.get_reaction_users(xi)
            print(useri)
            for yi in useri:
                member = discord.utils.get(ctx.message.server.members, name=yi.name)
            #userf=discord.Server.get_member(ctx.message.server,user[2:len(user)-1])
            #Ranger=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
            #Milkmaid=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
            #Approved=discord.utils.get(ctx.message.server.roles, id=self.Approved)
            #Trainer=discord.utils.get(ctx.message.server.roles, id="284583203245916160")
            #SilentL5=discord.utils.get(ctx.message.server.roles, id=self.SilentL5)
            #SilentL4=discord.utils.get(ctx.message.server.roles, id=self.SilentL4)
            #isallowed=0
            #if Milkmaid in f: #ONLY FOR TESTING
            #    isallowed=1
            #if Ranger in f: #ONLY RANGER MAY DO THIS
            #    isallowed=1   
            #if isallowed==1:  
            
                try:
                    await self.bot.add_roles(member, exrole )
                except:
                    ar=1
                    
                #for yi in useri:
                    #await self.bot.remove_reaction(message, xi.emoji, yi)
                    #msg+=yi.mention
        #except:
        #    ar=1
    
    @commands.command(pass_context=True)
    async def removeexch(self,ctx,role):
        return
        xrp=ctx.message.role_mentions
        for yi in xrp:
            member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
            for f in ctx.message.server.members:
                if not f==None:
                    if any(xpp == yi for xpp in f.roles): #Member is approved
                        print("Remove "+f.name+" from "+yi.name)
                        await self.bot.remove_roles(f, yi)
                        #await self.bot.add_roles(f, roleL4)
                        #await asyncio.sleep(0.1)
                        #await self.bot.add_roles(f, roleL5)
                        a=1
                    else:
                        a=1
                        #print("Not Appr:"+f.name)
            #mems=yi.
        #roler = get(ctx.message.server.roles, name='member')
        #await bot.remove_roles(user, role)
        return
        if not ctx.message.author.id==self.CMK:
            return
        ch=self.bot.get_channel("362698126248771604")
        print(self.exroles[int(idn)-1])
        exrole=discord.utils.get(ctx.message.server.roles, id=self.exroles[int(idn)-1])
        print (exrole.id)
        await self.bot.delete_message(ctx.message)
        #try:
        a=await self.bot.get_message(ch, msgid)
        for xi in a.reactions:
            useri = await self.bot.get_reaction_users(xi)
            print(useri)
            for yi in useri:
                member = discord.utils.get(ctx.message.server.members, name=yi.name)        
                try:
                    await self.bot.add_roles(member, exrole )
                except:
                    ar=1

    
    @commands.command(pass_context=True)
    async def delemo(self,ctx): #Modify this to rework the original message
        type='kyogre'
        leglist=['<:Groudon_static:405777239670784001>','<:Kyogre_static:405777325725319169>','<:Rayquaza_static:405777431421779979>']
        if type.upper()=="GROUDON":
            dellist=['<:Kyogre_static:405777325725319169>','<:Rayquaza_static:405777431421779979>']
        if type.upper()=="KYOGRE":
            dellist=['<:Groudon_static:405777239670784001>','<:Rayquaza_static:405777431421779979>']
        if type.upper()=="RAYQUAZA":
            dellist=['<:Groudon_static:405777239670784001>','<:Kyogre_static:405777325725319169>']
        chtr = discord.utils.get(ctx.message.server.channels, id="403571368341536768")
        msg=''
        async for message in self.bot.logs_from(chtr, limit=1000): #Gets a list of the last 500 messages in the channel 
            #print(message.content)
            
            if message.content.startswith('@Start:'): #Then we need to get the ID of this message and see if it has the correct start time
                for xi in message.reactions:
                    
                    #,"<a:Groudon:407703535241920512>","<a:Kyogre:407703534784479234>","<a:Rayquaza:407703535145320460>"
                    #print(xi.emoji)
                    #print(leglist)
                    
                    if str(xi.emoji) in leglist:
                        if str(xi.emoji) in dellist:
                            #print("Delete this emoji " + str(xi.emoji))   
                            useri = await self.bot.get_reaction_users(xi)
                            #print(useri)
                            for yi in useri:
                                await self.bot.remove_reaction(message, xi.emoji, yi)
                                msg+=yi.mention
                        
        await self.bot.send_message(chtr,msg + " your reaction for this raid was removed since it is not the raid boss you desire.")
    
    @commands.command(pass_context=True)
    async def toggletr(self,ctx):
        if ctx.message.author.id=="345200594421547018":
            if self.troubleshoot=="1":
                self.troubleshoot="0"
                await self.bot.send_message(ctx.message.channel,"Troubleshooting mode off")
            elif self.troubleshoot=="0":
                self.troubleshoot="1"
                await self.bot.send_message(ctx.message.channel,"Troubleshooting mode on")
    
    @commands.command(pass_context=True)
    async def updatetest(self,ctx): #Modify this to rework the original message
        member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        f=b.roles
        isallowed=1
        if isallowed>-10:
            uname=ctx.message.author.display_name
            uname=uname+str(ctx.message.author.discriminator)
            #aar=1
            #if aar==1:
            try: #If the sheet exists, open it 
                df = pd.read_excel('RaidTrainer' + "\\" + uname + 'rt.xlsx')
                print(df)
                df.iloc[0,1]+=1    
                writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                #print('balh',df.iloc[0,0],df.iloc[0,1])
                if df.iloc[0,0]>=1 and df.iloc[0,1]>1:
                    notta=1
                elif df.iloc[0,0]==1 and df.iloc[0,1]==1:
                    #print('balh1')
                    rrL=discord.utils.get(ctx.message.server.roles, id=self.RaidTrainer)
                    #print('balh2')
                    fr=await subf.grantRT(self,b,rrL)
                    #print('balh3')
                    if fr==1:
                        await self.bot.send_message(ctx.message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                    else:
                        await self.bot.send_message(ctx.message.author,uname+", please pester an RO to give you access NOW!  We need your help!") 
                else:
                    await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of raid information without being reviewed, but it looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer. If you have already met this requirement, pester a RaidObserver to give you access.")
                    return
            #else:
            except: #The person hasn't established a level yet
                df = pd.read_excel('RaidTrainer' + "\\" + 'rt' + '.xlsx')
                df.iloc[0,1]=1   
                writer = pd.ExcelWriter('RaidTrainer' + "\\" +uname + 'rt.xlsx', engine='xlsxwriter')    
                df.to_excel(writer, sheet_name='Sheet1',index=False)
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                if df.iat[0,0]==1 and df.iat[0,1]==1:
                    rrL=discord.utils.get(ctx.message.server.roles, id=self.RaidTrainer)
                    fr=await subf.grantRT(self,b,rrL)
                    if fr==1:
                        await self.bot.send_message(ctx.message.author,uname+", looks like you are an expert at data entry. A message has been sent to get you approved as a Raid Trainer.  Congrats!") 
                    else:
                        await self.bot.send_message(ctx.message.author,uname+", please pester an RO to give you access NOW!  We need your help!")
                else:
                    await self.bot.send_message(ctx.message.author,"You do not have a role on this Discord that allows entry of raid information without a bit of review, but it looks like all of your information passed the test!  Once you have entered one `%raid` and one `%update` command, you will be a RaidTrainer. If you have already met this requirement, pester a RaidObserver to give you access.")        
                    return
    
    
    #Use this command to have Pollster react to a message with letter-based emoji
    #Ready for publication
    @commands.command(pass_context=True)
    async def RNGESUS(self,ctx,msgid,texx):
        '''Example `%RNGESUS 343435553434343434 RNGESU5` will react to message ID 343435553434343434 with `RNGESU5`'''
        await self.bot.delete_message(ctx.message)
        a=await self.bot.get_message(ctx.message.channel, msgid)
        newtexx=''.join(set(texx))
        if not len(texx)==len(newtexx):
            print('BAD')
            return
            
        for n in texx:
            nt=n.upper()
            emo=await subf.getemo(nt)
            await self.bot.add_reaction(a,emo)
    
    @client.event
    async def quest_error(error, ctx):
        if ctx.message.context.upper.startswith('%QUEST'):
            await self.bot.delete_message(ctx.message)
            await self.bot.send_message(ctx.message.author,"Over here! The command is `%quest <pokestop name>`.  You only need to give me a keyword for the pokestop name.")

    #Calculate the probability that a pokemon will get better after a trade
    #Can be used by anyone
    #Ready for publication
    @commands.command(pass_context=True)
    async def reroll(self,ctx,*,currentIVs : str=""):
        '''Use this command to determine the odds of a pokemon getting better during trade
           **Inputs:**
           IV inputs : Percentage    --> 65  __OR__
                       Attack/Def/HP --> 5 5 9
           Example:
           %reroll 5 8 6'''
        arrg=currentIVs.split(" ")
        if len(arrg)==1:
            #make sure
            try:
                if float(arrg[0])<0. or float(arrg[0])>100.:
                    await self.bot.send_message(ctx.message.channel, "The IV percentage must be between 0 and 100") 
                    return
                else:
                    miniv0=0./15.
                    miniv1=1./15.
                    miniv2=2./15.
                    miniv3=3./15.
                    miniv4=5./15.
                    miniv5=10./15.
                    perc=float(arrg[0])/100.0
                    odd0=str(round(min(1.,max(0.,1.-(perc-miniv0)/(1.-miniv0)))*100.,2))
                    odd1=str(round(min(1.,max(0.,1.-(perc-miniv1)/(1.-miniv1)))*100.,2))
                    odd2=str(round(min(1.,max(0.,1.-(perc-miniv2)/(1.-miniv2)))*100.,2))
                    odd3=str(round(min(1.,max(0.,1.-(perc-miniv3)/(1.-miniv3)))*100.,2))
                    odd4=str(round(min(1.,max(0.,1.-(perc-miniv4)/(1.-miniv4)))*100.,2))
                    odd5=str(round(min(1.,max(0.,1.-(perc-miniv5)/(1.-miniv5)))*100.,2))
                    #determine odds here
                    await self.bot.send_message(ctx.message.channel, "__The chance your pokemon will get better IVs is:__\n   **No Friend** --> " + odd0 +"%\n** Good Friend**--> " + odd1 +"%\n**Great Friend** --> " + odd2 +"%\n**Ultra Friend** --> " + odd3 +"%\n** Best Friend** --> " + odd4 + "%\n**LUCKY 'Mon** --> " + odd5 + "%") 
            except:
                await self.bot.send_message(ctx.message.channel, "The IV percentage was not a number") 
        elif len(arrg)==3:  #individual IVs were entered
            try:
                if float(arrg[0])<0. or float(arrg[0])>15.:
                    await self.bot.send_message(ctx.message.channel, "The IV for attack must be between 0 and 15") 
                    return
                if float(arrg[1])<0. or float(arrg[1])>15.:
                    await self.bot.send_message(ctx.message.channel, "The IV for attack must be between 0 and 15") 
                    return
                if float(arrg[2])<0. or float(arrg[2])>15.:
                    await self.bot.send_message(ctx.message.channel, "The IV for attack must be between 0 and 15") 
                    return
                
                #for x in range(3):
                miniv0=0./15.
                miniv1=1./15.
                miniv2=2./15.
                miniv3=3./15.
                miniv4=5./15.
                miniv5=10./15.
                perc=float(arrg[0])/15.0
                aodd0=str(round(min(1.,max(0.,1.-(perc-miniv0)/(1.-miniv0)))*100.,2))
                aodd1=str(round(min(1.,max(0.,1.-(perc-miniv1)/(1.-miniv1)))*100.,2))
                aodd2=str(round(min(1.,max(0.,1.-(perc-miniv2)/(1.-miniv2)))*100.,2))
                aodd3=str(round(min(1.,max(0.,1.-(perc-miniv3)/(1.-miniv3)))*100.,2))
                aodd4=str(round(min(1.,max(0.,1.-(perc-miniv4)/(1.-miniv4)))*100.,2))
                aodd5=str(round(min(1.,max(0.,1.-(perc-miniv5)/(1.-miniv5)))*100.,2))
                perc=float(arrg[1])/15.0
                dodd0=str(round(min(1.,max(0.,1.-(perc-miniv0)/(1.-miniv0)))*100.,2))
                dodd1=str(round(min(1.,max(0.,1.-(perc-miniv1)/(1.-miniv1)))*100.,2))
                dodd2=str(round(min(1.,max(0.,1.-(perc-miniv2)/(1.-miniv2)))*100.,2))
                dodd3=str(round(min(1.,max(0.,1.-(perc-miniv3)/(1.-miniv3)))*100.,2))
                dodd4=str(round(min(1.,max(0.,1.-(perc-miniv4)/(1.-miniv4)))*100.,2))
                dodd5=str(round(min(1.,max(0.,1.-(perc-miniv5)/(1.-miniv5)))*100.,2))
                perc=float(arrg[2])/15.0
                hodd0=str(round(min(1.,max(0.,1.-(perc-miniv0)/(1.-miniv0)))*100.,2))
                hodd1=str(round(min(1.,max(0.,1.-(perc-miniv1)/(1.-miniv1)))*100.,2))
                hodd2=str(round(min(1.,max(0.,1.-(perc-miniv2)/(1.-miniv2)))*100.,2))
                hodd3=str(round(min(1.,max(0.,1.-(perc-miniv3)/(1.-miniv3)))*100.,2))
                hodd4=str(round(min(1.,max(0.,1.-(perc-miniv4)/(1.-miniv4)))*100.,2))
                hodd5=str(round(min(1.,max(0.,1.-(perc-miniv5)/(1.-miniv5)))*100.,2))
                #determine odds here
                await self.bot.send_message(ctx.message.channel, "__The chance your pokemon will get better IVs is:__\n   **No Friend** --> " + aodd0 + "% / " + dodd0 + "% / " + hodd0 +"%\n** Good Friend**--> " + aodd1 + "% / " + dodd1 + "% / " + hodd1 +"%\n**Great Friend** --> " + aodd2 + "% / " + dodd2 + "% / " + hodd2 +"%\n**Ultra Friend** --> " + aodd3 + "% / " + dodd3 + "% / " + hodd3 +"%\n** Best Friend** --> " + aodd4 + "% / " + dodd4 + "% / " + hodd4 +"%\n**LUCKY 'Mon** --> " + aodd5 + "% / " + dodd5 + "% / " + hodd5 + "%")
            except:
                await self.bot.send_message(ctx.message.channel, "The IVs weren't numbers") 
        else: 
            await self.bot.send_message(ctx.message.channel, "You need to enter __**either**__ IV percentage or individual IVs.") 
            return  
    
    @commands.command(pass_context=True)
    async def getrex(self,ctx):
        await subf.gethell(self,ctx)
        return
        
    @commands.command(pass_context=True)
    async def clearthis(self,ctx):  #Function is depricated
        if not ctx.message.channel.id=='501888572333359115':
            return
        server=self.bot.get_server(self.serverid)
        allowrole=discord.utils.get(server.roles, id='502680369758339072')
        b=discord.Server.get_member(server,ctx.message.author.id)
        if not allowrole in b.roles:  #must be a ranger to do this
            await self.bot.delete_message(ctx.message)
            return
        
        async for message in self.bot.logs_from(ctx.message.channel, limit=500): #Gets a list of the last 500 
            if not message.id=='502678279224819722':
                await self.bot.delete_message(message)
     
     
    #This function places a quest notification in the quest channel
    #Can be used by anyone
    
    @commands.command(pass_context=True)
    async def quest(self,ctx,*,pokestop : str=""):
        if not (ctx.message.channel.is_private==True or ctx.message.channel.id==self.raidsightings):  #These should be entered via DM or in raid-sightings to prevent clutter
            await self.bot.send_message(ctx.message.author,"Over here! The command is `%quest <pokestop name>`.  You only need to give me a keyword for the pokestop name.")
            await self.bot.delete_message(ctx.message)
            return
        #await self.bot.send_message(ctx.message.channel,"This is being built right now! An announcement will me made when its ready")
        #f not ctx.message.author.id==self.CMK:
        #    await self.bot.send_message(ctx.message.channel,"This is being built right now! An announcement will me made when its ready")
        #    return
        alltimeout=30
        
        #print(location)
        cntt=0
        uniq=0
        grid=0
        
        Lvalue=pokestop
        if Lvalue=="":
            await self.bot.send_message(ctx.message.channel,"Please give me some information about the pokestop name.\nPress `q` to exit.")
            pokestop = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            Lvalue=pokestop.content
        
        if Lvalue.upper()=="Q":
            await self.bot.send_message(ctx.message.channel, "I'm sad")
            return
        #print(self.sWL)
        scrubmess=await subf.filtNameval(self,Lvalue.upper())          
        locn=""
        #Try finding the names of the gyms
        loclist=[]
        for y in Lvalue.split(' '):
            for x in self.sWL:
                if y.upper() == x.upper():  #was "in"
                    loclist.append(x)
        #Xref the list with the gym names
        possn=[]
        maxcom=0
        gyml=""
        cntt=0
        gymlist=[]
        suggch=[]
        
        #get the highest word count for stops
        for y in self.stopnam:
            comwords=0
            tpp=await subf.filtNameval(self,y)
            for x in loclist:
                if x.upper() in tpp.upper():
                    comwords+=1
                    gymlist.append(y)
            if comwords>maxcom:
                suggch.append(y)
                #gyml=self.lngroup[cntt]
                gyml="HELLO"
                maxcom=comwords
            cntt+=1
        
        print(comwords)
        
        gymlist=[]
        suggch=[]
        #print (maxcom)
        #print (loclist)
        if maxcom>0:
            for y in self.stopnam:
                comwords=0
                tpp=await subf.filtNameval(self,y)
                for x in loclist:
                    if x.upper() in tpp.upper():
                        comwords+=1
                        print(x.upper() + tpp.upper())
                        #gymlist.append(y)
                if comwords==maxcom:
                    print(y)
                    gymlist.append(y)
                    #gyml=self.lngroup[cntt]
                    #gyml="HELLO"
                    #maxcom=comwords
                cntt+=1
        #get unique gyms names only
        #print (suggch)
        #print ("Hello Christ AFEAFEJAFKJEAKFJEAFKJAEKFJAEF")
        ugym=[]
        for x in gymlist:
            if x not in ugym:
                ugym.append(x) 
        print (ugym)
        print (gymlist)
        
        if len(ugym)==0:
            await self.bot.send_message(ctx.message.channel,"I found no pokestops with any words you typed in.  Try again.\n")
            return
            
        
        txt="`"
        cntr=1
        for x in ugym:
            txt+=str(cntr)+ ") " +x +" \n"
            cntr+=1
        txt+="`"
        print(txt)
        print(ugym)
        
        #User selects which gym if confused
        alltimeout=30
        attempt=0
        if len(ugym)>1:
            if len(txt)>1950:
                await self.bot.send_message(ctx.message.channel,"Too many options.  I quit.\n")
                return
            await self.bot.send_message(ctx.message.channel,"I got confused. \nPlease clarify which stop you wanted by typing in the number for the stop:\n")
            await self.bot.send_message(ctx.message.channel,txt)
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            try:
                loclist=ugym[int(msgrt.content)-1]
                #newloca=loc
                #print(loc)
            except:
                attempt+=1
                dontcont=1
                return
        else:
            loclist=ugym[0]
        cntt=0
        #Get the correct mentions here
        channre = discord.utils.get(self.bot.get_all_channels(), server__name=self.servername, id=self.programid)
        rolem=None
        rolem2=None
        server=channre.server
        chan = self.bot.get_channel(self.questsightings)
        for y in self.stopnam:
            if loclist==y:
                #gyml=self.lngroup[cntt]
                gymlat=self.stoplat[cntt]
                gymlon=self.stoplon[cntt]
                cntsto=cntt
            cntt+=1
        #Check to see if the pokestop has a quest attached to it
        foundmess=0
        #print(tempna+" FK")
        async for messa in self.bot.logs_from(chan, limit=1000): #Gets a list of the last 500 messages in the channel 
            if loclist in messa.content:  
                foundmess=1#update the message
                
        if foundmess==1:
            await self.bot.send_message(ctx.message.channel, "That quest has already been added today.  If you think you got this message in error, pester the Milk Maid.")
            return

        
        #linkn="Directions to " + loclist + " can be found here:\n " + "https://www.google.com/maps/place/" + gymlat + "+" + gymlon +""+ ""
        #await self.bot.send_message(ctx.message.channel, linkn) 
        #print(loclist)
        ##self.tasklist=["Win a Raid","Make 4 Great Curves in a Row","Evolve 3 Natu or Sunkern","Make 3 Excellent Throws","Hatch 5 eggs"]
        ##self.rewardlist=[["PORYGON"],["MILTANK"],["PINECO"],["ONIX/SCYTHER"],["CHANSEY"]]#,["NULL"]]
        #self.tasklist=["Catch 10 pokemon","Transfer 10 pokemon","Battle a gym 5 times","Catch a Dragon Type","Catch a Skitty or Poochyena","Evolve a Meowth","Make 3 Excellent Throws in a row","Hatch 5 eggs"]
        #self.rewardlist=[["MAGIKARP"],["MISDREAVUS"],["MACHOP"],["DRATINI"],["SNUBULL"],["HOUNDOUR"],["LARVITAR"],["CHANSEY"]]#,["NULL"]]#,"Something else"]
        #self.tasklist=["Catch 10 pokemon","Send 5 gifts","Battle a gym 5 times","Catch a Dragon Type","Make a great curve throw","Catch 5 fire type","Make 3 Excellent Throws in a row","Hatch 5 eggs","Use 10 berries to help catch pokemon"]
        #self.rewardlist=[["MAGIKARP"],["ROSELIA"],["MACHOP"],["DRATINI"],["SPINDA"],["SILVER PINAP"],["LARVITAR"],["CHANSEY"],["GROWLITHE"]]
        #self.altrewards=[]
        
        #self.tasklist=["Catch 10 pokemon","Battle a gym 5 times","Catch a Dragon Type","Make 2 NICE curve throws","Catch 5 water type","Make 3 Excellent Throws in a row","Hatch 5 eggs","Use 10 berries to help catch pokemon","Hatch 2 eggs","Evolve 10 Water Type","Catch 10 Psychic Type"]
        #self.rewardlist=[["MAGIKARP"],["MACHOP"],["DRATINI"],["SPINDA"],["KRABBY"],["LARVITAR"],["CHANSEY"],["GROWLITHE"],["WAILMER"],["DRATINI"],["1000 Stardust"]]
        
        #self.tasklist=["Catch 10 pokemon","Battle a gym 5 times","Catch a Dragon Type","Make 3 NICE curve throws","Evolve 2 Pidgey","Catch 5 Bug Type","Hatch 5 eggs","Hatch 2 eggs"]
        #self.rewardlist=[["MAGIKARP"],["MACHOP"],["DRATINI"],["SPINDA"],["CATERPIE"],["NINCADA"],["CHANSEY"],["AERODACTYL"]]
        #self.tasklist=["Catch 10 pokemon","Battle a gym 5 times","Catch a Dragon Type","Make a great curve throw","Trade a pokemon","Win a raid","Hatch 5 eggs","Hatch 2 eggs"]
        #self.rewardlist=[["MAGIKARP"],["MACHOP"],["DRATINI"],["SPINDA"],["FEEBAS"],["PORYGON"],["CHANSEY"],["AERODACTYL"]]
        #self.tasklist=["Catch 10 pokemon","Battle a gym 5 times","Catch a Dragon Type","Make 5 great curve throws in a row","Catch 10 ground type","Catch 10 ice type","Hatch 5 eggs","Use an evolution item"]
        #self.rewardlist=[["MAGIKARP"],["MACHOP"],["DRATINI"],["SPINDA"],["SANDSHREW"],["KABUTO"],["CHANSEY"],["AERODACTYL"]]
        
        self.altrewards=[]
        #self.altrewards=["1000 dust","1500 dust"]
        linkn="**What must you do to complete the task from " + loclist + "?**\nEither enter a number or **your own task**\nPress `q` to exit.\n"
        cntt=0
        for x in self.tasklist:
            y=self.rewardlist[cntt]
            linkn+="**"+str(cntt+1)+")** "+x+" for a "+y[0]+"\n"
            cntt+=1
        await self.bot.send_message(ctx.message.channel, linkn) 
        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
        reward=msgrt.content
        realreward=""
        if reward.upper()=="Q":
            await self.bot.send_message(ctx.message.channel, "I'm sad") 
            return
        try:  #see if the reward is from the list
            retnum=int(reward)
            if retnum<=len(self.tasklist) and retnum>=1: #This is a predefined task
                #if len(self.rewardlist[retnum-1]+self.altrewards)<2:
                #    realreward=self.rewardlist[retnum-1]
                #    realreward=realreward[0]
                #else: #We need to ask what it is
                    realreward=self.rewardlist[retnum-1]
                    realreward=realreward[0]
                    questn=self.tasklist[retnum-1]
                    nall=1#updat
                    if nall==0:
                        msgstuff="**What is the reward from " + loclist + "?**\n*Enter a number or type in manually.*\n"
                        cntr=0
                        templist=self.rewardlist[retnum-1]+self.altrewards
                        for x in templist:
                            msgstuff+=" **"+str(cntr+1)+")** "+x+"\n"
                            cntr+=1
                        
                        
                        await self.bot.send_message(ctx.message.channel, msgstuff) 
                        msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                        if msgrt.content.upper()=="Q":
                            await self.bot.send_message(ctx.message.channel, "I'm sad") 
                            return
                        try:
                            if int(msgrt.content)<1 or int(msgrt.content)>len(self.rewardlist[retnum-1]):
                                await self.bot.send_message(ctx.message.channel, "You entered something wrong.  Please try again.") 
                                return
                            realreward=templist[int(msgrt.content)-1]
                        except:
                            print("Got manual entry")
                            realreward=msgrt.content
                            #await self.bot.send_message(ctx.message.channel, "You entered something wrong.  Please try again.") 
                            #return
                        questn=self.tasklist[retnum-1]
                    
            else:
                await self.bot.send_message(ctx.message.channel, "What must you do to complete the task from " + loclist + "?") 
                msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                questn=msgrt.content
                if questn.upper()=="Q":
                    await self.bot.send_message(ctx.message.channel, "I'm sad") 
                    return
                #linkn="What reward will you get from " + loclist + "?\nPress `q` to exit."
                linkn="What reward will you get by completing " + questn.upper() + "?\nPress `q` to exit."#loclist + "?\nPress `q` to exit."
                await self.bot.send_message(ctx.message.channel, linkn) 
                msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
                realreward=msgrt.content
                if realreward.upper()=="Q":
                    await self.bot.send_message(ctx.message.channel, "I'm sad") 
                    return
        except:
            #await self.bot.send_message(ctx.message.channel, "What must you do to complete the task from " + loclist + "?") 
            #msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            questn=reward
            if reward.upper()=="Q":
                await self.bot.send_message(ctx.message.channel, "I'm sad") 
                return
            linkn="What reward will you get from " + loclist + "?\nPress `q` to exit."
            await self.bot.send_message(ctx.message.channel, linkn) 
            msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            realreward=msgrt.content
            if realreward.upper()=="Q":
                await self.bot.send_message(ctx.message.channel, "I'm sad") 
                return
            
        #print(realreward)
        await self.bot.send_message(ctx.message.channel, "Got it! You'd get a " + realreward + " from "+ loclist + " by completing "+questn +".") 
        reward=realreward
        
        if "CHARGE" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.chargedtm)
        if "CHANSEY" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.chansey)
        if "CHANCEY" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.chansey)
        if "RARE" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.rarecandy)
        if "CANDY" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.rarecandy)
        if "TANGELA" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.tangela)
        if "MAGIKARP" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.magikarp)
        if "SILVER" in reward.upper():
            rolem=discord.utils.get(server.roles, id=self.silverpinap)
        if "ABSOL" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.absol)
        if "NINCADA" in reward.upper():
            rolem = discord.utils.get(server.roles, id="507930130472239117")
        if "GROWLITHE" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.growlithe)
        if "DRATINI" in reward.upper():
            rolem = discord.utils.get(server.roles, id=self.dratini)
        if "SPINDA" in reward.upper():
            rolem = discord.utils.get(server.roles, id="474314526389698571")
        if "LARVITAR" in reward.upper():
            rolem  = discord.utils.get(server.roles, id="431538336977387523")
        if "DUST" in reward.upper():
            if "1500" in reward.upper():
                rolem = discord.utils.get(server.roles, id=self.dust1500) 
            if "1000" in reward.upper():
                rolem = discord.utils.get(server.roles, id=self.dust1000)                
        for yr in self.shinylist:
            if yr in reward.upper():
                rolem2 = discord.utils.get(server.roles, id=self.shinyquest)
        
        qmaster=0
        if "LARVITAR" in reward.upper():
            qmaster=1
        if "1500" in reward:
            qmaster=1
        if "HATCH 5" in questn.upper():
            qmaster=1
        if "HOUNDOUR" in reward.upper():
            qmaster=0
        
        timestt=str(datetime.utcnow()+timedelta(hours=self.timez))
        
        
        chan = self.bot.get_channel(self.questsightings)
        
        rr=""
        if not rolem2==None:
            rr=rolem2.mention
        
            
        
        #if rolem==None:
        #    await self.bot.send_message(chan,rr + " " + loclist + " has the " + reward + " for " + questn + "  quest.\nhttps://www.google.com/maps/place/" + gymlat + "+" + gymlon +"")
        #else:
        #    #print(rolem)
        #    await self.bot.send_message(chan,rr + " " + rolem.mention + " " + loclist + " has the " + reward + " for " + questn + "  quest.\nhttps://www.google.com/maps/place/" + gymlat + "+" + gymlon +"")
        if rolem==None:
            #await self.bot.send_message(chan,rr + " " + loclist + " has the " + reward + " for " + questn + "  quest.\nhttps://www.google.com/maps/place/" + gymlat + "+" + gymlon +"")
            #linkn="Directions to " + loclist + " can be found here:\n " + "https://www.google.com/maps?q=" + gymlat + "," + gymlon +""+ ""
            #This was the correct one below
            #await self.bot.send_message(chan,rr + " " + loclist + " has the " + reward + " for " + questn + "  quest.\nhttps://www.google.com/maps?q=" + gymlat + "," + gymlon +"")
            
            
            #timeval=datetime.utcnow()+timedelta(hours=self.timez)
            timeval=datetime.today()
            timeval=timeval.strftime('%b %d, %Y')

            embed=discord.Embed(title="**"+reward+" for "+questn+"**" , color=0x00ff00)
            #embed.set_author(name="Use 5 berries to catch a pokemon for Cubone")
            embed.add_field(name="__**Location:**__ "+loclist, value="[Map Link Here](https://www.google.com/maps?q=" + gymlat + "," + gymlon +")", inline=True)
            #embed.add_field(name="Server Rank", value="12", inline=True)
            #embed.add_field(name="Badges", value=":1: :2:", inline=True)
            embed.set_footer(text="Valid until 11:59pm on " + str(timeval))
            #await self.bot.say(embed=embed)
            await self.bot.send_message(chan,"---------------" + rr + "\n**Location:** " + loclist + " \n" + reward.upper() + " for " + questn + "  quest",embed=embed)
            
        else:
            #print(rolem)
            print(reward)
            #await self.bot.send_message(chan,rr + " " + rolem.mention + " " + loclist + " has the " + reward + " for " + questn + "  quest.\nhttps://www.google.com/maps/place/" + gymlat + "+" + gymlon +"")
            #if "SILVER" in reward.upper():
            
            #    await self.bot.send_message(chan,rr + " " + rolem.mention + " " + loclist + " has the OBTAIN 5 PHYRE-CLASSIFIED MONSTER FOR A BLOODY STERLING PINAP quest.\nhttps://www.google.com/maps?q=" + gymlat + "," + gymlon +"")
            #else:
            #This was the correct one below
            #await self.bot.send_message(chan,rr + " " + rolem.mention + " " + loclist + " has the " + reward + " for " + questn + " quest.\nhttps://www.google.com/maps?q=" + gymlat + "," + gymlon +"")
            
            timeval=datetime.today()
            timeval=timeval.strftime('%b %d, %Y')

            embed=discord.Embed(title="**"+reward+" for "+questn+"**" , color=0x00ff00)
            #embed.set_author(name="Use 5 berries to catch a pokemon for Cubone")
            embed.add_field(name="__**Location:**__ "+loclist, value="[Map Link Here](https://www.google.com/maps?q=" + gymlat + "," + gymlon +")", inline=True)
            #embed.add_field(name="Server Rank", value="12", inline=True)
            #embed.add_field(name="Badges", value=":1: :2:", inline=True)
            embed.set_footer(text="Valid until 11:59pm on " + str(timeval))
            #await self.bot.say(embed=embed)
            await self.bot.send_message(chan,"---------------" + rr+ " " + rolem.mention + "\n**Location:** " + loclist + " \n" + reward.upper() + " for " + questn + "  quest",embed=embed)
            
        
        try:    
            if len(msgrt.content)>0:
                #await self.bot.send_message(ctx.message.channel, "Got it! "+ loclist + " has the " + reward + " for " + questn + "  quest.")
                with open("quests.txt","a") as f:
                    line=str(cntsto) + " ~ " + ctx.message.author.display_name + " ~ " + str(datetime.utcnow()+timedelta(hours=self.timez)) + " ~ " + reward + " ~ " + questn
                    print(line,file=f)
        except:
            await self.bot.send_message(ctx.message.channel, "Something went really wrong there.  Try again.")
        
        if qmaster==1:
            await self.bot.send_message(ctx.message.channel,"It looks like you found a really cool quest.  Can I recognize you by awarding you the Quest Master role for today?")
            respons = await self.bot.wait_for_message(timeout = alltimeout, author = ctx.message.author, channel = ctx.message.channel)
            if respons.content.startswith("Y") or respons.content.startswith("y"):
                await self.bot.send_message(ctx.message.channel, "Awesome! You are a Quest Master today.") 
                member = discord.utils.get(server.members, id=ctx.message.author.id)
                Questrole=discord.utils.get(server.roles, id="432527087748775947") #471684789276246016
                if Questrole in member.roles:
                    await self.bot.send_message(ctx.message.channel, "You're a go-getter, but it looks like you are already the quest master!") 
                else:
                    await self.bot.add_roles(member,Questrole) 
                    await asyncio.sleep(0.25)
                  
            else:
                await self.bot.send_message(ctx.message.channel, "No worries.  This will be our little secret.") 
            return
        
        
        return
            
        #Grab the quests channel:
    
    #Clear messages in bulk - must be less than 2 weeks old to use this method
    #Ready for publication
    @checks.admin() #Only allow admins to use this 
    @commands.command(pass_context=True)
    async def clm(self,ctx,num):                
        deleted=await self.bot.purge_from(ctx.message.channel, limit=int(num))
    
    
    @commands.command(pass_context=True)
    async def userreset(self,ctx,member):
        server=self.bot.get_server(self.serverid)
        #verify member is a tag
    
    
    @commands.command(pass_context=True)
    async def approval(self,ctx):
        server=self.bot.get_server(self.serverid)
        member = discord.utils.get(server.members, id=ctx.message.author.id)
        print(member.roles)
        Trainer=discord.utils.get(server.roles, id="284583203245916160")
        #Trainer=discord.utils.get(server.roles, id="284600666805239808")  #Approved
        
        chan2 = self.bot.get_channel(member.id)
        #print(chan2)
        #mess = await self.bot.wait_for_message(timeout=15,channel = ctx.message.channel,author=ctx.message.author)
        #print(mess.content)
        #print(Trainer.name)
        #for x in member.roles:
            #print(x.name)
        if Trainer in member.roles:
            await subf.approvehelper(self,member,ctx.message.channel)
        else: 
            await self.bot.send_message(member,"You have already been approved!")
    
    
    @client.event
    async def on_member_join(self,member): 
        if member.id in self.bannedlist:
            #We need to send them a message and kick them
            await self.bot.send_message(member,"You have been banned from the server. Save yourself the effort and stop trying to rejoin.")
            with open('images/samuel-l-jackson-banned.gif', 'rb') as f:
                await self.bot.send_file(member, f)
            await self.bot.kick(member)
            return
        arss=1
        if arss==1:
            #await self.bot.send_message(member,"Hi, you have arrived.")
            server=self.bot.get_server(self.serverid)
            chan = self.bot.get_channel(self.getapproved) #get approved channel
            chanr = self.bot.get_channel(self.programid) #get approved channel
            Ranger=discord.utils.get(server.roles, id=self.POGOmod)
            Trainer=discord.utils.get(server.roles, id=self.Unapproved)
            inschan = self.bot.get_channel(self.instinctch)
            myschan = self.bot.get_channel(self.mysticch)
            valchan = self.bot.get_channel(self.valorch)
            chan2 = self.bot.get_channel(member.id)
            Valor=discord.utils.get(server.roles, id=self.valor)
            Mystic=discord.utils.get(server.roles, id=self.mystic)
            Instinct=discord.utils.get(server.roles, id=self.instinct)

            success=0
            osuccess=0
            while osuccess==0:
                sto=3600*24  #Allow the bot to hang up for 24 hours
                await self.bot.send_message(member,"Welcome to the " + self.servername + " Discord Server and welcome to the world of Pokémon! My name is Purdue Pollster! People call me the stupid blind bird! This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Other use them for fights. Myself… I am one.\nAnyway, I am here to help your joining process.  If I do not respond within a few seconds of you answering a question, type `%approval` back here. So, without further ado, let's get started:\n__**What is your trainer name in Pokemon Go? Please enter it exactly as it is shown in the game!**__")
                ggh=1
                if ggh==1:
                #try:
                    while success==0:    
                        
                        
                        tsucc=0
                        while tsucc==0:
                            nmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                            if not nmess.channel.is_private:
                                await self.bot.send_message(member,"Hey! Over here! \n__**What is your trainer name in Pokemon Go? Please enter it exactly as it is shown in the game!**__ ")
                            else:
                                tsucc=1
                        username=nmess.content
                        print(username)
                        #return
                        success2=0
                        await self.bot.send_message(member,"You told me your Pokemon Go Trainer name is " + username + ".  \nDid I get that correct? (Y/N) ")
                        #success=1
                        while success2==0:
                            mess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                            if mess.content.upper()=="Y":
                                success2=1#update
                                success=1
                            elif mess.content.upper()=="N":
                                success2=1
                                await self.bot.send_message(member,"__**What is your trainer name in Pokemon Go? Please enter it exactly as it is shown in the game!**__")
                            elif mess.content.upper()=="END":
                                return
                            else:
                                await self.bot.send_message(member,"Please answer Y or N.")
                                
                    #Now change the nickname
                    await self.bot.change_nickname(member, username)    
                    
                    success=0
                    teamname=""
                    await self.bot.send_message(member,"What is your team name?:\n1) Instinct (Yellow)\n2) Mystic   (Blue)\n3) Valor    (Red)")
                    while success==0:
                        
                        nmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                        if nmess.content.upper()=="1" or nmess.content.upper()=="INSTINCT" or nmess.content.upper()=="YELLOW":
                            #teamass=Instinct
                            teamname="Instinct"
                            role=Instinct
                            #success=1
                        elif nmess.content.upper()=="2" or nmess.content.upper()=="MYSTIC" or nmess.content.upper()=="BLUE":
                            #teamass=self.mystic
                            teamname="Mystic"
                            role=Mystic
                            #success=1
                        elif nmess.content.upper()=="3" or nmess.content.upper()=="VALOR" or nmess.content.upper()=="RED":
                            #teamass=self.valor
                            teamname="Valor"
                            role=Valor
                            #success=1
                        elif nmess.content.upper()=="END":
                                return
                        else:
                            await self.bot.send_message(member,"I didn't get that.\n__**What is your team name?:**__)\n1) Instinct (Yellow)\n2) Mystic   (Blue)\n3) Valor    (Red)")
                        if not teamname=="":
                            success2=0
                            await self.bot.send_message(member,username + ", it looks like you are team " + teamname + ". Right? (Y/N)")
                            #success=1
                            while success2==0:
                                mess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                                if mess.content.upper()=="Y":
                                    success2=1#update
                                    success=1
                                elif mess.content.upper()=="N":
                                    success2=1
                                    await self.bot.send_message(member,"What is your team name?:\n1) Instinct (Yellow)\n2) Mystic   (Blue)\n3) Valor    (Red)")
                                else:
                                    await self.bot.send_message(member,"Please answer Y or N.")
                    #add the team role to lock down the trainer name    
                    await self.bot.add_roles(member,role) 
                    await asyncio.sleep(0.75)
                    await self.bot.remove_roles(member,Trainer) 
                    await asyncio.sleep(0.75)  
                                       
                    
                    
                    #Now for the approval side
                    success=0
                    #await self.bot.send_message(member,"Now, please follow me into the discord to review the rules.")
                    #await subf.gethell(self,member)
                    #teamname=""
                    if member.id == "23775784967182745611":
                        await self.bot.send_message(member,"At this time, follow me into the discord to review the rules.")
                        
                        
                        rulesch = self.bot.get_channel("351617228157878272")
                        #print(rulesch.id)
                        msgid1 = await self.bot.get_message(rulesch,"387389760068386821")
                        msgid2 = await self.bot.get_message(rulesch,"387389972094648341")
                        print(msgid2.content)
                        ARPr=await self.bot.send_message(rulesch,member.mention + " review this and react to the rules with any emoji to continue!")
                        
                        
                        #tmess1 = await self.bot.wait_for_reaction(emoji=None, user=member, timeout=None, message=msgid1, check=None)
                        tmess2 = await self.bot.wait_for_reaction(message=msgid2)
                        await self.bot.delete_message(ARPr)
                        
                    
                    
                    #Now for the approval side
                    success=0
                    #teamname=""
                    await self.bot.send_message(member,"At this time, upload a screen capture of the screen with your trainer name and buddy to finalize the approval process.")
                    while success==0:
                        try:
                            tmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member) #print (tmess.attachments[0]['filename'])
                            if tmess.attachments[0]['size']:
                                success2=0
                                await self.bot.send_message(member,username + ", are you sure you want to upload this image? (Y/N)")
                                success=1
                                while success2==0:
                                    mess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                                    if mess.content.upper()=="Y":
                                        success2=1#update
                                        success=1
                                    elif mess.content.upper()=="N":
                                        success2=1
                                        await self.bot.send_message(member,"At this time, upload a screen capture of the screen with your trainer name and buddy to finalize the approval process.")
                                    else:
                                        await self.bot.send_message(member,"Please answer Y or N.")

                        except:
                            await self.bot.send_message(member,"That didn't look like an image to me.  Try again.")
                        #nmess = await self.bot.wait_for_message(timeout=sto,channel = chan2,author=member)
                    
                    if teamname=="Instinct":
                        await self.bot.send_message(inschan,member.mention+" has joined Team Instinct! Welcome!")
                    if teamname=="Mystic":
                        await self.bot.send_message(myschan,member.mention+" has joined Team Mystic! Welcome!")
                    if teamname=="Valor":
                        await self.bot.send_message(valchan,member.mention+" has joined Team Valor! Welcome!")
                        
                    print("Passing image to Rangers.")
                    await self.bot.send_message(chan,"Rangers" + ", a user named " + username + " has joined team " + teamname + ".\nPlease verify that their user name and team are correct and `!approve` " + member.mention + " to approve the user.  If the image doesn't match this information, type `!decline` "+ member.mention + " so the trainer can re-enter their information.")
                    await self.bot.send_message(chan,tmess.attachments[0]['url'])
                    await self.bot.send_message(member,"Your request has been submitted! Welcome")
                    pending=discord.utils.get(server.roles, id=self.pendingApp)
                    await asyncio.sleep(0.75)  
                    await self.bot.add_roles(member,pending) 
                    await asyncio.sleep(0.75)                      
                    osuccess=1
                else:
                #except:
                    await self.bot.send_message(member,"Please finish registration before using any of the channels. \nLet's try this again.")
                    osuccess=0
            #await self.bot.send_message(member,"Once you have been approved, come back here and type `%guide` to get some the tools used on this server configured for you.  Welcome!")#chan
            #await self.bot.send_message(chan,"I am about to take over the world.  \nJust kidding!  Stinkpot is trying something here.")
    
    @client.event
    async def on_message(self,message):  

        tmess=message
        #if not message.author.id==self.CMK and not message.author.id==self.botid:
        #    await self.bot.send_message(message.channel,"Hi")
        #    return
        #piggyback off of !approve
        
        #if 
        #try:
        try:
            server=self.bot.get_server(self.serverid)
            Ranger=discord.utils.get(server.roles, id=self.POGOmod)
            MilkMaid=discord.utils.get(server.roles, id=self.POGOmod)
            Discmods=discord.utils.get(server.roles, id=self.POGOmod)
            Pogomods=discord.utils.get(server.roles, id=self.POGOmod)
            
            #print(tmess.author)
            arp=0
            b=discord.Server.get_member(server,tmess.author.id)
            if Ranger in b.roles:  #must be a ranger to do this
                arp=1
            if MilkMaid in b.roles:
                arp=1
            if Discmods in b.roles:
                arp=1
            if Pogomods in b.roles:
                arp=1
            #if tmess.author.id=="147553893310660612":
            #    arp=0
            if arp==1:
                
                if tmess.channel.id==self.getapproved: #must be in get-approved channel
                    if tmess.content.startswith("!decline"):
                        #return
                        Valor=discord.utils.get(server.roles, id=self.valor)
                        Mystic=discord.utils.get(server.roles, id=self.mystic)
                        Instinct=discord.utils.get(server.roles, id=self.instinct)
                        Trainer=discord.utils.get(server.roles, id=self.Unapproved)
                        sploo=tmess.content.split(" ")
                        #get the user mentioned
                        reason=""
                        for y in sploo[2:]:
                            reason+=y + " "
                        userm=tmess.mentions[0]  #This is a member
                        
                        await self.bot.add_roles(userm,Trainer) 
                        await asyncio.sleep(0.5)
                        await self.bot.remove_roles(userm,Instinct) 
                        await asyncio.sleep(0.5)  
                        await self.bot.remove_roles(userm,Valor) 
                        await asyncio.sleep(0.5)  
                        await self.bot.remove_roles(userm,Mystic) 
                        await asyncio.sleep(0.5)  
                        await self.bot.send_message(userm,"Hey, looks like something didn't go quite right.  \nYou couldn't be approved for this reason: Its been longer than 7 days since you joined. \nTo try getting approved again type `%approval` here and answer a few questions.")
                        
                        #await self.bot.send_message(message.channel,userm.name + " was declined and will be required to re-enter their trainer info. This trainer has also been removed from their assigned team. Thanks!")   
                        
                        return
                if tmess.channel.id==self.getapproved: #must be in get-approved channel
                    if tmess.content.startswith("!approve"):
                        #get the user mentioned
                        userm=tmess.mentions[0]  #This is a member
                        await self.bot.send_message(userm,"Hey, you just got approved!  Can you do a favor for me and type `%guide` here so I can help you get your trainer account setup?")
                        await self.bot.send_message(message.channel,userm.name + " was approved and will now be guided to set up their account. Thanks!")
                        pending=discord.utils.get(server.roles, id=self.pendingApp)
                        await self.bot.remove_roles(userm,pending) 
                        await asyncio.sleep(0.5) 
                        approved=discord.utils.get(server.roles, id=self.Approved)
                        await self.bot.add_roles(userm,approved) 
                        await asyncio.sleep(0.5) 
                        return
                    if tmess.content.startswith("!decline"):
                        #return
                        Valor=discord.utils.get(server.roles, id=self.valor)
                        Mystic=discord.utils.get(server.roles, id=self.mystic)
                        Instinct=discord.utils.get(server.roles, id=self.instinct)
                        Trainer=discord.utils.get(server.roles, id=self.Unapproved)
                        sploo=tmess.content.split(" ")
                        #get the user mentioned
                        reason=""
                        for y in sploo[2:]:
                            reason+=y + " "
                        userm=tmess.mentions[0]  #This is a member
                        
                        await self.bot.add_roles(userm,Trainer) 
                        await asyncio.sleep(0.5)
                        await self.bot.remove_roles(userm,Instinct) 
                        await asyncio.sleep(0.5)  
                        await self.bot.remove_roles(userm,Valor) 
                        await asyncio.sleep(0.5)  
                        await self.bot.remove_roles(userm,Mystic) 
                        await asyncio.sleep(0.5)  
                        await self.bot.send_message(userm,"Hey, looks like something didn't go quite right.  \nYou couldn't be approved for this reason: " + reason + "\nTo try getting approved again type `%approval` here and answer a few questions.")
                        
                        await self.bot.send_message(message.channel,userm.name + " was declined and will be required to re-enter their trainer info. This trainer has also been removed from their assigned team. Thanks!")   
                        
                        return
        except:
            arrer=1
        #try:
        if tmess.content.startswith("%level") and len(tmess.content)>6:
            if not " " in tmess.content:
                lvl=tmess.content[6:]
                await subf.levelhelper(self,tmess,lvl) 
                #self.bot.send_message(message.channel, "I didn't understand.  Please use a space between `%level` and your trainer level number.")
                return
        

        try:
            
            majorg=self.g1locaid+self.g2locaid+self.g3locaid+self.L3groupid+self.L4groupid+self.L5groupid+self.PSgroupid
            if any(x==message.channel.id for x in majorg): #It is a raid channel and the bot needs to delete user messages
                if not message.author.id==self.botid: #This is the bot
                    if message.content.startswith("@Start") or message.content.startswith("@start"):
                        await self.bot.delete_message(message)
                        await self.bot.send_message(message.author,"React with an emoji please.  Press and hold the message of the time to which to sign up for and 'add reaction'")
                        return
  
                    chnid=message.channel.id
                    chnam=message.channel.name
                    argg=chnam.split('---')
                    found=await subf.findboss(self,chnid)
                    #If the channel is a raid boss specific channel, the second channel will lead with the raid boss
                    #if found==1:
                    raidboss=argg[0]
                    location=argg[1]
                    namel2=raidboss + "---" +  location
                    #else:
                    #    raidboss=argg[0]
                    #    location=argg[1]
                    #    namel2=location + "---" +  raidboss
                    #print(message.content.upper())
                    if "WHERE IS THIS" in message.content.upper() or "WHERE IS THE" in message.content.upper():
                        cntt=0
                        linkn=""
                        print(message.content.upper())
                        for x in self.sngroup:
                            Nameval=self.cngroup[cntt]
                            chnloc=await subf.filtNameval(self,Nameval)
                            #print(chnloc + " " + location)
                            if location==chnloc:
                                #linkn=self.lngroup[cntt]
                                gymlat=self.latgroup[cntt]
                                gymlon=self.longroup[cntt]
                                linkn= "" + gymlat + "," + gymlon +""+ ""
                                linkn="Directions to " + Nameval + " can be found here:\n " + "https://www.google.com/maps?q=" + linkn + ""
                            cntt=cntt+1
                        await self.bot.send_message(message.channel,"Here you go "+message.author.mention+"\n"+linkn)
                        return
                    #channel2 = discord.utils.get(message.server.channels, name=namel2)
                    #await self.bot.send_message(channel2,message.author.display_name+ " : " + message.content)
                else:
                    arr=1
                    
        except:
            arr=1 
        
        
    
    @client.event
    async def on_message_edit(self,message1,message):
        
        if message.channel.id=="413488064447381514" or message.channel.id=="403550523984183296" or message.channel.id=="408330312125382656":
            #await self.bot.send_message(message.channel,"This")
            tmess=message
            #if not message.author.id==self.CMK and not message.author.id==self.botid:
            #    await self.bot.send_message(message.channel,"Hi")
            #    return
            #print (tmess.content)
            if tmess.content.upper().startswith("<@360051594311630850>") and not message.author.id==self.botid:
                if not ("MEWTWO" in tmess.content.upper() or "EX-RAID" in tmess.content.upper() or "EXRAID" in tmess.content.upper()):
                    await self.bot.send_message(message.channel,"This doesn't look like a Mewtwo raid to me.")
                    return
                chpost=message.channel 
                chpost=self.bot.get_channel(self.mewtwoposts)
                #Try finding the boss name
                
                
                #uniqwords=[]
                #for x in self.WL:
                #    if x not in uniqwords:
                #        if len(x)>4:
                #            uniqwords.append(x) 
                #self.WL=uniqwords
                scrubmess=await subf.filtNameval(self,tmess.content.upper())
                
                
                bossn=""
                bossf=""
                for x in self.Bosstypes:
                    if x.upper() in tmess.content.upper(): 
                        bossn=x
                        break
                locn=""
                #Try finding the names of the gyms
                loclist=[]
                for x in self.WL:
                    if x.upper() in tmess.content.upper(): 
                        loclist.append(x)
                #Xref the list with the gym names
                possn=[]
                maxcom=0
                gyml=""
                cntt=0
                gymlist=[]
                suggch=[]
                
                for y in self.cngroup:
                    comwords=0
                    tpp=await subf.filtNameval(self,y)
                    for x in loclist:
                        if x.upper() in tpp.upper():
                            comwords+=1
                            #gymlist.append(y)
                    if comwords>maxcom:
                        #suggch.append(y)
                        suggch=y
                        gyml=self.lngroup[cntt]
                        maxcom=comwords
                    cntt+=1
                #get unique gyms names only
                for y in self.cngroup:
                    comwords=0
                    tpp=await subf.filtNameval(self,y)
                    for x in loclist:
                        if x.upper() in tpp.upper():
                            comwords+=1
                            #gymlist.append(y)
                    if comwords==maxcom:
                        #suggch.append(y)
                        #suggch=y
                        gymlist.append(y)
                        #gyml=self.lngroup[cntt]
                        #maxcom=comwords
                    cntt+=1
                
                ugym=[]
                for x in gymlist:
                    if x not in ugym:
                        ugym.append(x) 
                print (ugym)
                print (gymlist)
                
                txt="`"
                cntr=1
                for x in ugym:
                    txt+=str(cntr)+ ") " +x +" \n"
                    cntr+=1
                txt+="`"
                #User selects which gym if confused
                alltimeout=30
                if len(ugym)>1:
                    await self.bot.send_message(message.channel,"I got confused. \nPlease clarify which gym you wanted by typing in the number for the gym:\n")
                    await self.bot.send_message(message.channel,txt)
                    msgrt = await self.bot.wait_for_message(timeout = alltimeout, author = message.author, channel = message.channel)
                    try:
                        loclist=ugym[int(msgrt.content)-1]
                        #newloca=loc
                        #print(loc)
                    except:
                        attempt+=1
                        dontcont=1
                        return
                else:
                    loclist=ugym[0]
                
                
                
                cntt=0

                
                for y in self.cngroup:
                    if loclist==y:
                        gyml=self.lngroup[cntt]
                    cntt+=1
                
                print(loclist)
                
                arggs=tmess.content.split("/")
                mm=0
                dd=0
                yy=0
                cntt=0
                for x in arggs:
                    argg2=x.split(" ")
                    print(argg2[len(argg2)-1] + " " + argg2[0])
                    for y in argg2:
                        if cntt==0: ##MM
                            mm=int(argg2[len(argg2)-1])
                        elif cntt==1: ##MM
                            dd=int(argg2[0])
                        elif cntt==2: ##YY
                            yy=int(argg2[0])
                    cntt+=1
                if yy<2000:
                    yy+=2000
                
                if mm==1:
                    mon="January"
                elif mm==2:
                    mon="February"
                elif mm==3:
                    mon="March"
                elif mm==4:
                    mon="April"
                elif mm==5:
                    mon="May"
                elif mm==6:
                    mon="June"
                elif mm==7:
                    mon="July"
                elif mm==8:
                    mon="August"
                elif mm==9:
                    mon="September"
                elif mm==10:
                    mon="October"
                elif mm==11:
                    mon="November"    
                elif mm==12:
                    mon="December"    
                    
                #Try finding the time of the raid
                #loclist=suggch
                arggs=tmess.content.split(":")
                hashour=0
                hour=0
                minute=0
                for x in arggs:
                    argg2=x.split(" ")
                    for y in argg2:
                        try:
                            if hashour==0:
                                hour=int(y)
                                hashour=1
                            else:
                                minute=int(y)
                                #hashour=1
                        except:
                            notnum=1
                #Create second time
                minute1=minute+30
                hour1=hour
                if minute1>=60:
                    minute1-=60
                    hour1+=1
                    
                
                await self.bot.send_message(chpost,"__**EX-RAID:**__ "+ mon + " "+str(dd)+","+str(yy) + "\n" + loclist + "\n" +"https://goo.gl/" + gyml + "\n"+"React for Start Time: " + str(hour).zfill(2)+":"+str(minute).zfill(2)+":00")# + str(mm).zfill(2) + " "+str(dd).zfill(2)+","+str(yy))
                #msgg2=await self.bot.send_message(chpost,"React for Start Time: " + str(hour).zfill(2)+":"+str(minute).zfill(2)+":00")
                await self.bot.send_message(chpost,"React for Late Start: " + str(hour1).zfill(2)+":"+str(minute1).zfill(2)+":00")
                msgg4=await self.bot.send_message(chpost,"**--------------------------------**")
                #msgg=await self.bot.send_message(chpost,tmess.content)
                #rtt=await self.bot.pin_message(msgg)
                #
                async for ms in self.bot.logs_from(chpost, limit=10): #Gets a list of the last 500 messages in the channel 
                    if ms.type==discord.MessageType.pins_add:
                        b=1
                        #await self.bot.delete_message(ms)
                #await self.bot.delete_message(message)
                return
                #else:
                    #msgg=await self.bot.send_message(chpost,"Sorry, but I had a bit of trouble on recognizing the gym.  I __**am**__ only a computer afterall.")
                    #return
    
    #This program is used to setup raid-day type events in a channel
    #Ready for publication
    @checks.admin() #Require admin level
    @commands.command(pass_context=True)
    async def setuptrains(self,ctx):
        await self.bot.delete_message(ctx.message)
        ch=ctx.message.channel
        await self.bot.send_message(ch,"__** Mystic: Raid Group #1 = **__") 
        await self.bot.send_message(ch,"__** Mystic: Raid Group #2 = **__") 
        await self.bot.send_message(ch,"__** Mystic: Raid Group #3 = **__") 
        await self.bot.send_message(ch,"__** Mystic: Raid Group #4 = **__") 
        await self.bot.send_message(ch,"__** Mystic: Raid Group #5 = **__") 
        await self.bot.send_message(ch,"__** Mystic: Raid Group #6 = **__") 
        await self.bot.send_message(ch,"__** Mystic: Raid Group #7 = **__") 
        await self.bot.send_message(ch,"__** Mystic: Raid Group #8 = **__") 
        await self.bot.send_message(ch,"__**  Valor: Raid Group #1 = **__") 
        await self.bot.send_message(ch,"__**  Valor: Raid Group #2 = **__") 
        await self.bot.send_message(ch,"__**  Valor: Raid Group #3 = **__") 
        await self.bot.send_message(ch,"__**  Valor: Raid Group #4 = **__")
        await self.bot.send_message(ch,"__**  Valor: Raid Group #5 = **__") 
        await self.bot.send_message(ch,"__**  Valor: Raid Group #6 = **__")
        await self.bot.send_message(ch,"__**  Valor: Raid Group #7 = **__") 
        await self.bot.send_message(ch,"__**  Valor: Raid Group #8 = **__")
        await self.bot.send_message(ch,"__**Instinct:Raid Group #1 = **__") 
        await self.bot.send_message(ch,"__**Instinct:Raid Group #2 = **__") 
        await self.bot.send_message(ch,"__**Instinct:Raid Group #3 = **__") 
        await self.bot.send_message(ch,"__**Instinct:Raid Group #4 = **__") 
        await self.bot.send_message(ch,"__**Instinct:Raid Group #5 = **__") 
        await self.bot.send_message(ch,"__**Instinct:Raid Group #6 = **__") 
        await self.bot.send_message(ch,"__**Instinct:Raid Group #7 = **__") 
        await self.bot.send_message(ch,"__**Instinct:Raid Group #8 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #1 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #2 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #3 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #4 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #5 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #6 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #7 = **__") 
        await self.bot.send_message(ch,"__**   Mixed:Raid Group #8 = **__") 

    #This program is used to delete raid-day type events in a channel
    #Ready for publication
    @checks.admin() #Require admin level
    @commands.command(pass_context=True)
    async def deletetrains(self,ctx):
        await self.bot.delete_message(ctx.message)
        ch=ctx.message.channel
        await self.bot.purge_from(ch, limit=100)
    
    #This is a discord event-based function, and serves multiple subfunctions
    @client.event
    async def on_reaction_add(self,reaction,user):
        tmess=reaction.message 
       

        
        #print("Here")
        ################################################################
        ################################################################
        ########################THIS IS THE MEAT################################
        ################################################################
        ################################################################
        arr=10
        if tmess.channel.id in self.alllocch:
        #try:
            
            raidrestr=discord.utils.get(reaction.message.server.roles, id=self.raidrestr)
            #print (user.roles)
            if raidrestr in user.roles:
                await self.bot.remove_reaction(reaction.message,reaction.emoji,user)
                
                return
            assiRM=0
            raidlevel=5 #Use this in the meantime
            #print("Here")
            message=reaction.message
            if not message.content.startswith('@Start:'):
                return
            chnid=reaction.message.channel.id
            ctx=reaction
            chnam=reaction.message.channel.name
            #channel1=discord.utils.get(ctx.message.server.channels, id=channel_id)
            #chnam=channel1.name
            #chnid=channel1.id
            argg=chnam.split('---')
            found=await subf.findboss(self,chnid)
            
            #If the channel is a raid boss specific channel, the second channel will lead with the raid boss
            if found==1:
                raidboss=argg[1]
                location=argg[0]
                namel2=raidboss + "---" +  location
            else:
                raidboss=argg[0]
                location=argg[1]
                namel2=location + "---" +  raidboss
            
            #Get the two channels
            channel1=ctx.message.channel   
            channel2 = discord.utils.get(ctx.message.server.channels, name=namel2)
            
            if "_" in  channel1.name:
                newargg=raidboss.split("_")
                raidboss=newargg[1]
            
            cnttt=0
            BossmaxCP=30.0
            Bossoffset=30.0
            Bossslope=0.0
            Bosspeeps=0.0 
            print(raidboss)
            for rp in self.Bosstypes:
                if rp.upper()==raidboss.upper():
                    BossmaxCP=self.BossmaxCP[cnttt]
                    Bossemoji=self.Bossemoji[cnttt]
                    Bossoffset=self.Bossoffset[cnttt]
                    Bossslope=self.Bossslope[cnttt]*0.0
                    Bosspeeps=self.Bosspeeps[cnttt]*0.0    
                    break
                cnttt+=1
            print(Bossoffset)
            
            #Get the corresponding message from the other channel
            try:
                async for message2 in self.bot.logs_from(channel2, limit=50): #Gets a list of the last 500 messages in the channel 
                    if message2.content.startswith(message.content[0:15]):
                        break
            except:
                arr=10
            try:
                async for trigger in self.bot.logs_from(channel1, limit=50): #Gets a list of the last 500 messages in the channel 
                    if message2.content.startswith(message.content[0:15]):
                        break
            except:
                arr=10
                #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 0")
            #await self.bot.send_message(self.bot.get_channel(self.programid),message.content + " " +  message2.content)
            #Now that we have both messages, we need to tally all of the reactions
            #await self.bot.send_message(self.bot.get_channel(self.programid),message.content+" "+message2.content)
            art=1
            if art==1:
                print(self.valor)
                botmember = discord.utils.get(ctx.message.server.members, id=self.botid)
                RaidMan=discord.utils.get(ctx.message.server.roles, id=self.RaidManager)
                #Ranger=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
                #Milk=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
                #Moder=discord.utils.get(ctx.message.server.roles, id=self.POGOmod)
                Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
                Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
                Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
            #try:
                print(Valor.id)
                a=message
                argg=a.content.split('--> ')
                a2=argg[0].split("(Delay for 2 minutes")
                argg[0]=a2[0]
                #argg[0]=argg[0][0:16]
                #await self.bot.send_message(self.bot.get_channel(self.programid),"yt")
                #Get the list of users and their levels
                levelsum=0
                totalpeeps=0
                memberlist=""
                numdelay=0
                #instmem="```http\nINSTINCT: Levelsum="  #Use x at start of line
                #valomem="```diff\nVALOR: Levelsum="  #Use - at start of line was diff 
                #mystmem="```md\nMYSTIC: Levelsum="    #Use # at start of line
                instmem="__**INSTINCT:**__ Levelsum="  #Use x at start of line
                valomem="__**VALOR:**__ Levelsum="  #Use - at start of line was diff 
                mystmem="__**MYSTIC:**__ Levelsum="    #Use # at start of line
                instmemt=""
                valomemt=""
                mystmemt=""
                ninst=0
                nmyst=0
                nvalo=0
                linst=0
                lmyst=0
                lvalo=0
                RMname=""
                for xi in range(0,len(a.reactions)):
                    useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                    for yi in range(0,len(useri)):
                        namer=useri[yi]
                        #member = discord.utils.get(ctx.message.server.members, name=namer.name)
                        member = discord.utils.get(ctx.message.server.members, id=namer.id)
                        f=member.roles
                        team=""
                        
                        #if assiRM==0:
                        #    if Milk in f:
                        #        RMname=member.display_name
                        #        assiRM=1
                        if assiRM==0:
                            if RaidMan in f:
                                RMname=member.display_name
                                assiRM=1
                        #if assiRM==0:
                        #    if Ranger in f:
                        #        RMname=member.display_name
                        #        assiRM=1    
                        
                        #if assiRM==0:
                        #    if Moder in f:
                        #        RMname=member.display_name
                        #        assiRM=1
                        if Valor in f:
                            team=" Val. "
                        elif Mystic in f:
                            team=" Mys. "
                        elif Instinct in f:
                            team=" Ins. "
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer)
                        namer2=member.display_name+str(useri[yi].discriminator)
                        #namer3=namer.name+str(useri[yi].discriminator)
                        #print(namer2)
                        #print(namer3)
                        #print(namer.name)
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer2)
                        getuserlevel= int(await subf.getuserlevel(self,namer2))
                        #print(getuserlevel)
                        if getuserlevel==-1: #They havent entered it yet
                            if user==namer:
                                await self.bot.send_message(member,member.display_name+", would you mind heading over to #raid-alerts and typing %level XX (replace XX with your trainer level), please?")
                                #await self.bot.send_message(member,member.display_name+", would you mind entering your trainer level so I can see if you all can beat this raid boss? (Enter __**1**__-__**40**__)")
                                #tata=await self.bot.wait_for_message(timeout = 30, author = user)
                                #await subf.setlevel(self,reaction,tata.content,user)
                                #await self.bot.add_reaction(a,"item_pokeball:284615009299070976")
                                #await asyncio.sleep(0.01)
                                #await self.bot.remove_reaction(a,"item_pokeball:284615009299070976",botmember)
                                #except:
                                #    a=1
                            getuserlevel=0
                        print(getuserlevel)
                        if totalpeeps>0:
                            memberlist=memberlist 
                        totalpeeps+=1
                        cntt=0
                        levelsum+= getuserlevel#int(f[cntt].name[0:2])
                        try:
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum-getuserlevel
                                #memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->200"  + "\n"
                            else:                        
                                #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                                memberlist=memberlist
                        except:
                            memberlist=memberlist
                            #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                        clevel=getuserlevel
                        #try:
                        try:
                            isspecialactive=0
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum+400
                                memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->400"  + "\n"
                                isspecialactive=1
                            elif a.reactions[xi].emoji==self.delay:
                                levelsum=levelsum-int(clevel)
                                totalpeeps=totalpeeps-1
                                addlmess=' (Delayed) '
                                #Insert the delay code here
                                if numdelay==0:
                                    argg[0]=argg[0] + "(Delay for 2 minutes for "
                                else:
                                    argg[0]=argg[0] + "/"
                                argg[0]=argg[0] + member.display_name
                                numdelay=numdelay+1
                                isspecialactive=1
                                #memberlist=memberlist + member.display_name + addlmess + "     Level-" + clevel + "\n"
                        except:
                            rrr=1
                        fndemo=0
                        if isspecialactive==0:
                            #print(isspecialactive)
                            #if True:
                            try:
                                namer=member
                                for popdx in range(4):
                                #clevel=0
                                    if ((a.reactions[xi].emoji))==self.shadowid[popdx]: #one
                                        namer=member
                                        uname=namer.display_name
                                        uname=uname+str(namer.discriminator)
                                        uname=namer2
                                        #print(namer2)
                                        #print(uname)
                                        df = pd.read_excel('Shadows2' + "\\" + uname + 'shadow.xlsx')
                                        fndemo=1
                                        levelsum=levelsum-int(clevel)
                                        clevel=0
                                        clevel=df.iloc[0,popdx]
                                        tnum=int(df.iloc[1,popdx])
                                        if int(clevel)>0:
                                            levelsum=levelsum+clevel
                                            if tnum==2:
                                                nvalo+=1
                                                lvalo+=clevel
                                                valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==1:
                                                nmyst+=1
                                                lmyst+=clevel
                                                mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==0:
                                                ninst+=1
                                                linst+=clevel
                                                instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + str(clevel) + ") " + team + "\n"
                                        else:
                                            levelsum=levelsum+0
                                            if Valor in f:
                                                nvalo+=1
                                                lvalo+=0
                                                valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Mystic in f:
                                                nmyst+=1
                                                lmyst+=0
                                                mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Instinct in f:
                                                ninst+=1
                                                linst+=0
                                                instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + "<20" + ") " + team + "\n"
                                print(fndemo)
                                if fndemo==0:  
                                    #if namer2=="mikeko945239":
                                    #    ninst+=1
                                    #    linst+=clevel
                                    #    instmemt+="^**"+"MK4694"+"**"+" (" + str(clevel) + ")\n"
                                    #if member.display_name=="Haswari":
                                    #    nmyst+=1
                                    #    lmyst+=clevel
                                    #    mystmemt+="#**"+"Eranthus"+"**"+" (" + str(clevel) + ")\n"
                                    #print(member.display_name + str(clevel))
                                    if Valor in f:
                                        nvalo+=1
                                        lvalo+=clevel
                                        valomemt+="-**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                    elif Mystic in f:
                                        nmyst+=1
                                        lmyst+=clevel
                                        mystmemt+="#**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                    elif Instinct in f:
                                        ninst+=1
                                        linst+=clevel
                                        instmemt+="^**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                            #memberlist=memberlist + member.display_name + "     (" + str(clevel) + ") " + team + "\n"
                            #else:
                            except:
                                
                                if Valor in f:
                                    nvalo+=1
                                    lvalo+=0
                                    valomemt+="-**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                elif Mystic in f:
                                    nmyst+=1
                                    lmyst+=0
                                    mystmemt+="#**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                elif Instinct in f:
                                    ninst+=1
                                    linst+=0
                                    instmemt+="^**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                #memberlist=memberlist + member.display_name + "     (" + "<20" + ") " + team + "\n"
                            cntt=cntt+1
                a2=a
            else:
            #except:
                arr=10
            
                #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 2")    
            #await self.bot.send_message(self.bot.get_channel(self.programid),str(totalpeeps)+" "+str(numdelay)+" "+str(levelsum)+" ")  
            numpeeps=totalpeeps
            if numdelay>0:
                argg[0]=argg[0] + ")"
            
            if levelsum>0:
                #if raidlevel==5:
                crit=Bossoffset+(Bosspeeps-4)*Bossslope
                if levelsum>=1.0*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / HIGH CHANCE OF PASSING /' + str(numpeeps) + ' will attend'          
                elif levelsum>=0.80*crit and levelsum<1.00*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / REASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                elif levelsum>=0.60*crit and levelsum<0.80*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / UNREASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                else:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / GNAT''S WING CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
            else:
                newmsg=argg[0] + ""
            memberlist3=""
            memberlist4=""   
            if ninst>0:
                #memberlist3+=instmem+"("+str(linst)+")\n"+instmemt+"```"
                memberlist3+=instmem+"("+str(linst)+")\n"+instmemt#+"```"
            if nmyst>0:
                #memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt+"```"
                memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt#+"```"
            if nvalo>0:
                #memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt+"```" 
                memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt#+"```" 
            if not memberlist=="":
                #memberlist3+="```"+memberlist+"```"   
                memberlist3+=memberlist#+"```"
            if assiRM==1:
                if RMname=="MrDonGiovanni":
                    RMname="AJswagmaster420"
                if RMname=="MrMasterMiltank":
                    RMname="MilkMaid"
                #memberlist4="```Assigned RM: " + RMname + "```"
                memberlist4="__**Assigned RM: " + RMname + "**__\n"
            memberlist=memberlist4+memberlist3
            if memberlist=="" and numpeeps>0:
                memberlist=str(numpeeps) + ' will attend'
                #print(a.channel.name)
            newmsg=newmsg + "\n" + memberlist

            await self.bot.edit_message(a,new_content=str(newmsg))
            #REVERT to 02092018v2 if needed
            #Find maximum number of people
            maxrxn=0
            async for msg in self.bot.logs_from(a.channel, limit=500): #Gets a list of the last 500 messages in the channel 
                rxncnt=0
                if msg.content.startswith("@Start"):
                    for xi in range(0,len(msg.reactions)):
                        useri = await self.bot.get_reaction_users([x for x in msg.reactions][xi])
                        for yi in range(0,len(useri)):
                            rxncnt+=1
                    if rxncnt>maxrxn:
                        maxrxn=rxncnt
            
            orignameo=a.channel.name
            if "_" in a.channel.name: #Number of people is assigned
                lgh=a.channel.name.split("_")
                orignameo=lgh[1]
            lgh=orignameo.split("---")
            newnameo=lgh[0]+ self.chanstrsp +lgh[1]
            if maxrxn>0:
                print(""+str(maxrxn)+"_"+newnameo)
                await self.bot.edit_channel(a.channel, name=str(maxrxn)+"_"+newnameo)
            else:            
                print(newnameo)
                await self.bot.edit_channel(a.channel, name=newnameo)
            print(a.channel.name+"\n"+str(newmsg))
            return   
        else:
        #except:
            arrrg=10
        
        arp=1
        tmess=reaction.message
        if tmess.channel.id=="284575672716886016" or tmess.channel.id=="403550523984183296" or tmess.channel.id=="408330312125382656" or tmess.channel.id=="340254221918273536":
        #try:
            instmem="```http\n"  #Use x at start of line
            valomem="```diff\n"  #Use - at start of line 
            mystmem="```md\n"    #Use # at start of line
            ninst=0
            nmyst=0
            nvalo=0
            #Attempt to try single channel version
            #cnttt=0
            tmess=reaction.message
            a=tmess
            

            
            
            BossmaxCP=30.0
            Bossoffset=30.0
            Bossslope=0.0
            Bosspeeps=0.0 
            #for rp in self.Bosstypes:
            #    if rp.upper()==raidboss.upper():
            #        BossmaxCP=self.BossmaxCP[cnttt]
            #        Bossemoji=self.Bossemoji[cnttt]
            #        Bossoffset=self.Bossoffset[cnttt]
            #        Bossslope=self.Bossslope[cnttt]*0.0
            #        Bosspeeps=self.Bosspeeps[cnttt]*0.0    
            #        break
            #    cnttt+=1
            tmess=reaction.message
            message=tmess
            #Get the information about the raid channel
            if not tmess.content.startswith("__**RAID:**__"):
                return
            #    await self.bot.delete_message(message)
            art=1
            if art==1:
                ctx=reaction
                Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
                Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
                Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
                a=message
                argg=a.content.split('(Delay for 2 ')
                argg=argg[0].split('--> ')
                a2=argg[0].split("(Delay for 2 minutes")
                argg[0]=a2[0]
                #argg[0]=argg[0][0:16]

                #Get the list of users and their levels
                levelsum=0
                totalpeeps=0
                memberlist=""
                numdelay=0
                for xi in range(0,len(a.reactions)):
                    useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                    for yi in range(0,len(useri)):
                        namer=useri[yi]
                        member = discord.utils.get(ctx.message.server.members, name=namer.name)
                        f=member.roles
                        team=""
                        if Valor in f:
                            team=" Val. "
                        elif Mystic in f:
                            team=" Mys. "
                        elif Instinct in f:
                            team=" Ins. "
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer)
                        namer2=member.display_name+str(useri[yi].discriminator)
                        #print(namer2)
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer2)
                        getuserlevel= int(await subf.getuserlevel(self,namer2))
                        if getuserlevel==-1: #They havent entered it yet
                            if user==namer:
                                await self.bot.send_message(member,member.display_name+", would you mind entering your trainer level so I can see if you all can beat this raid boss? (Enter __**1**__-__**40**__)")
                                tata=await self.bot.wait_for_message(timeout = 30, author = user)
                                await subf.setlevel(self,reaction,tata.content,user)
                                await self.bot.add_reaction(a,"item_pokeball:284615009299070976")
                                await asyncio.sleep(0.01)
                                await self.bot.remove_reaction(a,"item_pokeball:284615009299070976",botmember)
                            getuserlevel=0
                        
                        if totalpeeps>0:
                            memberlist=memberlist 
                        totalpeeps+=1
                        cntt=0
                        levelsum+= getuserlevel#int(f[cntt].name[0:2])
                        try:
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum-getuserlevel
                                #memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->200"  + "\n"
                            else:                        
                                #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                                memberlist=memberlist
                        except:
                            memberlist=memberlist
                            #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                        clevel=getuserlevel
                        #try:
                        try:
                            isspecialactive=0
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum+400
                                memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->400"  + "\n"
                                isspecialactive=1
                            elif a.reactions[xi].emoji==self.delay:
                                levelsum=levelsum-int(clevel)
                                totalpeeps=totalpeeps-1
                                addlmess=' (Delayed) '
                                #Insert the delay code here
                                if numdelay==0:
                                    argg[0]=argg[0] + "(Delay for 2 minutes for "
                                else:
                                    argg[0]=argg[0] + "/"
                                argg[0]=argg[0] + member.display_name
                                numdelay=numdelay+1
                                isspecialactive=1
                                #memberlist=memberlist + member.display_name + addlmess + "     Level-" + clevel + "\n"
                        except:
                            rrr=1
                        fndemo=0
                        if isspecialactive==0:
                            try:
                                for popdx in range(4):
                                #clevel=0
                                    if ((a.reactions[xi].emoji))==self.shadowid[popdx]: #one
                                        uname=namer.display_name
                                        uname=uname+str(namer.discriminator)
                                        uname=namer2
                                        #print(uname)
                                        df = pd.read_excel('Shadows2' + "\\" + uname + 'shadow.xlsx')
                                        fndemo=1
                                        levelsum=levelsum-int(clevel)
                                        clevel=0
                                        clevel=df.iloc[0,popdx]
                                        tnum=int(df.iloc[1,popdx])
                                        if int(clevel)>0:
                                            levelsum=levelsum+clevel
                                            if tnum==2:
                                                nvalo+=1
                                                valomem+="-"+member.display_name+"-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==1:
                                                nmyst+=1
                                                mystmem+="#"+member.display_name+"-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==0:
                                                ninst+=1
                                                instmem+="^"+member.display_name+"-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + str(clevel) + ") " + team + "\n"
                                        else:
                                            levelsum=levelsum+0
                                            if Valor in f:
                                                nvalo+=1
                                                valomem+="-"+member.display_name+"-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Mystic in f:
                                                nmyst+=1
                                                mystmem+="#"+member.display_name+"-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Instinct in f:
                                                ninst+=1
                                                instmem+="^"+member.display_name+"-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + "<20" + ") " + team + "\n"
                                if fndemo==0:                        
                                    
                                    if Valor in f:
                                        nvalo+=1
                                        valomem+="-"+member.display_name+""+" (" + str(clevel) + ")\n"
                                    elif Mystic in f:
                                        nmyst+=1
                                        mystmem+="#"+member.display_name+""+" (" + str(clevel) + ")\n"
                                    elif Instinct in f:
                                        ninst+=1
                                        instmem+="^"+member.display_name+""+" (" + str(clevel) + ")\n"
                            #memberlist=memberlist + member.display_name + "     (" + str(clevel) + ") " + team + "\n"
                            except:
                                if Valor in f:
                                    nvalo+=1
                                    valomem+="-"+member.display_name+""+" (" + "<20" + ")\n"
                                elif Mystic in f:
                                    nmyst+=1
                                    mystmem+="#"+member.display_name+""+" (" + "<20" + ")\n"
                                elif Instinct in f:
                                    ninst+=1
                                    instmem+="^"+member.display_name+""+" (" + "<20" + ")\n"
                                #memberlist=memberlist + member.display_name + "     (" + "<20" + ") " + team + "\n"
                            cntt=cntt+1
                a2=a
            else:
                tt=1
        #else:    
        #except:
            #att=-1
            try:
                numpeeps=totalpeeps
                if numdelay>0:
                    argg[0]=argg[0] + ")"
                
                if levelsum>0:
                    #if raidlevel==5:
                    crit=Bossoffset+(Bosspeeps-4)*Bossslope
                    if levelsum>=1.0*crit:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / HIGH CHANCE OF PASSING /' + str(numpeeps) + ' will attend'          
                    elif levelsum>=0.80*crit and levelsum<1.00*crit:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / REASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                    elif levelsum>=0.60*crit and levelsum<0.80*crit:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / UNREASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                    else:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / GNAT''S WING CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                else:
                    newmsg=argg[0] + ""
                
                memberlist3=""
                
                if ninst>0:
                    memberlist3+=instmem+"\n```"
                if nmyst>0:
                    memberlist3+=mystmem+"\n```"
                if nvalo>0:
                    memberlist3+=valomem+"\n```" 
                if not memberlist=="":
                    memberlist3+="```"+memberlist+"```"   
                memberlist=memberlist3
                if memberlist=="" and numpeeps>0:
                    memberlist=str(numpeeps) + ' will attend'
                newmsg=newmsg + "\n" + memberlist
                #await self.bot.send_message(self.bot.get_channel(self.programid),newmsg+str(numpeeps))
                #try:
                await self.bot.edit_message(a,new_content=str(newmsg))
                #except:
                #    arr=10
                #    await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 3")
                try:
                    await self.bot.edit_message(a2,new_content=str(newmsg))
                except:
                    arr=10
                    #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 4")
                return 
            except:
                afarp=1
        
    @client.event
    async def on_reaction_remove(self,reaction,user):
        tmess=reaction.message 
       

        
        #print("Here")
        ################################################################
        ################################################################
        ########################THIS IS THE MEAT################################
        ################################################################
        ################################################################
        arr=10
        if tmess.channel.id in self.alllocch:
        #try:
            
            raidrestr=discord.utils.get(reaction.message.server.roles, id=self.raidrestr)
            #print (user.roles)
            if raidrestr in user.roles:
                await self.bot.remove_reaction(reaction.message,reaction.emoji,user)
                
                return
            assiRM=0
            raidlevel=5 #Use this in the meantime
            #print("Here")
            message=reaction.message
            if not message.content.startswith('@Start:'):
                return
            chnid=reaction.message.channel.id
            ctx=reaction
            chnam=reaction.message.channel.name
            #channel1=discord.utils.get(ctx.message.server.channels, id=channel_id)
            #chnam=channel1.name
            #chnid=channel1.id
            argg=chnam.split('---')
            found=await subf.findboss(self,chnid)
            
            #If the channel is a raid boss specific channel, the second channel will lead with the raid boss
            if found==1:
                raidboss=argg[1]
                location=argg[0]
                namel2=raidboss + "---" +  location
            else:
                raidboss=argg[0]
                location=argg[1]
                namel2=location + "---" +  raidboss
            
            #Get the two channels
            channel1=ctx.message.channel   
            channel2 = discord.utils.get(ctx.message.server.channels, name=namel2)
            
            if "_" in  channel1.name:
                newargg=raidboss.split("_")
                raidboss=newargg[1]
            
            cnttt=0
            BossmaxCP=30.0
            Bossoffset=30.0
            Bossslope=0.0
            Bosspeeps=0.0 
            print(raidboss)
            for rp in self.Bosstypes:
                if rp.upper()==raidboss.upper():
                    BossmaxCP=self.BossmaxCP[cnttt]
                    Bossemoji=self.Bossemoji[cnttt]
                    Bossoffset=self.Bossoffset[cnttt]
                    Bossslope=self.Bossslope[cnttt]*0.0
                    Bosspeeps=self.Bosspeeps[cnttt]*0.0    
                    break
                cnttt+=1
            print(Bossoffset)
            
            #Get the corresponding message from the other channel
            try:
                async for message2 in self.bot.logs_from(channel2, limit=50): #Gets a list of the last 500 messages in the channel 
                    if message2.content.startswith(message.content[0:15]):
                        break
            except:
                arr=10
            try:
                async for trigger in self.bot.logs_from(channel1, limit=50): #Gets a list of the last 500 messages in the channel 
                    if message2.content.startswith(message.content[0:15]):
                        break
            except:
                arr=10
                #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 0")
            #await self.bot.send_message(self.bot.get_channel(self.programid),message.content + " " +  message2.content)
            #Now that we have both messages, we need to tally all of the reactions
            #await self.bot.send_message(self.bot.get_channel(self.programid),message.content+" "+message2.content)
            art=1
            if art==1:
                print(self.valor)
                botmember = discord.utils.get(ctx.message.server.members, id=self.botid)
                RaidMan=discord.utils.get(ctx.message.server.roles, id=self.RaidManager)
                #Ranger=discord.utils.get(ctx.message.server.roles, id=self.Ranger)
                #Milk=discord.utils.get(ctx.message.server.roles, id=self.Milkmaid)
                #Moder=discord.utils.get(ctx.message.server.roles, id=self.POGOmod)
                Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
                Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
                Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
            #try:
                print(Valor.id)
                a=message
                argg=a.content.split('--> ')
                a2=argg[0].split("(Delay for 2 minutes")
                argg[0]=a2[0]
                #argg[0]=argg[0][0:16]
                #await self.bot.send_message(self.bot.get_channel(self.programid),"yt")
                #Get the list of users and their levels
                levelsum=0
                totalpeeps=0
                memberlist=""
                numdelay=0
                #instmem="```http\nINSTINCT: Levelsum="  #Use x at start of line
                #valomem="```diff\nVALOR: Levelsum="  #Use - at start of line was diff 
                #mystmem="```md\nMYSTIC: Levelsum="    #Use # at start of line
                instmem="__**INSTINCT:**__ Levelsum="  #Use x at start of line
                valomem="__**VALOR:**__ Levelsum="  #Use - at start of line was diff 
                mystmem="__**MYSTIC:**__ Levelsum="    #Use # at start of line
                instmemt=""
                valomemt=""
                mystmemt=""
                ninst=0
                nmyst=0
                nvalo=0
                linst=0
                lmyst=0
                lvalo=0
                RMname=""
                for xi in range(0,len(a.reactions)):
                    useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                    for yi in range(0,len(useri)):
                        namer=useri[yi]
                        #member = discord.utils.get(ctx.message.server.members, name=namer.name)
                        member = discord.utils.get(ctx.message.server.members, id=namer.id)
                        f=member.roles
                        team=""
                        
                        #if assiRM==0:
                        #    if Milk in f:
                        #        RMname=member.display_name
                        #        assiRM=1
                        if assiRM==0:
                            if RaidMan in f:
                                RMname=member.display_name
                                assiRM=1
                        #if assiRM==0:
                        #    if Ranger in f:
                        #        RMname=member.display_name
                        #        assiRM=1    
                        
                        #if assiRM==0:
                        #    if Moder in f:
                        #        RMname=member.display_name
                        #        assiRM=1
                        if Valor in f:
                            team=" Val. "
                        elif Mystic in f:
                            team=" Mys. "
                        elif Instinct in f:
                            team=" Ins. "
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer)
                        namer2=member.display_name+str(useri[yi].discriminator)
                        #namer3=namer.name+str(useri[yi].discriminator)
                        #print(namer2)
                        #print(namer3)
                        #print(namer.name)
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer2)
                        getuserlevel= int(await subf.getuserlevel(self,namer2))
                        #print(getuserlevel)
                        if getuserlevel==-1: #They havent entered it yet
                            if user==namer:
                                await self.bot.send_message(member,member.display_name+", would you mind heading over to #raid-alerts and typing %level XX (replace XX with your trainer level), please?")
                                #await self.bot.send_message(member,member.display_name+", would you mind entering your trainer level so I can see if you all can beat this raid boss? (Enter __**1**__-__**40**__)")
                                #tata=await self.bot.wait_for_message(timeout = 30, author = user)
                                #await subf.setlevel(self,reaction,tata.content,user)
                                #await self.bot.add_reaction(a,"item_pokeball:284615009299070976")
                                #await asyncio.sleep(0.01)
                                #await self.bot.remove_reaction(a,"item_pokeball:284615009299070976",botmember)
                                #except:
                                #    a=1
                            getuserlevel=0
                        print(getuserlevel)
                        if totalpeeps>0:
                            memberlist=memberlist 
                        totalpeeps+=1
                        cntt=0
                        levelsum+= getuserlevel#int(f[cntt].name[0:2])
                        try:
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum-getuserlevel
                                #memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->200"  + "\n"
                            else:                        
                                #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                                memberlist=memberlist
                        except:
                            memberlist=memberlist
                            #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                        clevel=getuserlevel
                        #try:
                        try:
                            isspecialactive=0
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum+400
                                memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->400"  + "\n"
                                isspecialactive=1
                            elif a.reactions[xi].emoji==self.delay:
                                levelsum=levelsum-int(clevel)
                                totalpeeps=totalpeeps-1
                                addlmess=' (Delayed) '
                                #Insert the delay code here
                                if numdelay==0:
                                    argg[0]=argg[0] + "(Delay for 2 minutes for "
                                else:
                                    argg[0]=argg[0] + "/"
                                argg[0]=argg[0] + member.display_name
                                numdelay=numdelay+1
                                isspecialactive=1
                                #memberlist=memberlist + member.display_name + addlmess + "     Level-" + clevel + "\n"
                        except:
                            rrr=1
                        fndemo=0
                        if isspecialactive==0:
                            #print(isspecialactive)
                            #if True:
                            try:
                                namer=member
                                for popdx in range(4):
                                #clevel=0
                                    if ((a.reactions[xi].emoji))==self.shadowid[popdx]: #one
                                        namer=member
                                        uname=namer.display_name
                                        uname=uname+str(namer.discriminator)
                                        uname=namer2
                                        #print(namer2)
                                        #print(uname)
                                        df = pd.read_excel('Shadows2' + "\\" + uname + 'shadow.xlsx')
                                        fndemo=1
                                        levelsum=levelsum-int(clevel)
                                        clevel=0
                                        clevel=df.iloc[0,popdx]
                                        tnum=int(df.iloc[1,popdx])
                                        if int(clevel)>0:
                                            levelsum=levelsum+clevel
                                            if tnum==2:
                                                nvalo+=1
                                                lvalo+=clevel
                                                valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==1:
                                                nmyst+=1
                                                lmyst+=clevel
                                                mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==0:
                                                ninst+=1
                                                linst+=clevel
                                                instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + str(clevel) + ") " + team + "\n"
                                        else:
                                            levelsum=levelsum+0
                                            if Valor in f:
                                                nvalo+=1
                                                lvalo+=0
                                                valomemt+="-**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Mystic in f:
                                                nmyst+=1
                                                lmyst+=0
                                                mystmemt+="#**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Instinct in f:
                                                ninst+=1
                                                linst+=0
                                                instmemt+="^**"+member.display_name+"**-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + "<20" + ") " + team + "\n"
                                print(fndemo)
                                if fndemo==0:  
                                    #if namer2=="mikeko945239":
                                    #    ninst+=1
                                    #    linst+=clevel
                                    #    instmemt+="^**"+"MK4694"+"**"+" (" + str(clevel) + ")\n"
                                    #if member.display_name=="Haswari":
                                    #    nmyst+=1
                                    #    lmyst+=clevel
                                    #    mystmemt+="#**"+"Eranthus"+"**"+" (" + str(clevel) + ")\n"
                                    #print(member.display_name + str(clevel))
                                    if Valor in f:
                                        nvalo+=1
                                        lvalo+=clevel
                                        valomemt+="-**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                    elif Mystic in f:
                                        nmyst+=1
                                        lmyst+=clevel
                                        mystmemt+="#**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                                    elif Instinct in f:
                                        ninst+=1
                                        linst+=clevel
                                        instmemt+="^**"+member.display_name+"**"+" (" + str(clevel) + ")\n"
                            #memberlist=memberlist + member.display_name + "     (" + str(clevel) + ") " + team + "\n"
                            #else:
                            except:
                                
                                if Valor in f:
                                    nvalo+=1
                                    lvalo+=0
                                    valomemt+="-**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                elif Mystic in f:
                                    nmyst+=1
                                    lmyst+=0
                                    mystmemt+="#**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                elif Instinct in f:
                                    ninst+=1
                                    linst+=0
                                    instmemt+="^**"+member.display_name+"**"+" (" + "<20" + ")\n"
                                #memberlist=memberlist + member.display_name + "     (" + "<20" + ") " + team + "\n"
                            cntt=cntt+1
                a2=a
            else:
            #except:
                arr=10
            
                #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 2")    
            #await self.bot.send_message(self.bot.get_channel(self.programid),str(totalpeeps)+" "+str(numdelay)+" "+str(levelsum)+" ")  
            numpeeps=totalpeeps
            if numdelay>0:
                argg[0]=argg[0] + ")"
            
            if levelsum>0:
                #if raidlevel==5:
                crit=Bossoffset+(Bosspeeps-4)*Bossslope
                if levelsum>=1.0*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / HIGH CHANCE OF PASSING /' + str(numpeeps) + ' will attend'          
                elif levelsum>=0.80*crit and levelsum<1.00*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / REASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                elif levelsum>=0.60*crit and levelsum<0.80*crit:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / UNREASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                else:
                    newmsg=argg[0] + '--> \nLevel Sum = '+ str(levelsum) +' / GNAT''S WING CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
            else:
                newmsg=argg[0] + ""
            memberlist3=""
            memberlist4=""   
            if ninst>0:
                #memberlist3+=instmem+"("+str(linst)+")\n"+instmemt+"```"
                memberlist3+=instmem+"("+str(linst)+")\n"+instmemt#+"```"
            if nmyst>0:
                #memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt+"```"
                memberlist3+=mystmem+"("+str(lmyst)+")\n"+mystmemt#+"```"
            if nvalo>0:
                #memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt+"```" 
                memberlist3+=valomem+"("+str(lvalo)+")\n"+valomemt#+"```" 
            if not memberlist=="":
                #memberlist3+="```"+memberlist+"```"   
                memberlist3+=memberlist#+"```"
            if assiRM==1:
                if RMname=="MrDonGiovanni":
                    RMname="AJswagmaster420"
                if RMname=="MrMasterMiltank":
                    RMname="MilkMaid"
                #memberlist4="```Assigned RM: " + RMname + "```"
                memberlist4="__**Assigned RM: " + RMname + "**__\n"
            memberlist=memberlist4+memberlist3
            if memberlist=="" and numpeeps>0:
                memberlist=str(numpeeps) + ' will attend'
                #print(a.channel.name)
            newmsg=newmsg + "\n" + memberlist

            await self.bot.edit_message(a,new_content=str(newmsg))
            #REVERT to 02092018v2 if needed
            #Find maximum number of people
            maxrxn=0
            async for msg in self.bot.logs_from(a.channel, limit=500): #Gets a list of the last 500 messages in the channel 
                rxncnt=0
                if msg.content.startswith("@Start"):
                    for xi in range(0,len(msg.reactions)):
                        useri = await self.bot.get_reaction_users([x for x in msg.reactions][xi])
                        for yi in range(0,len(useri)):
                            rxncnt+=1
                    if rxncnt>maxrxn:
                        maxrxn=rxncnt
            
            orignameo=a.channel.name
            if "_" in a.channel.name: #Number of people is assigned
                lgh=a.channel.name.split("_")
                orignameo=lgh[1]
            lgh=orignameo.split("---")
            newnameo=lgh[0]+ self.chanstrsp +lgh[1]
            if maxrxn>0:
                print(""+str(maxrxn)+"_"+newnameo)
                await self.bot.edit_channel(a.channel, name=str(maxrxn)+"_"+newnameo)
            else:            
                print(newnameo)
                await self.bot.edit_channel(a.channel, name=newnameo)
            print(a.channel.name+"\n"+str(newmsg))
            return   
        else:
        #except:
            arrrg=10
        
        arp=1
        tmess=reaction.message
        if tmess.channel.id=="284575672716886016" or tmess.channel.id=="403550523984183296" or tmess.channel.id=="408330312125382656" or tmess.channel.id=="340254221918273536":
        #try:
            instmem="```http\n"  #Use x at start of line
            valomem="```diff\n"  #Use - at start of line 
            mystmem="```md\n"    #Use # at start of line
            ninst=0
            nmyst=0
            nvalo=0
            #Attempt to try single channel version
            #cnttt=0
            tmess=reaction.message
            a=tmess
            

            
            
            BossmaxCP=30.0
            Bossoffset=30.0
            Bossslope=0.0
            Bosspeeps=0.0 
            #for rp in self.Bosstypes:
            #    if rp.upper()==raidboss.upper():
            #        BossmaxCP=self.BossmaxCP[cnttt]
            #        Bossemoji=self.Bossemoji[cnttt]
            #        Bossoffset=self.Bossoffset[cnttt]
            #        Bossslope=self.Bossslope[cnttt]*0.0
            #        Bosspeeps=self.Bosspeeps[cnttt]*0.0    
            #        break
            #    cnttt+=1
            tmess=reaction.message
            message=tmess
            #Get the information about the raid channel
            if not tmess.content.startswith("__**RAID:**__"):
                return
            #    await self.bot.delete_message(message)
            art=1
            if art==1:
                ctx=reaction
                Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
                Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
                Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
                a=message
                argg=a.content.split('(Delay for 2 ')
                argg=argg[0].split('--> ')
                a2=argg[0].split("(Delay for 2 minutes")
                argg[0]=a2[0]
                #argg[0]=argg[0][0:16]

                #Get the list of users and their levels
                levelsum=0
                totalpeeps=0
                memberlist=""
                numdelay=0
                for xi in range(0,len(a.reactions)):
                    useri = await self.bot.get_reaction_users([x for x in a.reactions][xi])
                    for yi in range(0,len(useri)):
                        namer=useri[yi]
                        member = discord.utils.get(ctx.message.server.members, name=namer.name)
                        f=member.roles
                        team=""
                        if Valor in f:
                            team=" Val. "
                        elif Mystic in f:
                            team=" Mys. "
                        elif Instinct in f:
                            team=" Ins. "
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer)
                        namer2=member.display_name+str(useri[yi].discriminator)
                        #print(namer2)
                        #await self.bot.send_message(self.bot.get_channel(self.programid),namer2)
                        getuserlevel= int(await subf.getuserlevel(self,namer2))
                        if getuserlevel==-1: #They havent entered it yet
                            if user==namer:
                                await self.bot.send_message(member,member.display_name+", would you mind entering your trainer level so I can see if you all can beat this raid boss? (Enter __**1**__-__**40**__)")
                                tata=await self.bot.wait_for_message(timeout = 30, author = user)
                                await subf.setlevel(self,reaction,tata.content,user)
                                await self.bot.add_reaction(a,"item_pokeball:284615009299070976")
                                await asyncio.sleep(0.01)
                                await self.bot.remove_reaction(a,"item_pokeball:284615009299070976",botmember)
                            getuserlevel=0
                        
                        if totalpeeps>0:
                            memberlist=memberlist 
                        totalpeeps+=1
                        cntt=0
                        levelsum+= getuserlevel#int(f[cntt].name[0:2])
                        try:
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum-getuserlevel
                                #memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->200"  + "\n"
                            else:                        
                                #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                                memberlist=memberlist
                        except:
                            memberlist=memberlist
                            #memberlist=memberlist + member.display_name + "     Level-" + clevel + "\n"
                        clevel=getuserlevel
                        #try:
                        try:
                            isspecialactive=0
                            if a.reactions[xi].emoji==self.train or a.reactions[xi].emoji==self.train2 or a.reactions[xi].emoji==self.train3 or a.reactions[xi].emoji==self.train4 or a.reactions[xi].emoji==self.train5:
                                levelsum=levelsum+400
                                memberlist=memberlist + "RAID TRAIN/PAIN TRAIN" + "     Level->400"  + "\n"
                                isspecialactive=1
                            elif a.reactions[xi].emoji==self.delay:
                                levelsum=levelsum-int(clevel)
                                totalpeeps=totalpeeps-1
                                addlmess=' (Delayed) '
                                #Insert the delay code here
                                if numdelay==0:
                                    argg[0]=argg[0] + "(Delay for 2 minutes for "
                                else:
                                    argg[0]=argg[0] + "/"
                                argg[0]=argg[0] + member.display_name
                                numdelay=numdelay+1
                                isspecialactive=1
                                #memberlist=memberlist + member.display_name + addlmess + "     Level-" + clevel + "\n"
                        except:
                            rrr=1
                        fndemo=0
                        if isspecialactive==0:
                            try:
                                for popdx in range(4):
                                #clevel=0
                                    if ((a.reactions[xi].emoji))==self.shadowid[popdx]: #one
                                        uname=namer.display_name
                                        uname=uname+str(namer.discriminator)
                                        uname=namer2
                                        #print(uname)
                                        df = pd.read_excel('Shadows2' + "\\" + uname + 'shadow.xlsx')
                                        fndemo=1
                                        levelsum=levelsum-int(clevel)
                                        clevel=0
                                        clevel=df.iloc[0,popdx]
                                        tnum=int(df.iloc[1,popdx])
                                        if int(clevel)>0:
                                            levelsum=levelsum+clevel
                                            if tnum==2:
                                                nvalo+=1
                                                valomem+="-"+member.display_name+"-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==1:
                                                nmyst+=1
                                                mystmem+="#"+member.display_name+"-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            elif tnum==0:
                                                ninst+=1
                                                instmem+="^"+member.display_name+"-"+str(popdx+1)+" (" + str(clevel) + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + str(clevel) + ") " + team + "\n"
                                        else:
                                            levelsum=levelsum+0
                                            if Valor in f:
                                                nvalo+=1
                                                valomem+="-"+member.display_name+"-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Mystic in f:
                                                nmyst+=1
                                                mystmem+="#"+member.display_name+"-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            elif Instinct in f:
                                                ninst+=1
                                                instmem+="^"+member.display_name+"-"+str(popdx+1)+" (" + "<20" + ")\n"
                                            #memberlist=memberlist + member.display_name + "-"+str(popdx+1)+"     (" + "<20" + ") " + team + "\n"
                                if fndemo==0:                        
                                    
                                    if Valor in f:
                                        nvalo+=1
                                        valomem+="-"+member.display_name+""+" (" + str(clevel) + ")\n"
                                    elif Mystic in f:
                                        nmyst+=1
                                        mystmem+="#"+member.display_name+""+" (" + str(clevel) + ")\n"
                                    elif Instinct in f:
                                        ninst+=1
                                        instmem+="^"+member.display_name+""+" (" + str(clevel) + ")\n"
                            #memberlist=memberlist + member.display_name + "     (" + str(clevel) + ") " + team + "\n"
                            except:
                                if Valor in f:
                                    nvalo+=1
                                    valomem+="-"+member.display_name+""+" (" + "<20" + ")\n"
                                elif Mystic in f:
                                    nmyst+=1
                                    mystmem+="#"+member.display_name+""+" (" + "<20" + ")\n"
                                elif Instinct in f:
                                    ninst+=1
                                    instmem+="^"+member.display_name+""+" (" + "<20" + ")\n"
                                #memberlist=memberlist + member.display_name + "     (" + "<20" + ") " + team + "\n"
                            cntt=cntt+1
                a2=a
            else:
                tt=1
        #else:    
        #except:
            #att=-1
            try:
                numpeeps=totalpeeps
                if numdelay>0:
                    argg[0]=argg[0] + ")"
                
                if levelsum>0:
                    #if raidlevel==5:
                    crit=Bossoffset+(Bosspeeps-4)*Bossslope
                    if levelsum>=1.0*crit:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / HIGH CHANCE OF PASSING /' + str(numpeeps) + ' will attend'          
                    elif levelsum>=0.80*crit and levelsum<1.00*crit:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / REASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                    elif levelsum>=0.60*crit and levelsum<0.80*crit:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / UNREASONABLE CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                    else:
                        newmsg=argg[0] + '--> Level Sum = '+ str(levelsum) +' / GNAT''S WING CHANCE OF PASSING /' + str(numpeeps) + ' will attend'
                else:
                    newmsg=argg[0] + ""
                
                memberlist3=""
                
                if ninst>0:
                    memberlist3+=instmem+"\n```"
                if nmyst>0:
                    memberlist3+=mystmem+"\n```"
                if nvalo>0:
                    memberlist3+=valomem+"\n```" 
                if not memberlist=="":
                    memberlist3+="```"+memberlist+"```"   
                memberlist=memberlist3
                if memberlist=="" and numpeeps>0:
                    memberlist=str(numpeeps) + ' will attend'
                newmsg=newmsg + "\n" + memberlist
                #await self.bot.send_message(self.bot.get_channel(self.programid),newmsg+str(numpeeps))
                #try:
                await self.bot.edit_message(a,new_content=str(newmsg))
                #except:
                #    arr=10
                #    await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 3")
                try:
                    await self.bot.edit_message(a2,new_content=str(newmsg))
                except:
                    arr=10
                    #await self.bot.send_message(self.bot.get_channel(self.programid),"Failed on 4")
                return 
            except:
                afarp=1  

    @commands.command(pass_context=True)
    async def raidstore(self, ctx):
        Valor=discord.utils.get(ctx.message.server.roles, id=self.valor)
        Mystic=discord.utils.get(ctx.message.server.roles, id=self.mystic)
        Instinct=discord.utils.get(ctx.message.server.roles, id=self.instinct)
        await subf.storedata(self,Valor,Mystic,Instinct)
    
    @commands.command(pass_context=True)
    async def joindate(self,ctx,user): 
        await self.bot.delete_message(ctx.message)
        #rolePS = discord.utils.get(ctx.message.server.roles, id=self.SilentPS)
        #roleL3 = discord.utils.get(ctx.message.server.roles, id=self.SilentL3)
        #roleL4 = discord.utils.get(ctx.message.server.roles, id=self.SilentL4)
        #roleL5 = discord.utils.get(ctx.message.server.roles, id=self.SilentL5)
        #await self.bot.send_message(
        ar=ctx.message.mentions
        userf=discord.Server.get_member(ctx.message.server,ar[0].id)
        #print(userf.id)
        #member = discord.utils.get(ctx.message.server.members, name=ctx.message.author.name)
        #b=discord.Server.get_member(ctx.message.server,ctx.message.author.id)
        await self.bot.send_message(ctx.message.channel,userf.display_name + " joined the PurdueMon Discord on " + userf.joined_at.strftime("%d %b %Y %H:%M:%S"))
    
    #Allow admins to pre-emptively block a user from joining the server
    #Ready for publication
    @checks.mod()
    @commands.command(pass_context=True)  
    async def pollsterban(self, ctx, user_id: int, *, reason: str = None):
        """Preemptively bans user from the server

        A user ID needs to be provided, but you must also kick the member to make this all work
        """
        user_id = str(user_id)
        author = ctx.message.author
        server = author.server
        
        #append the user to banned list
        self.bannedlist.append(user_id)
        
        #only keep unique IDs
        ulist=[]
        for x in self.bannedlist:
            if x not in ulist:
                ulist.append(x) 
        
        self.bannedlist=ulist
        print(self.bannedlist)
        
        #Need to write the bannedlist file
        file = open("configuration/bannedlist.json","w",encoding='utf-8')
        txt='{\n  "bannedlist" : ["'
        lenlist=len(self.bannedlist)
        for x in range(0,lenlist):
            txt+=self.bannedlist[x] + '","'
        txt=txt[:-2]+"]\n}"
        
        file.write(txt)
        file.close()
        
        await self.bot.send_message(ctx.message.channel,"I have banned the user with ID " + user_id + " from rejoining this server.")        
    
    #Allow admins to increase the level of a trainer beyond level 40, for showing off purposes
    #Ready for publication
    @checks.admin() #Must be admin or higher
    @commands.command(pass_context=True)    
    async def higherlevelxx(self,ctx,user,level):
        if "!" in user:
            userf=discord.Server.get_member(ctx.message.server,user[3:len(user)-1])
        else:
            userf=discord.Server.get_member(ctx.message.server,user[2:len(user)-1])
        arapr=1  #flag to allow entry, set to zero to deactivate
        if arapr==1:
            if not (ctx.message.channel.id==self.setupch):  #Only allow admins to enter this in the setup channel
                axp=1
            uname=userf.name+userf.discriminator #message.author.display_name

            arapr=1  #flag to allow entry, set to zero to deactivate
            if arapr==1:
            #try:
                newlev=float(level)
                newlev=int(newlev)
                posid=min(50,max(newlev,1))
                if (ctx.message.author.display_name=="MrMasterMiltank"):  #For personal usage  LOL
                    posid=min(1000,max(newlev,1))
                #open the sheet and see if the person exists
                try: #If the sheet exists, open it 
                    df = pd.read_excel('ExcelFiles' + "\\" + uname + 'level.xlsx')
                    currlev=df.iloc[0,0]
                    df.loc[0]=posid    
                    writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    await self.bot.send_message(ctx.message.channel,userf.name +", your level has been changed from " + str(currlev) + " to " + str(posid))
                except: #The person hasn't established a level yet
                    df = pd.read_excel('ExcelFiles' + "\\" + 'level' + '.xlsx')
                    df.loc[0]=posid    
                    writer = pd.ExcelWriter('ExcelFiles' + "\\" +uname + 'level.xlsx', engine='xlsxwriter')    
                    df.to_excel(writer, sheet_name='Sheet1',index=False)
                    workbook  = writer.book
                    worksheet = writer.sheets['Sheet1']
                    # Close the Pandas Excel writer and output the Excel file.
                    writer.save()
                    await self.bot.send_message(ctx.message.channel,userf.name +", your new assigned level is " + str(posid))
            #except:
            else:
                await self.bot.send_message(ctx.message.channel,userf.name +", please stop being an idiot and enter a number already!")
        else:
        #except:
            arpr=10
    
    #Use this command to send a message to anyone who reacted to a particular message
    #Command ready for publication
    @checks.admin() #Must be admin or higher
    @commands.command(pass_context=True)
    async def sendrxnmess(self,ctx,msgid,*, messtxt : str): 
        await self.bot.delete_message(ctx.message)
        msgid1 = await self.bot.get_message(ctx.message.channel,msgid)
        msgtxt=""
        memlist=[]
        for xi in range(0,len(msgid1.reactions)):
            useri = await self.bot.get_reaction_users([x for x in msgid1.reactions][xi])
            for yi in range(0,len(useri)):
                namer=useri[yi]
                member = discord.utils.get(ctx.message.server.members, name=namer.name)
                memlist.append(member)
        
        uniqemo=[]
        for x in memlist:
            if x not in uniqemo:
                uniqemo.append(x) 
        memlist=uniqemo
        
        #Now compile the message
        for x in memlist:
            msgtxt += x.mention
        msgtxt+= "\n\n" + messtxt
        
        await self.bot.send_message(ctx.message.channel,msgtxt)
    
    #This function lists all trainers in the discord (i.e. Unapproved).
    #Command ready for publication
    @checks.admin() #Must be admin or higher
    @commands.command(pass_context=True)
    async def listtrainers(self,ctx): 
        await self.bot.delete_message(ctx.message)
        Approved=discord.utils.get(ctx.message.server.roles, id=self.Approved)
        for member in ctx.message.server.members:
            userf=member
            if not Approved in userf.roles:
                await self.bot.send_message(ctx.message.channel,userf.display_name + " joined the " + self.servername + " on " + userf.joined_at.strftime("%d %b %Y %H:%M:%S"))
    
    #This function only works with a proper Google API key.  This is not provided.
    #Command ready for publication
    @commands.command(pass_context=True)
    async def addlookup(self,ctx,*, newmsg : str): 
        return
        geolocator = Nominatim()
        R = 6373.0

        print(newmsg)
        geolocator = GoogleV3(format_string="%s, Lafayette IN")
        location = geolocator.geocode(newmsg)
        print(location.address)
        latitude=location.latitude
        longitude=location.longitude
        print(str(latitude) + " " + str(longitude))
        #Now search for the closest pokestop
        cntt=0
        tarr=[]
        for y in self.stoplat:
            tarr.append(float(y))
        dist=np.array(tarr)
        for y in self.stoplat:
            gymlat=float(self.stoplat[cntt])
            gymlon=float(self.stoplon[cntt])
            lat1 = radians(gymlat)
            lon1 = radians(gymlon)
            lat2 = radians(latitude)
            lon2 = radians(longitude)

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            #distance = R * c

            
            dist[cntt]=R * c #((gymlat-latitude)*(gymlat-latitude)+(gymlon-longitude)*(gymlon-longitude))**0.5
            print(dist[cntt])
            cntt+=1
        minr=dist.argsort()[:10]
        msgtxt=""
        for x in range(0,9):
            dr=dist[minr[x]]*1609.34
            msgtxt+=self.stopnam[minr[x]] + " - " + "%.2f" % dr + " m\n"
        
        await self.bot.send_message(ctx.message.channel,msgtxt)
    
    #Acquire a list of not approved members and print to the console
    #Command ready for publication
    @checks.admin() #Must be admin or higher
    @commands.command(pass_context=True)
    async def plist(self,ctx): 
        roleApp= discord.utils.get(ctx.message.server.roles, id=self.Approved)
        for f in ctx.message.server.members:
            if not f==None:
                if any(xpp == roleApp for xpp in f.roles): #Member is approved, do nothing
                    a=1
                else:  #Append the use to the list of non-approved members
                    polltime = datetime.utcnow()+timedelta(hours=self.timez)
                    tpolltime=polltime.strftime("%d %b %Y %H:%M:%S")
                    tdeltat = datetime.strptime(tpolltime,"%d %b %Y %H:%M:%S")-datetime.strptime(f.joined_at.strftime("%d %b %Y %H:%M:%S"),"%d %b %Y %H:%M:%S")
                    print("Not Appr@"+f.display_name+" "+str(tdeltat.days))

        
def setup(bot):
    n = ballzy(bot)
    bot.add_cog(n)
    #bot.loop.create_task(ballzy.checkraidbuffer())
    


