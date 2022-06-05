import discord
import random
from random import randrange
from discord.ext import commands
import discord.ext
import re

periodsFound = 0
emptyList = []
TOKEN = ""##insert token here

client = discord.Client()

IPembed = discord.Embed(title="IP detected",
                      description="Your message has been detected as an ip! Uh oh!",
                      color=0xFF5733)
linkEmbed = discord.Embed(title="Invite detected",
                          description="Your message has been detected as discord link stop advertising",
                                      color=0xFF5733)

#responses for 8ball
responsesball = [
    "No",
    "Not Likely",
    "I wouldn't advise it",
    "Yes",
    "Do it quickly",
    "I am in your walls",
    "Very likely",
]

regex = "[0-9]+\."


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "discord.gg/" in message.content:#removes any discord links
        await message.delete()
        await message.channel.send(embed=linkEmbed)


    if "." in message.content and "1" in message.content or "." in message.content and "2" in message.content or "." in message.content and "3" in message.content or "." in message.content and "4" in message.content or "." in message.content and "5" in message.content or "." in message.content and "6" in message.content or "." in message.content and "7" in message.content or "." in message.content and "8" in message.content or "." in message.content and "9" in message.content:
        periodsFound = 0
        for m in re.finditer('.', message.content):
            periodsFound += 1
        if periodsFound == 13:
            match = re.findall(regex, message.content)
            if match != emptyList:
                if len(match) == 3:
                    await message.delete()
                    await message.channel.send(embed=IPembed)


    if message.content.startswith("(ping"):
        await message.channel.send("pong")

    if message.content.startswith("(say"):
        mes = message.content.split()
        output = ""
        for word in mes[1:]:
            output += word
            output += " "
        await message.channel.send(output)
        await message.delete()
    if message.content.startswith("(8ball"):
        await message.channel.send(random.choice(responsesball))
    if message.content.startswith("(randomnumber"):
        await message.channel.send(randrange(1, 10000000000000000))
    if message.content.startswith("(creator"):
        await message.channel.send("The creator of this bot is BackGroundSignal#0477")
    if message.content.startswith("(help"):
        await message.channel.send("All of the commands are:")
        await message.channel.send("(randomnumber, (ping, (8ball, (say, (balls, (whoasked, (dogwater, (urmom, (amogus, (minecraft, and (creator")


    if message.content.startswith("@everyone"):
        await message.delete()
        await message.channel.send("Ayo bro dont do dat")
    if message.content.startswith("fuck off"):
        await message.delete()
        await message.channel.send("no u")
    if message.content.startswith("Fuck off"):
        await message.delete()
        await message.channel.send("no u")


    if message.content.startswith("(balls"):
        await message.channel.send("in yo jaw")

    if message.content.startswith("(whoasked"):
        whoasked = randrange(1, 6)
        if whoasked == 1:
            await message.channel.send("https://tenor.com/view/who-asked-me-trying-to-find-who-asked-spongebob-spunch-bob-gif-22526294")
        if whoasked == 2:
            await message.channel.send("https://tenor.com/view/who-asked-gif-19808527")
        if whoasked == 3:
            await message.channel.send("https://tenor.com/view/nobody-asked-6million-years-who-asked-fartic-gif-20339864")
        if whoasked == 4:
            await message.channel.send("https://tenor.com/view/dont-care-didnt-ask-cope-_ratio-skill-issue-canceled-gif-24148064")
        if whoasked == 5:
            await message.channel.send("https://tenor.com/view/thats-crazy-thats-crazy0people-asked-who-asked-gif-22903987")

    if message.content.startswith("(dogwater"):
        dogwater = randrange(1, 6)
        if dogwater == 1:
            await message.channel.send("https://tenor.com/view/dogwater-dog-water-insult-gif-21871318")
        if dogwater == 2:
            await message.channel.send("https://tenor.com/view/callofduty-dog-water-based-gif-20367591")
        if dogwater == 3:
            await message.channel.send("https://tenor.com/view/dog-water-ez-owned-trash-kid-gif-21522383")
        if dogwater == 4:
            await message.channel.send("https://tenor.com/view/rage-gamplay-gif-21883046")
        if dogwater == 5:
            await message.channel.send("https://tenor.com/view/dog-water-gif-22171564")

    if message.content.startswith("(urmom"):
        amongus = randrange(1, 6)
        if amongus == 1:
            await message.channel.send("https://tenor.com/view/urmom-your-mom-baldi-defaultdance-gif-19665250")
        if amongus == 2:
            await message.channel.send("https://tenor.com/view/doin-your-mom-on-my-way-omw-me-on-my-way-to-do-your-mom-plague-doctor-gif-20519290")
        if amongus == 3:
            await message.channel.send("https://tenor.com/view/meme-gif-23433360")
        if amongus == 4:
            await message.channel.send("https://tenor.com/view/ur-mom-ur-mom-mario-gandam-gif-24232237")
        if amongus == 5:
            await message.channel.send("https://tenor.com/view/pixelplace-gif-24586548")

    if message.content.startswith("(amogus"):
        amongus = randrange(1, 6)
        if amongus == 1:
            await message.channel.send("https://tenor.com/view/amogus-gif-24170637")
        if amongus == 2:
            await message.channel.send("https://tenor.com/view/among-us-anime-dance-anime-dance-among-us-dance-gif-21490226")
        if amongus == 3:
            await message.channel.send("https://tenor.com/view/among-us-gif-24283650")
        if amongus == 4:
            await message.channel.send("https://tenor.com/view/among-us-crazy-among-us-game-dance-vent-impostor-gif-22582313")
        if amongus == 5:
            await message.channel.send("https://tenor.com/view/19dollar-fortnite-card-among-us-amogus-sus-red-among-sus-gif-20549014")


    if message.content.startswith("(minecraft"):
        minecraft = randrange(1, 6)
        if minecraft == 1:
            await message.channel.send("https://tenor.com/view/diamonds-minecraft-mining-gif-20393111")
        elif minecraft == 2:
            await message.channel.send("https://tenor.com/view/minecraft-boxer-boxing-minecraft-boxer-gif-18025297")
        elif minecraft == 3:
            await message.channel.send("https://tenor.com/view/blue-gif-23313127")
        elif minecraft == 4:
            await message.channel.send("https://tenor.com/view/andycringe-alex-jones-minecraft-gaming-gif-16682554")
        elif minecraft == 5:
            await message.channel.send("https://tenor.com/view/vamo-jogar-free-fire-gif-22693525")


@client.event
async def on_ready():
    print("Running")

client.run(TOKEN)
