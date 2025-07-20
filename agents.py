from crewai import Agent
from tools.search_tools import WebSearchTool
from tools.code_gen_tools import CodeGenTool
from tools.vector_db_tools import VectorDBTool

# Define individual agents

topic_selector = Agent(
    role='Topic Selector',
    goal='Find trending AI/ML research topics',
    backstory='Expert in identifying cutting-edge areas in AI.',
    tools=[WebSearchTool()],
    verbose=True
)

literature_agent = Agent(
    role='Literature Reviewer',
    goal='Review recent literature on selected AI/ML topic',
    backstory='PhD-level researcher summarizing academic findings.',
    tools=[VectorDBTool()],
    verbose=True
)

coder_agent = Agent(
    role='Code Generator',
    goal='Write Python code to reproduce a key ML method from the paper',
    backstory='Senior ML engineer focused on practical code generation.',
    tools=[CodeGenTool()],
    verbose=True
)

writer_agent = Agent(
    role='Research Writer',
    goal='Compile a full research paper draft with citations and results',
    backstory='An academic writer who specializes in AI publications.',
    tools=[],
    verbose=True
)