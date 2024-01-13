import nest_asyncio
import sys
import os
import asyncio
import random
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = '27668783'
api_hash = '0931ae1c0f547465580a2e563e5e1bfa'

session_string = '1BVtsOGkBu6QFBhOuwd4pgrjqDdpDJzS_dRkgAvBgR7MtYOwuUjoJ4BR44oqP0su_QgLVzH6ADJL_W5mCRsUPF4a6wqiZae8VMwoClmKNFsGqdWbInlkOd9uDnkPmBebQNqSENW8j4EApg8vFlRTrAlio9mHJ391AgnZR-M9XUMpf6w0R83Xwiy9rgC1UglC6TQOWIwFFz108torAE_RXcpc4US4Yv8Fgj9eMr-tQWtUOIb68FAKZaUpgPRR_jC8QybCvmlQAU6T0gHsPhQF18tMKGE_nhPAEn8YdNS5ySjSkhRt_j-ljZhQunHvYOG61wxFtHtuH85DYIe1BvIudY-h_n16yO00='
username = '@roronoa_zoro_robot'

session = StringSession(session_string)
client = TelegramClient(session, api_id, api_hash)

async def run_bot():
    await client.start()
    await main()
    await client.run_until_disconnected()

async def main():
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

        # Loop indefinitely and place /bet commands with a 4-second delay
        while True:
            for bet_amount in divided_bounties:
                # Send the /bet command with a random h or t (heads or tails)
                coin_toss_result = random.choice(['h', 't'])
                await client.send_message(username, f"/bet {bet_amount} {coin_toss_result}")

                # Wait for 4 seconds before placing the next bet
                await asyncio.sleep(4)

# Run the bot in a separate thread
client_thread = asyncio.new_event_loop().create_task(run_bot())
