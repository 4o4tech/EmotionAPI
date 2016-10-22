########### Python 2.7 #############
import httplib, urllib, base64,os

body='''
{
"url": "http://imgtu.5011.net/uploads/content/20160918/2485321474183930.jpg"
}
'''

def key(self):
    # path = os.path.abspath('/home/jimze/db.txt')
    path = os.path.abspath('d:/emotion_key.txt')
    dbFile = open(path)
    key = dbFile.readlines()
    return key


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key()
}

params = urllib.urlencode({

})


try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST","/emotion/v1.0/recognize?%s" % params,body,headers)
    response = conn.getresponse()
    data = response.read()
    print data
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

