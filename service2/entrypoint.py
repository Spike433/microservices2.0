import requests
import sys

SERVICE1_URL = "http://10.48.1.1:8080"

message = requests.get('https://api.github.com').text # (sys.stdin.readline() , lets use this website for testing inst$

data = ["md5", message]

print("Hash for website https://api.github.com is : "+requests.post(SERVICE1_URL, data="\n".join(data)).text) # command tested with 'https://httpbin.org/post' website

#with .post() I get Response<200> which is OK but I want hash that watchdog returns to me

'''

 docs for watchdog is terrible, I would use https://github.com/openfaas/python-flask-template beacuse you can
 see in code what is happening

 they moved orginal watchtog https://github.com/openfaas/faas/tree/master/watchdog and renamed it to 
 classic https://github.com/openfaas/classic-watchdog/ to confuse me to maximum

 in the end, I just accepted that watchdogs will comunicate with each other via stdin and stdout 

'''

