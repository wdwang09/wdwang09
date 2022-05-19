from request_info import request_info
from get_bar import get_bar
from render import render

d = request_info()
if d is None:
    print("Fail to request API.")
    exit(1)
bars = get_bar(d)
render(bars)
