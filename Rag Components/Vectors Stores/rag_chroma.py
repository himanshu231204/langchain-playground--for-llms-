from langchain_core.documents import Document

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


#  Use Updated Ollama Embedding Model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text-v2-moe"
)

# create langchain documents fro ipl players

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )

# create a list of documents
docs=[doc1, doc2, doc3, doc4, doc5]

#create the vector store

vector_store=Chroma(
    collection_name="ipl_players", #name of the collection to store the vectors
    embedding_function=embeddings, #embedding function to convert the documents into vectors
    persist_directory="./chroma_db" #directory to persist the vector store
)

#add the documents to the vector store
print("Adding documents to the vector store...")
result=vector_store.add_documents(docs)
print("Documents added successfully!")
print("Result:", result)

#view documents in the vector store

# view documents
#print("viewing documents in the vector store...")
view_docs = vector_store.get(include=['embeddings','documents', 'metadatas'])
#print("Stored Documents in Vector Store:", stored_docs)



#searching the vector store

search=vector_store.similarity_search(
    query="Who is the best captain in IPL history?", #query to search for
    k=2 #number of similar documents to return
)
print("Search Results:", search)

# vextore_store.similarity_search_with_score( gives the similar documents along with the similarity score)
search_with_score=vector_store.similarity_search_with_score(
    query="Who is the best captain in IPL history?", #query to search for
    k=2
)
print("Search Results with Scores:", search_with_score)

print('\n') 
#filtering the vector store based on metadata
filtered_search=vector_store.similarity_search(
    query="Who is the best captain in IPL history?", #query to search for
    filter={"team": "Mumbai Indians"}, #filter to apply based on metadata, in this case we are filtering for documents where the team is Mumbai Indians
    k=2
)
print("Filtered Search Results:", filtered_search)

print('\n')

#updateing the documents in the vector store

updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)

vector_store.update_documents(ids=['e896ff98-61e6-4921-93ff-371806843ce0'], documents=[updated_doc1])
print("Document updated successfully!")

print(view_docs)