#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-04-15 14:56:12
# Project: PySpiderChinaProvinceCity

from pyspider.libs.base_handler import *

import os
import json
import codecs
import base64
import gzip
import copy
import time
import re
import csv
# import datetime
from datetime import datetime, timedelta


######################################################################
# Const
######################################################################

OutputRoot = "/Users/crifan/dev/dev_root/crifan/PySpiderChinaProvinceCity/output"

constProvinceListFullpath = os.path.join(OutputRoot, "provinceList.json")

constCityListNamePattern = "cityList_%s_%s.json"

constUserAgentMacChrome = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

######################################################################
# Config & Settings
######################################################################



######################################################################
# Global Varaibles
######################################################################

gProvinceCityList = []

######################################################################
# Common Util Functions
######################################################################

def saveJsonToFile(fullFilename, jsonValue):
    """save json dict into file"""
    with codecs.open(fullFilename, 'w', encoding="utf-8") as jsonFp:
        json.dump(jsonValue, jsonFp, indent=2, ensure_ascii=False)
        print("Complete save json %s" % fullFilename)

def loadJsonFromFile(fullFilename):
    """load and parse json dict from file"""
    with codecs.open(fullFilename, 'r', encoding="utf-8") as jsonFp:
        jsonDict = json.load(jsonFp)
        print("Complete load json from %s" % fullFilename)
        return jsonDict

######################################################################
# Project Specific Functions
######################################################################


######################################################################
# Main
######################################################################

