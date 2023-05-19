import streamlit as st
import json

# Function to load JSON
def load_json(uploaded_file):
    data = json.load(uploaded_file)
    return data

# Function to save JSON
def save_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# Upload the JSON file
uploaded_file = st.file_uploader("Choose a JSON file", type='json')
if uploaded_file is not None:
    data = load_json(uploaded_file)

    # Display JSON in a text area (as a string for editing)
    #json_str = st.text_area("JSON Input", json.dumps(data, indent=4))
    #json_str = st.text_area("JSON Input", json.dumps(data, indent=4), height=len(json.dumps(data, indent=4).split('\n'))*20)
    #edited_data = json.loads(json_str)
    # Display JSON in a text area (as a string for editing)
    #json_str = st.text_area("JSON Input", json.dumps(data, indent=4), height=500)
    json_str = st.text_area("JSON Input", json.dumps(data, indent=4), height=len(json.dumps(data, indent=4).split('\n'))*20)
    # Load the edited JSON data
    edited_data = json.loads(json_str)
    # Input for the file path
    file_path = st.text_input("Enter the file path where you want to save the edited file")

    # Button to save the changes
    if st.button('Save JSON'):
        if file_path:
            save_json(file_path.strip(), edited_data)
            st.success('File saved')
        else:
            st.error('Please enter a file path')
