#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mastodon import StreamListener
import re
import subprocess

class Streamer(StreamListener):
    '''Override StreamListenerClass on streaming.py.'''

    def __init__(self,speaker_info={}):
        if(len(speaker_info)!=0):
            self.__set_speaker_info(speaker_info)
        else:
            self.__set_speaker_info({})

    def __set_speaker_info(self,speaker_info):
        self.__speaker_info=speaker_info

    def get_speaker_info(self):
        return self.__speaker_info

    def on_update(self, status):
        '''Behavior when streaming is updated.'''
        pattern_content1=re.compile('<.*?>')
        pattern_content2=re.compile('http[s]?.*[\s$]*?')
        pattern_content3=re.compile('\#.*[\s]*')
        time=status['created_at'].replace('T',' ').split('.')[0]
        content=pattern_content1.sub('',status['content'])
        content=pattern_content2.sub('',content)
        content=pattern_content3.sub('',content)
        username=status['account']['display_name']
        text = username+'('+time+'): '+content
        print(text)
        if(len(self.get_speaker_info())!=0):
            if(self.get_speaker_info()['speaker_type']=='SofTalk'):
                proc=subprocess.Popen(['SofTalk.exe', '/X:1',
                    ' /V:'+self.get_speaker_info()['speaker_volume'],
                    ' /S:'+self.get_speaker_info()['speaker_speed'],
                    ' /T:'+self.get_speaker_info()['speaker_voicetype'],
                    ' /W:'+content])
