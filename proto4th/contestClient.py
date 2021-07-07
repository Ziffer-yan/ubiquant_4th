# -*- coding: utf-8 -*-
import grpc
import contest_pb2
import contest_pb2_grpc

address = '47.100.97.93:40723'

## LoginRequest
# 1.建立与服务器的连接
channel = grpc.insecure_channel(address)

# 2.创建客户端助手(对函数名、参数打包)
stub = contest_pb2_grpc.ContestStub(channel)

# 3.封装请求参数类型对象
request = contest_pb2.LoginRequest()
# 账号
request.user_id = 103
request.user_pin = "UJUs08XPlG"

# 4.调用远程函数
response = stub.login(request)
# print(dir(response))
print('session_key:',response.session_key)
print('success:',response.success)
print('init_capital:',response.init_capital)
print('reason:',response.reason)
# 获取返回的数据key
key = response.session_key


print('-'*30)


## AnswerRequest
# 上传仓位信息
request2 = contest_pb2.AnswerRequest()
# 账号
request2.user_id = 103
request2.user_pin = "UJUs08XPlG"
request2.session_key = key

# 序列号及头寸
request2.sequence = 1
# 头寸的数据类型为repeated double
# request2.positions.append(0)
# request2.positions.extend([0,1,2,3])


import numpy as np
pos = np.random.randint(-1000,1000,size=(500))
request2.positions.extend(pos)

response2 = stub.submit_answer(request2)
# print(dir(response2))
print('accepted:',response2.accepted)
print('reason:',response2.reason)


