#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mastodon import StreamListener
import re

class Streamer(StreamListener):
    '''Override StreamListenerClass on streaming.py.'''

    def __init__(self):
        pass

    def on_update(self, status):
        '''Behavior when streaming is updated.'''
        pattern_content1=re.compile('<.*?>')
        pattern_content2=re.compile('http[s]?.*')
        pattern_content3=re.compile('\#.*[\s]*')
        time=status['created_at'].replace('T',' ').split('.')[0]
        content=pattern_content1.sub('',status['content'])
        content=pattern_content2.sub('',content)
        content=pattern_content3.sub('',content)
        username=status['account']['display_name']
        text = username+'('+time+'): '+content
        print(text)
