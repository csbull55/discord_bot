import discord
import numpy as np

# i need to put this in a local file and read from it
token = ''


client = discord.Client()

# defines the arma drop rates, I kept true to jamflex's drop rate code config
arma_drops = [
    ['Arma Helm', 30,31,32,33],
    ['Arma Plate', 150,151,152,153],
    ['Arma Skirt', 270,271,272,273],
    ['Arma Hilt', 390,391,392],
    ['Shard 1', 420,421],
    ['Shard 2', 540,541],
    ['shard 3', 660,661]
    ]

# this is the arma sim, replies to message format below
@client.event
async def on_message(message):
    if message.content.startswith('!arma'):
        channel = message.channel
        # assigns input as an integer
        kc = int(message.content[6:])

        # creates an array of rolls for kc entered
        roll = np.random.randint(1, 1524, size=kc)

        drops = []

        # checks rolls against drop table, returns item and adds to 'drops' list
        for i in arma_drops:
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
        await channel.send(drops_msg)


# this is just to make sure it's running, could remove
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)