import nest_asyncio
import sys
import os
import asyncio
import random
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 'your_api_id'
api_hash = 'your_api_hash'

session_string = 'your_session_string'
username = 'your_username'

session = StringSession(session_string)
client = TelegramClient(session, api_id, api_hash)


@client.on(events.NewMessage(from_users=[username]))
async def _(event):
    # Send the /bal command
    await client.send_message(username, "/bal")

    # Wait for the bot's response
    response = await client.get_messages(username, limit=1)

    # Extract and use the bounty information
    if response:
        bounty_message = response[0].raw_text
        # Extract the current bounty amount
        current_bounty = int(bounty_message.split(' ')[-1])

        # Divide the bounty dynamically based on the current amount
        divided_bounties = [current_bounty // (2 ** i) for i in range(4)]

        # Wait for 1 second before placing the first bet
        await asyncio.sleep(1)

        # Loop indefinitely and place /bet commands with a 4-second delay
        while True:
            for bet_amount in divided_bounties:
                # Send the /bet command with a random h or t (heads or tails)
                coin_toss_result = random.choice(['h', 't'])
                await client.send_message(username, f"/bet {bet_amount} {coin_toss_result}")

                # Wait for 4 seconds before placing the next bet
                await asyncio.sleep(4)

    # Disconnect and restart the script
    await client.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)


async def main():
    await client.start()
    await client.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
  
