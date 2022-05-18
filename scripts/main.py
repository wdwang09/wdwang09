import config
from request_info import request_info
from render import render

exclude_lang = config.exclude_lang
exclude_repo = config.exclude_repo
top_x_language = config.top_x_language

d = request_info()
if d is None:
    print("Fail to request API.")
    exit(1)

repos = d["data"]["user"]["repositories"]["nodes"]
names = []

code_sizes = {}

for repo in repos:
    name = repo["name"]
    if name.lower() in exclude_repo:
        continue
    names.append(name)
    for node in repo["languages"]["edges"]:
        size = node["size"]
        lang = node["node"]["name"]
        if lang.lower() in exclude_lang:
            continue
        code_sizes[lang] = code_sizes.get(lang, 0) + size

code_sizes_list = list(code_sizes.items())
code_sizes_list.sort(key=lambda x: x[1], reverse=True)
# print(names)
# print(code_sizes_list)

code_size_sum = 0
for x in code_sizes_list:
    code_size_sum += x[1]

code_sizes_list = code_sizes_list[:top_x_language]

block_t = "█"
block_f = "░"
block_len = 25

lang_len = 0
for lang, _ in code_sizes_list:
    lang_len = max(lang_len, len(lang))

bars = []

for lang, size in code_sizes_list:
    lang = " " * (lang_len - len(lang)) + lang
    percentage = size / code_size_sum
    true_num = round(block_len * percentage)
    false_num = block_len - true_num
    bar = "{}: {}{} {:.2%}".format(
        lang, block_t * true_num, block_f * false_num, percentage
    )
    bars.append(bar)

render(bars)
