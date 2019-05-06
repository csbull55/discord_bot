# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:12:34 2019

@author: Christian
"""

# Work with Python 3.6
import discord

token = 'NTcxNTEwNzAwNTE4NjcwMzQx.XMOzSQ.xj-iFzWlaIbYCha3X_xugiq6lkk'

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    
    
@client.event
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])

client.run(token)