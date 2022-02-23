import os, textwrap
from datetime import datetime


def linuxCmd(cmd):
    import subprocess
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

#mpcText = linuxCmd('mpc')

# try:
#     if mpcText.splitlines()[0][0:12] == 'NPO Radio2: ':
#         radioAan = True
#         trackText = textwrap.fill(mpcText.splitlines()[0][12:],27)
#     else:
#         radioAan = False
#         trackText = textwrap.fill(mpcText.splitlines()[0],27)
# except:
#     trackText = ''
#     radioAan = False
# text = ''
# iptxt = linuxCmd('ifconfig')
# x=0
# for i in iptxt.splitlines():
#     if i[:5]=='wlan0':
#         text += iptxt.splitlines()[x+1].split()[1]
#         break
#     x += 1
# ssid = open('./wlan.txt','r').read()
# text+= '           ' + ssid.splitlines()[0].split()[1]
try:
    vStatus = linuxCmd(['volumio' ,'status'])
    import json
    data = json.loads(vStatus.replace('\n','').replace('\'',''))
    try:
        trackText = textwrap.fill(data['artist'] + ' - ' + data['title'],27)
    except:
        trackText = ''
    try:
        trackText += '\nAlbum: ' + textwrap.fill(data['album'],27)
    except:
        pass
    try:
        trackText += '\nVolume: ' + textwrap.fill(str(data['volume']),27)
    except:
        pass
    try:
        trackText += '\nStatus: ' + textwrap.fill(data['status'],27)
    except:
        pass
    
    #trackText = data['artist']+ ' - ' + data['title'] + '\nAlbum: '+data['album'] + '\nVolume: ' + str(data['volume']) 
except:
    trackText = ''

text = ''
text += datetime.now().strftime('%H:%M - %d-%m-%y')



# if radioAan == False:
#     try:
#         percentage = int(mpcText.splitlines()[1][-5:-2])
#     except:
#         try:
#             percentage = int(mpcText.splitlines()[1][-4:-2])
#         except:
#             try:
#                 percentage = int(mpcText.splitlines()[1][-3:-2])
#             except:
#                 percentage = 0
#     else:
#         percentage = 0
#     text += '\n['
#     for i in range(1,25):
#         if i < 25 * (percentage/100):
#             text += '#'
#         else:
#             text += '-'
#     text += ']'
text += '\n' + trackText    
textFile = open('text.txt','w')
n = textFile.write(text)
textFile.close()
