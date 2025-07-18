from dotenv import load_dotenv  
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from agents import linkedin_lookup_agent 
from services import linkedin_scraper as linkedin_scrape_agent
from services.output_parser import summary_parser, Summary
from typing import Tuple

def generate_profile_summary(name: str, details: str = "no details provided", mock: bool = False) -> Tuple[Summary, str]:
    """Generate a profile summary based on the LinkedIn profile of a person."""
    

    linkedin_url = linkedin_lookup_agent.lookup(name, details, mock)
    linkedin_data = linkedin_scrape_agent.scrape(linkedin_url, mock)
    print(f"LINKEDIN DATA: {linkedin_data}")
    
    if not linkedin_url:
        return "No LinkedIn profile data found."
    

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    \n {format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        partial_variables={"format_instructions":summary_parser.get_format_instructions()}, 
        template=summary_template
        )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke({"information": linkedin_data})
    print(f"PROFILE SUMMARY: {res}")
    
    # Extract profile image URL from linkedin_data
    profile_image_url = None
    if linkedin_data and isinstance(linkedin_data, dict):
        data = linkedin_data.get("data", {})
        profile_image_url = data.get("profile_image_url")
    
    return res, profile_image_url


if __name__ == "__main__":
    generate_profile_summary("Burak Solak", "Artificial Intelligence AAS student in Houston Community College", mock=False)