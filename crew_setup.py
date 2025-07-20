from crewai import Crew
from tasks import task1, task2, task3, task4

crew = Crew(
    tasks=[task1, task2, task3, task4],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    with open("outputs/paper_draft.txt", "w") as f:
        f.write(result)

