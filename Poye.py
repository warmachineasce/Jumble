import nest_asyncio
import asyncio
from telethon import TelegramClient, events
from telethon.tl import types
from telethon.sessions import StringSession
from appium import webdriver
import time

api_id = '21124978'
api_hash = '63f41b60df295e52b2a967e5f9c02977'
session_string = '1BVtsOMgBuzMHr2PoXkLqH1EAKb3Il_bNri_WlPVKEi49UALTfMVwiZIBnRCkrK8CEiOzd9n-MyRkHvJ_p0z6QILYAk9FuGR5MGd0aBoYqZAzw7B0zknrHOE-1gZRC6jxbw07zGJPcmya2CMsRE3Gtjy5Y6wGF0rwfx8_hPkunPbLH98pSV8pvz3ZmK7ivvj0J1P3dVS_Ly0EnjdSVcGD3GImJUTIZmNTUYk3u8xbsTR95to2h73NdFfh-QMLuFGm4UhAZzc0unCg3B_IuoqDHqrx6v32Qx8yclyCq0Dg_8l7xrprYMDwhRtp23dl7BQxby_xUGMkhvFWgcWLsWU-ECOFX9kQMXQ='
bot_username = '@Naruto_X_Boruto_Bot'

# Add the desired capabilities for the Android emulator or real device
desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'IN_2b',
    'appPackage': 'org.telegram.messenger',
    'appActivity': 'org.telegram.ui.LaunchActivity',
    'automationName': 'UiAutomator2'  # Use UiAutomator2 for Android
}

# Appium server URL
appium_server_url = 'http://127.0.0.1:4723/wd/hub'

# Create a session to interact with the app
appium_driver = webdriver.Remote(appium_server_url, desired_capabilities)

session = StringSession(session_string)
client = TelegramClient(session, api_id, api_hash)


@client.on(events.NewMessage(from_users=[bot_username], incoming=True))
async def handle_bot_message(event):
    # Send /explore command when a message from the bot is received
    await client.send_message(bot_username, "/explore")


@client.on(events.NewMessage(incoming=True))
async def handle_any_message(event):
    if "has challenged you" in event.message.text:
        # Specify the x and y coordinates of the button you want to click
        x_coordinate = 249
        y_coordinate = 1253

        # Click the element using coordinates
        appium_driver.tap([(x_coordinate, y_coordinate)])


async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    appium_driver.quit()  # Close the Appium session when the script is finished
  
