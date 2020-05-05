import praw
import weather

reddit = praw.Reddit('bot1')

print(weather.forecast())

subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")