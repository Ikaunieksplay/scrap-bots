import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "`")

chat_filter = ["FUCK", "FUCKING", "SHIT", "FREAKING"]
bypass_list = ["430316110550794241"]
@client.event
async def on_ready():
    print("HoksiAI is up and running!")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content == "Test":
        await client.send_message(message.channel, "If you are seeing this I am working!")
    if message.content == "You dont work":
        await client.send_message(message.channel, "I am working")       
    if message.content == "Hoksi":
        await client.send_message(message.channel, "**This is written by Mario and Dan:** Hoksi started off as a toy (not a toy brand). Then I thought: I want to make a car company! The name wasnt sure yet. Later on, I named the company Hoksi. That time, I really wanted to make my own games too. The characters were the RimHoly (weird name) Bros. They had a tiger that could fly. It didnt have wings but he used compressed farts as a rocket engine. Then later I realised it was too cringey and now I wanted to make buses. I had found the names for the cars in 2015. Moccha, Cappu, Latte and Expresso. The sportscar was called Malta. Then I wanted to make planes and trains... Time went on.. I realised planes and trains were too large. Then 5 months after I got Discord, I officialy founded Hoksi. Jack was the Co-founder, but soon Hoksi fell apart due to Evelina and Jack, a few days later I(Dan) noticed that hoksi was gone and I asked Mario about it. So then we decided to make a new secret Hoksi and we began work on some supercars, then Hoksi was unsecreted and Jack joined back in, so here we are now planning and designing cars. Then Hoksi founded Hoksi Airlines with Jack as the owner. Sadly he soon deleted it for lack of work and now Dan remade it with Mario, Alex, Oreo and Luigi/Ryan, now Hoksi and Hoksi Airlines are striving.")
    if message.content == "HFM-01":
        await client.send_message(message.channel, "**This is the current state of the HFM-01:** https://cdn.discordapp.com/attachments/429295427997925376/429985218284355598/unknown.png")
    if message.content.upper().startswith('/PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('/SAY'):
        args = message.content.split(" ")
        #args[0] = /SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.upper().startswith('/AMIDAN'):
          if message.author.id == "300188652884197376":
              await client.send_message(message.channel, "You are Dan!")
          else:
              await client.send_message(message.channel, "You are not Dan!") 
    if message.content.upper().startswith('/DOIHAVEANYONE'):
        if "429286317671841814" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, 'You have the rank anyone.')
        else:
            await client.send_message(message.channel, 'You dont have the rank anyone.')
    elif message.content.upper().startswith('/HELP'):
        emb = (discord.Embed(description="**Current commands:** cookie, Test, You dont work, Hoksi, HFM-01, /ping, /say, /amidan, /doihaveanyone, /help.(**All of the commands that dont have a / before them are case sensitive!**", colour=0x3DF270))
        emb.set_author(name="List of current commands!", icon_url=' ')
        await client.send_message (message.channel, embed=emb)
client.run("NDMwMDA0NDM1NTc0MzI1MjU1.DaPwHg.EdT5yywUrO6ky4ekzm4ZUZKGPSY")
                                  
