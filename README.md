# PySpiderChinaProvinceCity

最后更新：`20190416`

## 项目目的

* 演示如何用[PySpider](http://book.crifan.com/books/python_spider_pyspider/website)从[大众点评网站](http://www.dianping.com/citylist)爬取**中国省市区**的数据信息
* 生成得到**中国省市区数据**
  * 供别人或自己以后使用

## git仓库

crifan/PySpiderChinaProvinceCity

https://github.com/crifan/PySpiderChinaProvinceCity

## 如何运行项目得到数据

### 初始化PySpider环境

```bash
pipenv install
pipenv shell
```

注意：Mac中`pipenv install`时如果报错

```bash
__main__.ConfigurationError: Curl is configured to use SSL, but we have not been able to determine which SSL backend it is using. Please see PycURL documentation for how to specify the SSL backend manually
```

可以参考：

```bash
pipenv shell
pip3 uninstall pycurl
export PYCURL_SSL_LIBRARY=openssl
export LDFLAGS=-L/usr/local/opt/openssl/lib;export CPPFLAGS=-I/usr/local/opt/openssl/include;pip3 install pycurl --compile --no-cache-dir
```

详见：[【已解决】pipenv虚拟环境中用pip安装pyspider出错：\_\_main\_\_.ConfigurationError: Curl is configured to use SSL, but we have not been able to determine which SSL backend it is using](http://www.crifan.com/pipenv_virtual_environment_pip_install_pyspider_error_main_configurationerror_curl_is_configured_to_use_ssl_but_we_have_not_been_able_to_determine_which_ssl_backend_it_is_using)

### 拷贝PySpider代码

```bash
pyspider
```

默认用`5000`端口，然后打开：

http://0.0.0.0:5000/

再去：

`Create` -> `PySpiderChinaProvinceCity` -> `Create` -> 把`PySpiderChinaProvinceCity.py`粘贴进去->点击`save`，即可保存代码。

再去把`OutputRoot`改为你要保存数据的目录。

### 运行PySpider代码

先去把代码改为：

```python
        self.dowloadProvinceCity()
        # self.mergeProvinceCity()
```

然后去运行：

界面中把`status`改为`RUNNING`，再点击`Run`

即可在`output`文件夹中生成：

* `provinceList.json`：省的列表信息
* `cityList_{cityId}_{cityName}.json`：每个省的城市信息，包括市和市下属的区/县

```bash
➜  output git:(master) ✗ ll
total 2272
-rw-r--r--  1 crifan  staff    30K  4 16 09:32 cityList_10_江苏.json
-rw-r--r--  1 crifan  staff    35K  4 16 09:32 cityList_11_浙江.json
-rw-r--r--  1 crifan  staff    36K  4 16 09:32 cityList_12_安徽.json
-rw-r--r--  1 crifan  staff    30K  4 16 09:32 cityList_13_福建.json
-rw-r--r--  1 crifan  staff    41K  4 16 09:32 cityList_14_江西.json
-rw-r--r--  1 crifan  staff    50K  4 16 09:31 cityList_15_山东.json
-rw-r--r--  1 crifan  staff    56K  4 16 09:32 cityList_16_河南.json
-rw-r--r--  1 crifan  staff    36K  4 16 09:32 cityList_17_湖北.json
-rw-r--r--  1 crifan  staff    44K  4 16 09:32 cityList_18_湖南.json
-rw-r--r--  1 crifan  staff    43K  4 16 09:32 cityList_19_广东.json
-rw-r--r--  1 crifan  staff   2.6K  4 16 09:31 cityList_1_北京.json
-rw-r--r--  1 crifan  staff    39K  4 16 09:32 cityList_20_广西.json
-rw-r--r--  1 crifan  staff   8.6K  4 16 09:32 cityList_21_海南.json
-rw-r--r--  1 crifan  staff    13K  4 16 09:32 cityList_22_重庆.json
-rw-r--r--  1 crifan  staff    72K  4 16 09:32 cityList_23_四川.json
-rw-r--r--  1 crifan  staff    39K  4 16 09:32 cityList_24_贵州.json
-rw-r--r--  1 crifan  staff    59K  4 16 09:32 cityList_25_云南.json
-rw-r--r--  1 crifan  staff    35K  4 16 09:32 cityList_26_西藏.json
-rw-r--r--  1 crifan  staff    42K  4 16 09:32 cityList_27_陕西.json
-rw-r--r--  1 crifan  staff    36K  4 16 09:32 cityList_28_甘肃.json
-rw-r--r--  1 crifan  staff    20K  4 16 09:32 cityList_29_青海.json
-rw-r--r--  1 crifan  staff   2.5K  4 16 09:32 cityList_2_天津.json
-rw-r--r--  1 crifan  staff   7.9K  4 16 09:32 cityList_30_宁夏.json
-rw-r--r--  1 crifan  staff    45K  4 16 09:31 cityList_31_新疆.json
-rw-r--r--  1 crifan  staff   479B  4 16 09:32 cityList_32_香港.json
-rw-r--r--  1 crifan  staff   469B  4 16 09:32 cityList_33_澳门.json
-rw-r--r--  1 crifan  staff   8.8K  4 16 09:32 cityList_34_台湾.json
-rw-r--r--  1 crifan  staff    64K  4 16 09:31 cityList_3_河北.json
-rw-r--r--  1 crifan  staff    47K  4 16 09:32 cityList_4_山西.json
-rw-r--r--  1 crifan  staff    41K  4 16 09:32 cityList_5_内蒙古.json
-rw-r--r--  1 crifan  staff    25K  4 16 09:32 cityList_6_辽宁.json
-rw-r--r--  1 crifan  staff    22K  4 16 09:31 cityList_7_吉林.json
-rw-r--r--  1 crifan  staff    35K  4 16 09:32 cityList_8_黑龙江.json
-rw-r--r--  1 crifan  staff   891B  4 16 09:32 cityList_9_上海.json
-rw-r--r--  1 crifan  staff   2.6K  4 16 09:31 provinceList.json
```

然后再去把代码改为：

```python
        # self.dowloadProvinceCity()
        self.mergeProvinceCity()
```

去调试，点击`run`，即可生成

* `provinceCityList_20190416.json`：包含了合并后的，所有的`中国省市区`的数据。

## 中国省市区数据结构简介

### 数据在哪里

* 在`OutputRoot`变量定义的目录下的：`provinceCityLis_YYYYMMDD.json`
  * 比如：
    * [中国省市区数据列表 provinceCityList_20190416.json](https://github.com/crifan/PySpiderChinaProvinceCity/raw/master/output/provinceCityList_20190416.json)

### 数据结构关系

上述的省市区的数据内部的字段含义和逻辑层次关系：

```bash

  {
    "areaId": 3, # 地区编号
    "provinceId": 10, # 省份编号
    "provinceName": "江苏", # 省份名
    "currentNodeLevel": 1, # 当前节点层级：1=省，2=市，3=区/县
    "children": [
      {
        "cityAbbrCode": "SUZ", # 市缩写编码
        "cityAreaCode": "0512", # 市地区编码=邮政编码
        "cityEnName": "suzhou", # 市英文名称
        "cityId": 6, # 市编号
        "cityLevel": 2, # 几线城市：1=一线，2=二线，3=三线，4=四线，100=五线？
        "cityName": "苏州", # 市中文名
        "cityOrderId": 4888, # 市排序编号
        "cityPyName": "suzhou", # 市拼音名
        "gLat": 31.297779, # 地理信息：经度
        "gLng": 120.585586, # 地理信息：维度
        "provinceId": 10, # 所属省份编号
        "currentNodeLevel": 2, # 当前节点层级：1=省，2=市，3=区/县
        "children": [
          {
            "cityAbbrCode": "CS",
            "cityAreaCode": "0512",
            "cityEnName": "changshu",
            "cityId": 417,
            "cityLevel": 100,
            "cityName": "常熟",
            "cityOrderId": 712,
            "cityPyName": "changshu",
            "gLat": 31.65355,
            "gLng": 120.75239,
            "parentCityId": 6, # 父亲城市=市 的编号
            "provinceId": 10,
            "currentNodeLevel": 3 # 当前节点层级：1=省，2=市，3=区/县
          },
          ...
      },
      ...
```
