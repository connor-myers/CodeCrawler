import unittest

from codecrawler.crawl import FileCrawler, InvalidLinkError

class TestCrawl(unittest.TestCase):
    def test_code_download(self):
        url = "https://github.com/apache/httpcomponents-client/blob/master/httpclient5-cache/src/main/java/org/apache/hc/client5/http/impl/cache/ResourceReference.java"

        fc = FileCrawler(url, use_cache=True)

        if fc.source is None or len(fc.source) == 0:
            self.fail("Source code not downloaded properly")

if __name__ == "__main__":
    unittest.main()
