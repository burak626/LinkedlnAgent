import os
import json
from tools.tools import get_profile_url
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool 
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub
from dotenv import load_dotenv
load_dotenv()



def lookup(name: str, details: str = "no details provided", mock: bool = False) -> str:
    cache_file = "cache/linkedin_tavily_cache.json"
    cache_key = f"{name}_{details}"
    
    # If mock is True, try to use cache
    if mock:
        try:
            with open(cache_file, 'r') as f:
                cache = json.load(f)
            if cache_key in cache:
                return cache[cache_key]
        except FileNotFoundError:
            pass
    
    # Make research using the tool
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    
    template = """Given the full name {name_of_person} and additional details: {detail_info}, find the LinkedIn profile URL for this specific person. Use the provided details effectively to identify the exact right person when multiple people share the same name. Return only the raw LinkedIn URL. (e.g., https://www.linkedin.com/in/username/)"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person", "detail_info"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the LinkedIn Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    print(react_prompt.template)

    
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name, detail_info=details).to_string()}
    )
    
    linked_profile_url = result["output"]
    
    # Save to cache
    try:
        with open(cache_file, 'r') as f:
            cache = json.load(f)
    except FileNotFoundError:
        cache = {}
    
    cache[cache_key] = linked_profile_url
    with open(cache_file, 'w') as f:
        json.dump(cache, f, indent=2)
    
    return linked_profile_url

if __name__ == "__main__":
    linkedin_url = lookup("Burak Solak", "Artificial Intelligence AAS student in Houston Community College", mock=True)
    print(f"LinkedIn URL: {linkedin_url}")