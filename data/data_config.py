
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 14:49
# @Author  : Mandy
from utils.operate_json import OperationJson


class global_var:
    op_json = OperationJson()
    col_case_id = 0
    col_api = 1
    col_is_run = 2
    col_method = 3
    col_header = 4
    col_depend_id = 5
    col_depend_data = 6
    col_depend_key = 7
    col_request_data = 8
    col_expect = 9
    col_result = 10

    def get_col_id(self):
        return global_var.col_case_id

    def get_col_api(self):
        return global_var.col_api

    def get_col_run(self):
        return global_var.col_is_run

    def get_col_method(self):
        return global_var.col_method

    def get_col_header(self):
        return global_var.col_header

    def get_col_depend_id(self):
        return global_var.col_depend_id

    def get_col_depend_data(self):
        return global_var.col_depend_data

    def get_col_depend_key(self):
        return global_var.col_depend_key

    def get_col_request_data(self):
        return global_var.col_request_data

    def get_col_expect(self):
        return global_var.col_expect

    def get_col_result(self):
        return global_var.col_result

    def get_header_data(self):
        header = self.op_json.get_data('headers')
        return header