class Handler(BaseHandler):
    crawl_config = {
        "connect_timeout": 100,
        "timeout": 600,
        "retries": 15,
        "headers": {
            "User-Agent": constUserAgentMacChrome,
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json",
            "Origin": "http://www.dianping.com",
            # "X-Requested-With": "XMLHttpRequest",
        }
    }

    #----------------------------------------
    # Util Functions
    #----------------------------------------

    #----------------------------------------
    # Crawl Logic
    #----------------------------------------


    def on_start(self):
        # init province city list
        self.dowloadProvinceCity()
        # self.mergeProvinceCity()

    def mergeProvinceCity(self):
        gProvinceCityList = loadJsonFromFile(constProvinceListFullpath)

        for eachProvoince in gProvinceCityList:
            curCityListFilename = constCityListNamePattern % (eachProvoince["provinceId"], eachProvoince["provinceName"])
            curCityListFullpath = os.path.join(OutputRoot, curCityListFilename)
            curCityList = loadJsonFromFile(curCityListFullpath)
            eachProvoince["currentNodeLevel"] = 1
            eachProvoince["children"] = []

            """
            {
                "activeCity": True,
                "appHotLevel": 1,
                "cityAbbrCode": "SUZ",
                "cityAreaCode": "0512",
                "cityEnName": "suzhou",
                "cityId": 6,
                "cityLevel": 2,
                "cityName": "苏州",
                "cityOrderId": 4888,
                "cityPyName": "suzhou",
                "directURL": "",
                "gLat": 31.297779,
                "gLng": 120.585586,
                "overseasCity": False,
                "parentCityId": 0,
                "provinceId": 10,
                "scenery": False,
                "tuanGouFlag": 1
            },

            {
                "activeCity": True,
                "appHotLevel": 1,
                "cityAbbrCode": "TC",
                "cityAreaCode": "0512",
                "cityEnName": "taicang",
                "cityId": 420,
                "cityLevel": 100,
                "cityName": "太仓",
                "cityOrderId": 4994,
                "cityPyName": "taicang",
                "directURL": "",
                "gLat": 31.45868,
                "gLng": 121.13003,
                "overseasCity": False,
                "parentCityId": 6,
                "provinceId": 10,
                "scenery": False,
                "tuanGouFlag": 1
            },
            """

            # extract main city
            for eachCityItem in curCityList:
                toDelKeyList = [
                    "activeCity",
                    "appHotLevel",
                    "directURL",
                    "overseasCity",
                    "tuanGouFlag",
                    "scenery",
                ]
                for eachKeyToDel in toDelKeyList:
                    if eachKeyToDel in eachCityItem:
                        eachCityItem.pop(eachKeyToDel)
                        # del eachCityItem[eachKeyToDel]

                parentCityId = eachCityItem["parentCityId"]
                print("parentCityId=%s" % parentCityId)
                if parentCityId == 0:
                    # is main city
                    eachCityItem["currentNodeLevel"] = 2
                    eachCityItem["children"] = []
                    eachProvoince["children"].append(eachCityItem)

            # extract sub city
            for eachCityItem in curCityList:
                print("eachCityItem=%s" % eachCityItem)
                parentCityId = eachCityItem["parentCityId"]
                print("parentCityId=%s" % parentCityId)
                if parentCityId > 0:
                    # is sub city
                    eachCityItem["currentNodeLevel"] = 3
                    # add to  main city
                    curMainCityList = eachProvoince["children"]
                    for earchMainCity in curMainCityList:
                        if earchMainCity["cityId"] == parentCityId:
                            earchMainCity["children"].append(eachCityItem)
                else:
                    eachCityItem.pop("parentCityId")

        provinceCityListFilename = "provinceCityList_%s.json" % datetime.now().strftime("%Y%m%d")
        provinceCityListFullpath = os.path.join(OutputRoot, provinceCityListFilename)
        saveJsonToFile(provinceCityListFullpath, gProvinceCityList)

    def dowloadProvinceCity(self):
        getAllDomesticProvinceUrl = "http://www.dianping.com/ajax/citylist/getAllDomesticProvince"
        self.crawl(
            getAllDomesticProvinceUrl,
            method="POST",
            data="",
            callback=self.getAllDomesticProvinceCallback,
        )

    def getAllDomesticProvinceCallback(self, response):
        respUrl = response.url
        print("respUrl=%s" % respUrl)
        respContent = response.content
        print("respContent=%s" % respContent)
        respJson = response.json
        print("respJson=%s" % respJson)
        provinceList = respJson["provinceList"]

        for eachProvince in provinceList:
            provinceIdStr = eachProvince["provinceId"]
            print("provinceIdStr=%s" % provinceIdStr)
            provinceIdInt = int(provinceIdStr)
            eachProvince["provinceId"] = provinceIdInt

        saveJsonToFile(constProvinceListFullpath, provinceList)

        # get all cities for each province
        getCityUrl = "http://www.dianping.com/ajax/citylist/getDomesticCityByProvince"
        for eachProvince in provinceList:
            print("eachProvince=%s" % eachProvince)
            provinceIdInt = eachProvince["provinceId"]
            paramDict = {
                "provinceId": provinceIdInt,
            }
            paramDictStr = json.dumps(paramDict)

            provinceDict = eachProvince
            provinceDict["provinceId"] = provinceIdInt
            gProvinceCityList.append(provinceDict)

            # add itag and hash value for url to force re-crawl when POST url not changed
            timestampStr = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            # fakeItag = "%s_%s" % (provinceIdInt, timestampStr)
            urlWithHash = "%s#%s_%s" % (getCityUrl, provinceIdInt, timestampStr)

            self.crawl(
                # getCityUrl,
                urlWithHash,
                # itag=fakeItag,
                method="POST",
                # data=paramDict,
                data=paramDictStr,
                callback=self.getCityCallback,
                save=provinceDict,
            )

    def getCityCallback(self, response):
        provinceDict = response.save
        print("provinceDict=%s" % provinceDict)
        respUrl = response.url
        print("respUrl=%s" % respUrl)
        respJson = response.json
        print("respJson=%s" % respJson)
        cityList = respJson["cityList"]
        print("cityList=%s" % cityList)

        curCityListFilename = constCityListNamePattern % (provinceDict["provinceId"], provinceDict["provinceName"])
        curCityListFullpath = os.path.join(OutputRoot, curCityListFilename)
        saveJsonToFile(curCityListFullpath, cityList)
