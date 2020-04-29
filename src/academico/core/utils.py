from lxml import etree
import re

def parse_xpath(content: str, xpath: str) -> str:
    tree = etree.HTML(content)

    return tree.xpath(xpath)[0].text.strip()

def parse_regex(content: str, regex: str) -> str:
    return re.search(regex, content).group(0)
