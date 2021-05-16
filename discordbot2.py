import discord
import sys
import os
import pickle
import random


client = discord.Client()
CHANNEL_ID =  # 任意のチャンネルID(int)
path = "C:/Users/avatail/Desktop/学習用プロジェクト/discord_bot2/.user_info/"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')
text_path = os.path.join(path,"info.sav")
try:
    file = open(text_path,"rb")
    texten = pickle.load(file)
    file.close
except:
    texten = []

# リプライを貰うとそのユーザーのSAVファイルが作成されるようにする
@client.event
async def reply(message):
    if message.content.endswith("セーブファイル作って"):
        random_mention = ["君の事憶えとくね！", "これから憶えとくね！", "記憶力〇", "記憶力◎", "記憶しとくよ～"]
        mention_hentou = random.choice(random_mention)
        reply = f'{message.author.mention}' + mention_hentou 
        await message.channel.send(reply)
        user_info_id = f'{message.author.id}'
        text_path = os.path.join(path, user_info_id + "info.sav")
        file = open(text_path, "wb")
        pickle.dump(texten,file)
        file.close()        
    
@client.event
async def on_message(message):
    if message.author.bot:
        return
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    #誰かがセーブお願いと発言すると蓄積したデータがtext.savに保存される。
    if message.content.endswith("セーブお願い"):
        file =open(text_path, "wb")
        pickle.dump(texten,file)
        file.close()
        await message.channel.send('セーブ完了！')

    # ランダム12桁整数
    if message.content.endswith("パスワード作って"): 
        num_random12 = random.randrange(100000000000,999999999999)
        random12 = str(num_random12)
        await message.channel.send("はいよ！" + random12)

    # 発言時に実行されるイベントハンドラを定義
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

    if message.content.startswith('!SHUTDOWN_BOT'):#!SHUTDOWN_BOTが入力されたら強制終了
        await client.logout()
        await sys.exit()

# token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("")