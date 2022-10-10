import re

comments_regex_1 = re.compile("/\*.*?\*/",re.DOTALL ) # to remove /*COMMENT */
comments_regex_2 = re.compile("//.*?\n" ) # to remove // comment

html_regex = re.compile("<.*?>")
links_regex = re.compile("http\\S+")

javadoc_replacements = [
    ("\n", " "),
    ("\t", " "),
    ("/**", ""),
    ("*/", ""),
    ("*", "")
]

code_replacements = [
    ("\n", " "),
    ("\t", " ")
]

def clean_method_data(md):
    md.code = clean_code(md.code)
    md.javadoc = clean_javadoc(md.javadoc)

    return md

def clean_code(code):
    clean = remove_comments(code)

    for search, replacement in code_replacements:
        clean = clean.replace(search, replacement)

    clean = ' '.join(clean.split())

    return clean

def remove_comments(string):
    string = re.sub(comments_regex_1, "", string)
    string = re.sub(comments_regex_2, "", string)

    return string

def clean_javadoc(javadoc):
    clean = javadoc
    for search, replacement in javadoc_replacements:
        clean = clean.replace(search, replacement)

    clean = re.sub(html_regex, "", clean)
    clean = re.sub(links_regex, "", clean)  

    clean = ' '.join(clean.split())

    return clean