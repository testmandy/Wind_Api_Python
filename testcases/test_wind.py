#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 21:57
# @Author  : Mandy
import conftest
from common.common_url import CommonUrl
from utils.operate_json import OperationJson
from utils.read_ini import ReadIni
from common.test_method import RunMain
from data.get_sheet_data import GetSheetData

read = ReadIni(conftest.env_dir)
op_json = OperationJson()
common = CommonUrl()
sheet = GetSheetData(1)

class TestWind():
    def test_register(self):
        method = sheet.get_method()
        url = sheet.get_url()
        headers = sheet.get_header()
        data = sheet.get_request_data()
        res = RunMain(method, url, data, headers)
        return res


test = TestWind()
res = test.test_register()
print(res)