from pydoc import doc
import sys
import os
import os.path

from codecrawler.url import *
from codecrawler.cache import FileCache

from enum import Enum

import javalang

cache_dir = "__cache__"

class ClassType(Enum):
    ABSTRACT = 0
    CLASS = 1
    INTERFACE = 2

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
        self.source_split = self.source.split('\n')

        try:
            self.parsed = javalang.parse.parse(self.source)
        except:
            raise BadJavaFileError(self.link)

        self.file_class_type = self.__get_file_class_type()

    def __get_file_class_type(self):
        if type(self.parsed.types[0]) == javalang.tree.ClassDeclaration:
            if "abstract" in self.parsed.types[0].modifiers:
                return ClassType.ABSTRACT
            else:
                return ClassType.CLASS
        elif type(self.parsed.types[0]) == javalang.tree.InterfaceDeclaration:
            return ClassType.INTERFACE

        raise BadJavaFileError(self.link)

    def get_method_data(self, method_name, allow_dups=False):
        method_nodes = self.__get_method_nodes(method_name, allow_dups)

        method_data = []
        for method_node in method_nodes:
            documentation = method_node.documentation
            code = self.__get_method_code(method_node)

            md = MethodData(code, documentation)

            if md is not None:
                method_data.append(md)

        return method_data

    def __get_method_nodes(self, method_name, allow_dups):
        method_nodes = []
        for _, method_node in self.parsed.filter(javalang.tree.MethodDeclaration):
            if method_name == method_node.name:
                method_nodes.append(method_node)
                if not allow_dups:
                    break
        
        return method_nodes

    def __get_method_code(self, method_node):
        startline, endline, _, _ = self.__get_method_margins(method_node)

        if startline is None or endline is None:
            return None

        code = []
        for i in range(startline - 1, endline - 1):
            code.append(self.source_split[i])
        code = '\n'.join(code)

        if self.file_class_type == ClassType.INTERFACE:
            return code[0:code.rfind(';')+1].rstrip()
        else:
            return code[0:code.find("/**")].rstrip()

    def __get_method_margins(self, method_node):
        startpos  = None
        endpos    = None
        startline = None
        endline   = None

        for path, node in self.parsed:
            if startpos is not None and method_node not in path:
                endpos = node.position
                endline = node.position.line if node.position is not None else None
                break
            if startpos is None and node == method_node:
                startpos = node.position
                startline = node.position.line if node.position is not None else None

        return startline, endline, startpos, endpos

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

class MethodData():
    def __init__(self, code, javadoc):
        # need to clean
        self.code = code
        self.javadoc = javadoc

class BadJavaFileError(Exception):
    def __init__(self, link):
        self.link = link
        self.message = f"Cannot parse Java code at f{link}"
        super().__init__(self.message)