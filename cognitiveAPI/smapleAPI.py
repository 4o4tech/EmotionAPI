########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '770f02c81d39406ba202e374f313d76c'
}

params = urllib.urlencode({

})

body='''
{
"url": "http://imgtu.5011.net/uploads/content/20160918/2485321474183930.jpg"
}
'''



try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST","/emotion/v1.0/recognize?%s" % params,body,headers)
    response = conn.getresponse()
    data = response.read()
    print data
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

