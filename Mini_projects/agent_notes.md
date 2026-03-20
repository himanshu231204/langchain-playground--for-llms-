LANGCHAIN AGENTS NOTES

1) Agent:
Agent is an LLM that can use tools.
It reasons about the problem and decides which tool to call.

Agent = LLM + Reasoning + Tool selection

2) ReAct Pattern:
ReAct = Reason + Act

Format:
Thought
Action
Action Input
Observation
Final Answer

3) create_react_agent:
Function that creates a ReAct style agent.
It injects tool descriptions into the prompt.
It enables reasoning before tool calling.

4) AgentExecutor:
Responsible for running the agent.
Executes tools.
Handles the loop.
Returns final response.

5) Flow:
User Input
→ Agent Think
→ Select Tool
→ Tool Execution
→ Observation
→ Final Answer

6) Important:
Tools must have:
- name
- function
- description

Agent decides tool usage based on description.