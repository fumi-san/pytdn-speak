#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
from mstdn import Mstdn
from streamer import Streamer

class Config:
    def __init__(self,filepath):
        self.__username='username'
        self.__password='password'
        self.__client_id='client_id'
        self.__client_secret='client_secret'
        self.__api_base_url='https://mstdn-workers.com'
        reader=configparser.SafeConfigParser()
        reader.read(filepath)
        self.__set_username(reader.get('mastodon_user_settings', 'username'))
        self.__set_password(reader.get('mastodon_user_settings', 'password'))
        self.__set_client_id('ab5d9c575b91c1f46c2da284a62a82fe1b5adfa91b618e597025651ab0cb6d7f')
        self.__set_client_secret('e25bb615a28ffef88f9d167e8da9e742c4e8a18af8e44e20e0e5b37a1d4f4138')
        self.__set_api_base_url(reader.get('mastodon_base_settings', 'api_base_url'))

    def __set_username(self,username):
            self.__username=username
    def __set_password(self,password):
            self.__password=password
    def __set_client_id(self,client_id):
            self.__client_id=client_id
    def __set_client_secret(self,client_secret):
            self.__client_secret=client_secret
    def __set_api_base_url(self,api_base_url):
            self.__api_base_url=api_base_url
    def get_username(self):
            return self.__username
    def get_password(self):
            return self.__password
    def get_client_id(self):
            return self.__client_id
    def get_client_secret(self):
            return self.__client_secret
    def get_api_base_url(self):
            return self.__api_base_url

if __name__ == "__main__":
    filepath="./pytdn.conf"
    cf = Config(filepath)
    mastodon=Mstdn(client_id=cf.get_client_id(), client_secret=cf.get_client_secret(), api_base_url=cf.get_api_base_url())
    access_token=mastodon.log_in(cf.get_username(),cf.get_password())
    listener=Streamer()
    mastodon.local_stream(listener)
