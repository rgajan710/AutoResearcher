from crewai import Task
from agents import topic_selector, literature_agent, coder_agent, writer_agent

# Define task flow

task1 = Task(
    agent=topic_selector,
    description="Identify a trending topic in AI/ML by analyzing recent sources."
)

task2 = Task(
    agent=literature_agent,
    description="Perform literature review on the selected topic.",
    depends_on=[task1]
)

task3 = Task(
    agent=coder_agent,
    description="Generate Python code to replicate methodology discussed in the papers.",
    depends_on=[task2]
)

task4 = Task(
    agent=writer_agent,
    description="Compile a LaTeX-style paper with all findings, including abstract, intro, related work, method, results, and conclusion.",
    depends_on=[task3]
)
