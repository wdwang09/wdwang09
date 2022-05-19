import os

user = os.getenv("USER")
token = os.getenv("API_TOKEN")
exclude_lang = os.getenv("EXCLUDE_LANG")  # for empty str, you can write ":"
exclude_repo = os.getenv("EXCLUDE_REPO")  # for empty str, you can write ":"

try:
    import config_private  # don't commit this file

    user = config_private.user
    token = config_private.token
    exclude_lang = config_private.exclude_lang
    exclude_repo = config_private.exclude_repo
except ImportError:
    pass

top_x_language = 5

template_file = "template.md"
output_file = "README.md"

if not user:
    user = ""

if not token:
    token = ""

if exclude_lang:
    exclude_lang = exclude_lang.split(":")
else:
    exclude_lang = []
for i in range(len(exclude_lang)):
    exclude_lang[i] = exclude_lang[i].lower()

if exclude_repo:
    exclude_repo = exclude_repo.split(":")
else:
    exclude_repo = []
for i in range(len(exclude_repo)):
    exclude_repo[i] = exclude_repo[i].lower()
