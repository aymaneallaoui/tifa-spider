# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AnimeItem(scrapy.Item):
    Title = scrapy.Field()
    score = scrapy.Field()
    genres = scrapy.Field()
    episodes = scrapy.Field()
    status = scrapy.Field()
    airing = scrapy.Field()
    typeAnime = scrapy.Field()
    brodcastDate = scrapy.Field()
    description = scrapy.Field()