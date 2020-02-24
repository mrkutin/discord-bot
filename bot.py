import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is connected!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('привет'):
        await message.channel.send('и тебе привет, {0}!'.format(message.author.mention))

    if message.content.startswith('пока'):
        await message.channel.send('и тебе пока, {0}!'.format(message.author.mention))

@client.event
async def on_typing(channel, user, when):
    await channel.send('я вижу, как {0} печатает!'.format(user.name))

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send('Спасибо, {0}, очень приятно!'.format(user.name))

@client.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name.startswith('👀'):
        await client.get_channel(payload.channel_id).send('{0}, 👀'.format(payload.member.name))


client.run(os.environ['DISCORDTOKEN'])
