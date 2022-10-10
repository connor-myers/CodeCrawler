import unittest

from codecrawler.crawl import FileCrawler, InvalidLinkError

# class TestCrawl(unittest.TestCase):
#     def test_validate_link_invalid(self):
#         domain = "https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitignore"
#         self.assertRaises(InvalidLinkError, FileCrawler, domain)

#     def test_validate_link_valid(self):
#         domain = "https://github.com/connor-myers/CHIP-8_Emulator/blob/master/README.md"
#         try:
#             FileCrawler(domain)
#         except InvalidLinkError:
#             self.fail("FileCrawler() raised InvalidLinkError unexpectedly")

#     def test_convert_link(self):
#         domain = "https://github.com/apache/httpcomponents-client/tree/master/httpclient5-cache/src/main/java/org/apache/hc/client5/http/impl/cache/ResourceReference.java"
#         fc = FileCrawler(domain)

if __name__ == "__main__":
    unittest.main()
