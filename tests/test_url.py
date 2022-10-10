import unittest

from codecrawler.url import InvalidLinkError, convert_github_to_raw_github, validate_link, convert_url_to_path

class TestUrl(unittest.TestCase):
    def test_validate_link_invalid(self):
        url = "https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitignore"
        self.assertRaises(InvalidLinkError, validate_link, url)

    def test_validate_link_valid(self):
        url = "https://github.com/connor-myers/CHIP-8_Emulator/blob/master/README.md"
        try:
            validate_link(url)
        except InvalidLinkError:
            self.fail("Raised InvalidLinkError unexpectedly")

    def test_convert_link(self):
        url = "https://github.com/apache/httpcomponents-client/tree/master/httpclient5-cache/src/main/java/org/apache/hc/client5/http/impl/cache/ResourceReference.java"
        raw_url = convert_github_to_raw_github(url)
        self.assertEquals(raw_url, "https://raw.githubusercontent.com/apache/httpcomponents-client/master/httpclient5-cache/src/main/java/org/apache/hc/client5/http/impl/cache/ResourceReference.java")

    def test_convert_url_to_path(self):
        url = "https://github.com/apache/httpcomponents-client/tree/master/httpclient5-cache/src/main/java/org/apache/hc/client5/http/impl/cache/ResourceReference.java"
        self.assertEquals(convert_url_to_path(url), "apache_httpcomponents-client_tree_master_httpclient5-cache_src_main_java_org_apache_hc_client5_http_impl_cache_ResourceReference.java")

if __name__ == "__main__":
    unittest.main()
