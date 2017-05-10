from discord.ext import commands
import asyncio
import datetime
import time
class celestial:
    """BNS Celestial Basin Countdown Timer"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    
    #param i_str = previous boss (0 = Aomak, 1 = Excavation, 2 = Snapjaw
    #param month_str, day_str, hour_str, min_str are month/day/hour/minute of any previous boss spawn
    async def countdown(self, ctx, i_str, month_str, day_str, hour_str, min_str, min_sec, order):

        ############## CHANGE ONLY THESE VARIABLES TO SUIT YOUR NEEDS #####################
        #String to hold the names of your server group
        SERVER = "Mushin/OMC"
        #
        #String to hold your name so people can message you if something goes wrong
        OWNER = "Tatsu"
        ####################################################################################

        #Length of time between boss spawns 43min (in seconds)
        BOSS_CD = 2580
        
        #List to hold boss names
        #boss = ["Aomak", "Excavation", "Croxar"]
        boss = ["Aomak Temple", "Excavation Site", "Croxar Camp", "Unknown"]
        
        #Convert boss identifier to integer
        i = int(i_str)
        
        #Initial countdown message that bot will edit continuously
        countdown_msg = await self.bot.say("```css" + "\n" + "[" + boss[i] + "] - [" + SERVER + "] " + "\nTimer: xx minutes ```")

        #Time of the previous boss spawn
        known_spawn = datetime.datetime(year=2017, month=int(month_str), day=int(day_str), hour=int(hour_str), minute=int(min_str), second=int(min_sec))

        #Infinite loop because I don't want to do conditionals with datetime
        while True:
            
            #Figure out current time
            now = datetime.datetime.now()

            #Flag to keep track if spawn_msg was successfully created
            #Timer sometimes jumps past 180 so we need some leeway
            #But we don't want multiple messages
            flag = -1

            #Keep going until timer <= 2 then break out
            while True:

                #Figure out current time
                now = datetime.datetime.now()

                #Figure out how many minutes and seconds are remaining and current boss
                cur_min = (BOSS_CD - ((now - known_spawn).seconds) % BOSS_CD) // 60
                cur_sec = (BOSS_CD - ((now - known_spawn).seconds) % BOSS_CD) % 60
                time_left = (cur_min * 60) + cur_sec
                
                #Give 5min or 3min warning depending on if we know boss rotation or not
                if i == 3:
                    if time_left <= 300:
                        if flag == -1:
                            spawn_msg = await self.bot.say("@here " + boss[i] + " spawning in 5 minutes! (if order is wrong PM " + OWNER + ")")
                            flag = 0
                else:
                    if time_left <= 180:
                        if flag == -1:
                            spawn_msg = await self.bot.say("@here " + boss[i] + " spawning in 3 minutes! (if order is wrong PM " + OWNER + ")")
                            flag = 0

                #If the boss has spawned, then move boss index accordingly and delete notification message
                #Timer sometimes jumps over 0s so we need some leeway
                #If we enter early, make sure we don't leave early
                if time_left <= 2:
                    await self.bot.delete_message(spawn_msg)
                    time.sleep(2)
                    break

                #Have to subtract the seconds in our minutes from our total seconds
                await self.bot.edit_message(countdown_msg, new_content=("```css" + "\n" + "[" + boss[i] + "] - [" + SERVER + "] " + "\nTimer: " + str(cur_min) + " minutes and " + str(cur_sec) + " seconds  ```"))
                await asyncio.sleep(1)

            #Move boss index accordingly
            #Assumed counter-clockwise unless stated otherwise
            if order.lower() == 'cw':
                if i == 0:
                    i = 2
                elif i == 3:
                    i = 3
                else:
                    i -= 1
            else:
                if i == 2:
                    i = 0
                elif i == 3:
                    i = 3
                else:
                    i += 1

def setup(bot):
    bot.add_cog(celestial(bot))
