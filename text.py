import os, textwrap
from datetime import datetime


def linuxCmd(cmd):
    import subprocess
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

mpcText = linuxCmd('mpc')

if mpcText.splitlines()[0][0:12] == 'NPO Radio2: ':
    trackText = textwrap.fill(mpcText.splitlines()[0][12:],28)
else:
    trackText = textwrap.fill(mpcText.splitlines()[0],28)
text = 'KNOPPEN\n1. Next track    2.Mute\n3. Volume up    4. Volume down'    
text += '\n\n' + datetime.now().strftime('%H:%M - %d-%m-%y')
text += '\n' + trackText    
textFile = open('text.txt','w')
n = textFile.write(text)
textFile.close()
