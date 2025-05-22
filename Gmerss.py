# -*- coding: utf-8 -*-
import os
import json
import time
import feedparser

######################################################################################
displayDay=10000 # 抓取多久前的内容  #最大
displayMax=10000 # 每个RSS最多抓取数 #最大
weeklyKeyWord="" # 周刊过滤关键字

rssBase={
    "不死鸟 - 分享为王":{
        "url":"https://iui.su/feed",
        "type":"post",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#ff96b4"
    },

    "独立开发者出海周刊":{
        "url":"https://gap.weijunext.com/rss.xml",
        "type":"post",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#ff6347"
    },
 
    "猫鱼周刊":{
        "url":"https://ameow.xyz/feed/categories/weekly.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#F5DEB3"
    },

    "潮流周刊":{
        "url":"https://weekly.tw93.fun/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#F0E68C"
    },

    "老胡的周刊":{
        "url":"https://weekly.howie6879.com/rss/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#DEB887"
    },
    
    "阮一峰":{
        "url":"http://www.ruanyifeng.com/blog/atom.xml",
        "type":"weekly",
        "timeFormat":"%Y-%m-%dT%H:%M:%SZ",
        "nameColor":"#B0E0E6"
    },
     
    "HelloGitHub月刊":{
        "url":"https://hellogithub.com/rss",
        "type":"monthly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#98FB98"
    },
    
    "二丫讲梵":{
        "url":"https://wiki.eryajf.net/learning-weekly.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#87CEFA"
    },

    "小众软件":{
        "url":"https://feeds.appinn.com/appinns/",
        "type":"daily",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#7FFFD4"
    },
    
    "Portable Apps":{
        "url":"https://feeds.feedburner.com/portableapps_com",
        "type":"daily",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"6495ED"
    },

    "不上班研究所":{
        "url":"https://www.toocool.cc/feed",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#ff7f50"
    },

    "独立开发变现":{
        "url":"https://www.ezindie.com/feed/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#ffefd5"
    },
        
    "豌豆花下猫":{
        "url":"https://pythoncat.top/rss.xml",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S GMT",
        "nameColor":"#CCFF99"
    },
    
    "Publickey":{
        "url":"https://www.publickey1.jp/atom.xml",
        "type":"post",
        "timeFormat":"%Y-%m-%dT%H:%M:%SZ",
        "nameColor":"#00CCCC"
    },
    
    "Qiita_kjm_nuco":{
        "url":"https://qiita.com/kjm_nuco/feed.atom",
        "type":"post",
        "timeFormat":"%Y-%m-%dT%H:%M:%S%z",
        "nameColor":"#660066"
    },
    
    "老王写真乐园关注":{
        "url":"https://www.laowangidol.xyz/feed/",
        "type":"post",
        "timeFormat":"%a, %d %b %Y %H:%M:%S %z",
        "nameColor":"#ffd700"
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
