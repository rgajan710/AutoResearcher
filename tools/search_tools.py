from langchain.tools import DuckDuckGoSearchResults

class WebSearchTool(DuckDuckGoSearchResults):
    name = "web_search"
    description = "Useful for finding trending AI research topics or papers."
