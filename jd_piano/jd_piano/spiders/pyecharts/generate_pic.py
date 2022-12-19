# Description ==> TODO
# BelongsProject ==> project_piano
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-12-18 11:49:42
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from pyecharts import options as opts
from pyecharts.charts import Pie
from urllib import request
from lxml import etree

import json
import jsonpath

json_p = json.load(open(file=r'../pianos/pianos.json', mode='r', encoding='utf-8'))

json_brand = jsonpath.jsonpath(json_p, expr='$..brand')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

url = 'https://list.jd.com/list.html?cat=6233%2C18615%2C18686&psort=4&psort=4&page=1&s=1&click=0'

request01 = request.Request(url=url, headers=headers)

resp01 = request.urlopen(request01)

brand_ = etree.HTML(resp01.read().decode('utf-8'))

brand_l0 = brand_.xpath('//div[@class="sl-v-logos"]//a/@title')

brand_l = []

for l in range(len(brand_l0)):
    brand_l.append(str(brand_l0[l]).split('（')[0])

others = 0

for i in range(len(brand_l)):
    locals()[str(brand_l[i])] = 0

for b in range(len(json_brand)):
    for j in range(len(brand_l)):
        if str(json_brand[b]).find(brand_l[j]) >= 0:
            locals()[brand_l[j]] = locals()[brand_l[j]] + 1
            break
        if j == (len(brand_l) - 1):
            others = others + 1

brand_list = [
    brand_l[0],
    brand_l[1],
    brand_l[3],
    brand_l[4],
    brand_l[9],
    brand_l[10],
    brand_l[16],
    brand_l[17],
    brand_l[24],
    brand_l[26],
    'others'
]

num_list = [
    locals()[brand_l[0]],
    locals()[brand_l[1]],
    locals()[brand_l[3]],
    locals()[brand_l[4]],
    locals()[brand_l[9]],
    locals()[brand_l[10]],
    locals()[brand_l[16]],
    locals()[brand_l[17]],
    locals()[brand_l[24]],
    locals()[brand_l[26]],
    others
]

c = (
    Pie(init_opts=opts.InitOpts(height='800px'))
        .add("", [list(z) for z in zip(brand_list, num_list)])
        .set_colors(["blue", "green", "aqua", "red", "pink", "orange", "purple"])
        .set_global_opts(title_opts=opts.TitleOpts(title="京东钢琴品牌分布扇形图",pos_top='50px'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("pie_set_color.html")
)
