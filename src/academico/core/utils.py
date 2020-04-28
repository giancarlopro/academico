from lxml import etree
import re

def parse_xpath(content: str, xpath: str) -> str:
    tree = etree.fromstring(content, etree.HTMLParser())

    return tree.xpath(xpath)[0].text

def parse_regex(content: str, regex: str) -> str:
    return re.search(regex, content).group(0)
