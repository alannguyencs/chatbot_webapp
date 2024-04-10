import streamlit as st

# Function to count characters
def count_characters(input_text):
    return len(input_text)

# Initialize session state for conversation history if it doesn't exist
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Streamlit application layout
st.title('Character Count Chatbot')

# Create a form for the user input and button
with st.form(key='user_input_form'):
    # User input text box inside the form
    user_input = st.text_input("Type your message here:")

    # Submit button for the form
    submit_button = st.form_submit_button("Send")

# When the user submits the form
if submit_button and user_input:
    # Count the number of characters
    char_count = count_characters(user_input)
    
    # Append user input and bot response to the conversation history
    st.session_state['history'].append(f"You: {user_input}")
    st.session_state['history'].append(f"Bot: The number of characters in your message is: {char_count}")

# Display the conversation history
for message in st.session_state['history']:
    st.text(message)