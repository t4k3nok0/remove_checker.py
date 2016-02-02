import sys
import os.path
import tweepy
from tweepy.error import TweepError


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

follower_list = []
follower_list_about = []
    
if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
else:
    pass

if os.path.isfile("follower_list_base.txt") != True:
    print ("初回起動につき準備中です少しお待ちください")
    
    follower_list = open('follower_list_base.txt','w')
    follower_about = open('follower_about.txt', 'w')

    try:
        pos = 1
        for user in tweepy.Cursor(api.friends, count=200, cursor=-1).items():
            follower_list.write(str(user.screen_name) + ",")
            follower_about.write(str(user.name) + " " + "@" +str(user.screen_name) + "\n")
            pos += 1

    except TweepError as e:
        print(e.reason)

    print ("Finish")

    follower_list.close()
    follower_about.close()

    print ("2〜3日してから再度このプログラムを実行してください")
    print ("次回起動時には誰からフォローを外されたか確認し表示します")    



else:

    print ("フォローを外した人をチェック中です")

    now_follower = open('now_follower_list.txt', 'w')

    try:
        pos = 1
        for user in tweepy.Cursor(api.friends, count=200, cursor=-1).items():
            now_follower.write(str(user.screen_name) + ",")
            pos += 1

    except TweepError as e:
        print(e.reason)
        sys.exit()

    now_follower.close()
    print("取得成功")
    open_follower_list_base = open("follower_list_base.txt", "r")
    base = open_follower_list_base.read()
    open_follower_list_base.close()

    open_now_follower_list = open("now_follower_list.txt", "r")
    now = open_now_follower_list.read()
    open_now_follower_list.close()

    base = base.split(",")
    now = now.split(",")
    

    set_base_new = (set(base) -set(now))
    print ("検索中です")
    if len(set_base_new)  ==  0:
        print ("誰からもフォローを外されていません")
    else:
        print ("以下のユーザにフォローを外されています")
        print (list(set_base_new))

    set_base_new = (set(now) -set(base))
    if len(set_base_new) == 0:
        pass
    else:
        print ("以下のユーザに新たにフォローされています")
        print (list(set_base_new))
