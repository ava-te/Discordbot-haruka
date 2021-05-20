import discord
import sys
import os
import pickle
import random
import datetime


client = discord.Client()
CHANNEL_ID = 831420404286881827 # 任意のチャンネルID(int)
path = "C:/Users/avatail/Desktop/学習用プロジェクト/discord_bot2/.user_info/"
datetime_today = f'{datetime.date.today()}'
user_info_list = []

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')      

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # メッセージやメンションを貰うとそのユーザーのsavが日付ごとに作成・リストにその内容が追記される。
    if message.content.endswith("セーブファイル作って"):
        random_mention = ["君の事憶えとくね！", "これから憶えとくね！", "記憶力〇", "記憶力◎", "記憶しとくよ～"]
        mention_hentou = random.choice(random_mention)
        reply = f'{message.author.mention}' + mention_hentou 
        await message.channel.send(reply)
        user_info_id = f'{message.author.id}'
        text_path = os.path.join(path, user_info_id + "date" + datetime_today + "info.sav")        
        file = open(text_path, "wb")
        pickle.dump(user_info_list,file)
        file.close()
    else:
        user_mention = f'{message.content}'
        user_info_id = f'{message.author.id}'
        text_path = path + user_info_id + "date" + datetime_today + "info.sav"
        file = open(text_path, "wb")
        user_info_list.append(user_info_id + user_mention)
        pickle.dump(user_info_list,file)
        file.close()
        print(user_info_list)

    # 「おはよう」で始まるか調べる
    if message.content.endswith("おはよう"):
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    # ランダム12桁整数
    if message.content.endswith("パスワード作って"): 
        num_random12 = random.randrange(100000000000,999999999999)
        random12 = str(num_random12)
        await message.channel.send("はいよ！" + random12)

    if message.content.startswith('!SHUTDOWN_BOT'):#!SHUTDOWN_BOTが入力されたら強制終了
        await client.logout()
        await sys.exit()

# token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("ODQxMzA4MjEyMTgzODI2NDQ0.YJk3VA.F-5ZkiZjxCZMaCsmMyrYcYqFAOM")