import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
#将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']
"""一个列表，列表的元素是字典"""
names,plot_dicts = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value':repo_dict['stargazers_count'],
                 'lable':repo_dict['description'],
                 'xlink':repo_dict['html_url'],
                 }
    plot_dicts.append(plot_dict)
#可视化
my_style = LS('#333366',base_style = LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size =14
my_config.major_lable_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('pyton_repos-2.svg')
# print("Repositories returned:",len(repo_dicts))
# repo_dict = repo_dicts[0]
# """列表中第一个元素，即第一个字典"""
# print("\nKeys:",len(repo_dict))
# """第一个字典，即第一个项目，包含了多少项信息"""
# for key in sorted(repo_dict.keys()):
#     """sorted，返回一个新列表"""
#     print(key +":" + str(repo_dict[str(key)]))