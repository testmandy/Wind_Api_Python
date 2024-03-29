# coding=utf-8
# @Time    : 2019/9/3 11:05
# @Author  : Mandy
import os
import logging
import logging.config

import allure
import pytest
import yaml

project_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(project_dir, 'logs\\')

report_dir = os.path.join(project_dir, 'report\\')
allure_result_dir = os.path.join(project_dir, 'allure_result\\')

elements_dir = os.path.join(project_dir, 'elements')

android_elements_dir = os.path.join(elements_dir, 'android\\elements.ini')
android_axis_dir = os.path.join(elements_dir, 'android\\axis.ini')

screenshots_dir = os.path.join(project_dir, 'screenshots\\')
screenshots_list = os.path.join(project_dir, 'screenshots')

testcase_dir = os.path.join(project_dir, 'testcases\\')
apk_dir = os.path.join(project_dir, 'testapp')

config_dir = os.path.join(project_dir, 'config')

userconfig_dir = os.path.join(config_dir, 'userconfig.yaml')
android_case_dir = os.path.join(testcase_dir, 'android')
env_dir = os.path.join(config_dir, 'env.ini')
data_dir = os.path.join(config_dir, 'data.json')
excel_dir = os.path.join(config_dir, 'case.xls')


def get_logger():
    CONF_LOG = "../config/logging.ini"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()


