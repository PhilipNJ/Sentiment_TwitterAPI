# Tweet Mining and Sentiment Analysis

Python packages used: 
``
Pandas, Seaborn, Numpy, NLTK, Regex, TextBlob, Matplotlib, Tweepy, Numpy
``

## Mining the tweets

__Refer to file <a href="https://github.com/PhilipNJ/Sentiment_TwitterAPI/blob/main/Twitter_mining.py">Twitter_mining.py</a>__

1. We first create our <a href="https://developer.twitter.com/en">Twitter Developer Account</a> and generate the required API Keys. 
2. Using <a href="https://www.tweepy.org/">Tweepy</a> and our API keys we define a function to scrape 
* Username
* Description
* Location
* Following
* Followers
* Total Tweets
* Retweet Count
3. Run the code and in put hastag as "Johnny Depp" and specify time period from the start of 2020.
4. A csv with the minded tweets with hashtag as #johnnydepp will be generated to the local drive.

##Sentiment Analysis

__Refer to file <a href="https://github.com/PhilipNJ/Sentiment_TwitterAPI/blob/main/Sentiment_Analysis.ipynb">Sentiment_Analysis.ipynb</a>__

1. Import and Read the data
- Drop Blanks and unncessary columns
- Generate a wordcloud to check commonly occuring words that are not required for our analysis
- Basic check on where the tweets generated from:

![output](https://user-images.githubusercontent.com/97375173/187123412-adf3e063-c01b-46af-a229-1084284c05b5.png)

- Convert Username, Location and Description to string.

2. Cleaning the textual data:
- Replace different variants of our hashtag to generic 'johnnydepp'
- Remove non-ascii, non-english characters
- Remove single letters or digits or special characters
- Remove spaces, links, etc
- Remove all punctuation
- Remove all stop words
- Lemmitize all the words
- Check for least frequently occuring words in case of typos etc
- Check for most frequently occuring words in case anything has been missed

3. Sentiment Analysis
- Define a function to get Subjectivity and Polarity.
- Apply it in our data

4. Results
- The general sentiment is Positive to Nuetral 

![output](https://user-images.githubusercontent.com/97375173/187124124-548b7610-9a23-4598-8c04-e897d3815f63.png)

- Words contributing to the positivity of the tweets are:

![output](https://user-images.githubusercontent.com/97375173/187124255-734f784f-4286-4b56-917e-1038b66d2cec.png)

