from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, web_scraper
from dotenv import load_dotenv
load_dotenv()
import os

from langchain_openrouter import ChatOpenRouter

# used Groq and OpenRouter for LLMs to avoid OpenAI API key issues. You can switch to OpenAI if you have a valid API key.
# My POV:  OpenRouter free models are very good and fast compared to Groq. 

open_model = ChatOpenRouter(
    model="openrouter/free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0,
    max_retries=2,
)

search_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_retries=2,
)

scrape_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_retries=2,
)

writer_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_retries=2,
)

critic_llm = ChatOpenRouter(
    model="openrouter/free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0,
    max_retries=2,
)


# search agent
def build_search_agent():
    return create_agent(
        model=open_model,
        tools=[web_search],
    )

# scraper/reader agent
def build_scrape_agent():
    return create_agent(
        model=open_model,
        tools=[web_scraper],
    )

# writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert researcher and writer. You will be given a topic and you need to write a clear, structured, detailed report on it."),
    ("human", """Write a detailed report on the topic given below
        Topic: {topic}
        Research Gathered: {research}

        Structure the report as follows:
        1. Introduction
        2. Key Findings
        3. Background
        4. Current Developments
        5. Challenges and Opportunities
        6. Conclusion
        7. References (List the sources of information used in the report, including URLs and titles of articles or papers cited)
    
    Be detailed, factual, professional, and ensure that the report is well-structured and easy to read. Use clear headings and subheadings for each section. Avoid plagiarism and ensure that all information is properly cited.
    """)
])

writer_chain = writer_prompt | writer_llm | StrOutputParser()

# critic chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert researcher, sharp, critic. You will be given a report and you need to critique it for accuracy, clarity, and completeness."),
    ("human", """Critique the report given below
        Report: {report}

        Provide a detailed critique of the report, focusing on the following aspects:
        1. Accuracy: Are the facts and information presented in the report accurate and reliable? Are there any errors or inaccuracies?
        2. Clarity: Is the report clear and easy to understand? Are there any sections that are confusing or unclear?
        3. Completeness: Does the report cover all relevant aspects of the topic? Are there any important points that are missing or overlooked?

        Score each aspect on a scale of 1 to 10, with 10 being the highest score.
        Score: Accuracy: X/10, Clarity: Y/10, Completeness: Z/10

        Provide specific examples and suggestions for improvement in each area. Be constructive and professional in your critique.
    """)
])

critic_chain = critic_prompt | critic_llm | StrOutputParser()