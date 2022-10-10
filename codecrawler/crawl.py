from codecrawler.url import *
from codecrawler.cache import FileCache

import sys
import os
import os.path

cache_dir = "__cache__"

class FileCrawler():
    def __init__(self, link, use_cache=True):
        self.use_cache = use_cache
        if self.use_cache:
            self.file_cache = self.__init_cache()

        try:
            validate_link(link)
        except InvalidLinkError as e:
            sys.exit(e.message)

        self.link = link
        self.raw_link = convert_github_to_raw_github(link)

        self.source = self.__get_code()

    def __init_cache(self):
        return FileCache(cache_dir)

    def __get_code(self):
        file_name = convert_url_to_path(self.link)
        if self.use_cache:
            file = self.file_cache.get_file_from_cache(file_name)
            if file is not None:
                file_contents = file.read()
                file.close()
                return file_contents

        file_contents = read_url_contents(self.raw_link)

        if self.use_cache:
            self.file_cache.add_file_to_cache(file_name, file_contents)

        return file_contents