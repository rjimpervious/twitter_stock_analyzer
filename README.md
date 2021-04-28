# Twitter Stock Analyzer
A modolurized version of a web app available on my ![portfolio website]((https://www.rjlopez.me/twitter_stock/). It pulls tweets from twitter (using TweePy module) and analyzes the polarity of the tweets using NLTK's Vader Sentimer Analyzer. It also utilizes matplotlib to create a graphical representation of the results.

## Prerequisities:
* Tweepy (you also need a customer key and secret from  developer.twitter.com)
* Python 3
* NLTK
* Matplotlib

## Usage

1. Run the script in the Terminal(Linux/Mac), CMD(Windows) or alternatively in an IDE. Then enter the stock ticketer and the number of tweets to be pulled (recommended is at least 100).
![](https://github.com/rjimpervious/twitter_stock_analyzer/blob/main/images/pic_1.png)

2. Wait for the tweets to analyzed. Depending on the your input (the number of tweets), and the speed of your machine, this can take minutes. The script will print out all the tweets and will generate a summary at the end.
![](https://github.com/rjimpervious/twitter_stock_analyzer/blob/main/images/pic2.png)

3. The script will also generate a pie graph (powered by Matplotlib) from the data.
![](https://github.com/rjimpervious/twitter_stock_analyzer/blob/main/images/pic3.png)


