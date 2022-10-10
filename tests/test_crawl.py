import unittest

from codecrawler.crawl import FileCrawler, InvalidLinkError

class TestCrawl(unittest.TestCase):
    def test_validate_link_invalid(self):
        domain = "https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitignore"
        self.failUnlessRaises(InvalidLinkError, FileCrawler, domain)

    def test_validate_link_valid(self):
        domain = "https://github.com/connor-myers/CHIP-8_Emulator/blob/master/README.md"
        try:
            FileCrawler(domain)
        except InvalidLinkError:
            self.fail("FileCrawler() raised InvalidLinkError unexpectedly")

if __name__ == "__main__":
    unittest.main()
