# -*- coding: utf-8 -*-
import grpc
import question_pb2
import question_pb2_grpc

address = '47.100.97.93:40722'

# 1.建立与服务器的连接
channel = grpc.insecure_channel(address)
# 2.创建客户端助手(对函数名、参数打包)
stub = question_pb2_grpc.QuestionStub(channel)
# 3.封装请求参数类型对象
request = question_pb2.QuestionRequest()

# 账号
request.user_id = 103
request.user_pin = "UJUs08XPlG"
# 回测数据
request.sequence = 0 #初始的请求查询

# 4.调用远程函数
response = stub.get_question(request)
# print(dir(response))

print('user_id:',response.user_id)
print('sequence:',response.sequence) 
print('has_next_question:',response.has_next_question)
print('capital:',response.capital)
print('dailystk:',len(response.dailystk),type(response.dailystk))
print('positions:',response.positions)


# for i in range(len(response.dailystk)):
#     for j in range(7):#sequence+stkno+OHLCV格式
#         print('{:.4f}'.format(response.dailystk[i].values[j]),end='  ')
#     print()


import numpy as np
import time
import datetime
import os 
request.sequence = response.sequence #调整到服务器的sequence

# 创建存储接收数据的文件夹
t = datetime.datetime.now()
t_str = f'{t.month}-{t.day} {t.hour:02d}_{t.minute:02d}'
datapath = f'data {t_str}' 
if not os.path.exists(datapath):
    os.mkdir(datapath)

N = 1000 #网盘里面的900天数据，额外发送100天
while(N):
    try: #异常捕获
        request.sequence += 1
        while(stub.get_question(request).sequence==-1): #如果请求的sequence没产生
            # print('request/response sequence:{},{}'.format(request.sequence,stub.get_question(request).sequence))
            time.sleep(0.1)
        response = stub.get_question(request)
        seq = response.sequence #server返回的当前的序列号
        print(seq)
        
        #对数据的处理——首先尝试的为文件存储
        filepath = os.path.join(datapath, f'dailystk{seq}.csv')
        rst = []
        for i in range(len(response.dailystk)):#500只股票 
            tmp = []
            for j in range(108): #sequence+stkno+OHLCVT格式+100因子
                tmp.append(response.dailystk[i].values[j])
            rst.append(tmp)
        # print(rst)
        np.savetxt(filepath,rst,delimiter=',',fmt=['%d']*2+['%f']*4+['%d']*2+['%f']*100)
        N -= 1
    except Exception as e: #重新推流的开始
        print('Error as:',e)
        request.sequence = 0
        while(1):
            try:
                if(stub.get_question(request).sequence==1): #sequence从1重新开始
                    break
                else: #不为1
                    time.sleep(0.5)
            except: #断流
                time.sleep(0.5)
        

