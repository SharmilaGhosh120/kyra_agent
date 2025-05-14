
import streamlit as st
from datetime import datetime
from gpt_agent_logic import get_gpt_response
from student_connector import save_to_db

st.title("Ky'ra Student Query Assistant")

st.write("Please fill in your details and query.")

apaar_id = st.text_input("APAAR ID")
query = st.text_area("Enter your query here")
submit = st.button("Submit")

if submit and apaar_id and query:
    with st.spinner("Generating response..."):
        response = get_gpt_response(query)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success("Response generated!")
        st.markdown(f"**Response:** {response}")
        
        save_to_db(apaar_id, query, response, timestamp, feedback=None)

        feedback = st.radio("Was this helpful?", ("Yes", "No"))
        if feedback:
            save_to_db(apaar_id, query, response, timestamp, feedback)
