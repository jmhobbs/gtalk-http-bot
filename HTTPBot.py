#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyGtalkRobot import GtalkRobot
import requests


class HTTPBot(GtalkRobot):
    '''
    This bot takes a google talk message, and does a GET request
    to the provided endpoint, then replies to the user the text
    response from that HTTP request.
    '''

    def setEndpoint(self, endpoint):
        self.endpoint = endpoint

    def command_001_postback(self, user, message, args):
        '''.*'''
        print '%s --> %s' % (user.getStripped(), message)
        r = requests.get(self.endpoint, params={'message': message, 'user': user.getStripped()})
        print r.status_code, '-', r.text
        if r.status_code != 200:
            self.replyMessage(user, "Ooops, an error occurred!")
        else:
            self.replyMessage(user, r.text)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='HTTP Google Talk Bot')
    parser.add_argument('gtalk_email', type=str, help='GTalk email address')
    parser.add_argument('gtalk_password', type=str, help='GTalk password')
    parser.add_argument('url', type=str, help='where to send requests')

    args = parser.parse_args()

    bot = HTTPBot()
    bot.setState('available', "HTTP Bot")
    bot.setEndpoint(args.url)
    bot.start(args.gtalk_email, args.gtalk_password)
