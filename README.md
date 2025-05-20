# 小饅頭の部屋 ー RSS收藏夹

 🔗 https://hst1189.github.io/gmerss
 
## 文件结构
```
Gmerss.py　　   ←爬虫
docs
　∟index.html　 ←网页 js,css直接写里面了
```

## 设置
```
- displayDay=100   # 抓取多久前的内容  #最近100天（约3个月）
- displayMax=300   # 每个RSS最多抓取数 #300个（概算一天3个）
- weeklyKeyWord="" # 周刊过滤关键字
- rssBase={        # 抓取内容
    "HelloGitHub月刊":{
        "url":"https://hellogithub.com/rss",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S +0800",
        "nameColor":"#d00150"
    },
    "xxxx月刊":{
        "url":"https://xxx.com/rss",
        "type":"weekly",
        "timeFormat":"%a, %d %b %Y %H:%M:%S +0800",
        "nameColor":"#fff"
    }
 }


date_str_tz = 'Thu Feb 11 17:21:52 +0900 2021'
format_str_tz = '%a %b %d %H:%M:%S %z %Y'

date_str_tz = '2024-11-23 11 17:21:52 +0900'
format_str_tz = '%Y-%b-%d %H:%M:%S %z '

date_str_tz = 'Thu Feb 11 17:07:53 JST 2021'
format_str_tz = '%a %b %d %H:%M:%S %Z %Y'
 
```

---
RSS-Reader All in Github | Powered by ❤️ [Meekdai/Gmerss](https://github.com/Meekdai/Gmerss)
