import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("в интересную игру, а в какую не скажу!")
    await client.change_presence(status=discord.Status.dnd, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.author.send('Привет!\nЯ бот этого канала.\nЯ знаю следующие команды:\n$one\n$two\n$three')

# @client.event
# async def on_typing(channel, user, when):
#     await user.send(content='@{0} что-то пишет! Скорее бы прочесть...'.format(user))

@client.event
async def on_reaction_add(reaction, user):
    print('reaction {0}'.format(reaction))
    print('user {0}'.format(user))

# @client.event
# async def on_raw_reaction_add(payload):
#     print('payload {0}'.format(payload))
#     if payload.emoji.name == '👍' or payload.emoji.name == '😆' or payload.emoji.name == '🙂':
#         await client.get_channel(payload.channel_id).send('Спасибо, @{0}#{1}! Мне приятно.'.format(payload.member.name, payload.member.discriminator))
#
#     if payload.emoji.name == '💩':
#         await client.get_channel(payload.channel_id).send('@{0}#{1}, сам ты 💩!'.format(payload.member.name, payload.member.discriminator))
#
client.connect()
client.run('NjgwNDIyNTczMDc4ODcyMDY2.XlO2-g.vVcfZ7WwazYAB3j8KUIcoW64M5E')