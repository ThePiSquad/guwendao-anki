"""Details of a single article"""

import requests
import re
from bs4 import BeautifulSoup
from loguru import logger


class Article:
    """Representing a single article"""

    url: str

    title: str
    author: str
    content: str

    content_translation: list[str]
    word_translation: list[tuple[str,str]]

    translation_id: int
    appreciation_id: int
    idjm_string: str  # some identifier used for verification

    @staticmethod
    def _get_translation_id(soup: BeautifulSoup) -> int:
        """Get the translation id for current article
        Guwendao uses this id to fetch detailed content
        """
        return int(
            soup.select_one('[id^="fanyiquan"]').get("id").replace("fanyiquan", "")
        )

    @staticmethod
    def _get_appreciation_id(soup: BeautifulSoup) -> int:
        return int(
            soup.select_one('[id^="shangxiquan"]').get("id").replace("shangxiquan", "")
        )

    @staticmethod
    def _get_idjm_string(soup: BeautifulSoup) -> str:
        href = soup.find_all("a", href=re.compile(r"^javascript:shangxiShow"))[0].get(
            "href"
        )
        match = re.search(r"shangxiShow\(\d+,'([A-Z0-9]{16})'\)", href)
        if match:
            return match.group(1)
        else:
            raise ValueError(href)

    def __init__(self, url):
        self.url = url
        self.content_translation = list()
        self._load_basic()
        self._load_detail()

    def _load_basic(self):
        logger.info(f"fetching article {self.url}")
        response = requests.get(self.url, timeout=1000)
        if response.status_code != 200:
            raise ConnectionRefusedError()

        logger.info("parsing content")
        soup = BeautifulSoup(response.text, "lxml")

        content_block = soup.h1.parent
        self.title = content_block.select_one("h1").text.strip()
        self.author = content_block.select_one("p").text.strip()
        self.content = (
            content_block.select_one(".contson").text.replace(" ", "").strip()
        )

        self.translation_id = self._get_translation_id(soup)
        self.appreciation_id = self._get_appreciation_id(soup)
        self.idjm_string = self._get_idjm_string(soup)

        logger.info(
            f""""parsing result:
title: {self.title}
author: {self.author}
translation_id:{self.translation_id}
appreciation_id:{self.appreciation_id}
idjm_string:{self.idjm_string}
content:{self.content}"""
        )

    def _load_detail(self):
        # https://www.gushiwen.cn/nocdn/ajaxfanyi.aspx?id=57185&idjm=9551045DD9900B21
        logger.info("loading translation...")
        response = requests.get(
            f"https://www.gushiwen.cn/nocdn/ajaxfanyi.aspx?id={self.translation_id}&idjm={self.idjm_string}",
            timeout=1000,
        )
        if response.status_code != 200:
            raise ConnectionRefusedError()
        logger.info("parsing translation data")
        soup = BeautifulSoup(response.text, "lxml")

        content_block = soup.select_one(".contyishang")
        children = content_block.select("p")

        content_translation = children[0]
        word_translation = children[1]

        for element in content_translation.children:
            text: str = element.text
            if text.startswith("译文") or len(text) == 0:
                continue
            self.content_translation.append(text)
        # print(self.content_translation)

        for element in word_translation.children:
            text: str = element.text
            if len(text) == 0 or text.startswith("注释") or text.startswith("▲"):
                continue
            self.word_translation.append()
