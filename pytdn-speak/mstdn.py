#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import closing
import requests
from mastodon import Mastodon
import re

class Mstdn(Mastodon):
    '''Override MastodonClass on Mastodon.py.'''

    def local_stream(self, listener):
        '''
        Streams local events. 'listener' should be a subclass of
        StreamListener.
        '''
        return self.__stream('/api/v1/streaming/public/local', listener)

    def __stream(self, endpoint, listener, params = {}):
        """
        Internal streaming API helper.
        """

        headers = {}
        if self.access_token != None:
            headers = {'Authorization': 'Bearer ' + self.access_token}

        url = self.api_base_url + endpoint
        with closing(requests.get(url, headers = headers, data = params, stream = True)) as r:
            listener.handle_stream(r.iter_lines())

