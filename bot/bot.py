import json
import logging
import os

import config

import boto
import tweepy


logger = logging.getLogger()
logger.setLevel(logging.INFO)

auth = tweepy.OAuthHandler(config.twitter['key'], config.twitter['secret'])
auth.set_access_token(config.twitter['token'], config.twitter['token_secret'])
twitter = tweepy.API(auth)

s3conn = boto.connect_s3(config.aws['key'], config.aws['secret'])
bucket = s3conn.get_bucket(config.aws['bucket'])
data_key = bucket.get_key(config.aws['data'], validate=False)


def get_one_word_meaning():
    d = json.loads(data_key.get_contents_as_string())
    ret_v = d.popitem()
    data_key.set_contents_from_string(json.dumps(d))
    logger.info('got thing: {}'.format(ret_v))
    return ret_v


def post_next():
    try:
        word, meaning = get_one_word_meaning()
        status_str = '%s: %s' % (word, meaning)
        twitter.update_status(status=status_str)
        logger.info('updated status')
    except Exception, e:
        logger.error(e)


def handler_lew(event, context):
    post_next()
