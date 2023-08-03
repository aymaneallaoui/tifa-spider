import scrapy


class AnimespiderSpider(scrapy.Spider):
    name = "animespider"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        # Get the current URL
        current_url = response.url

        # Stop the crawl when the desired URL is reached
        if "limit=15000" in current_url:
            return

        # Parse the anime details on the current page
        animes = response.css('div.detail')
        for anime in animes:
            relative_url = anime.css('h3.hoverinfo_trigger > a::attr(href)').extract_first()
            yield scrapy.Request(relative_url, callback=self.parse_anime)

        # Check if there's a "Next" button and follow it if it exists
        next_page = response.css('a.next ::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), self.parse)

    def parse_anime(self, response):
        score = response.css('div.score-label::text').extract_first()
        genre = response.xpath('//div[@class="spaceit_pad"]/a[contains(@href, "/genre/")]/text()').getall()
        episodes = response.xpath("//span[text()='Episodes:']/following-sibling::text()").get()
        status = response.xpath("//span[text()='Status:']/following-sibling::text()").get()
        airing = response.xpath("//span[text()='Aired:']/following-sibling::text()").get()
        typeAnime = response.xpath("//span[text()='Type:']/following-sibling::a/text()").get()
        brodcastDate = response.xpath("//span[text()='Broadcast:']/following-sibling::text()").get()

        episodes = episodes.strip() if episodes else None
        status = status.strip() if status else None
        airing = airing.strip() if airing else None
        brodcastDate = brodcastDate.strip() if brodcastDate else None

        description = response.xpath('//p[@itemprop="description"]/text()').get().strip()
        Title = response.css('h1.title-name strong::text').extract_first()
        yield {
            'Title': Title,
            'score': score,
            'genres': genre,
            'episodes': episodes,
            'status': status,
            'airing': airing,
            'typeAnime': typeAnime,
            'brodcastDate': brodcastDate,
            'description': description,
        }
