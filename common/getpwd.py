import os
import time

def data_dir(data=None,fileName=None):
    '''查找文件路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)

def getNowTime():
    return time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))

def get_cwd(cwd):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),cwd)

#print(get_cwd('report'))

#print(data_dir('report',getNowTime()+'testReport.html'))

#print(data_dir('report','2019-04-08_16-55-21testReport.html'))