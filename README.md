# pytdn-speak
get timeline and speak it by using Mastodon.py

Usage:
  1) Install Mastodon.py by pip  
    `# python -m pip install Mastodon.py`
  2) Edit mstdn.conf  
  3) Run streaming.py  
    `# python pytdn-speak.py`
  4) End when you're bored (Ctrl + c)  

Option:
    A) Using SofTalk for speaking.
        1) Make speak_enable 'True'  
        2) Make speaker_type 'SofTalk'  
        3) Edit [softalk] section 
        4) Add SofTalk.exe to $PATH  
            `# PATH=$PATH:<PATH to SofTalk.exe>`
    B) Using VOICEROID for speaking.
        1) Make speak_enable 'True'  
        2) Make speaker_type 'VOICEROID'
        3) Add vrx.exe to $PATH  
            `# PATH=$PATH:<PATH to vrx.exe>`  
        Note: This program pass speaking texts to VOICEROID vir vrx.exe.  
              Beforehand, you have to arrange its settings.  
              You can find it here: http://publish-tool.blogspot.jp/  
