from http.client import HTTPSConnection
import json

import config

from typing import Union, Dict

# query is from:
# https://github.com/anuraghazra/github-readme-stats/blob/master/src/fetchers/top-languages-fetcher.js

# learn more:
# https://docs.github.com/en/graphql/reference/objects#topic
# https://docs.github.com/en/graphql/reference/objects#repository

query = """
query userInfo($login: String!) {
    user(login: $login) {
        repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {
            nodes {
                name
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
                    edges {
                        size
                        node {
                            color
                            name
                        }
                    }
                }
            }
        }
    }
}
"""


def request_info() -> Union[Dict, None]:
    user = config.user
    token = config.token

    headers = dict()
    headers["Authorization"] = "token {}".format(token)
    headers["User-Agent"] = "My-App"

    data = dict()
    data["variables"] = {"login": user}
    data["query"] = query

    connection = HTTPSConnection("api.github.com")
    connection.request("POST", "/graphql", body=json.dumps(data), headers=headers)
    res = connection.getresponse()
    if res.status != 200:
        print(res.status, res.reason)
        return None

    data = eval(res.read())
    return data
