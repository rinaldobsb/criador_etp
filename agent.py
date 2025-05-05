from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat

info_collector_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    markdown=True
)

writer_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    markdown=True
)

revisor_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")