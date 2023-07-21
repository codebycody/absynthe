import requests 
import os 
import requests
from bs4 import BeautifulSoup


wordlist = './wordlists/common.txt'
soup = BeautifulSoup()
reconData = {}

def fingerPrinter(url):
    noHttp = url.replace('https://', '').replace('http://', '')
    noSubDomain = url.split('.', 1)[1]
    builtWith(noHttp)
    w3Techs(noSubDomain)
    reScan(noHttp)
    return True

def reconDataCheck(key, value):
    if key in reconData:
        reconData[key].append(str(value))
    else:
        reconData[key] = [str(value)]

def builtWith(url):
    # example webpage: https://builtwith.com/sub.site.com
    page = requests.get('https://builtwith.com/' + url)
    soup = BeautifulSoup(page.content, 'html.parser')
    bowlFull = soup.findAll(True, {'class':['card-title']})
    for index, scoop in enumerate(bowlFull):
        if(str(scoop) == '<h6 class="card-title">Frameworks</h6>'):
            values = bowlFull[index].parent.parent.parent.findAll(True, {'class': ['text-dark']})
            for val in values:
                reconDataCheck('Frameworks', val.text)
        elif(str(scoop) == '<h6 class="card-title">Web Servers</h6>'):
            values = bowlFull[index].parent.parent.parent.findAll(True, {'class': ['text-dark']})
            for val in values:
                reconDataCheck('Web Servers', val.text)
        elif(str(scoop) == '<h6 class="card-title">Document Encoding</h6>'):
            values = bowlFull[index].parent.parent.parent.findAll(True, {'class': ['text-dark']})
            for val in values:
                reconDataCheck('Document Encoding', val.text)
        elif(str(scoop) == '<h6 class="card-title">Document Standards</h6>'):
            values = bowlFull[index].parent.parent.parent.findAll(True, {'class': ['text-dark']})
            for val in values:
                reconDataCheck('Document Standards', val.text)
    return reconData

def whatCMS(url):
    # page needs to load look into this
    page = requests.get('https://whatcms.org/?s=' + url)
    soup = BeautifulSoup(page.content, 'html.parser')
    bowlFull = soup.findAll(True, {'class': ['table']})
    print(bowlFull)
    for index, scoop in enumerate(bowlFull):
        print(scoop)
    return True

def w3Techs(url):
    # example webpage: https://builtwith.com/site.com
    page = requests.get('https://w3techs.com/sites/info/' + url)
    soup = BeautifulSoup(page.content, 'html.parser')
    bowlFull = soup.findAll(True, {'class': ['si_h']})
    containers = ['Server-side Programming Language','Client-side Programming Language','Web Server', 'Web Hosting Provider','Data Cent Provider','Data Center Provider','DNS Server Provider','SSL Certificate Authority','Site Elements','Markup Language','Character Encoding', 'Image File Formats', 'Top Level Domain','Server Location','Content Language']
    lastContainer = ''
    for index, scoop in enumerate(bowlFull):
        if(scoop.get_text() in containers):
            tagText = bowlFull[index].findNext('p').findNext('a').get_text()
            pTag = bowlFull[index].findNext('p', {'class': ['si_tech']})
            # multiple values not taken into account like for "site elements"
            if tagText not in containers:
                reconDataCheck(lastContainer, tagText)
            else:
                lastContainer = tagText
    return reconData

def reScan(url):
    # example webpage: https://builtwith.com/subdomain.site.com
    page = requests.get('https://rescan.io/analysis/' + url)
    soup = BeautifulSoup(page.content, 'html.parser')
    bowlFull = soup.find('div', {'class': ['indexpage-content']}).findAll('div', {'class': ['row']})
    containers = []
    for index, scoop in enumerate(bowlFull):
        category = bowlFull[index].find('span', {'class': ['marker__w']}).text.strip(' ')
        value = bowlFull[index].parent.findAll('h4')
    return reconData

def dirb(url):
    arr=[]
    try:
        if url[:7] != 'http://':
            url="http://"+url
        r=requests.get(url)
        if r.status_code == 200:
            print('Host is up.')
        else:
            print('Host is down.')
            return
        if os.path.exists(os.getcwd()+wordlist):
            fs=open(os.getcwd()+wordlist,"r")
            for i in fs:
                print(url+"/"+i)
                rq=requests.get(url+"/"+i)
                if rq.status_code == 200:
                    print(">OK".rjust(len(url+"/"+i)+5,'-'))
                    arr.append(str(url+"/"+i))
                else:
                    print(">404".rjust(len(url+"/"+i)+5,'-'))
            fs.close()
            print("output".center(100,'-'))
            l=1
            for i in arr:
                print(l, "> ", i)
                l+=1
        else:
            print(wordlist+" don't exists in the directory.")
    except Exception as e:
        print(e)
