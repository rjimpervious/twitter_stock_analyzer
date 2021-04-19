import tweepy
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import pyinputplus as pyip


# run for the first time to download lexicon
# nltk.downloader.download('vader_lexicon')

CONSUMER_KEY = 'njUfYLmQGWygeWj1hCiMa4wiz'
CONSUMER_SECRET = 'yjLRe1tfkcScKoDpo78tf2RKCMwBO9ICOQXlYNMt5KESOK1k6y'


# This is using twitter Oath2 authentication (without user context)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)


def percentage(part, whole):
    return round((float(part)/ float(whole)) * 100, 2)


def analyze_tweets():

    stock_code = pyip.inputStr("Please enter a stock code:$")
    no_of_tweets = pyip.inputNum("Please enter number of tweets to be parsed:")
    print("Pulling tweets from twitter....")
    results = [status._json for status in
               tweepy.Cursor(api.search, q="$"+stock_code, tweet_mode='extended', lang='en').items(no_of_tweets)]

    positive_tweet_count = 0
    negative_tweet_count = 0
    neutral_tweet_count = 0

    positive_score = 0
    negative_score = 0
    neutral_score = 0

    tweets = ""
    tweet_list = []

    for result in results:
        tweet = result["full_text"]
        tweets += tweet
        tweet_list.append(tweet)
        print(tweet)
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)

        # access the corresponding score from the result of SentimentIntensityAnalyzer
        pos = score['pos']
        neg = score['neg']
        neu = score['neu']

        # determine which polarity of tweet is it by taking the max argument
        max_score = max(score.values())
        print(max_score)
        print('*' * 10)
        # now get the index to be used for comparison to classify which kind of tweet is it
        if pos > neg:
            positive_tweet_count += 1
        elif neg > pos:
            negative_tweet_count += 1
        elif neg == pos:
            neutral_tweet_count += 1

    print("*" * 20)

    print(f"Number of positive tweets: {positive_tweet_count} ({percentage(positive_tweet_count, no_of_tweets)}%)")
    print(f"Number of negative tweets: {negative_tweet_count} ({percentage(negative_tweet_count, no_of_tweets)}%)")
    print(f"Number of neutral tweets: {neutral_tweet_count} ({percentage(neutral_tweet_count, no_of_tweets)}%)")

    counts = [positive_tweet_count, negative_tweet_count, negative_tweet_count]

    plt.style.use('seaborn')
    colors = ['#ff9999','#66b3ff','#99ff99']
    fig, ax,  = plt.subplots()
    explode = (0.1, 0.1, 0.1)
    ax.axis('equal')
    ax.pie(counts, explode=explode, labels=["positive", "negative", "neutral"],
           autopct='%1.1f%%', shadow=True, startangle=90,
           colors=colors
           )

    plt.show()


if __name__ == '__main__':
    analyze_tweets()




