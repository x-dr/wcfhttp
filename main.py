#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import argparse
import os
import uvicorn
from wcferry import Wcf
from wcfhttp import Http, __version__
from dotenv import load_dotenv

load_dotenv()

def main():

    logging.basicConfig(level="INFO", format="%(asctime)s %(message)s")
    wcf_host=os.environ.get("WCF_HOST") or None
    wcf_port=os.environ.get("WCF_PORT") or 10086
    wcf_debug=os.environ.get("WCF_DEBUG") or True
    wcf_cb=os.environ.get("WCF_CB") or ""
    wcf_http_host=os.environ.get("WCF_HTTP_HOST") or "0.0.0.0"
    wcf_http_port=os.environ.get("WCF_HTTP_PORT") or 9999


 
    if not wcf_cb:
        logging.warning("没有设置接收消息回调，消息直接通过日志打印；请通过 --cb 设置消息回调")
        logging.warning(f"回调接口规范参考接收消息回调样例：http://{wcf_http_host}:{wcf_http_port}/docs")


    wcf = Wcf(wcf_host, int(wcf_port), wcf_debug)
    home = "https://github.com/lich0821/WeChatFerry"

    http = Http(wcf=wcf,
                cb=wcf_cb,
                title="WeChatFerry HTTP 客户端",
                description=f"Github: <a href='{home}'>WeChatFerry</a>",)

    uvicorn.run(app=http, host=wcf_http_host, port=int(wcf_http_port))


if __name__ == "__main__":
    main()