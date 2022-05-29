# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:25
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import time
from typing import Optional
import pymongo
from pymongo import MongoClient
import datetime
import pprint

from selenium.common.exceptions import WebDriverException

from services.hcaptcha_challenger import ArmorCaptcha, ArmorUtils
from services.hcaptcha_challenger.exceptions import ChallengePassed
from services.settings import logger, HCAPTCHA_DEMO_SITES, DIR_MODEL, DIR_CHALLENGE
from services.utils import get_challenge_ctx
busy = False

@logger.catch()
def goto(linenum):
    global line
    line = linenum

def runner(
    sample_site: str,
    lang: Optional[str] = "zh",
    silence: Optional[bool] = False,
    onnx_prefix: Optional[str] = None,
):
    logger.info("Starting demo project...")
    """Human-Machine Challenge Demonstration | Top Interface"""
    challenger = ArmorCaptcha(dir_workspace=DIR_CHALLENGE, lang=lang, debug=True)
    challenger_utils = ArmorUtils()

    # Instantiating the Challenger Drive
    ctx = get_challenge_ctx(silence=silence, lang=lang)
    logger.info("Starting demo project...")
    client = MongoClient("mongodb://20.118.216.29:27018")
    mydatabase = client['1']
    mydatabase2 = client['4']
    db = client["responses"]
    #sitekey1={"12345678":"1", "date":datetime.datetime.utcnow()}
      #mydatabase.sitekey.insert_one(sitekey1)
      #mydatabase.create_collection("response")
      #mydatabase.create_collection('sitekey')
    tasklist=mydatabase.res.count_documents({})
    while (tasklist==0):
        tasklist=mydatabase.res.count_documents({})

        print(tasklist)
  
    ai_task=mydatabase.res.find_one_and_delete({})
    print(ai_task)
    print(ai_task['2'])
    object_id=ai_task['_id']
    if (ai_task['2']=="2cae9d15-bde9-4a43-9e2a-5f4a1578d40b"):
      for i in range(20):
          if i!=0 :
             if (token!="") and i!=0:
                   break
          ctx.get("http://20.118.216.29/demo1")

          challenger.anti_checkbox(ctx)

                # Enter iframe-content --> process hcaptcha challenge --> exit iframe-content

          resp = challenger.anti_hcaptcha(ctx, dir_model=DIR_MODEL, onnx_prefix=onnx_prefix)
          token = ctx.execute_script("return hcaptcha.getResponse();")
         # while (token==""):
            #  challenger.anti_checkbox(ctx)

                # Enter iframe-content --> process hcaptcha challenge --> exit iframe-content

            #  resp = challenger.anti_hcaptcha(ctx, dir_model=DIR_MODEL, onnx_prefix=onnx_prefix)
            #  token = ctx.execute_script("return hcaptcha.getResponse();")
            
          if resp == challenger.CHALLENGE_SUCCESS and token != "":
                    token = ctx.execute_script("return hcaptcha.getResponse();")
                    sitekey1={'_id': object_id, '6': '2cae9d15-bde9-4a43-9e2a-5f4a1578d40b', '5': token, 'groups': []}
                    mydatabase2.res.insert_one(sitekey1)
                    print ("done!")
          elif resp == challenger.CHALLENGE_RETRY or token=="":
                    ctx.refresh()
                    goto(55)
    
    #go to http://20.118.216.29/demo1 
    # Instantiating Challenger Components
    if (ai_task['2']=="6ba78ccd-f275-4c2d-be45-5e4b46a4a4d8"):
      for i in range(20):
          if i!=0:
              if (token!="") and i!=0:
                   break

          ctx.get("http://20.118.216.29/demo2")

          challenger.anti_checkbox(ctx)

                # Enter iframe-content --> process hcaptcha challenge --> exit iframe-content

          resp = challenger.anti_hcaptcha(ctx, dir_model=DIR_MODEL, onnx_prefix=onnx_prefix)
          token = ctx.execute_script("return hcaptcha.getResponse();")
          #while (token==""):
            #  challenger.anti_checkbox(ctx)

                # Enter iframe-content --> process hcaptcha challenge --> exit iframe-content

            #  resp = challenger.anti_hcaptcha(ctx, dir_model=DIR_MODEL, onnx_prefix=onnx_prefix)
             # token = ctx.execute_script("return hcaptcha.getResponse();")
             
          if resp == challenger.CHALLENGE_SUCCESS and token != "":
                    token = ctx.execute_script("return hcaptcha.getResponse();")
                    sitekey1={'_id': object_id, '6': '6ba78ccd-f275-4c2d-be45-5e4b46a4a4d8', '5': token, 'groups': []}
                    mydatabase2.res.insert_one(sitekey1)
                    print ("done!")
          elif resp == challenger.CHALLENGE_RETRY or token == "":
                    ctx.refresh()
                    goto(83)
