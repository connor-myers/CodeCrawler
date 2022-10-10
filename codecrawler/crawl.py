from urllib.parse import urlparse

github_domain = "github.com"

class FileCrawler():
    def __init__(self, link):
        if not FileCrawler.__validate_link(link):
            raise InvalidLinkError(link)
        self.link = link

    @staticmethod
    def __validate_link(link):
        domain = urlparse(link).netloc
        return domain == github_domain

class InvalidLinkError(Exception):
    def __init__(self, link):
        self.link = link
        self.message = f"{self.link} is not a valid link. CodeCrawler can only crawl GitHub links."
        super().__init__(self.message)