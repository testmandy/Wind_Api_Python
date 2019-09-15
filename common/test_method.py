#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 21:40
# @Author  : Mandy
import json

import requests


class RunMethod:
    def __init__(self):
        pass

    def get_method(self, url, data, headers=None):
        if headers is None:
            res = requests.get(url=url, data=data).json
        else:
            res = requests.get(url=url, headers=headers, data=data).json()
        res = json.dumps(res, indent=2)
        return res

    def post_method(self, url, data, headers=None):
        if headers is None:
            res = requests.post(url=url, data=data).json
        else:
            res = requests.post(url=url, headers=headers, data=data).json()
        res = json.dumps(res, indent=2)
        return res

    def main(self, method, url, headers, data):
        if method == 'get':
            res = self.get_method(url, data, headers)
        else:
            res = self.post_method(url, data, headers)
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return res

