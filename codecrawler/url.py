from urllib.parse import urlparse, urlunparse
from urllib.request import urlopen

github_domain = "github.com"
github_raw_domain = "raw.githubusercontent.com"

class InvalidLinkError(Exception):
    def __init__(self, link):
        self.link = link
        self.message = f"{self.link} is not a valid link."
        super().__init__(self.message)

def validate_link(link):
    domain = urlparse(link).netloc

    if domain != github_domain:
        raise InvalidLinkError(link)

    return True

def convert_github_to_raw_github(link):
    parsed_url = urlparse(link)

    updated_path = parsed_url.path.split('/')
    del updated_path[3]
    updated_path = '/'.join(updated_path)

    parsed_url = parsed_url._replace(netloc=github_raw_domain, path=updated_path)

    return urlunparse(parsed_url)

def convert_raw_github_to_github(link):
    return None

def convert_url_to_path(link):
    parsed_url = urlparse(link)
    return parsed_url.path.replace('/', '_')[1:]

def read_url_contents(link):
    try:
        opened_url = urlopen(link)
    except:
        raise InvalidLinkError(link)
    return opened_url.read().decode("utf-8")