import discord
import numpy as np
import pandas as pd
import drop_rate

# this is the arma sim, replies to message format below
@client.event
async def on_message(message):
    if message.content.startswith('!boss'):

        # assigns inputs to variables
        user_input = message.content.split(' ')
        boss = user_input[1]
        kc = int(user_input[2])

        # creates df off boss with items and rates + rolls
        drop_rate.roll_df(boss)

        # creates an array of rolls for kc entered, uses function to find lcm for boss
        roll = np.random.randint(1, drop_rate.boss_lcm(boss), size=kc)

        drops = []

        # checks rolls against drop table, returns item and adds to 'drops' list
        for i in boss_drops:
            for drop in roll:
                if drop in i[1:]:
                    drops.append(i[0])

        # returns message based on drops
        if len(drops) == 0:
            drops_msg = "After {} kc at Kree'arra, you've received zero uniques, the bird is victorious".format(kc)
        elif len(drops) >= 1:
            drop_lines = ("\n".join(drops))
            drops_msg = "In {} kc at Kree'arra, you've been blessed with the following items:\n{}".format(kc, drop_lines)

        # sends message with results
        channel = message.channel
        await channel.send(drops_msg)

