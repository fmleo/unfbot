import tweepy
from time import sleep

consumer_key = "kA7btSPyTtXD1WeLKkpTjgbRl"
api_secret = "J7UVenQKCu6Z1Eay11Jn4V9uRLPDCTF6OI6PByIAcwXuVYW9lK"
access_token = "1252349748964667392-jKSDT6RSx6uUy7cKrHFGkehex1nB65"
access_token_secret = "WXe3Ot5fDd71vxitZ6gclRyJMRDHUQV70DxPq17r1YIoV"
auth = tweepy.OAuthHandler(consumer_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_followers(screen_name):
    ids = list()
    for page in tweepy.Cursor(api.followers_ids, screen_name=screen_name).pages():
        ids.extend(page)
    return ids

for idbf in get_followers(api.me().screen_name):
    oldf = open(f"./followers/{idbf}.txt", 'r').read().strip("\n").split("\n")
    newf = open(f"./followers/{idbf}.txt", '+w')
    for idff in get_followers(api.get_user(idbf).screen_name):
        newf.write(f"{idff}\n")
    newf.close()
    newf = open(f"./followers/{idbf}.txt", 'r').read()
    unfs = list()
    for follower in oldf:
        if follower not in newf:
            unfs.append(api.get_user(int(follower)).screen_name)
    print(unfs)
    text = "Ninguém deixou de te seguir" if len(unfs)==0 else ("{} pessoas deixaram de te seguir: {}".format(len(unfs), "\n".join(unfs)))
    api.send_direct_message(recipient_id=int(idbf), text=text)

