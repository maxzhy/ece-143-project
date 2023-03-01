'''
Description: Plot timeline from dataset

Author: Zhaoyang
'''

import csv
from pyecharts.charts import Line
from pyecharts import options as opts

count_csv = './dataset/station_count.csv'
all_data = []

with open(count_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        all_data.append(row)

x_data = all_data[0]

(
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="Num of charging outlets",
        #stack="总量",
        y_axis=all_data[1],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="Num of stations",
        y_axis=all_data[2],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="Num of Level 1 charger",
        y_axis=all_data[3],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="Num of Level 2 charger",
        y_axis=all_data[4],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="Num of DC charger",
        y_axis=all_data[5],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="", pos_top='5%'),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("count_with_time.html")
)