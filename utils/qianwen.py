import revTongYi.qianwen as qwen

# question = "nihao"

# chatbot = qwen.Chatbot(
#     cookies=<cookies_dict>  # 以dict形式提供cookies
# )
# chatbot = qwen.Chatbot(
#     cookies_str="login_current_pk=1070776907690709; currentRegionId=cn-hangzhou; aliyun_site=CN; l=fBM0R-XrPi5m4IHOBOfanurza77OSIRY5uPzaNbMi9fPOQfB5vJRW1eDt3Y6C3hVF6PkR3zzwi5HBeYBcQd-nxvtGwBLE8DmndLHR35..; _samesite_flag_=true; cookie2=179d56d4993d4104ce32686107ea5a7b; munb=2215515615801; csg=812e0ba9; t=01d609559d25a857ef6c8c5327729f01; _tb_token_=57de6e8e5e7a1; login_tongyi_ticket=v2JwPo8D9Z8hgPiyGEmovXrEtK2ifrHkpHrMXUaIrrMUaL5WA5msOWIsQUGnTR*W0; cnaui=1070776907690709; login_aliyunid_csrf=_csrf_tk_1304311449588045; cna=8pOJHls3tCwCASvjiXo92XLY; atpsida=65c047984f9220657608c969_1711452084_5; aui=1070776907690709; sca=e208b76e; help_csrf=Qnux%2FZeGEtyaqEcQKMgmty0t0BB4McfqOGGBWk9jJvJXjqICTn0lsIW3n9sQwe5OP0HCoF2MzKizmHTbYbm2QzD0rE6PunQ0YAKYixyLT%2BfY1XKJZJFlCaSxAhKvbbSu69%2BWM%2BNZtnQtGWrNnbDXww%3D%3D; cr_token=7ad4223a-a13d-49b8-bd9a-ac75f739e7c6; isg=BDMz4ZpOUdjFFB5d20WFhCp1wjFdaMcqx96AW-XUytKM5FqGfTpAeNo2nxQK_h8i;XSRF-TOKEN=e9296190-5bcb-4616-bd99-10b854fbfdaa;tfstk=c4ZlBQDvYjO1Ug9AnTi5m8I8I6qhaZ1xwblQ0ONQlpno2QgqUsb6uFWgWFcc1_8C"
# )

# print(chatbot.ask(prompt=question))


def Ask(question):
    """
    Asks a question to the chatbot and returns the response.

    Args:
        question (str): The question to ask the chatbot.

    Returns:
        dict: The response from the chatbot.
        {
            'content': '你好！有什么我能帮助你的吗？',
            'contentType': 'text', 
            'id': '84392f964f064cc795c42340010e9adc_0', 
            'role': 'assistant', 
            'status': 'finished',
        }
    """
    chatbot = qwen.Chatbot(
        cookies_str="login_current_pk=1070776907690709; currentRegionId=cn-hangzhou; aliyun_site=CN; l=fBM0R-XrPi5m4IHOBOfanurza77OSIRY5uPzaNbMi9fPOQfB5vJRW1eDt3Y6C3hVF6PkR3zzwi5HBeYBcQd-nxvtGwBLE8DmndLHR35..; _samesite_flag_=true; cookie2=179d56d4993d4104ce32686107ea5a7b; munb=2215515615801; csg=812e0ba9; t=01d609559d25a857ef6c8c5327729f01; _tb_token_=57de6e8e5e7a1; login_tongyi_ticket=v2JwPo8D9Z8hgPiyGEmovXrEtK2ifrHkpHrMXUaIrrMUaL5WA5msOWIsQUGnTR*W0; cnaui=1070776907690709; login_aliyunid_csrf=_csrf_tk_1304311449588045; cna=8pOJHls3tCwCASvjiXo92XLY; atpsida=65c047984f9220657608c969_1711452084_5; aui=1070776907690709; sca=e208b76e; help_csrf=Qnux%2FZeGEtyaqEcQKMgmty0t0BB4McfqOGGBWk9jJvJXjqICTn0lsIW3n9sQwe5OP0HCoF2MzKizmHTbYbm2QzD0rE6PunQ0YAKYixyLT%2BfY1XKJZJFlCaSxAhKvbbSu69%2BWM%2BNZtnQtGWrNnbDXww%3D%3D; cr_token=7ad4223a-a13d-49b8-bd9a-ac75f739e7c6; isg=BDMz4ZpOUdjFFB5d20WFhCp1wjFdaMcqx96AW-XUytKM5FqGfTpAeNo2nxQK_h8i;XSRF-TOKEN=e9296190-5bcb-4616-bd99-10b854fbfdaa;tfstk=c4ZlBQDvYjO1Ug9AnTi5m8I8I6qhaZ1xwblQ0ONQlpno2QgqUsb6uFWgWFcc1_8C"
    )

    result = chatbot.ask(prompt=question)

    return result['contents'][0]

