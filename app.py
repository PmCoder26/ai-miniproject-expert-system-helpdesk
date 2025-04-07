import streamlit as st
from expert_system import HelpDeskExpertSystem  # Import the expert system class

def main():
    # Initialize the expert system
    expert_system = HelpDeskExpertSystem()

    # Streamlit interface
    st.title("Help Desk Expert System")

    st.write("Please describe your issue below, and the system will suggest possible solutions.")
    st.write("Type 'quit' to exit the session.")

    # Take input from the user
    user_input = st.text_input("Enter your issue:")

    # If the user types something and doesn't quit, diagnose the issue
    if user_input:
        if user_input.strip().lower() == "quit":
            st.write("Thank you for using the Help Desk Expert System. Goodbye!")
        else:
            expert_system.diagnose_issue(user_input)  # Diagnose the issue and show solutions

if __name__ == "__main__":
    main()