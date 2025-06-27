# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import requests
import threading
import time
import asyncio

class Bot(Client):

    def __init__(self):
        super().__init__(
            "techvj login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        max_retries = 5
        retry_count = 0
        while retry_count < max_retries:
            try:
                await super().start()
                print('Bot Started Powered By @VJ_Botz')
                # Start keep-alive thread
                self.keep_alive_thread = threading.Thread(target=self.keep_alive, daemon=True)
                self.keep_alive_thread.start()
                break
            except Exception as e:
                if "FloodWait" in str(e):
                    wait_time = int(str(e).split("A wait of")[1].split(" seconds")[0])
                    capped_wait = min(wait_time, 10)  # Cap wait time to 10 seconds
                    print(f"FloodWait detected. Waiting for {capped_wait} seconds (capped from {wait_time})...")
                    await asyncio.sleep(capped_wait)
                    retry_count += 1
                else:
                    print(f"Unexpected error: {e}")
                    break
        if retry_count >= max_retries:
            print("Max retries reached. Bot failed to start.")

    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')

    def keep_alive(self):
        while True:
            try:
                requests.get("http://0.0.0.0:10000")  # Adjust URL/port as needed
                print("Keep-alive ping sent")
            except Exception as e:
                print(f"Keep-alive error: {e}")
            time.sleep(300)  # Ping every 5 minutes

if __name__ == "__main__":
    bot = Bot()
    asyncio.run(bot.run())

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
