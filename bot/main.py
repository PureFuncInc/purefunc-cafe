import json
import random
import time

import discord
import urllib3

client = discord.Client()
random.seed(time.time())

http = urllib3.PoolManager()


@client.event
async def on_ready():
    print(f"bot name: {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!pheme create"):
        if len(message.content) < 16:
            await message.channel.send(f"無效的名稱, 輸入名稱過短")
        else:
            account = message.content[14:]
            resp = http.request(
                method="POST",
                url="https://pheme.social/voice-service/api/v1.0/admin/test/user",
                headers={"Content-Type": "application/json",
                         "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJpcCI6IjAuMC4wLjAvMCIsImp0aSI6IjE4MmJkNmUyLTYyM2EtNDNkNS05OGIyLWMyYTQxOGU5NjIxMCIsImlhdCI6MTY1NjU2Mzk3MSwiaXNzIjoidm9pY2Utc2VydmljZSIsImV4cCI6MTY2NTIwMzk3MSwic3ViIjoiYm9AcHVyZWZ1bmMubmV0In0.VAfV7ex78ri8h7JK58o3On0kZWoKgDRhimFUzqB4V0zyw6z69N50BqiRZQ0cSAmuUMtgQkgh7dJ6ULLj6mLl1Q"},
                         body=json.dumps({"email": f"{account}@purefunc.net"}).encode("utf-8"),
            )
            if resp.status != 201:
                print(resp.status)
                message.channel.send(f"創建帳號 {account} 失敗, 回應碼 {resp.status}!")
            else:
                await message.channel.send(f"創建帳號 {account} 成功!")

    if message.content.startswith("!pheme remove"):
        if len(message.content) < 16:
            await message.channel.send(f"無效的名稱, 輸入名稱過短")
        else:
            account = message.content[14:]
            resp = http.request(
                method="DELETE",
                url=f"https://pheme.social/voice-service/api/v1.0/admin/test/user/{account}",
                headers={"authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJpcCI6IjAuMC4wLjAvMCIsImp0aSI6IjE4MmJkNmUyLTYyM2EtNDNkNS05OGIyLWMyYTQxOGU5NjIxMCIsImlhdCI6MTY1NjU2Mzk3MSwiaXNzIjoidm9pY2Utc2VydmljZSIsImV4cCI6MTY2NTIwMzk3MSwic3ViIjoiYm9AcHVyZWZ1bmMubmV0In0.VAfV7ex78ri8h7JK58o3On0kZWoKgDRhimFUzqB4V0zyw6z69N50BqiRZQ0cSAmuUMtgQkgh7dJ6ULLj6mLl1Q"},
            )
            if resp.status != 204:
                print(resp.status)
                message.channel.send(f"移除帳號 {account} 失敗, 回應碼 {resp.status}!")
            else:
                await message.channel.send(f"移除帳號 {account} 成功!")

    if message.content.startswith("!raffle cafe"):
        channel = client.get_channel(69158422)

        user_ids = []
        for user in channel.voice_states.keys():
            user_ids.append(user)

        idx = random.randint(0, len(user_ids))
        user = await client.fetch_user(user_ids[idx])

        await message.channel.send(f"{channel.name} 共有 {len(user_ids)} 人, 這次抽中的是 {user.mention}")


client.run("OTI3NTUxNjIyNjg1NTQwMzYz.GgeK70.zP9D2ypsjmzfyjOqWFG0usTXaT3yYRGR1tlx1Q")
