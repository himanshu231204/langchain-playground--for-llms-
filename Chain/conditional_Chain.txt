CONDITIONAL CHAIN – CONCEPT (LangChain)

1. Definition
A Conditional Chain is a workflow pattern in which different processing paths
(chains) are executed based on a condition or decision made at runtime.
It is similar to IF–ELSE logic in traditional programming, but applied to
LLM-based pipelines.

2. Core Idea
Input → Condition Check → Selected Chain → Output

The condition can be:
- A simple rule (keyword, regex, length, etc.)
- The output of an LLM (classification, intent detection)
- External signals (API response, database value)

3. Why Conditional Chains Are Needed
- To avoid running unnecessary chains
- To reduce cost and latency
- To handle multiple user intents in one system
- To build intelligent and flexible AI workflows

4. Basic Logic (Pseudo Code)

IF condition is true:
    run Chain A
ELSE:
    run Chain B

5. Typical Architecture

User Input
   |
   v
Classifier / Condition Logic
   |
   +--> Chain 1 (Action A)
   |
   +--> Chain 2 (Action B)

6. Example Use Case: Feedback Processing

Input: User Feedback
Condition: Is feedback Positive or Negative?

IF Positive:
    - Save feedback
    - Send acknowledgment
ELSE:
    - Raise complaint
    - Notify support team

7. How Conditions Are Determined
- Rule-based:
  - Keyword matching
  - Sentiment score threshold
- LLM-based:
  - Prompt asks model to classify intent/sentiment
- Hybrid:
  - LLM decides, code executes actions

8. Conditional Chain vs Sequential Chain

Sequential Chain:
- Fixed order of execution
- All steps always run
- Example: Step1 → Step2 → Step3

Conditional Chain:
- Dynamic execution
- Only one branch runs
- Example: IF–ELSE routing

9. Relation to Agents
An AI Agent can be considered an advanced form of a Conditional Chain where:
- Conditions are complex
- Tool selection is dynamic
- Multiple decisions are made iteratively

10. Advantages
- Efficient use of LLM calls
- Scalable design
- Better user experience
- Easy to extend with new conditions

11. Limitations
- More complex logic than linear chains
- Poorly designed conditions can increase LLM calls
- Requires careful prompt design

12. Interview One-Liner
A Conditional Chain dynamically selects which LLM chain to execute based on
runtime conditions, enabling flexible and decision-driven AI workflows.



------------------------

CONDITIONAL CHAIN – SHORT NOTES (LEARNED THROUGH ERRORS)

1. What is a Conditional Chain?
A Conditional Chain is an LLM workflow where execution is routed to different
chains based on a runtime condition (IF–ELSE logic).
It allows dynamic decision-making instead of fixed sequential execution.

2. Core Flow
Input → Classifier / Condition → Branch Selection → Action Chain → Output

3. Common Use Case
Feedback Analysis System:
- Analyze feedback sentiment
- If positive → send acknowledgment / save feedback
- If negative → raise complaint / notify support

4. Key Components in LangChain
- PromptTemplate: Defines how input is framed for the LLM
- ChatOllama / LLM: Generates classification or content
- OutputParser: Converts LLM output into usable format
- RunnableLambda: Transforms data between steps
- RunnableBranch: Routes execution based on conditions

5. Major Lessons Learned from Errors

5.1 Structured Output vs Branch Input
- PydanticOutputParser returns a typed object (not a dictionary)
- RunnableBranch conditions expect dictionary-like inputs
Lesson:
Always insert a mapping step (RunnableLambda) to convert structured objects
into routing dictionaries.

5.2 Why `classifier_chain | branch_chain` Fails
- Classifier output = Pydantic object
- Branch expects keys like "sentiment"
Lesson:
Never directly pipe a structured output into RunnableBranch.

5.3 Feedback Must Be Passed Explicitly
- Branch action prompts require `{feedback}`
- Classifier output does NOT automatically carry original input
Lesson:
Always forward required fields explicitly through the pipeline.

5.4 Literal Validation Errors Are Not Bugs
- Real-world feedback can be mixed (positive + negative)
- Pydantic Literal validation fails if output is outside allowed values
Lesson:
Define clear business rules (e.g., “any complaint = negative”).

5.5 LLM Output Is Probabilistic
- LLM may return unexpected labels (e.g., "mixed")
Lesson:
Use strict prompts and fallback logic to constrain outputs.

6. Correct Design Pattern (Best Practice)

Classifier Chain
→ RunnableLambda (mapping step)
→ RunnableBranch (IF–ELSE routing)
→ Action Chains

7. Why RunnableLambda Is Critical
- Converts structured output into branch-friendly format
- Enables clean data flow
- Improves debuggability and extensibility

8. Conditional Chain vs Sequential Chain
- Sequential Chain: Always runs all steps
- Conditional Chain: Runs only one selected branch
Conditional Chains are more efficient and cost-aware.

9. Interview-Ready One-Liner
A Conditional Chain dynamically routes execution to different LLM chains based
on structured runtime decisions, enabling flexible and efficient workflows.

10. Final Takeaway
Most Conditional Chain errors are wiring errors, not logic errors.
Correct data flow and explicit mappings are more important than complex prompts.
