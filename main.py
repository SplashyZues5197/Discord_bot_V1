import discord
import random
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()



TOKEN = "OTA5MTk3MzQ0MzE3MjY4MDI5.YZAyAg.iLlLpJR2_ZgaSxVgcXhDYoUUkAI"

client = discord.Client()
num1 = int
num2 = int
@client.event
async def on_ready():
    print("We have logged in as {0.user}" .format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == 'project':
        if message.content.startswith('burnaby'):
            response = chatbot.request(message.content[7:])
            await message.channel.send(response)

        elif user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == '!info':
            await message.channel.send('adget')
            await message.channel.send('Does that help?')
            if user_message.lower() == 'no':
                await message.channel.send('Contact')
            eliff user_message.lower() == 'yes':
                await message.channel.send('I am glad it helps')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f"See you later {username}!")
            return
        elif user_message.lower() == "!random":
            response = f'This is your random number : {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'how is it going?':
            await message.channel.send(f'It is going well {username}!, How are you?')
            return

        elif user_message.lower() == '!help':
            await message.channel.send(f'{username}, You could send hello, !info, bye, !random, how is it going?')
            return





client.run(TOKEN)