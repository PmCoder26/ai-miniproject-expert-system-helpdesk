import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import streamlit as st
from knowledge_base import knowledge_base, issue_keywords

# Download necessary NLTK resources
nltk.download('punkt')

class HelpDeskExpertSystem:
    def __init__(self):
        """Initialize the expert system with a rule-based knowledge base."""
        self.knowledge_base = knowledge_base
        self.issue_keywords = issue_keywords
        self.stemmer = PorterStemmer()  # For stemming words

    def preprocess_input(self, user_input):
        """Tokenize and stem user input to extract meaningful keywords."""
        tokens = word_tokenize(user_input.lower())
        stemmed_words = [self.stemmer.stem(word) for word in tokens]
        return stemmed_words

    def diagnose_issue(self, user_input):
        """Match user input with the knowledge base."""
        words = self.preprocess_input(user_input)

        for issue, keywords in self.issue_keywords.items():
            # Check if any of the issue keywords are present in the user input
            if any(keyword in words for keyword in keywords):
                self.provide_solution(issue)
                return
        
        # If no matching issue is found
        st.write("Sorry, we couldn't identify the issue.")
        st.write("Please describe your problem more specifically or contact IT support.")

    def provide_solution(self, issue):
        """Display suggested solutions for a given issue in Streamlit."""
        solutions = self.knowledge_base.get(issue, [])
        st.write(f"### Suggested Solutions for '{issue}':")
        for i, solution in enumerate(solutions, 1):
            st.write(f"{i}. {solution}")