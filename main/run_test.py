#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 17:18
# @Author  : Mandy
import json

from common.test_method import RunMethod
from data.get_data import GetSheetData
from utils.common_util import CommonUtil


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetSheetData()
        self.common_util = CommonUtil()

    def go_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.is_run(i)
            id = self.data.get_id(i)
            url = self.data.get_url(i)
            method = self.data.get_method(i)
            header = self.data.get_header(i)
            depend_id = self.data.get_depend_id(i)
            depend_data = self.data.get_depend_data(i)
            depend_key = self.data.get_depend_key(i)
            data = self.data.get_request_data(i)
            expect = self.data.get_expect(i)

            if is_run:
                res = self.run_method.main(method, url, header, data)
                # 把结果写入excel
                # print(expect)
                # print(res)
                if self.common_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    print(u"测试通过")
                else:
                    self.data.write_result(i, res)
                    print(u"测试失败")
                return res


run = RunTest()
run.go_run()



