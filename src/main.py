
import requests
from dotenv import  load_dotenv
import os
import asyncio
import json
import  telegram
load_dotenv()


async def send_message( context):

    bot_token = os.getenv('bot_token')
    chat_id = os.getenv('chat_id')
    # bot_token = "7783935901:AAFAN2QNWeN7dOtdmJF0qnNPnEiCnUc_DX8"
    # chat_id = "7100950465"
    bot = telegram.Bot(token=bot_token)
    await bot.sendMessage(chat_id=chat_id, text=context)



# 登录页面的 URL 和表单数据
def  request_check_in(email, psd):
    # 创建一个 Session 对象
    session = requests.Session()
    login_url = 'https://ikuuu.one/auth/login'
    login_data = {'host': 'ikuuu.one',
                  'email': email,
                  'passwd': psd
                  }
    print(login_data)
    # 发送登录请求
    response = session.post(login_url, data=login_data)

    # 检查登录是否成功
    if response.status_code == 200:
        # 访问需要登录后才能访问的页面
        target_url = 'https://ikuuu.one/user'
        response = session.get(target_url)

        # 检查请求是否成功
        if response.status_code == 200:

            json_data = session.post('https://ikuuu.one/user/checkin')
            if response.status_code == 200:
                print(type (json_data.json()))
                msg = login_data['email'] + '\n'+str(json.loads(json_data.text))
                asyncio.run(send_message(msg)) 
            else:
                print(f'请求失败，状态码: {response.status_code}')
        else:
            print(f'请求失败，状态码: {response.status_code}')
    else:
        print(f'登录失败，状态码: {response.status_code}')



if __name__ == '__main__':
    emails=os.getenv('email')
    json_data = json.loads(emails)
    psd = '123456789'
    for e in json_data:
        request_check_in(e, psd)