from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load the API key from your .env file
load_dotenv()

# Initialize the Gemini embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Generate an embedding vector for text
text = [
    "Machine learning enables predictive analytics.",
    "Neural networks are used for deep learning.",
    "Generative AI can create realistic text and images."
]

vector = embeddings.embed_query(text)

print(f"Vector length: {len(vector)}")
print(f"First 10 values: {vector[:10]}")
