#coding=utf-8

try:
    from  setuptools import setup
except ImportError:
    from distutils.core import  setup

config = {
    'description':'My skeleton',
    'author':'Elanqueen',
    'url':'URL to get it at.',
    'download_url':'Where to download it.',
    'author_email':'775254855@qq.com',
    'version':'1.0',
    'install_requires':['unittest'],
    'packages':['NAME'],
    'scripts':[],
    'name':'skeleton'

}

setup(**config)