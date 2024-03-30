import discord

intents = discord.Intents.default()
intents.message_content = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

async def send_message(server_id, channel_id, content):
    guild = client.get_guild(server_id)
    if guild:
        channel = guild.get_channel(channel_id)
        if channel:
            await channel.send(content)
        else:
            print("Channel not found in the guild!")
    else:
        print("Guild not found!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$pi'):
        await message.channel.send('3.14')

    if message.content.startswith('$message'):
        await send_message(server_id, channel_id, content)


        


client.run('your token')