# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    developer = scrapy.Field()
    categorie = scrapy.Field()
    inapp_purchases = scrapy.Field()
    link = scrapy.Field()
    age = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    cover_image = scrapy.Field()
    screenshots = scrapy.Field()
    preview_vid = scrapy.Field()
    badge_title = scrapy.Field()
    star_rating = scrapy.Field()
    top_comments = scrapy.Field()
    recent_changes = scrapy.Field()
    additional_information = scrapy.Field()
    see_more = scrapy.Field()
    similar_app = scrapy.Field()
    more_from_developer = scrapy.Field()
    name = scrapy.Field()

