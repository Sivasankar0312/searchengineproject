import streamlit as st 
import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.get_collection(name="my_collection")

st.title("Search Engine for movie Subtitiles 🔍🎞️")

st.subheadings("Enter the query")

title=st.text_input("Movie title")

if st.button("Search"):
    title=[title]
    results = collection.query(
    query_texts=title,
    n_results=10,)
    st.write(results['metadatas'][0])

