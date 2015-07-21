import scrapy
from .. import scraper
from scraper.items import *
import locale

URL = "https://play.google.com/store/apps/collection/topselling_free?hl=en"
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class GoogleSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftDMHM"]

    def parse(self, response):
        item = ScraperItem()
        item['name'] = response.xpath('//div[@class = "document-title"]/div/text()').extract_first()
        item['url'] = response.url
        item['developer'] = response.xpath('//span[@itemprop = "name"]/text()').extract()
        item['categorie'] = response.xpath('//span[@itemprop = "genre"]/text()').extract()
        item['inapp_purchases'] = response.xpath('//div[@class = "inapp-msg"]/text()').extract_first(default = 'No in-app purchase.')
        item['age'] = response.xpath('//div[@class = "document-subtitle content-rating-title"]/text()').extract_first(default = "No age specification.")
        item['rating'] = locale.atof(response.xpath('//div[@class = "score"]/text()').extract_first())
        item['rating_count'] = locale.atoi(response.xpath('//div[@class = "reviews-stats"]/span/text()').extract_first())
        item['cover_image'] = response.xpath('//div[@class = "cover-container"]//@src').extract()
        item['badge_title'] = response.xpath('//span[@class = "badge-title"]/text()').extract_first(default = "No badge title.") 

        string = ""
        string += response.xpath('//div[@class = "id-app-orig-desc"]/text()').extract_first()
        for node in response.xpath('//div[@class = "id-app-orig-desc"]/p'):
            string += node.xpath('text()').extract_first()
        item['description'] = string

        
        lst = []
        for node in response.xpath('//div[@class = "thumbnails"]/img'):
            lst.append(str(node.xpath('@src').extract_first()))
        item['screenshots'] = lst 

        item['preview_vid'] = response.xpath('//div[@class = "thumbnails"]/span//@data-video-url').extract_first(default = "No trailer video.")
        
        collection = []
        review = {}
        for node in response.xpath('//div[@class = "single-review"]'):
            author = node.xpath('div[1]/div[@class = "review-info"]/span[@class = "author-name"]/a/text()').extract_first()
            date = node.xpath('div[1]/div[@class = "review-info"]/span[@class = "review-date"]/text()').extract_first()
            stars = int(node.xpath('div[1]/div[@class = "review-info"]/div[@class = "review-info-star-rating"]//@style').extract_first().split(" ")[1].split('%')[0])/100.0
            title = node.xpath('div[2]/span[@class = "review-title"]/text()').extract_first()
            comment = node.xpath('div[2]/text()').extract()[1]
            review['author'] = author
            review['date'] = date
            review['rating'] = stars
            review['title'] = title
            review['comment'] = comment
            collection.append(review)
            review = {}
        item['top_comments'] = collection 


        lst = []
        for node in response.xpath('//div[@class = "details-section whatsnew"]//div[@class = "recent-change"]'):
            lst.append(node.xpath('text()').extract_first())
        item['recent_changes'] = lst


        additional = {}
        for node in response.xpath('//div[@class = "details-section-contents"]//div[@class = "meta-info"]'):
            title = node.xpath('div[@class = "title"]/text()').extract_first()
            print "title"
            print title
            content = node.xpath('div[@class = "content"]/text()').extract_first()
            print content
            additional[title] = content
        item['additional_information'] = additional

             
        yield item

 