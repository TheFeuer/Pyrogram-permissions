import asyncio
from pyrogram import Client
from datetime import datetime, time

from config import api_id, api_hash, chat_id, tz
from permissions import perm
from messages import send_access_message


async def main():
    app = Client(
        "my_account",
        api_id=api_id,
        api_hash=api_hash,
    )
    await app.start()

    chat = await app.get_chat(chat_id)
    current_permissions = chat.permissions

    now = datetime.now(tz)
    opening_time = time(hour=6, minute=0)
    closing_time = time(hour=20, minute=0)

    if opening_time <= now.time() <= closing_time:
        desired_permissions = perm(True)
        if current_permissions != desired_permissions:
            print("allowed")
            await send_access_message(app, chat_id, "allowed")
            await app.set_chat_permissions(chat_id=chat_id, permissions=desired_permissions)
        else:
            print(f'permissions are already set: {now}')
    else:
        desired_permissions = perm(False)
        if current_permissions != desired_permissions:
            await app.set_chat_permissions(chat_id=chat_id, permissions=desired_permissions)
            await send_access_message(app, chat_id, "restricted")
            print("restricted")
        else:
            print(f'permissions are already set: {now}')
    await app.stop()


async def on_startup():
    while True:
        now = datetime.now(tz)
        # if now == now: #для тестов
        if now.weekday() in [0, 2, 4] and 6 <= now.hour <= 20 and 0 <= now.minute <= 10:
            await main()
        # Задержка на 1 минуту перед следующим циклом
        await asyncio.sleep(60)


asyncio.run(on_startup())