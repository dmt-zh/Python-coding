# When users post an update on social media,such as a URL, image, status update etc.,
# other users in their network are able to view this new post on their news feed.
# Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
# Since sometimes posts are published and viewed in different time zones, this can be confusing.
# You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

import datetime
def time_delta(time1, time2):
    t1 = datetime.datetime.strptime(time1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(time2, '%a %d %b %Y %H:%M:%S %z')
    delta = round(abs((t1 - t2).total_seconds()))
    return str(delta)