#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 22:11
# @Author  : Mandy


class CommonUtil:
    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否在另一个字符串中
        :param str_one:
        :param str_two:
        :return: flag
        '''
        flag = None
        if isinstance(str_one, str):
            str_one = str_one.encode('unicode-escape').decode('string-escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
