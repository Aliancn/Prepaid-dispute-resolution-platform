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


def qianfan_pre_Yi_34B_Chat(ques):
    chat_comp = qianfan.ChatCompletion()
    questionPre = [
        "你是一个消费法律维权的律师，现在你根据我的描述分析维权案例",
        # "并按照以下模版回答我",
        # "1. 您的维权需求所涉纠纷主要为“(预付式消费)...”",
        # "1. 您的维权需求所涉纠纷主要为“ ”",
        # "2. 本类型纠纷主要涵盖：.. 责任",
        # "3. 根据您在“取证固证”上传的证据可知，本案涉案金额为 ",
        # "4. (暂未/已有设计涉及刑事责任)，综合上述分析，我们认为您可以先采取（调解方式：12315等投诉平台）",
        # "5. 如果您已经采取调解未果，可提供通过诉讼方式进一步维护自身合法权益。我平台为您推介下列律所：好评率、胜诉率...等",
    ]
    question = ""
    question += questionPre[0]
    question += "以下是我的案例：" + ques
    questionSet = [
        "请回答以下问题:"    ,
        "1. 维权需求所涉纠纷主要为? 例如: 预付式消费",
        "2. 本类型纠纷主要涵盖：.. 责任",
        "3. 根据上传信息能否知道本案涉案金额为多少",
        "4. 是否设计涉及刑事责任",
        "5. 综合上述分析，认为我可以先采取什么方式",
        "6. 如果已经采取调解未果，可提供通过诉讼方式进一步维护自身合法权益"
    ]
    for q in questionSet:
        question += q 
    resp = chat_comp.do(model="Yi-34B-Chat", messages=[{
        "role": "user",
        "content": question
    }])
    # resp.body -> json format dict
    return resp


def qianfan_Yi_34B_Chat(question):
    chat_comp = qianfan.ChatCompletion()
    resp = chat_comp.do(model="Yi-34B-Chat", messages=[{
        "role": "user",
        "content": question
    }])
    # resp.body -> json format dict
    return resp


def qianfan_liu_Yi_34B_Chat(question):
    # 流式调用
    comp = qianfan.Completion()

    # 续写功能同样支持流式调用
    resp = comp.do(model="ERNIE-Bot", prompt="你好", stream=True)
    for r in resp:
        print(r)
    return resp
