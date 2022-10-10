from urllib.parse import urlparse, urlunparse

from codecrawler.url import InvalidLinkError, convert_github_to_raw_github, validate_link

class FileCrawler():
    def __init__(self, link):
        if not validate_link(link):
            raise InvalidLinkError(link)
        self.link = link
        self.raw_link = convert_github_to_raw_github(link)

    def __download_code(self):
        return None