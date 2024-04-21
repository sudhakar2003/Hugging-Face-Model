import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit app
def main():
    st.title("Text Summarization App")
    st.write("Enter some text to summarize:")

    # Text input box
    text = st.text_area("Text input", "Enter text here...")

    # Button to summarize text
    if st.button("Summarize"):
        # Perform text summarization
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]

        # Display summary
        st.write("Summary:")
        st.write(summary["summary_text"])

# Run the app
if __name__ == "__main__":
    main()
