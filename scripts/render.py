import time

import config


def render(bars: list[str]):
    template_file = config.template_file
    output_file = config.output_file

    content = None

    with open(template_file, "r", encoding="utf-8") as f:
        content = f.read()

    bar_location = "{{ bar }}"
    bar_idx = content.find(bar_location)
    if bar_idx == -1:
        return
    content = (
        content[:bar_idx] + "\n".join(bars) + content[bar_idx + len(bar_location) :]
    )

    # print(content)

    t = time.strftime("%a %b %d %H:%M %Y (UTC)", time.gmtime())
    time_location = "{{ time }}"
    time_idx = content.find(time_location)
    if time_idx == -1:
        return
    content = content[:time_idx] + t + content[time_idx + len(time_location) :]

    # print(content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
