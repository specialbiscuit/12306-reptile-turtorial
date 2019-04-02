# 12306 数据爬虫

备注: 本项目借鉴实验楼平台的 实现火车票查询![https://www.shiyanlou.com/courses/623/labs/2072/document] 功能，纯属自娱自乐。
##该项目使用的是python3

##项目中需要用到一下扩展包:
  - requests 请求包 
  - docopt 解析命令行参数
  - prettytable table结构化界面
  - colorama 上色
  
##自行添加如上包
```
pip install requests docopt prettytable colorama
```

##python doc设置, 大同小异, 复制过来的
"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
  
##数据源
12306API: https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-04-02&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=NJH&purpose_codes=ADULT (打开12306选票列表，f12查看network的请求)

问题：以上链接发现，出发和到站地点都是代号来代替中文筛选
解决：
https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971
有个json map 解析到本地station.py
```
python parse_station.py > station.py
```
the last step:
```
python tickets.py -dg 北京 上海 2019-04-02
```


