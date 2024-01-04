from telethon.sessions import StringSession
import nest_asyncio
nest_asyncio.apply()
import asyncio
import random
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import unidecode

api_id = '21124978'
api_hash = '63f41b60df295e52b2a967e5f9c02977'
session_string = '1BVtsOMgBuzMHr2PoXkLqH1EAKb3Il_bNri_WlPVKEi49UALTfMVwiZIBnRCkrK8CEiOzd9n-MyRkHvJ_p0z6QILYAk9FuGR5MGd0aBoYqZAzw7B0zknrHOE-1gZRC6jxbw07zGJPcmya2CMsRE3Gtjy5Y6wGF0rwfx8_hPkunPbLH98pSV8pvz3ZmK7ivvj0J1P3dVS_Ly0EnjdSVcGD3GImJUTIZmNTUYk3u8xbsTR95to2h73NdFfh-QMLuFGm4UhAZzc0unCg3B_IuoqDHqrx6v32Qx8yclyCq0Dg_8l7xrprYMDwhRtp23dl7BQxby_xUGMkhvFWgcWLsWU-ECOFX9kQMXQ='
bot_username = '@Naruto_X_Boruto_Bot'
characters_file = 'naruto_characters.txt'

jumble_command = "/jumble"
jumble_prompt = "Type correct word to get reward.\nJumbled :"

session = StringSession(session_string)
client = TelegramClient(session, api_id, api_hash)

# Read Naruto character names from file
with open(characters_file, 'r') as file:
    naruto_characters = [line.strip() for line in file]

def jumble_solver(jumbled_name):
    # Rearrange the characters of the jumbled word
    shuffled_name = ''.join(random.sample(jumbled_name, len(jumbled_name)))
    return shuffled_name

def find_correct_name(rearranged_name):
    # Try all possible matchups of the rearranged name
    possible_matches = [name for name in naruto_characters if sorted(name.lower()) == sorted(rearranged_name.lower())]
    
    if possible_matches:
        return possible_matches[0]
    else:
        return "Name not found"  # Replace with your own handling for not finding the name

async def send_jumble_command():
    while True:
        await asyncio.sleep(2)  # Send the command every 2 seconds
        await client.send_message(bot_username, jumble_command)

@client.on(events.NewMessage(from_users=[bot_username]))
async def on_message(event):
    if jumble_prompt in event.raw_text:
        # Extracting the jumbled name from the bot's response
        jumbled_name = event.raw_text.split(jumble_prompt)[1].strip()

        # Rearrange the jumbled word
        rearranged_name = jumble_solver(jumbled_name)

        # Finding the correct character name in the list
        correct_name = find_correct_name(rearranged_name)

        # Sending the correct name back to the bot
        await client.send_message(bot_username, f"{correct_name}")

async def main():
    await client.start()
    asyncio.ensure_future(send_jumble_command())
    await client.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
    
