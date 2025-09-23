# Install dependencies (run in terminal first if not installed)
# pip install sentence-transformers faiss-cpu

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ----------------------
# Step 1: Create Banking FAQs
# ----------------------
faqs = [
    "How can I reset my online banking password?",
    "How do I check my account balance?",
    "What should I do if my debit card is lost?",
    "How can I apply for a personal loan?",
    "How do I activate international transactions on my credit card?"
]

answers = {
    faqs[0]: "You can reset your password by clicking 'Forgot Password' on the login page and following the verification steps.",
    faqs[1]: "You can check your balance using the mobile app, internet banking, or by visiting an ATM.",
    faqs[2]: "Report the lost debit card immediately through the customer service helpline or the banking app.",
    faqs[3]: "You can apply for a personal loan online through the bank’s portal or by visiting your nearest branch.",
    faqs[4]: "International transactions can be activated via the mobile banking app or by contacting customer care."
}

# ----------------------
# Step 2: Load Embedding Model
# ----------------------
model = SentenceTransformer('all-MiniLM-L6-v2')
# lightweight & good for semantic search

# Encode FAQs into embeddings
faq_embeddings = model.encode(faqs)

# ----------------------
# Step 3: Create FAISS Index
# ----------------------
dimension = faq_embeddings.shape[1]  # embedding size
index = faiss.IndexFlatL2(dimension)  # L2 distance index
index.add(np.array(faq_embeddings))

# ----------------------
# Step 4: User Query
# ----------------------
user_query = "How do I reset my online banking password?"
query_embedding = model.encode([user_query])

# ----------------------
# Step 5: Search Closest FAQ
# ----------------------
# We want the top 1 most similar FAQ
number_of_results = 1

# Search the FAISS index: it returns both distances and indices
# - distances = how far the query is from each match
# - indices = the position of the matching FAQ in our 'faqs' list
distances, indices = index.search(np.array(query_embedding), number_of_results)

# Extract the first (and only) match index
first_match_index = indices[0][0]

# Find the matching FAQ question using the index
matched_faq = faqs[first_match_index]

# Now retrieve the prepared answer for that FAQ
matched_answer = answers[matched_faq]

# Show results
print("User Question:", user_query)
print("Matched FAQ:", matched_faq)
print("Answer:", matched_answer)
