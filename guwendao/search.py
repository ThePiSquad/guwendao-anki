"""Search functionalities"""


class SearchManager:
    """Manage Search Result"""

    page_count: int
    search_term: str

    def __init__(self, search_term: str):
        self.search_term = search_term
        self.page_count = 1

    def current_page(self) -> "SearchResult":
        """Get the SearchResult object for current page

        Returns:
            SearchResult: SearchResult object for current page
        """
        raise NotImplementedError()

    def next_page(self) -> "SearchResult":
        """Get the SearchResult object for next page
        and move increase the page count by one

        Returns:
            SearchResult: SearchResult object for next page
        """
        raise NotImplementedError()


class SearchResult:
    """Representing the search result for a single page"""

    def __init__(self):
        raise NotImplementedError()
