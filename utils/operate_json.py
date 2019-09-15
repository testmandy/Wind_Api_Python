#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 21:40
# @Author  : Mandy
import json

import conftest


class OperationJson:
    def __init__(self, file_path=None):
        if file_path is None:
            try:
                self.file_path = conftest.data_dir
            except Exception as msg:
                print(u"文件不存在%s" % msg)
        self.data = self.read_data()

    """
    加载json数据
    """
    def read_data(self):
        with open(self.file_path, 'r') as fp:
            data = json.load(fp)
            return data

    """
    获取value值
    """
    def get_data(self, id):
        return self.data[id]


if __name__ == '__main__':
    op = OperationJson()
    data = op.get_data('headers')
    print(data)


