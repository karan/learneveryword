import os

import boto
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, token_secret)
twitter = tweepy.API(auth)


def _get_current_index():
    if not(os.path.isfile(index_file_name)):
        return 0
    with open(index_file_name) as index_fh:
        return int(index_fh.read().strip())


def _increment_index(index):
    with open(index_file_name, "w") as index_fh:
        index_fh.truncate()
        index_fh.write("%d" % (index + 1))
        index_fh.close()


def _get_current_line(index):
    with open(source_file_name) as source_fh:
        # read the desired line
        for i, status_str in enumerate(source_fh):
            if i == index:
                break
        return status_str.strip()


def post_next():
    index = _get_current_index()
    status_str = _get_current_line(index)
    if prefix:
        status_str = prefix + status_str
    if suffix:
        status_str = status_str + suffix
    twitter.update_status(status=status_str,
                               lat=lat, long=long,
                               place_id=place_id)
    _increment_index(index)


def handler_lew(event, context):
    post_next()
