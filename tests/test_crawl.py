import unittest

from codecrawler.crawl import FileCrawler, InvalidLinkError

class TestCrawl(unittest.TestCase):
    def test_code_download(self):
        url = "https://github.com/apache/httpcomponents-client/blob/master/httpclient5-cache/src/main/java/org/apache/hc/client5/http/impl/cache/ResourceReference.java"

        fc = FileCrawler(url, use_cache=True)

        if fc.source is None or len(fc.source) == 0:
            self.fail("Source code not downloaded properly")

    def test_get_code(self):
        url = "https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/lang/Class.java"

        fc = FileCrawler(url, use_cache=True)

        md = fc.get_method_data("getResourceAsStream", False)

        print(md[0].code)

if __name__ == "__main__":
    unittest.main()
