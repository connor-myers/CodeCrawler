import os.path
import os

class FileCache():
    def __init__(self, cache_path):
        self.cache_path = cache_path 
        if not os.path.exists(cache_path):
            os.mkdir(cache_path)
    
    def get_file_from_cache(self, file_name):
        file_path = self.__get_local_file_path(file_name)

        if not os.path.exists(file_path):
            return None

        return open(file_path, 'r')

    def add_file_to_cache(self, file_name, file_contents):
        file_path = self.__get_local_file_path(file_name)

        # overwrite existing file (if it does exist)
        with open(file_path, 'w+') as file:
            file.truncate(0)
            file.write(file_contents)

    def __get_local_file_path(self, file_name):
        return os.path.join(self.cache_path, file_name)
