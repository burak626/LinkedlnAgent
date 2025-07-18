import os
import requests
from dotenv import load_dotenv
import http.client
import json
import urllib.parse

load_dotenv()


def scrape(linkedin_profile_url: str, mock: bool = False):
    """Scrape LinkedIn profile data using RapidAPI."""
    cache_file = "cache/linkedin_profile_cache.json"
    
    # Try cache first if mock=True
    if mock:
        try:
            with open(cache_file, 'r') as f:
                cache = json.load(f)
            if linkedin_profile_url in cache:
                return cache[linkedin_profile_url]
        except FileNotFoundError:
            pass
    
    # Setup connection and headers
    conn = http.client.HTTPSConnection("fresh-linkedin-profile-data.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': os.getenv("RAPIDAPI_KEY"),
        'x-rapidapi-host': "fresh-linkedin-profile-data.p.rapidapi.com"
    }
    
    # Build minimal endpoint
    encoded_url = urllib.parse.quote(linkedin_profile_url, safe='')
    endpoint = f"/get-profile-public-data?linkedin_url={encoded_url}&include_skills=false&include_certifications=false&include_publications=false&include_honors=false&include_volunteers=false&include_projects=false&include_patents=false&include_courses=false&include_organizations=false&include_profile_status=false&include_company_public_url=false"
    
    try:
        conn.request("GET", endpoint, headers=headers)
        res = conn.getresponse()
        
        if res.status != 200:
            return None
            
        profile_data = json.loads(res.read().decode("utf-8"))
        
        # Cache result
        try:
            with open(cache_file, 'r') as f:
                cache = json.load(f)
        except FileNotFoundError:
            cache = {}
        
        cache[linkedin_profile_url] = profile_data
        with open(cache_file, 'w') as f:
            json.dump(cache, f, indent=2)
        
        return profile_data
        
    except Exception as e:
        print(f"Error scraping LinkedIn: {e}")
        return None
    finally:
        conn.close()
    