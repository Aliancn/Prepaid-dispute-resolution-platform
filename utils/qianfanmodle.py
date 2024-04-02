# 通过环境变量传递（作用于全局，优先级最低）
import json
import qianfan
import os


# 调用默认模型，即 ERNIE-Bot-turbo
# resp = chat_comp.do(messages=[{
#     "role": "user",
#     "content": "你好"
# }])

# 指定特定模型
# resp = chat_comp.do(model="Yi-34B-Chat", messages=[{
#     "role": "user",
#     "content": "你好,你擅长干一些什么"
# }])


def qianfan_Yi_34B_Chat(question):
    chat_comp = qianfan.ChatCompletion()
    resp = chat_comp.do(model="Yi-34B-Chat", messages=[{
        "role": "user",
        "content": question
    }])
    # resp.body -> json format dict
    return resp


def qianfan_liu_Yi_34B_Chat(question):
    comp = qianfan.Completion()

    # 续写功能同样支持流式调用
    resp = comp.do(model="ERNIE-Bot", prompt="你好", stream=True)
    for r in resp:
        print(r)
    return resp
