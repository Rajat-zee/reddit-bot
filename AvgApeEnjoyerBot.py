import praw
import time
import os

def bot_login():
	print("Logging in...")
	r = praw.Reddit(username = "AvgApeEnjoyerBot",
				password = "ApesTogetherStrong",
				client_id = "zO4gKJiQAbnGqQ",
				client_secret = "SLSX_8_pD6vZmvwE54hOhyqYNtWH_Q",
				user_agent = "<console::>")
	print("Logged in!")

	return r

def run_bot(r, comments_replied_to):
	print("Searching last 1,000 comments")

	for comment in r.subreddit('wallstreetbets').comments(limit=1000):
		if("apes"or'Apes'or'ape'or'Ape' in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me()):
			print("String with \"Ape\" found in comment " + comment.id)
			comment.reply("Apes together stong")
			print("Replied to comment " + comment.id)

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print("Search Completed.")

	print(comments_replied_to)

	print("Sleeping for 10 seconds...")
	#Sleep for 10 seconds...		
	time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
	run_bot(r, comments_replied_to)