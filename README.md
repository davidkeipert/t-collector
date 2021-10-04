A simple python script that downloads all images posted by the same author in a given twitter thread. Requires that you have a Twitter Developer account with API v2 keys.

## Installation:

  ```git clone https://github.com/davidkeipert/t-collector.git```
  
  Open [example_config.py](example_config.py) and add your Twitter API Bearer Token. Then rename the file to config.py.
  
  If you don't have a Twitter Developer account, go to https://developer.twitter.com/en/apply-for-access to create one.
  

## Usage: 
  ```python3 twitter.py URL```

 - The script expects a Twitter URL of the form https://twitter.com/USERNAME/status/xxxxxxxxxxxxxxxxxx
 - Given a link to a thread on twitter, it will find all the replies in that thread by the same author. This is useful when you want to archive a compilation of photo dump that someone posted.
 - Due to limitations of the Twitter API, we can only find thread replies that were posted less than 7 days ago. If no replies can be found, only images attached to the original post will be found and downloaded.
 - Images will be downloaded to the directory in which this script resides.


## Known Issues:

  - previously downloaded photos in the scripts directory will be overwritten if you download them again. Should rarely be problematic because the filenames reflect the unique id given to them by twitter.
  - can't choose a directory in which to download photos. Might add this functionality soon.
  - will probably break if you pass a twitter URL that's not a twitter.com/USER/status/tweet_id format. Eg. a link directly to a users profile.
  
