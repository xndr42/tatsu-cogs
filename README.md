## Installation
1. Download Red-DiscordBot and follow their installation instructions: https://github.com/Twentysix26/Red-DiscordBot
2. Copy the "celestial.py" folder to the "cogs" directory of your bot.
3. To see if the cog was auto-loaded type: `[p]cogs`
4. If the module was not loaded, type: `[p]load celestial`

`Note: [p] is whatever prefix you setup with your bot.`

## Usage
Once the bot is in your server, use the following command to start the timer:  
`[p]countdown next_boss month day hour minute second order`  

`Note: [p] is whatever prefix you setup with your bot.`

***
`next_boss` is the next boss that should spawn in your rotation. The following values are valid:
```
0 = Aomak Temple
1 = Excavation Site
2 = Croxar Camp
3 = Unknown
```
If your rotation is not following the standard pattern, it might be best to set it as unknown.  
It will stay as unknown until you create a new countdown when the order stabilizes.  
***
`month/day/hour/minute/second` is the time of any known previous spawn.  
Use 24hr notation (3pm = 15, 9pm = 21, etc)  
***  
`order` is the rotation order of the bosses.
```
cw = clockwise
ccw = counter-clockwise
```


## Where users can get help with the project
[Click here to join our discord](https://discord.me/cbc).


Ask either Tatsu or Uki in the discord!

## Who maintains and contributes to the project
Tatsu/Uki
