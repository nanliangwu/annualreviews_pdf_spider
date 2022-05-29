## 1. 声明
本爬虫代码用于下载Annual Reviews期刊pdf文件，只供学习分享，切记用于商业用途。如有侵权，请联系删除。

## 2. 使用前提
- 有一个Annual Reviews会员账号，如无请科学找账号。
- 本地电脑装有python3环境。
- 安装了scrapy，如未安装可自行百度教程。

## 3. 使用说明

### 3.1 修改cookie
使用会员账号登录网站，查看登录 cookie，替换`AnnualreviewsPdfPipeline.py`和`AnnualReviews.py`代码的 cookie

如无会员账号，请科学找账号。

### 3.2 修改pdf下载目录
在`setting.py`修改**FILES_STORE**为 pdf 下载目录。

### 3.3 修改抓取页面url
Annual Reviews对学科期刊采取分卷的目录，你可以下载多个
在`AnnualReviews.py`修改urls的值为你的真是下载页面，可以放多条
```python
class AnnualReviews(scrapy.Spider):
    name = "annual-reviews"
    urls = [
        'https://xmu.liu06.ltd/https/77726476706e69737468656265737421e7e056d2263e66457f049ba98e5c26222a0a60acda/toc/soc/1/1'
    ]
```
还需要的地方是对 pdf 下载链接的处理：
```python
    def parse(self, response, **kwargs):
          ...
            # 这行代码，需要根据实际情况拼接出真实的下载地址
            pdf_url = 'https://xmu.liu06.ltd/' + pdf_urls[0].lstrip('/')
          ...
```

### 3.4 运行
执行命令：```scrapy crawl annual-reviews```，开启下载。

## 4. 注意问题
一次不要下载太多，防止账号被封。如果是科学找账号，亲测只会封IP，不会封号，可随意。

目前暂未支持IP代理池。

## 5.迭代记录
- [x] 解析页面，下载pdf

## 联系方式
- 邮箱：2287478364@qq.com