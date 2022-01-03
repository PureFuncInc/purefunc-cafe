import random
import time

import discord

client = discord.Client()
random.seed(time.time())


@client.event
async def on_ready():
    print(f"bot name: {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!raffle cafe"):
        channel = client.get_channel(921677421869158422)

        user_ids = []
        for user in channel.voice_states.keys():
            user_ids.append(user)

        idx = random.randint(0, len(user_ids))
        user = await client.fetch_user(user_ids[idx])

        await message.channel.send(f"{channel.name} 共有 {len(user_ids)} 人, 這次抽中的是 {user.mention}")


client.run("TOKEN")