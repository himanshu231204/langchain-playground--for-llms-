"""

🔷 What is LCEL?

LCEL = LangChain Expression Language

It is the declarative syntax system used in LangChain to build pipelines using Runnables in a clean, composable way.

🧠 One-Line Definition

LCEL is a pipe-based syntax (|) used to compose Runnables into chains in a simple and readable way.

With LCEL
chain = prompt | llm | parser
That’s LCEL.

This creates a RunnableSequence internally.
    """