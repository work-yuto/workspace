import tweepy
def main():
    CONSUMER_KEY="API key"
    CONSUMER_SECRET="API secret key"
    ACCESS_TOKEN="Access token"
    ACCESS_SECERET="Access token secret"

    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)
    api=tweepy.API(auth)


    q_list=["progate","#駆け出しエンジニアと繋がりたい","#ブログ書け"]
    count=50
    for q in q_list:
        print("Now:QUERY-->>{}".format(q))
        search_results=api.search(q=q,count=count)
        for status in search_results:
            tweet_id=status.id
            try:
                api.create_favorite(tweet_id)
            except:
                pass

if __name__ == '__main__':
    main()