
import requests



# 登录页面的 URL 和表单数据
def request_check_in(email, psd):
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
            # print(response.text)
            json = session.post('https://ikuuu.one/user/checkin')
            if response.status_code == 200:
                print(json.json())
            else:
                print(f'请求失败，状态码: {response.status_code}')
            # # # 解析 HTML 内容
            # soup = BeautifulSoup(response.content, 'html.parser')
            #
            # # 找到并打印标题
            # title = soup.find('title').text
            # print(f'页面标题: {title}')
        else:
            print(f'请求失败，状态码: {response.status_code}')
    else:
        print(f'登录失败，状态码: {response.status_code}')



if __name__ == '__main__':
    email = ['huuxjian@gmail.com', '3329334227@qq.com']
    psd = '123456789'
    for e in email:

        request_check_in(e, psd)