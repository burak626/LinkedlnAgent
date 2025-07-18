from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_profile_url(query: str):
    """Search for LinkedIn profile URL using Tavily API."""
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    
    # Add LinkedIn domain filter to search query
    search_query = f"{query} site:linkedin.com/in/"
    
    response = client.search(
        query=search_query,
        search_depth="basic",
        max_results=3
    )
    
    results = response.get("results", [])
    
    # Look for LinkedIn profile URLs
    for result in results:
        url = result.get("url", "")
        if "linkedin.com/in/" in url:
            return url
    
    # If no direct LinkedIn profile found, return the first result
    if results:
        return results[0].get("url", "")
    
    return ""