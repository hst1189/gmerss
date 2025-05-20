# -*- coding: utf-8 -*-
import os
import json
import time
import feedparser

######################################################################################
displayDay=365 # 抓取多久前的内容  #最近365天（约1年）
displayMax=3000 # 每个RSS最多抓取数 #3000个（一天10个概算）
weeklyKeyWord="" # 周刊过滤关键字

rssBase={
    "Qiita_kjm_nuco":{
        "url":"https://qiita.com/kjm_nuco/feed.atom",
        "type":"post",
        "timeFormat":"%Y-%m-%dT%H:%M:%S%z",
        "nameColor":"#ff3150"
    },

    "老王写真乐园关注":{
        "url":"https://www.laowangidol.xyz/feed/",
        "type":"post",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#563150"
    },

    "HelloGitHub月刊":{
        "url":"https://hellogithub.com/rss",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#d00150"
    },

    "小众软件":{
        "url":"https://feeds.appinn.com/appinns/",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#df7150"
    },
    
    "Portable Apps":{
        "url":"https://feeds.feedburner.com/portableapps_com",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#ff7950"
    },
    
    "潮流周刊":{
        "url":"https://weekly.tw93.fun/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#bc4c00"
    },

    "老胡的周刊":{
        "url":"https://weekly.howie6879.com/rss/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S +0806",
        "nameColor":"#A333D0"
    },
    
    "独立开发变现":{
        "url":"https://www.ezindie.com/feed/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#a4244b"
    },
    
    "不上班研究所":{
        "url":"https://www.toocool.cc/feed",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#a4ff00"
    },
    
    "二丫讲梵":{
        "url":"https://wiki.eryajf.net/learning-weekly.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#93bd76"
    },
    
    
    "阮一峰":{
        "url":"http://www.ruanyifeng.com/blog/atom.xml",
        "type":"weekly",
        "timeFormat":"%Y-%m-%dT%H:%M:%SZ",
        "nameColor":"#1f883d"
    },

    "豌豆花下猫":{
        "url":"https://pythoncat.top/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#bc4c00"
    }
    
}
######################################################################################

rssAll=[]
info=json.loads('{}')
info["published"]=int(time.time())
info["rssBase"]=rssBase
rssAll.append(info)

displayTime=info["published"]-displayDay*86400

print("====== Now timestamp = %d ======"%info["published"])
print("====== Start reptile Last %d days ======"%displayDay)

for rss in rssBase:
    print("====== Reptile %s ======"%rss)
    rssDate = feedparser.parse(rssBase[rss]["url"])
    i=0
    for entry in rssDate['entries']:
        if i>=displayMax:
            break
        if 'published' in entry:
            published=int(time.mktime(time.strptime(entry['published'], rssBase[rss]["timeFormat"])))

            if entry['published'][-5]=="+":
                published=published-(int(entry['published'][-5:])*36)

            if rssBase[rss]["type"]=="weekly" and (weeklyKeyWord not in entry['title']):
                continue

            if published>info["published"]:
                continue

            if published>displayTime:
                onePost=json.loads('{}')
                onePost["name"]=rss
                onePost["title"]=entry['title']
                onePost["link"]=entry['link']
                onePost["description"]=entry['description']
                onePost["published"]=published
                rssAll.append(onePost)
                print("====== Reptile %s ======"%(onePost["title"]))
                print("====== Reptile %s ======"%(onePost["description"]))
                i=i+1
        else:
            published = None
            print("Warning: 'published' key not found in entry")

            
print("====== Start sorted %d list ======"%(len(rssAll)-1))
#rssAll=sorted(rssAll,key=lambda e:e.__getitem__("published"),reverse=True)

if not os.path.exists('docs/'):
    os.mkdir('docs/')
    print("ERROR Please add docs/index.html")

listFile=open("docs/rssAll.json","w")
listFile.write(json.dumps(rssAll))
listFile.close()
print("====== End reptile ======")
######################################################################################
