#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 22:37
# @Author  : Mandy
import conftest
from utils.read_ini import ReadIni

read = ReadIni(conftest.env_dir)


class CommonUrl:
    def __init__(self):
        self.user_register_url = self.join_url('/user/register')
        self.user_register_url = self.join_url('/user/register')
        self.user_info_url = self.join_url('/user/info')
        self.user_edit_info_url = self.join_url('/user/editInfo')
        self.user_edit_gender_url = self.join_url('/user/editFavGender')
        self.user_basic_info_url = self.join_url('/user/basic')

    def join_url(self, test_url):
        base_url = read.get_value('base_url', 'api')
        url = base_url + test_url
        return url


common = CommonUrl()
print(common.user_register_url)
