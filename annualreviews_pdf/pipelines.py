# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.files import FilesPipeline


class AnnualreviewsPdfPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return request.meta.get('filename', '')

    def get_media_requests(self, item, info):
        url = item['pdf_url']
        name = item['pdf_name'] + '.pdf'
        meta = {'filename': name}
        ## 这里的 cookie 需要修改，在浏览器用 Annual Reviews 账号登录，F12查看网络请求，找到cookie值替换
        cookies = 'show_vpn=0; wengine_vpn_ticket=7abbaff5ad1aca68; ddhgguuy_session=nfsfsv09vp6e1tp08k6hjp38p1; refresh=0'
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        return [scrapy.Request(url, meta=meta, cookies=cookies)]
