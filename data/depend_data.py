#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 22:40
# @Author  : Mandy
from common.test_method import RunMethod
from data.get_data import GetSheetData
from utils.operate_excel import OperationExcel


class DependentData:
    def __init__(self, case_id):
        self.excel = OperationExcel()
        self.data = GetSheetData()
        self.run_method = RunMethod()
        self.case_id = case_id

    def get_case_line_data(self, case_id):
        row_data = self.excel.get_row_data(case_id)
        return row_data

    def run_dependent(self):
        row = self.excel.get_row_num(self.case_id)
        url = self.data.get_url(row)
        method = self.data.get_method(row)
        header = self.data.get_header(row)
        data = self.data.get_request_data(row)

        res = self.run_method.main(method, url, header, data)
        return res

    def get_depend_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()






