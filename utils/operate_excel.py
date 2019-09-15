#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 22:06
# @Author  : Mandy
import conftest
import xlrd
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_path=None, sheet_id=None):
        if file_path:
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            try:
                self.file_path = conftest.excel_dir
                sheet_id = 0
            except Exception as msg:
                print(u"文件不存在%s" % msg)
        # 打开文件
        self.workbook = xlrd.open_workbook(self.file_path)
        self.data = self.get_sheet(sheet_id)

    """获取表单"""
    def get_sheet(self, i=0):
        sheet = self.workbook.sheets()[i]
        return sheet

    """获取有效行数"""
    def get_rows(self):
        rows = self.data.nrows
        return rows

    """获取有效列数"""
    def get_cols(self):
        cols = self.data.ncols
        return cols

    """获取单元格"""
    def get_cell_value(self, row_num, col_num):
        cell = self.data.cell_value(row_num, col_num)
        return cell

    """写入数据"""
    def write_data(self, row_num, col_num, write_data):
        wb = copy(self.workbook)
        ws = wb.get_sheet(0)
        ws.write(row_num, col_num, write_data)
        wb.save(self.file_path)

    """根据caseid找到对应行的内容"""
    def get_row_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data

    """根据caseid找到对应的行号"""
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_col_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num+1

    """根据行号获取行的内容"""
    def get_row_values(self, row_num):
        row_data = self.data.row_values(row_num)
        return row_data

    """获取一列的内容"""
    def get_col_data(self, col_num=None):
        cols_data = None
        if col_num is not None:
            cols_data = self.data.col_values(col_num)
        else:
            clos_data = self.data.col_values(0)
        return cols_data








