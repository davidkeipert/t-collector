import requests
import urllib.parse
import re, os, sys
import config
from requests.models import PreparedRequest

token = "Bearer " + config.bearerToken
id = ""

# check for valid arguments
if len(sys.argv) > 2:
    sys.exit("invalid arguments have been used.\nBye...")
else:
    id = re.search("([^\/]+$)", sys.argv[1]).group()

def check_url(url):
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except requests.exceptions.MissingSchema as e:
        sys.exit("Invalid URL. Pls make sure the Twitter url is correct.")

tweetData = requests.get("https://api.twitter.com/2/tweets/" + id + "?expansions=attachments.media_keys&tweet.fields=conversation_id,author_id&media.fields=url,media_key",
                         headers={"Authorization": token})

tweet = tweetData.json()
linkList = []
tweetMedia = tweet.get("includes").get("media")
for d in tweetMedia:
    try:
        url = d.get("url")
        if url.endswith('.jpg'):
            url = url[:-4]
        linkList.append(url)
    except Exception as e:
        print(str(e))

author = tweet["data"]["author_id"]
conversation = tweet["data"]["conversation_id"]
print("Author: " + author)
print("Conversation ID: " + conversation)


conversationQuery = urllib.parse.quote(
    "conversation_id:" + conversation + " from:" + author)

conversationURL = "https://api.twitter.com/2/tweets/search/recent?query=" + conversationQuery + \
    "&expansions=attachments.media_keys&media.fields=url,media_key&tweet.fields=conversation_id&max_results=100"

thread = requests.get(conversationURL, headers={
                      "Authorization": token}).json()
currentItemIndex = 0
media = {}
try:
    media = thread.get("includes").get("media")
except Exception as e:
    print(str(e) + "\nCouldn't find media in thread.")

for d in media:
    try:
        url = d.get("url")
        if url.endswith('.jpg'):
            url = url[:-4]
        linkList.append(url)
    except Exception as e:
        print(str(e) + "\nMedia has no URL")


mediaCount = len(linkList)
try:
    for link in linkList:
        currentItemIndex += 1
        print(f'Downloading Media {currentItemIndex}/{mediaCount}', end='\r')
        filename = re.search("([^\/]+$)", link).group() + ".jpg"
        link += "?format=jpg&name=orig"
        file = open(filename, "wb")
        file.write(requests.get(link).content)
        file.close()
except Exception as e:
    print(str(e))

print("\n Finished downloading media from thread.")
