#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 14:37
# @Author  : Mandy
import conftest
from utils.operate_excel import OperationExcel
from utils.operate_json import OperationJson
from utils.read_ini import ReadIni
from data.data_config import global_var


class GetSheetData:
    def __init__(self):
        self.excel = OperationExcel()
        self.data_config = global_var()
        self.read = ReadIni(conftest.env_dir)
        self.op_json = OperationJson()

    """获取case行数"""
    def get_case_lines(self):
        lines = self.excel.get_rows()
        return lines

    """是否运行"""
    def is_run(self, row):
        col = self.data_config.get_col_run()
        run_model = self.excel.get_cell_value(row, col)
        flag = None
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    """获取case id"""
    def get_id(self, row):
        col = self.data_config.get_col_id()
        case_id = self.excel.get_cell_value(row, col)
        return case_id

    """获取api，拼接接口地址"""
    def get_url(self, row):
        col = self.data_config.get_col_api()
        api = self.excel.get_cell_value(row, col)
        url = self.read.get_value('base_url', 'api') + api
        return url

    """获取请求方法"""
    def get_method(self, row):
        col = self.data_config.get_col_method()
        method = self.excel.get_cell_value(row, col)
        return method

    """获取是否有header，是则从json数据中获取headers"""
    def get_header(self, row):
        col = self.data_config.get_col_header()
        header = self.excel.get_cell_value(row, col)
        header_data = self.op_json.get_data('headers')
        if header == 'yes':
            return header_data
        else:
            return None

    """获取依赖的case id"""
    def get_depend_id(self, row):
        col = self.data_config.get_col_depend_id()
        depend_id = self.excel.get_cell_value(row, col)
        if depend_id == '':
            return None
        else:
            return depend_id

    """获取依赖的数据"""
    def get_depend_data(self, row):
        col = self.data_config.get_col_depend_data()
        depend_data = self.excel.get_cell_value(row, col)
        if depend_data == '':
            return None
        else:
            return depend_data

    """获取依赖数据的字段"""
    def get_depend_key(self, row):
        col = self.data_config.get_col_depend_key()
        depend_key = self.excel.get_cell_value(row, col)
        if depend_key == '':
            return None
        else:
            return depend_key

    """根据命名的请求json名，获取请求数据"""
    def get_request_data(self, row):
        col = self.data_config.get_col_request_data()
        request_data_key = self.excel.get_cell_value(row, col)
        request_data = self.op_json.get_data(request_data_key)
        if request_data == '':
            return None
        else:
            return request_data

    """根据sql语句，获取期望值"""
    def get_expect(self, row):
        col = self.data_config.get_col_expect()
        expect = self.excel.get_cell_value(row, col)
        return expect

    """把结果写入实际结果中"""
    def write_result(self, row, result,):
        col = self.data_config.get_col_result()
        self.excel.write_data(row, col, result)

# sheet = GetSheetData()
# i = 1
# print(sheet.get_id(i))
# print(sheet.get_url(i))
# print(sheet.get_method(i))
# print(sheet.get_header(i))
# print(sheet.get_depend_id(i))
# print(sheet.get_depend_data(i))
# print(sheet.get_depend_key(i))
# print(sheet.get_request_data(i))
# print(type(sheet.get_request_data(i)))
# print(sheet.get_expect(i))

