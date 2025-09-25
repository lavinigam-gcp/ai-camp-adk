# Lab 3: Multi-Agent Collaboration - Blog Creation Team (Python Version)
# This lab demonstrates how multiple specialized agents work together

from google.adk import Agent
from google.adk.tools import google_search

# Researcher Agent - Gathers information
researcher_agent = Agent(
    model="gemini-2.5-flash",
    name="researcher",
    description="Expert at researching topics and gathering comprehensive information",

    instruction="""
    You are a meticulous researcher who gathers accurate, relevant information.

    Your process:
    1. Search for multiple perspectives on the topic
    2. Focus on recent, credible sources
    3. Extract key facts, statistics, and quotes
    4. Organize findings into clear categories
    5. Always cite your sources

    Output your research as a structured brief with:
    - Key findings (3-5 main points)
    - Supporting data/statistics
    - Notable quotes or expert opinions
    - Sources used
    """,

    tools=[google_search],

    # This is KEY for multi-agent data passing
    output_key="research_data"  # Stores research in state['research_data']
)

# Writer Agent - Creates content based on research
writer_agent = Agent(
    model="gemini-2.5-flash",
    name="writer",
    description="Creative writer who transforms research into engaging blog posts",

    instruction="""
    You are a talented blog writer who creates engaging, well-structured content.

    Use the research data provided: {research_data}

    Your writing process:
    1. Create an attention-grabbing title
    2. Write a compelling introduction (2-3 sentences)
    3. Develop 3-4 main sections with headers
    4. Include relevant data and quotes from the research
    5. End with a thought-provoking conclusion
    6. Keep the tone conversational yet informative

    Target length: 400-500 words
    Style: Engaging, accessible, and informative
    """,

    # No tools needed - just writing
    output_key="draft_content"  # Stores draft in state['draft_content']
)

# Editor Agent - Reviews and improves content
editor_agent = Agent(
    model="gemini-2.5-flash",
    name="editor",
    description="Professional editor who polishes content for publication",

    instruction="""
    You are a skilled editor who ensures content quality and readability.

    Review this draft: {draft_content}

    Your editing checklist:
    1. Grammar and spelling corrections
    2. Improve clarity and flow
    3. Ensure facts are accurately represented
    4. Check for engaging opening and strong conclusion
    5. Verify appropriate tone and style
    6. Suggest a catchy subtitle if needed

    Provide:
    - The edited, publication-ready version
    - A brief summary of changes made (2-3 bullet points)
    - A quality score out of 10
    """,

    output_key="final_content"  # Stores final content in state['final_content']
)

# Root Agent - Orchestrates the team
root_agent = Agent(
    model="gemini-2.5-flash",
    name="blog_team_lead",
    description="Team lead who coordinates the blog creation process",

    instruction="""
    You are the Blog Team Lead, managing a content creation team with three specialists:
    1. **Researcher**: Gathers information and sources
    2. **Writer**: Creates engaging blog posts
    3. **Editor**: Polishes content for publication

    Your workflow:
    - When asked to create content about any topic:
      1. First, delegate to the researcher to gather comprehensive information
      2. Then, pass the research to the writer to create a draft
      3. Finally, have the editor review and polish the content
      4. Present the final blog post to the user

    Always explain what each team member is doing as you coordinate the process.
    Be encouraging and highlight the strengths of each team member's contribution.
    """,

    # The team of specialized agents
    sub_agents=[researcher_agent, writer_agent, editor_agent]
)