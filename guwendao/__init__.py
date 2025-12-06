"""API Abstraction for Guwendao
https://www.gushiwen.cn
"""

from . import article


class Client:
    """_summary_"""

    def search(self, term: str):
        """Create a SearchManager"""
        raise NotImplementedError()

    def get_article_from_url(self, url: str) -> article.Article:
        """Create an article object from url"""
        return article.Article(url)
