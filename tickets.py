# coding: utf-8

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
from docopt import docopt
from station import stations
from prettytable import PrettyTable
from colorama import init, Fore

import requests

init()
header = '车次 车站 时间 历时 商务座 一等 二等 软卧 硬卧 硬座 无座'.split()
code2stations = {v: k for k, v in stations.items()}


def cli():
    """command-line interface"""
    arguments = docopt(__doc__)

    # 参数
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    options = '-gdtkz' if not options else options

    from_station = stations.get(arguments['<from>']) #出发站
    to_station = stations.get(arguments['<to>']) #入站点
    date = arguments['<date>'] #出发时间

    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station
    )

    r = requests.get(url, verify=False)
    rts = r.json()['data']['result']
    print(rts)

    tablev = PrettyTable()
    tablev._set_field_names(header)

    for rt in rts:
        cm = rt.split('|')
        if not cm[3][0].lower() in options:
            continue
        # train_no = cm[2];
        # train_no = cm[2];
        station_train_code = cm[3]
        # start_station_telecode = cm[4];
        # end_station_telecode = cm[5];
        from_station_telecode = cm[6]
        to_station_telecode = cm[7]
        start_time = cm[8]
        arrive_time = cm[9]
        lishi = cm[10]
        canWebBuy = cm[11]
        start_train_date = cm[13]
        location_code = cm[15]
        # 高级软卧
        gr_num = cm[21] or '--'
        # qt_num = cm[22];
        # 软卧
        rw_num = cm[23] or '--'
        # rz_num = cm[24];
        tz_num = cm[25] or '--'
        # 无座
        wz_num = cm[26] or '--'
        # 硬卧
        yw_num = cm[28] or '--'
        # 硬座
        yz_num = cm[29] or '--'
        # 二等座
        ze_num = cm[30] or '--'
        # 一等座
        zy_num = cm[31] or '--'
        # 商务座
        swz_num = cm[32] or '--'
        # 动卧
        srrb_num = cm[33]
        tablev.add_row([
            station_train_code,
            '\n'.join([
                Fore.GREEN + code2stations[from_station_telecode] + Fore.RESET,
                Fore.RED + code2stations[to_station_telecode] + Fore.RESET]),
            '\n'.join([
                Fore.GREEN + start_time + Fore.RESET,
                Fore.RED + arrive_time + Fore.RESET]),
            lishi,
            swz_num,
            zy_num,
            ze_num,
            rw_num,
            yw_num,
            yz_num,
            wz_num
        ])

    print(tablev)


if __name__ == '__main__':
    cli()

